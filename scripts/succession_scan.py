#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Re-read the sites of brokers we have already closed, looking for a change of owner.

_SILENT_FAILURES 224. Every confirmation in this tracker assumes the company that made
the promise still operates the system the promise was about. An acquisition breaks that
silently, and the artifact least likely to survive a data migration is exactly the one
carrying the promise:

    a deletion that fails to migrate is VISIBLE   -- records missing, somebody notices
    a suppression that fails to migrate is INVISIBLE -- the exclusion table is not
      revenue-generating, is not what anyone tests against, and dropping it makes the
      system look healthier. The only people who could notice are the ones who asked to
      be excluded, who by definition are not looking.

So a `confirmed` row is not durable evidence; it is evidence about a moment. This looks
for the moment having passed.

It was found by hand: zerotoone.ai was a residue row with no category, its homepage said
"ZeroToOne.AI has acquired GroundTruth", and there was an open GroundTruth request. That
is not a repeatable process, hence this.

Outcomes are reported separately from findings, per 214b. A site that cannot be fetched
is NOT a site with no acquisition -- one value must never stand for both a finding and
the absence of one.

    ./succession_scan.py             # terminal rows (confirmed / not_found)
    ./succession_scan.py --all       # every row that has been acted on
"""

import argparse
import concurrent.futures as cf
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from paths import state  # noqa: E402

CURATED = ROOT / "data" / "curated_brokers.json"

# Phrases that indicate the COMPANY changed hands. Ordered loosely by how often they
# turn out to be real.
# Only phrases that can ONLY mean a change of corporate ownership. The first pass
# included r"\ban? [A-Z]\w+ (?:company|business|brand)\b" -- meaning to catch taglines
# like "a Vericast Business" -- and it matched ordinary prose instead: "an indispensable
# asset in any business", "an extension of your business", "a B2B SaaS Brand". Eleven of
# twenty hits were that one rule. Same failure as 196, where the adtech classifier fired
# on the bare word "cookie" because every site has a cookie banner.
#
# "acquisition of" went too: in adtech copy it is nearly always about acquiring
# customers, and NOISE below cannot catch every phrasing of that.
HITS = [
    r"has (?:been )?acquired by",
    r"\bhas acquired\b",
    r"\bwe(?:'ve| have) acquired\b",
    r"is now (?:a )?part of\b",
    r"(?:has |have )?joined forces with",
    r"(?:has |have )?merged with",
    r"\bwholly[- ]owned subsidiary of",
    r"\bfollowing (?:the|our) acquisition\b",
]

# "acquisition" is a marketing word before it is a corporate one. Without these
# exclusions an adtech sweep is almost entirely false positives.
NOISE = re.compile(
    r"(customer|user|client|talent|data|audience|subscriber|lead|traffic|patient|"
    r"member|donor|student|guest)[- ]acquisition", re.I)

CHALLENGE = ("just a moment", "enable javascript and cookies", "checking your browser",
             "attention required", "verifying you are human", "access denied")


def fetch(url):
    """-> (visible_text, outcome). outcome: ok | empty | thin | challenge."""
    try:
        h = subprocess.run(
            ["curl", "-sL", "--compressed", "--max-time", "14",
             "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/120 Safari/537.36", url],
            capture_output=True, text=True, timeout=20, errors="replace").stdout
    except Exception:
        return "", "empty"
    if not h:
        return "", "empty"
    h = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", h)
    t = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]*>", " ", h))[:12000]
    low = t.lower()
    if not t.strip():
        return t, "empty"
    if any(c in low for c in CHALLENGE) and len(t) < 1200:
        return t, "challenge"
    if len(t) < 400:
        return t, "thin"
    return t, "ok"


def find(text):
    """Return a window around the match, or None. Noise is stripped before matching.

    The first version extracted a SENTENCE -- it required a full stop within 160
    characters after the phrase. That silently failed on the one page this tool was
    built for. zerotoone.ai's hero text reads:

        "ZeroToOne.AI has acquired GroundTruth This acquisition brings together
         ZeroToOne's predictive intelligence AI platform and GroundTruth's scaled
         real-world signal network to help enterprises anticipate..."

    -- the next full stop is 254 characters away, because nav and hero copy is not
    punctuated like prose. The scan reported 0 across 81 sites and the zero was an
    artifact of the extractor, not a finding about the sites.

    Caught only because the check was tested against a page known to contain the
    phrase. A clean run proves nothing until you have watched the thing fire (214b).
    """
    clean = NOISE.sub(" ", text)
    for pat in HITS:
        m = re.search(pat, clean, re.I)
        if m:
            a, b = max(0, m.start() - 110), min(len(clean), m.end() + 190)
            return re.sub(r"\s+", " ", clean[a:b]).strip()
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true",
                    help="scan every acted-on row, not only terminal ones")
    args = ap.parse_args()

    rows = {b["id"]: b for b in json.loads(CURATED.read_text())["brokers"]}
    st = json.loads(state("removal_status.json").read_text())
    st = st.get("brokers", st)

    want = ({"confirmed", "not_found"} if not args.all
            else {"confirmed", "not_found", "submitted", "manual_required", "email_pending"})
    targets = [rows[i] for i, r in st.items()
               if i in rows and rows[i].get("domain")
               and (r.get("status") if isinstance(r, dict) else r) in want]

    print(f"reading {len(targets)} site(s) for a change of owner\n")
    found, unread = {}, {}

    def one(b):
        text, outcome = fetch("https://" + b["domain"])
        return b["id"], (find(text) if outcome == "ok" else None), outcome

    with cf.ThreadPoolExecutor(10) as ex:
        for bid, hit, outcome in ex.map(one, targets):
            if outcome != "ok":
                unread[bid] = outcome
            elif hit:
                found[bid] = hit
                print(f"  {bid}\n      {hit[:200]}\n")

    read = len(targets) - len(unread)
    print(f"{len(found)} possible succession(s) in {read} site(s) actually read")
    if unread:
        # NOT counted as clean. Nothing was read, so nothing was concluded.
        print(f"{len(unread)} site(s) could not be read -- these are NOT clean results:")
        import collections
        for o, n in collections.Counter(unread.values()).most_common():
            print(f"  {n:>4}  {o}")
    print("\nEvery hit needs reading by a human: this matches marketing copy too, and a "
          "company describing someone else's acquisition looks identical from here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
