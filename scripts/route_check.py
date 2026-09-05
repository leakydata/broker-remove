#!/usr/bin/env python3
"""Check whether a recorded opt-out URL still LEADS SOMEWHERE.

Every route check this project had asked one question: does the opt-out URL
resolve? PublicRecordsNow answers yes. Its /optout/ path 302s to the homepage
and returns 200, so a checker that follows redirects -- which every HTTP client
does by default -- scores it as a healthy opt-out page for a site that has no
opt-out at all, no privacy policy, no contact link and no MX record.

A dead route that 404s is self-reporting. A dead route that redirects is a
silent failure by construction: it scores identically to a working route, and
better than a working route that happens to be down for maintenance. See
_SILENT_FAILURES 354.

So this checker does NOT ask whether the URL resolves. It asks whether the
thing it resolves to is still plausibly the opt-out page:

  OK             200, and the final path still carries the opt-out segment
  REDIRECT-AWAY  200, but the final path no longer does -- treat as missing
  GONE           404/410
  BLOCKED        403/429 or a bot wall; unknown, needs eyes
  ERROR          DNS failure, TLS failure, timeout

REDIRECT-AWAY and GONE mean the same thing operationally -- there is no form to
fill -- but they are reported separately because only one of them is honest.
"""
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import state  # noqa: E402

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"

# Path segments that mark a URL as the opt-out route rather than the front page.
SEGMENTS = re.compile(
    r"opt[-_]?out|do[-_]?not[-_]?sell|remove|removal|suppress|delete|privacy|"
    r"dsar|data[-_]?request|ccpa|subject[-_]?request|erase|unsubscribe|block[-_]?record",
    re.I,
)


def marker(url):
    """The opt-out-ness of a URL: its path plus query, lowercased."""
    p = urlparse(url)
    return f"{p.path}?{p.query}".lower()


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Follow redirects by hand so the chain is visible."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise _Redirect(newurl, code)


class _Redirect(Exception):
    def __init__(self, url, code):
        self.url, self.code = url, code


def fetch(url, hops=6):
    """Return (status, final_url, chain). Follows redirects manually."""
    opener = urllib.request.build_opener(NoRedirect)
    chain = []
    cur = url
    for _ in range(hops):
        req = urllib.request.Request(cur, headers={"User-Agent": UA})
        try:
            with opener.open(req, timeout=20) as r:
                return r.status, cur, chain
        except _Redirect as r:
            chain.append((r.code, r.url))
            cur = urllib.parse.urljoin(cur, r.url)
        except urllib.error.HTTPError as e:
            return e.code, cur, chain
    return None, cur, chain


def classify(url):
    try:
        status, final, chain = fetch(url)
    except Exception as e:  # noqa: BLE001 -- DNS, TLS, timeout, malformed
        return "ERROR", f"{type(e).__name__}: {e}"[:110], ""

    if status in (404, 410):
        return "GONE", f"HTTP {status}", final
    if status in (403, 429) or status is None:
        return "BLOCKED", f"HTTP {status}", final
    if status and status >= 500:
        return "ERROR", f"HTTP {status}", final

    started_specific = bool(SEGMENTS.search(marker(url)))
    ended_specific = bool(SEGMENTS.search(marker(final)))
    if started_specific and not ended_specific:
        hop = " -> ".join(f"{c} {u}" for c, u in chain) or "client-side"
        return "REDIRECT-AWAY", hop[:110], final
    return "OK", f"HTTP {status}", final


def main():
    cur = json.loads((ROOT / "data" / "curated_brokers.json").read_text())
    rows = cur if isinstance(cur, list) else cur.get("brokers", cur)
    rows = rows if isinstance(rows, list) else list(rows.values())
    st = json.loads(state("removal_status.json").read_text())

    only_pending = "--all" not in sys.argv
    targets = []
    for b in rows:
        bid = b.get("id")
        s = (st.get(bid) or {}).get("status", "pending")
        if only_pending and s != "pending":
            continue
        u = (b.get("optout_url") or "").strip()
        if u.startswith("http"):
            targets.append((bid, u, s))

    scope = "pending" if only_pending else "all"
    print(f"checking {len(targets)} {scope} opt-out URL(s)\n")

    results = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        for (bid, u, s), (verdict, detail, final) in zip(
            targets, pool.map(lambda t: classify(t[1]), targets)
        ):
            results.append((verdict, bid, u, detail, final))

    order = ["REDIRECT-AWAY", "GONE", "ERROR", "BLOCKED", "OK"]
    for v in order:
        rows_v = [r for r in results if r[0] == v]
        if not rows_v:
            continue
        print(f"=== {v}  ({len(rows_v)})")
        for _, bid, u, detail, final in sorted(rows_v, key=lambda r: r[1]):
            print(f"  {bid:34s} {u[:62]}")
            if v != "OK":
                print(f"  {'':34s}   {detail}")
                if final and final != u:
                    print(f"  {'':34s}   landed on {final[:70]}")
        print()

    print("=== summary")
    for v in order:
        n = sum(1 for r in results if r[0] == v)
        if n:
            print(f"  {v:15s} {n}")
    print()
    print("  REDIRECT-AWAY is the one to act on: the URL returns 200, so every")
    print("  check that asks 'does it resolve' passes it, and there is no form")
    print("  behind it. See _SILENT_FAILURES 354.")

    out = ROOT / "data" / "route_check.json"
    out.write_text(json.dumps(
        [{"verdict": v, "id": b, "url": u, "detail": d, "final": f}
         for v, b, u, d, f in results], indent=2))
    print(f"\nwrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
