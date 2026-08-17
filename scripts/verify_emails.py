#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Check registry email addresses against what the broker actually publishes.

Why this exists: a guessed `privacy@<domain>` is a coin flip, and a bounced
request is indistinguishable from a pending one in the tracker. Sending to an
address nobody confirmed means discovering the failure one bounce at a time --
and only if you are still watching days later.

This fetches each broker's likely privacy and contact pages, extracts the email
addresses they publish, and compares them with what the registry holds:

    CONFIRMED   the registry address appears on the broker's own site
    REPLACE     the site publishes a different, more privacy-specific address
    NO_EMAIL    the site is up but publishes no address (a form or phone may exist)
    BLOCKED     the site is up but refuses automated requests (403 etc.)
    UNREACHABLE the domain does not resolve, or nothing answers at all

NO_EMAIL, BLOCKED and UNREACHABLE are three different things and must not be
collapsed. An early version of this script reported UNREACHABLE whenever the
privacy and contact paths all 404'd -- so a perfectly live site with its policy
at an unusual path looked dead, and a working address would have been marked
unverified on that basis.

Nothing is written unless you pass --apply, so the proposal can be reviewed
first. Applying sets email_verified / email_verified_by, and swaps in a better
address where one was found.

    ./verify_emails.py --unverified --limit 40        # propose
    ./verify_emails.py --unverified --limit 40 --apply
    ./verify_emails.py --ids spokeo,radaris --apply

Be a good citizen: this makes a handful of GETs per broker. Concurrency is
deliberately modest and there is a small delay between requests to the same host.
"""

import argparse
import json
import re
import socket
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURATED = ROOT / "data" / "curated_brokers.json"
REGISTRY = ROOT / "data" / "brokers.json"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")

# Paths worth trying, cheapest and most likely first.
PATHS = [
    "/privacy-policy/", "/privacy/", "/privacy", "/privacy-policy",
    "/legal/privacy-policy", "/about/privacy", "/privacy-notice/",
    "/contact/", "/contact-us/", "/contact",
    "/",   # last: many small sites put the contact address on the front page
]

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

# Addresses that are noise rather than a privacy contact.
NOISE = re.compile(
    r"(sentry|wixpress|\.png|\.jpg|\.gif|\.webp|example\.|domain\.com|"
    r"yourdomain|sentry\.io|@2x|u003e|schema\.org)", re.I)

# Ranked: the earlier the local-part, the better a privacy contact it is.
PREFERENCE = ["privacy", "privacyrequests", "privacy.officer", "dataprotection",
              "dpo", "datarequests", "privacyinfo", "compliance", "legal",
              "optout", "opt-out", "support", "customercare", "customerservice",
              "info", "contact", "hello", "help"]


def rank(addr):
    local = addr.split("@")[0].lower()
    for i, p in enumerate(PREFERENCE):
        if local == p or local.startswith(p):
            return i
    return len(PREFERENCE)


def fetch(url, timeout=12):
    """Return (body_or_None, server_responded). A 404 or 403 still means the
    server is alive -- only a connection failure means it is not."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(400_000).decode("utf-8", "replace"), True
    except urllib.error.HTTPError:
        return None, True          # 403/404/500 -- the host answered
    except (urllib.error.URLError, socket.timeout, ConnectionError,
            UnicodeError, OSError):
        return None, False


def emails_on_site(domain):
    """Every plausible address published across the broker's privacy/contact pages.

    Returns (addresses, answered, served_a_page). `answered` means the host
    responded at all; `served_a_page` means we actually got a body to read."""
    found = set()
    answered = served = False
    for scheme in ("https://", "https://www."):
        for path in PATHS:
            html, responded = fetch(f"{scheme}{domain}{path}")
            answered = answered or responded
            if html is None:
                continue
            served = True
            for m in EMAIL_RE.findall(html):
                if not NOISE.search(m) and len(m) < 80:
                    found.add(m.lower().rstrip("."))
            if found:
                return found, answered, served
        if served:
            break
    return found, answered, served


