#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Find an opt-out ROUTE on brokers that publish no contact ADDRESS.

discover_contacts.py asks a domain "what email address do you publish?" For 240
domains probed this session it answered "none" 239 times (_SILENT_FAILURES 362).
That is a real answer and it closes the email question, but it does not close the
broker: a company with no published mailbox may still have a removal form, and a
removal form is a route.

So this asks the other question. For each domain it fetches the front page and the
usual policy pages, follows the links they contain, and reports any URL whose PATH
looks like a removal route -- opt-out, do-not-sell, remove, delete, ccpa, dsar and
the rest. It reports the LINK, not the page text, because a link is what a person
would click and because matching page text finds every privacy policy ever written.

Two deliberate limits, stated rather than hidden (361):

  - Only same-site links are reported as routes. An off-site link (a OneTrust or
    Osano portal) is reported separately and flagged, because it is a route but
    not one this domain controls, and the registry should record which.
  - A path match is a CANDIDATE, never a confirmed route. Nothing here checks that
    the page contains a working form. It cannot: that needs a browser, and the
    whole point is to produce a queue for one.
"""
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import state  # noqa: E402

CAP = 500_000

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")

# Path segments that mark a removal route. Deliberately narrower than the set
# route_check.py uses: "privacy" alone matches every site on the internet and
# would drown the result, so it is only accepted with a second qualifier.
STRONG = re.compile(
    r"opt[-_]?out|optout|do[-_]?not[-_]?sell|donotsell|remove|removal|suppress|"
    r"delete[-_]?(my|data|info)|erase|dsar|data[-_]?(subject|request)|"
    r"ccpa|cpra|gdpr[-_]?request|subject[-_]?access|privacy[-_]?(request|choices|center)",
    re.I)

SEED_PATHS = ["/", "/privacy", "/privacy-policy", "/privacy.html",
              "/legal/privacy", "/policies/privacy"]


def fetch(url, cap=None):
    cap = CAP if cap is None else cap
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        final = r.geturl()
        return final, r.read(cap).decode("utf-8", "replace")


# Assets, not routes. A stylesheet named banner-1-optout.css matched the path
# regex on the first run, and so did a base64 data: URI whose payload happened to
# contain the letters "remove" -- which dumped 30KB of image into the report. A
# URL is only a candidate route if a person could land on it.
ASSET = re.compile(r"\.(css|js|mjs|png|jpe?g|gif|svg|webp|ico|woff2?|ttf|eot|map)(\?|$)", re.I)

# Honeypots. locate-friend.com plants /crawler-trap-a81f92 and two siblings among
# the ordinary links on its surname pages -- URLs that exist only to catch anything
# walking the site automatically. This scanner follows links by design, so it has to
# know not to. The cost of tripping one is the requester's own address getting
# blocked, which closes the route for the person the request is being made for.
# See _SILENT_FAILURES 372.
TRAP = re.compile(r"crawler[-_]?trap|honey[-_]?pot|bot[-_]?trap|do[-_]?not[-_]?follow|spider[-_]?trap", re.I)


def links(base, html):
    out = []
    for m in re.finditer(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I):
        h = m.group(1).strip()
        if h.startswith(("mailto:", "tel:", "javascript:", "#", "data:", "blob:")):
            continue
        if ASSET.search(h) or TRAP.search(h) or len(h) > 300:
            continue
        try:
            out.append(urllib.parse.urljoin(base, h))
        except ValueError:
            continue
    return out


def catch_all(host, real_len):
    """Does this host answer 200 to a path that cannot exist?

    An HTTP 200 does not mean a page exists, it means something answered.
    Parked domains, catch-all rewrites and SPA routers answer every path
    identically, and a scanner that reads 200 as existence will report a route
    on all of them. Seventeen arrests.org domains were queued as human work on
    exactly that mistake -- nine served a 114-byte stub and four a 32KB landing
    page, byte-identical, for every path asked for. One extra request tells them
    apart: real sites 404 here. See _SILENT_FAILURES 427.

    Takes `real_len`, the length of a page that DOES exist on this host, and
    requires the bogus page to be near-identical to it. Comparing against the
    real page is the whole test and an earlier version of this function omitted
    it -- it flagged any host answering 200, which caught acxiom.com, a real
    broker with a real opt-out route whose site serves a full styled "page not
    found" body with a 200. That is a soft-404, not a catch-all: the content
    differs, so the host still distinguishes one path from another. Flagging it
    would have hidden a working route, which is a worse failure than the one
    this control exists to prevent -- a check that suppresses true positives is
    not a safer check, it is a differently wrong one.

    WHAT THIS CATCHES, AND WHAT IT DOES NOT. The baseline here is the host's
    FRONT PAGE, so this detects a wholly parked host -- one serving the same
    body for every path including "/". It does NOT catch a host that serves a
    real homepage and a generic page for everything else: floridaarrests.org
    has a 31,989-byte front page and returns ~32,288 bytes for /ccpaOptOut/ and
    for a nonsense path alike, so it passes here and is still a fake route.
    Catching that needs the candidate page itself as the baseline, which is
    route_has_form.py's CATCH-ALL check -- it compares the route it was asked
    about against a nonsense path on the same host, and is the authority on
    whether a specific route is real. This function only reports candidates, so
    a candidate surviving here means "worth checking", never "confirmed".

    Returns the bogus page's length when the host answers everything alike,
    else None.
    """
    for scheme in ("https://", "http://"):
        try:
            _, bogus = fetch(f"{scheme}{host}/zzz-not-a-real-page-9137/")
        except urllib.error.HTTPError:
            return None      # a 4xx here is the CORRECT answer: it discriminates
        except Exception:
            continue
        # If either page hit fetch()'s read cap, both lengths are the cap and
        # comparing them says nothing about the pages. acxiom.com -- a real
        # broker with a working opt-out route -- truncated at 499,898 bytes on
        # BOTH the front page and the bogus one and was flagged a catch-all on
        # the strength of two identical truncation points. A comparison whose
        # inputs were produced by the measuring instrument is not a comparison.
        if len(bogus) >= CAP - 1000 or real_len >= CAP - 1000:
            return None

        # Near-identical length is the signature of a page served regardless of
        # what was asked for. A tolerance rather than equality because parking
        # pages often echo the requested path back into the body.
        return len(bogus) if abs(len(bogus) - real_len) < 200 else None
    return None


def probe(bid, domain):
    host = domain.replace("https://", "").replace("http://", "").strip("/")
    same, off, reached, real_len = set(), set(), False, 0
    for path in SEED_PATHS:
        for scheme in ("https://", "http://"):
            try:
                final, html = fetch(f"{scheme}{host}{path}")
            except Exception:
                continue
            reached = True
            real_len = len(html)      # the control compares against this
            for u in links(final, html):
                p = urllib.parse.urlparse(u)
                marker = f"{p.path}?{p.query}"
                if not STRONG.search(marker):
                    continue
                if p.netloc.replace("www.", "").endswith(host.replace("www.", "")):
                    same.add(u)
                else:
                    off.add(u)
            break
        if same:
            break
    # Only worth asking once something answered, and only where it matters --
    # a host that produced no candidate route is already reported as "nothing".
    bogus = catch_all(host, real_len) if (reached and (same or off)) else None
    return {"id": bid, "domain": host, "reached": reached, "catch_all": bogus is not None,
            "same_site": sorted(same)[:4], "off_site": sorted(off)[:3]}


def main():
    st = json.loads(state("removal_status.json").read_text())
    byid = {}
    for src in ("brokers.json", "curated_brokers.json"):
        d = json.loads((ROOT / "data" / src).read_text())
        rows = d if isinstance(d, list) else d.get("brokers", d)
        rows = rows if isinstance(rows, list) else list(rows.values())
        for b in rows:
            byid.setdefault(b.get("id"), b)

    todo = [(k, (b.get("domain") or "").strip()) for k, b in byid.items()
            if k not in st
            and (b.get("domain") or "").strip()
            and not (b.get("email") or "").strip()
            and not (b.get("email_to") or "").strip()
            and not (b.get("optout_url") or "").strip()]
    todo.sort()
    print(f"probing {len(todo)} domain(s) that publish no contact address", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=12) as pool:
        res = list(pool.map(lambda t: probe(*t), todo))

    parked = [r for r in res if r.get("catch_all")]
    found = [r for r in res if r["same_site"] and not r.get("catch_all")]
    offonly = [r for r in res if not r["same_site"] and r["off_site"]
               and not r.get("catch_all")]
    dead = [r for r in res if not r["reached"]]

    print(f"\n=== SAME-SITE REMOVAL ROUTE ({len(found)})")
    for r in sorted(found, key=lambda r: r["id"]):
        print(f"  {r['id']:38s} {r['same_site'][0]}")
        for u in r["same_site"][1:]:
            print(f"  {'':38s} {u}")

    print(f"\n=== OFF-SITE ONLY ({len(offonly)}) -- a route, but not one they control")
    for r in sorted(offonly, key=lambda r: r["id"]):
        print(f"  {r['id']:38s} {r['off_site'][0]}")

    print(f"\n=== CATCH-ALL ({len(parked)}) -- answers 200 to a path that cannot exist,")
    print("    so any 'route' found on it is an artefact. See _SILENT_FAILURES 427.")
    for r in sorted(parked, key=lambda r: r["id"]):
        print(f"  {r['id']:38s} {r['domain']}")

    print(f"\n=== NOT REACHED ({len(dead)})")
    for r in sorted(dead, key=lambda r: r["id"]):
        print(f"  {r['id']:38s} {r['domain']}")

    n_none = len(res) - len(found) - len(offonly) - len(dead) - len(parked)
    print(f"\n=== summary")
    print(f"  same-site route   {len(found)}")
    print(f"  off-site only     {len(offonly)}")
    print(f"  reachable, none   {n_none}")
    print(f"  catch-all         {len(parked)}")
    print(f"  not reached       {len(dead)}")
    print("\n  A path match is a CANDIDATE. Nothing here confirms a working form;")
    print("  that needs a browser. The point is to hand one a queue.")

    out = ROOT / "data" / "optout_page_scan.json"
    out.write_text(json.dumps(res, indent=2) + "\n")
    print(f"\nwrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
