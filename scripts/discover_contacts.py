#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Find a privacy contact address for brokers that have no route at all.

280 rows in the registry came from the Optery catalogue as a name and sometimes a
domain, with no email and no opt-out URL. They are leads, not brokers we can write
to, and they sit outside every count of what is left to do. 122 of them do have a
domain, which is enough to go looking.

This does NOT guess. `privacy@<domain>` is a plausible address at almost any
company and a wrong one costs a send slot and a bounce; worse, a plausible-looking
guess that reaches a real mailbox at an unrelated company is a letter about a
stranger's data. So an address is only ever reported if the company PUBLISHED it
on one of its own pages.

Two things are borrowed from check_mailto.py, which exists because of the same
class of mistake:

  - HTML entities are decoded first. The working address is sometimes published
    only as entities while the machine-readable one is stale (_SILENT_FAILURES 64).
  - A mailto: href and its own anchor text are two independent claims. Where they
    disagree the row is reported as SPLIT and neither is auto-adopted, because a
    false confirmation is worse than finding nothing: NO_EMAIL sends you to look
    again, a wrong address does not.

Off-domain addresses are reported but flagged. A privacy page that points at a
different company's domain is usually a compliance vendor -- which is a real find
(_SILENT_FAILURES 109) -- but it is not the same claim as a first-party address,
and verify_emails.py already has a category for that.

Usage:
    ./discover_contacts.py --limit 20            # dry run, prints what it found
    ./discover_contacts.py --limit 200 --json out.json
