#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Find brokers that publish CCPA request-volume metrics, and read them.

_SILENT_FAILURES 320: Semasio's own published metrics table said something no
amount of correspondence had established -- four rights resolving in under a
second, and the one right that reports on CONTENT showing no response time at
all. It took a minute to find and produced a checkable question, which is more
than most of this project's nil results manage.

California requires businesses over a size threshold to publish, annually, the
number of requests received, complied with and denied, and the median days to
respond. That obligation makes the table unusual in this corpus: it is a number
the company did not choose freely, in a format it did not design, about its own
behaviour.

This looks for those tables on the largest brokers we have already written to,
because a metric is only actionable where there is a live thread to put it in.

It reports the URL and the surrounding text, and deliberately does NOT try to
parse the numbers. Table markup varies wildly and a parser that silently
mis-reads a column would manufacture exactly the kind of confident wrong number
_SILENT_FAILURES 301 was written about. A human reads the excerpt.

Usage:
    ./metrics_scan.py --limit 40
    ./metrics_scan.py --limit 40 --json out.json
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from paths import ROOT, state

UA = "Mozilla/5.0 (X11; Linux x86_64) privacy-request-research"

PATHS = [
    "/ccpa-metrics", "/privacy/metrics", "/legal/privacy-metrics",
    "/privacy-metrics", "/ccpa-request-metrics", "/legal/ccpa-metrics",
    "/privacy", "/privacy-policy", "/legal/privacy-policy",
    "/privacy-center", "/legal/privacy-choices", "/your-privacy-choices",
]

# A metrics table says all of: how many came in, how many were acted on, how long.
SIGNALS = [
    re.compile(r"requests?\s+received", re.I),
    re.compile(r"complied\s+with|fulfil?led\s+in\s+whole|in\s+whole\s+or\s+in\s+part", re.I),
    re.compile(r"median\s+(number\s+of\s+)?days|mean\s+number\s+of\s+days|median\s+response", re.I),
    re.compile(r"requests?\s+to\s+(know|delete|opt[- ]out)", re.I),
]


def fetch(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(700_000).decode("utf-8", "replace")


def strip(html):
    html = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html)


def probe(b):
    dom = (b.get("domain") or "").strip()
    if not dom:
        return None
    for p in PATHS:
        url = f"https://{dom}{p}"
        try:
            text = strip(fetch(url))
        except Exception:
            continue
        hits = [s.pattern for s in SIGNALS if s.search(text)]
        # Two independent signals, not one -- "requests received" alone appears
        # in ordinary policy prose about how to submit a request.
        if len(hits) >= 2:
            m = SIGNALS[0].search(text) or SIGNALS[2].search(text)
            i = m.start() if m else 0
            return {
                "id": b["id"], "url": url, "signals": len(hits),
                "excerpt": text[max(0, i - 200): i + 900],
            }
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--json")
    a = ap.parse_args()

    reg = json.load(open(ROOT / "data" / "curated_brokers.json"))["brokers"]
    st = json.load(open(state("removal_status.json")))
    # Only brokers we have actually written to: a metric is worth having where
    # there is a thread to put it in.
    live = {"submitted", "replied", "acknowledged", "email_pending", "manual_required"}

    def status(bid):
        r = st.get(bid) or {}
        if isinstance(r, str):
            return r
        if r.get("status"):
            return r["status"]
        h = r.get("history") or []
        return h[-1]["status"] if h else None

    cand = [b for b in reg
            if b.get("domain") and status(b["id"]) in live
            and int(b.get("priority", 0) or 0) >= 3]
    cand.sort(key=lambda b: -int(b.get("priority", 0) or 0))
    cand = cand[:a.limit]
    print(f"probing {len(cand)} broker domain(s) for a published metrics table")

    found = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        for r in ex.map(probe, cand):
            if r:
                found.append(r)
                print(f"\n=== {r['id']}  ({r['signals']} signals)\n{r['url']}\n{r['excerpt'][:700]}")

    print(f"\n{len(found)}/{len(cand)} publish something that looks like a metrics table")
    print("NOTE: signals only. The numbers are NOT parsed -- see the docstring, and SF 301.")
    if a.json:
        json.dump(found, open(a.json, "w"), indent=1)
        print(f"wrote {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
