#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Harvest structured broker facts from Optery's public data-broker directory.

Each directory page exposes a labelled table — opt-out URL, privacy contact
email, home country, broker type. That turns ~950 registry stubs into entries
with *verified* contacts, which matters because a guessed `privacy@<domain>`
bounces in a way that is indistinguishable from a pending request.

Polite by default: single-threaded-ish, small concurrency, real delay between
requests. Results are cached to disk so re-runs are cheap and don't re-fetch.

Usage:
    ./enrich_from_optery.py --limit 50          # try a slice first
    ./enrich_from_optery.py                     # everything not yet cached
    ./enrich_from_optery.py --merge             # fold cache into curated_brokers.json
"""

import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLUGS = ROOT / "data" / "optery_slugs.txt"
CACHE = ROOT / "data" / "optery_enriched.json"
CURATED = ROOT / "data" / "curated_brokers.json"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124 Safari/537.36")

# Labels as they appear in the directory table.
FIELDS = {
    "site_url": r"Site URL\s*(https?://\S+)",
    "optout_url": r"Primary Opt Out URL\s*(https?://\S+)",
    "email": r"Privacy Opt Out Support Email\s*([\w.+-]+@[\w-]+\.[\w.]+)",
    "country": r"Home Country\s*([A-Za-z ,.'-]+?)\s+Type of Data Broker",
    "type": r"Type of Data Broker\s*([A-Za-z /&,'-]+?)\s+Site URL",
}


def page_text(html_src: str) -> str:
    s = re.sub(r"<script.*?</script>", " ", html_src, flags=re.S | re.I)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S | re.I)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s)))


def scrape(slug: str, delay: float):
    url = f"https://www.optery.com/data-brokers/{slug}/"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return slug, {"error": f"HTTP {e.code}"}
    except Exception as e:
        return slug, {"error": type(e).__name__}
    finally:
        time.sleep(delay)

    t = page_text(body)
    out = {}
    for key, pat in FIELDS.items():
        m = re.search(pat, t)
        if m:
            out[key] = m.group(1).strip().rstrip(".,")
    # Optery marks discontinued brokers in prose.
    if re.search(r"no longer (?:operational|in business)|has shut down|is defunct", t, re.I):
        out["defunct"] = True
    return slug, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    ap.add_argument("--delay", type=float, default=0.4,
                    help="seconds each worker sleeps after a fetch")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--merge", action="store_true",
                    help="fold the cache into curated_brokers.json")
    args = ap.parse_args()

    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}

    if args.merge:
        return merge(cache)

    slugs = [s.strip().strip("/") for s in SLUGS.read_text().splitlines()
             if s.strip() and s.strip("/") != "data-brokers"]
    todo = [s for s in slugs if s not in cache]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(cache)} cached | {len(todo)} to fetch")

    done = 0
    try:
        with ThreadPoolExecutor(args.workers) as ex:
            for slug, rec in ex.map(lambda s: scrape(s, args.delay), todo):
                cache[slug] = rec
                done += 1
                if done % 25 == 0:
                    CACHE.write_text(json.dumps(cache, indent=2) + "\n")
                    print(f"  {done}/{len(todo)}", flush=True)
    except KeyboardInterrupt:
        print("\ninterrupted - saving what we have")
    CACHE.write_text(json.dumps(cache, indent=2) + "\n")

    ok = [r for r in cache.values() if not r.get("error")]
    print(f"\ncached {len(cache)} | parsed {len(ok)}")
    print(f"  with opt-out URL : {sum(1 for r in ok if r.get('optout_url'))}")
    print(f"  with email       : {sum(1 for r in ok if r.get('email'))}")
    print(f"  US brokers       : {sum(1 for r in ok if 'united states' in (r.get('country','')).lower())}")


def canonical_id(slug: str) -> str:
    s = re.sub(r"-\d+$", "", slug)
    s = re.sub(r"[-\s](llc|inc|ltd|limited|corp|corporation|gmbh|bv|plc|co|pty|ag|nv)$",
               "", s, flags=re.I)
    return s.replace("-", "_")


def merge(cache):
    """Fold scraped facts into curated_brokers.json without clobbering hand-verified
    entries -- curated values always win."""
    d = json.loads(CURATED.read_text())
    by_id = {b["id"]: b for b in d["brokers"]}
    added = enriched = 0

    for slug, rec in cache.items():
        if rec.get("error") or rec.get("defunct"):
            continue
        if "united states" not in (rec.get("country", "")).lower():
            continue
        if not (rec.get("optout_url") or rec.get("email")):
            continue

        cid = canonical_id(slug)
        domain = ""
        if rec.get("site_url"):
            domain = re.sub(r"^www\.", "",
                            re.sub(r"^https?://", "", rec["site_url"]).split("/")[0])

        existing = by_id.get(cid) or next(
            (b for b in d["brokers"] if domain and b.get("domain") == domain), None)

        if existing:
            # Only fill gaps; never overwrite a hand-verified value.
            for k, v in (("optout_url", rec.get("optout_url")),
                         ("email_to", rec.get("email"))):
                if v and not existing.get(k):
                    existing[k] = v
                    existing["email_verified"] = True if k == "email_to" else \
                        existing.get("email_verified")
                    enriched += 1
            existing.setdefault("optery_slug", slug)
        else:
            by_id[cid] = {
                "id": cid,
                "name": " ".join(w.capitalize() for w in re.sub(r"-\d+$", "", slug).split("-")),
                "domain": domain,
                "priority": 2,
                "method": "email" if rec.get("email") and not rec.get("optout_url") else "web_form",
                "optout_url": rec.get("optout_url", ""),
                "needs_email_confirm": None,
                "source": "optery_scrape",
                "optery_slug": slug,
            }
            if rec.get("email"):
                by_id[cid]["email_to"] = rec["email"]
                by_id[cid]["email_verified"] = True
            d["brokers"].append(by_id[cid])
            added += 1

    CURATED.write_text(json.dumps(d, indent=2) + "\n")
    print(f"merged: {added} new US brokers, {enriched} existing entries enriched")
    print(f"curated total: {len(d['brokers'])}")


if __name__ == "__main__":
    sys.exit(main())