"""

import argparse
import html
import json
import re
import socket
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from paths import state  # noqa: E402

# Ordered by how often they actually hold the address, because the scan stops at
# the first page that yields a linked one. Nine paths x two hosts x a 12s timeout
# against a domain that no longer resolves is four minutes of waiting for nothing.
PATHS = ["/privacy-policy", "/privacy", "/legal/privacy", "/ccpa",
         "/do-not-sell", "/contact", "/"]
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
ANCHOR = re.compile(r'<a[^>]*mailto:([^"\'?>]+)[^>]*>(.*?)</a>', re.I | re.S)
ADDR = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')

# Ordered best-first. A privacy-specific mailbox beats a general one, because a
# general one lands with whoever answers sales.
PREFER = ["privacy", "dataprivacy", "dpo", "dsr", "dsar", "optout", "opt-out",
          "donotsell", "compliance", "legal", "support", "info", "contact",
          "hello", "help"]

# Addresses that are never a privacy route, however privacy-ish they look.
# `example@` is here because socialcatfish.com publishes the literal placeholder
# `example@domain.com` in its page text; an earlier pattern only caught
# "example." and let it through.
JUNK = re.compile(r"(no-?reply|do-?not-?reply|^example@|example\.(com|org|net)|"
                  r"your-?email|user@|name@|sentry|wixpress|"
                  r"\.png$|\.jpg$|\.gif$|\.webp$|\.svg$)", re.I)

# A ROLE mailbox only. This is a rule, not a preference, and the difference
# matters twice over.
#
# The first run of this scan returned a named individual's work address at a
# large company, scraped out of a page footer -- someone who has nothing to do
# with this request, whose personal data would then have been written into a
# public repository and possibly written to. That is the exact harm the whole
# project exists to undo, produced by our own tooling.
#
# The second reason is smaller but real: ziprecruiter.com yielded
# `accessibility@` -- right domain, wrong function. Ranking it last still left it
# first when nothing better existed, so a privacy request would have gone to an
# accessibility desk.
#
# So: if no address on the page has a recognised role prefix, report nothing.
# "No published privacy contact" is the honest finding, and by this script's own
# doctrine it sends you to look again, which a wrong address does not.
ROLE = re.compile(r"^(" + "|".join(re.escape(p) for p in
                  ["privacy", "dataprivacy", "data-privacy", "dpo", "dsr", "dsar",
                   "optout", "opt-out", "donotsell", "do-not-sell", "compliance",
                   "legal", "gdpr", "ccpa"]) + r")[a-z0-9._-]*@", re.I)


def resolves(domain):
    """Cheap gate. Most of the cost of this scan is waiting on domains that are
    simply gone -- an Optery catalogue entry can outlive the company."""
    for host in (domain, "www." + domain):
        try:
            socket.gethostbyname(host)
            return True
        except OSError:
            continue
    return False


def fetch(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
            if r.status != 200:
                return None
            raw = r.read(600_000)
        return html.unescape(raw.decode("utf-8", "replace"))
    except (urllib.error.URLError, urllib.error.HTTPError, ssl.SSLError,
            TimeoutError, OSError, ValueError):
        return None


def rank(addr, domain):
    local, _, host = addr.partition("@")
    own = host == domain or host.endswith("." + domain)
    try:
        i = next(n for n, p in enumerate(PREFER) if local.lower().startswith(p))
    except StopIteration:
        i = len(PREFER)
    return (0 if own else 1, i, len(addr))


def scan(bid, domain):
    if not resolves(domain):
        return None
    linked, plain, split = {}, set(), []
    for path in PATHS:
        body = None
        for host in (f"https://www.{domain}", f"https://{domain}"):
            body = fetch(host + path)
            if body:
                break
        if not body:
            continue
        for href, inner in ANCHOR.findall(body):
            href = href.strip().lower()
            if not ADDR.fullmatch(href) or JUNK.search(href):
                continue
            texts = {t.lower() for t in ADDR.findall(re.sub(r"<[^>]*>", " ", inner))}
            # href and anchor text are two claims; disagreement is a finding,
            # not a tie to break silently.
            if texts and href not in texts:
                split.append({"path": path, "href": href, "text": sorted(texts)})
            else:
                linked.setdefault(href, path)
        stripped = re.sub(r"<a[^>]*>.*?</a>", " ", body, flags=re.I | re.S)
        plain |= {a.lower() for a in ADDR.findall(re.sub(r"<[^>]*>", " ", stripped))
                  if not JUNK.search(a)}
        if linked:
            break          # a linked address on an earlier path is the best signal

    cands = [a for a in sorted(linked, key=lambda a: rank(a, domain))
             if ROLE.match(a)]
    if not cands:
        cands = [a for a in sorted(plain, key=lambda a: rank(a, domain))
                 if ROLE.match(a)]
    if not cands:
        return None
    best = cands[0]
    _, _, host = best.partition("@")
    return {
        "id": bid, "domain": domain, "address": best,
        "source_path": linked.get(best, "plain-text"),
        "linked": best in linked,
        "offdomain": not (host == domain or host.endswith("." + domain)),
        "other_candidates": cands[1:5],
        "split_claims": split,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--json", help="write findings to this file")
    args = ap.parse_args()

    reg = {b["id"]: b for b in json.loads((ROOT / "data" / "brokers.json").read_text())["brokers"]}
    sp = state("removal_status.json")
    st = json.loads(sp.read_text()) if sp.exists() else {}

    todo = [(i, b["domain"]) for i, b in reg.items()
            if i not in st and (b.get("domain") or "").strip()
            and not (b.get("email_to") or "").strip()
            and not (b.get("optout_url") or "").strip()
            and not b.get("duplicate_of")]
    todo.sort()
    todo = todo[:args.limit]
    print(f"probing {len(todo)} domain(s) with no route on record", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=16) as pool:
        found = [r for r in pool.map(lambda t: scan(*t), todo) if r]

    for r in sorted(found, key=lambda r: (r["offdomain"], not r["linked"], r["id"])):
        flags = []
        if r["offdomain"]:
            flags.append("OFF-DOMAIN")
        if not r["linked"]:
            flags.append("plain-text only")
        if r["split_claims"]:
            flags.append(f"{len(r['split_claims'])} SPLIT href/text")
        print(f"{r['id']:34} {r['address']:42} {r['source_path']:18} "
              f"{' | '.join(flags)}")
    print(f"\n{len(found)}/{len(todo)} produced a published address", file=sys.stderr)

    if args.json:
        Path(args.json).write_text(json.dumps(found, indent=2) + "\n")
        print(f"wrote {args.json}", file=sys.stderr)


if __name__ == "__main__":
    main()