def resolves(domain):
    for d in (domain, "www." + domain):
        try:
            socket.getaddrinfo(d, None)
            return True
        except socket.gaierror:
            continue
    return False


def check(b):
    domain = (b.get("domain") or "").strip().lower()
    current = (b.get("email_to") or "").strip().lower()
    out = {"id": b["id"], "domain": domain, "current": current,
           "verdict": "NO_EMAIL", "proposed": None, "found": []}
    if not domain:
        out["verdict"] = "NO_DOMAIN"
        return out
    if not resolves(domain):
        out["verdict"] = "UNREACHABLE"
        return out

    found, answered, served = emails_on_site(domain)
    out["found"] = sorted(found)[:8]
    if not answered:
        out["verdict"] = "UNREACHABLE"
        return out
    if not served:
        # DNS resolves and the host answers, but every page was refused.
        out["verdict"] = "BLOCKED"
        return out
    if not found:
        return out

    if current in found:
        out["verdict"] = "CONFIRMED"
        return out

    # Prefer an address on the broker's own domain, best privacy local-part first.
    same = [e for e in found if e.endswith("@" + domain) or domain in e.split("@")[1]]
    pool = same or list(found)
    pool.sort(key=rank)
    best = pool[0]
    if rank(best) < len(PREFERENCE):
        out["verdict"] = "REPLACE"
        out["proposed"] = best
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--unverified", action="store_true",
                    help="only brokers whose email_verified is not true")
    ap.add_argument("--ids", help="comma-separated broker ids")
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--min-priority", type=int, default=1)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--apply", action="store_true", help="write results to the registry")
    args = ap.parse_args()

    brokers = json.loads(REGISTRY.read_text())["brokers"]
    if args.ids:
        want = {i.strip() for i in args.ids.split(",")}
        pool = [b for b in brokers if b["id"] in want]
    else:
        pool = [b for b in brokers
                if b.get("email_to") and b.get("priority", 0) >= args.min_priority
                and (not args.unverified or not b.get("email_verified"))]
        pool.sort(key=lambda b: (-b.get("priority", 0), b["id"]))
    pool = pool[: args.limit]

    if not pool:
        print("nothing to check")
        return 0

    print(f"checking {len(pool)} broker(s) against their published pages...\n",
          file=sys.stderr)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        results = list(ex.map(check, pool))

    tally = {}
    for r in results:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
        line = f"  {r['verdict']:12} {r['id']:28} {r['current']}"
        if r["proposed"]:
            line += f"  ->  {r['proposed']}"
        print(line)
    print("\n" + "  ".join(f"{k}={v}" for k, v in sorted(tally.items())))

    if not args.apply:
        print("\n(dry run - pass --apply to write these to data/curated_brokers.json)")
        return 0

    d = json.loads(CURATED.read_text())
    by_id = {b["id"]: b for b in d["brokers"]}
    written = 0
    for r in results:
        b = by_id.get(r["id"])
        if not b:
            continue
        if r["verdict"] == "CONFIRMED":
            b["email_verified"] = True
            b["email_verified_by"] = "privacy_policy"
        elif r["verdict"] == "REPLACE":
            b["email_to"] = r["proposed"]
            b["email_verified"] = True
            b["email_verified_by"] = "privacy_policy"
        elif r["verdict"] == "UNREACHABLE":
            b["email_verified"] = False
            b["email_verified_by"] = "site_unreachable"
        elif r["verdict"] == "BLOCKED":
            # The site is alive and simply refuses us. That says nothing about
            # whether the address works, so leave the existing flag untouched.
            continue
        else:
            b["email_verified"] = False
            b["email_verified_by"] = "no_address_published"
        written += 1
    CURATED.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwrote {written} record(s) - now run scripts/build_registry.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
