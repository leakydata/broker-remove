#!/usr/bin/env python3
"""Does a broker's privacy policy describe the product data, or only the visitor?

_SILENT_FAILURES §262. Two companies found by hand in one hour had policies that
covered cookies, analytics and account holders in detail and said nothing at all
about the dataset that *is* the business -- no sources, no retention, no route for
a named person to get out.

That gap has a direct operational cost. The standard fallback ask -- "if you are
not subject to these statutes, honour this under your published privacy policy" --
depends on the policy containing a commitment that reaches the requester. Where it
is visitor-shaped, the fallback silently degrades into a request for a favour.

So this checks it before the letter goes out rather than after.

Not a compliance verdict. A policy can be visitor-shaped and the company still
honour everything; a policy can name its sources and the company still stonewall.
The output is a routing hint: which letters cannot lean on the published policy.
"""
import argparse, json, re, sys, html
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from paths import ROOT  # noqa: E402

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")

CANDIDATES = [
    "/privacy", "/privacy-policy", "/privacy.html", "/privacy.php",
    "/legal/privacy", "/legal/privacy-policy", "/privacy-notice",
    "/policies/privacy", "/about/privacy", "/en/privacy-policy",
]

# Does the policy say where the PRODUCT data comes from?
SOURCE_SIGNALS = [
    r"sources? of (the )?(information|data)", r"we (obtain|acquire|purchase|licen[sc]e|receive)[^.]{0,60}from",
    r"public(ly available)? records?", r"third[- ]party sources", r"publicly available sources",
    r"government records?", r"our data sources", r"data suppliers?", r"data providers?",
]
# Does it tell a person who is IN the data how to get out?
EXIT_SIGNALS = [
    r"opt[- ]out of our (database|directory|data)", r"remove your (information|record|listing|profile)",
    r"removal request", r"suppress(ion)?", r"opt[- ]out (form|request|page|process)",
    r"delete your (record|listing|profile)", r"remove my (information|listing)",
    r"do not sell my personal information",
]
# Confirms we actually fetched a privacy policy and not a 404 page.
VISITOR_SIGNALS = [
    r"cookies?", r"google analytics", r"log files?", r"ip address", r"web beacons?",
    r"browser", r"advertis(ing|ers?) partners?",
]


def _text(body: bytes) -> str:
    t = body.decode("utf8", "replace")
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"\s+", " ", t).strip()


def _get(url: str, timeout: int = 15):
    req = Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    with urlopen(req, timeout=timeout) as r:
        return r.status, r.read(1_500_000)


def _hits(text: str, pats) -> list:
    out = []
    for p in pats:
        m = re.search(p, text, re.I)
        if m:
            out.append(m.group(0)[:40])
    return out


def scan(row: dict) -> dict:
    dom = (row.get("domain") or "").strip().lower()
    res = {"id": row["id"], "domain": dom, "url": None, "verdict": "no-policy-found"}
    if not dom:
        return res
    urls = [row["optout_url"]] if False else []
    urls += [f"https://{dom}{p}" for p in CANDIDATES]
    for u in urls:
        try:
            status, body = _get(u)
        except (URLError, HTTPError, OSError, ValueError):
            continue
        if status != 200 or len(body) < 1500:
            continue
        text = _text(body)
        if len(text) < 800:
            continue
        vis = _hits(text, VISITOR_SIGNALS)
        if len(vis) < 2:
            continue          # probably not a privacy policy at all
        src = _hits(text, SOURCE_SIGNALS)
        exi = _hits(text, EXIT_SIGNALS)
        res.update(url=u, chars=len(text), visitor=len(vis),
                   source=src, exit=exi,
                   verdict=("VISITOR-ONLY" if not src and not exi
                            else "partial" if not src or not exi
                            else "describes-product"))
        return res
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", action="append", default=[],
                    help="restrict to these category values (repeatable)")
    ap.add_argument("--limit", type=int, default=80)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    cur = json.loads((ROOT / "data" / "curated_brokers.json").read_text())
    rows = cur if isinstance(cur, list) else cur.get("brokers", [])
    if args.category:
        rows = [r for r in rows if r.get("category") in args.category]
    rows = [r for r in rows if r.get("domain")][: args.limit]
    print(f"scanning {len(rows)} rows", flush=True)

    out = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for r in ex.map(scan, rows):
            out.append(r)
            if r["verdict"] in ("VISITOR-ONLY", "partial"):
                print(f"  {r['verdict']:14} {r['id']:<28} {r.get('url','')}", flush=True)

    import collections
    tally = collections.Counter(r["verdict"] for r in out)
    print("\n=== verdicts")
    for k, v in tally.most_common():
        print(f"  {k:20} {v:4}")
    reached = sum(v for k, v in tally.items() if k != "no-policy-found")
    if reached:
        vo = tally["VISITOR-ONLY"]
        print(f"\n  of {reached} policies actually read, {vo} ({vo*100//reached}%) describe "
              f"neither where the data comes from nor how to get out")

    # A policy that never mentions removal does NOT mean no removal route exists.
    # The first run of this scan found 33 policies with no exit language and every
    # one of the 33 had a working opt-out URL on another page -- often on another
    # domain. Reporting the absence without this cross-check would have turned
    # "the policy does not say" into "there is no way out", which is false.
    # See _SILENT_FAILURES §263. Never print the one without the other.
    by_id = {r["id"]: r for r in rows}
    silent = [r for r in out if r.get("url") and not r.get("exit")]
    if silent:
        elsewhere = [r for r in silent if by_id.get(r["id"], {}).get("optout_url")]
        print(f"\n=== policies whose text names no way out: {len(silent)}")
        print(f"  a removal route is on record elsewhere for {len(elsewhere)} of them"
              f" -- so this measures what the POLICY omits, not what the SITE lacks")
        offsite = [r for r in elsewhere
                   if (by_id[r["id"]]["optout_url"].split("/")[2].replace("www.", "")
                       not in (r["domain"] or ""))]
        if offsite:
            print(f"  and for {len(offsite)} the route is on a DIFFERENT DOMAIN than the site:")
            for r in offsite[:12]:
                print(f"    {r['id']:<30} -> {by_id[r['id']]['optout_url']}")
        stranded = [r for r in silent if not by_id.get(r["id"], {}).get("optout_url")]
        if stranded:
            print(f"  NO route known at all for {len(stranded)}: "
                  + ", ".join(r["id"] for r in stranded[:12]))
    # Never let the breakdown quietly disagree with the total (§261).
    if sum(tally.values()) != len(out):
        print(f"  !! tally {sum(tally.values())} != {len(out)} scanned")
    if args.out:
        (ROOT / args.out).write_text(json.dumps(out, indent=1))
        print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
