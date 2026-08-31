#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Classify brokers by what they actually do, from their own site copy.

WHY THIS EXISTS. The letter that works depends on the category, and by 2026-08-30
that judgement was being made by hand, one broker per tick, by reading a homepage.
It decides which section of _CATEGORY_VARIANTS.md applies, and -- since
_SILENT_FAILURES 195 -- it decides WHICH IDENTIFIERS ARE SAFE TO SEND:

    name-keyed compiler / people-search  -> send everything; a partial search
                                            returns a truthful false negative
    identifier-keyed adtech / measurement -> send name and emails only; a postal
                                            address cannot match and would only
                                            be a disclosure

`make_optout_email.py --keys` reads the `category` field to suggest which. That
field was set on 48 of 1,248 rows, and inferring it from the broker NAME adds
only 48 more (195b): most names are just names. "Bliss Point Media" says nothing,
and it is CTV measurement.

So this reads the site instead. Title, meta description and the first few
thousand characters of visible text, matched against category vocabulary.

HONESTY ABOUT WHAT THIS PRODUCES. Every category written here is stamped
`category_source: "site_classifier <date>"`, and existing hand-set categories are
never overwritten. A reader -- including a later me -- cannot otherwise tell a
checked claim from a guessed one once both sit in the same field, which is the
mistake 192 was written about.

AND IT DOES NOT DECIDE ANYTHING. The category feeds a SUGGESTION. Choosing to
minimise an identifier set stays an explicit human act, because the two failure
modes are not symmetric: over-sending is a bounded disclosure, under-sending
draws a truthful "no record found" that is false and terminal (161a, 194).

    ./classify_brokers.py --pending        # classify pending rows only
    ./classify_brokers.py --ids a,b,c
    ./classify_brokers.py --apply          # write results; otherwise dry-run
"""
import argparse, json, re, subprocess, sys
import concurrent.futures as cf
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import state  # noqa: E402

CURATED = ROOT / "data" / "curated_brokers.json"

# ORDER MATTERS AND THE ORDER IS DEFENSIVE.
#
# First match wins, so the categories that must not be missed go first. The
# asymmetry from 195 decides the ordering: labelling a people-search site as
# adtech would make the tool suggest a MINIMISED identifier set, and a partial
# search against a name-keyed file returns a truthful "no record found" that is
# simply wrong and terminal. Labelling an adtech firm as people-search only
# costs an over-disclosure the sender chose. So the dangerous mislabel is
# people-search -> adtech, and people_search is therefore tested first.
#
# The first draft put adtech first AND matched on the bare word "cookie".
# Spokeo came back as adtech, because every site on the internet has a cookie
# banner. That is precisely the failure this ordering exists to prevent, and it
# was caught on the fifth test row rather than on the five hundredth letter.
# "cookie" and "maid" are gone: too generic to carry any weight.
#
# Vocabulary is drawn from how these companies describe themselves, not from
# how a critic would describe them.
RULES = [
    ("people_search", r"\b(people ?search|background ?check|public ?records|court ?records|"
                      r"people ?finder|reverse ?phone|phone ?lookup|address ?lookup|"
                      r"criminal ?record|arrest ?record|inmate|mugshot|find (anyone|people)|"
                      r"search for people|locate people|skip ?trac)"),
    ("screening", r"\b(consumer reporting agency|tenant screening|employment screening|"
                  r"pre[- ]?employment|fair credit reporting|background screening|"
                  r"credit header|prescreen)"),
    ("adtech", r"\b(dsp\b|ssp\b|ad exchange|programmatic|demand[- ]side|supply[- ]side|"
               r"bid ?stream|real[- ]time bidding|ad server|retarget|dmp\b|"
               r"data management platform|audience platform|identity resolution|"
               r"identity graph|attribution|connected tv|ctv\b|household graph|"
               r"media measurement|ad tech|adtech)"),
    ("b2b_contact", r"\b(b2b\b|sales intelligence|prospecting|lead generation|contact data|"
                    r"firmographic|intent data|account intelligence|sales leads|"
                    r"go[- ]to[- ]market|revenue intelligence|business contacts)"),
    ("list_broker", r"\b(list broker|list management|mailing list|direct mail|list rental|"
                    r"data card|list services|postal list|response list)"),
    ("compiler", r"\b(data compiler|consumer data|marketing data|data enrichment|"
                 r"data append|audience data|database marketing|consumer database|"
                 r"data solutions|data provider|third[- ]party data)"),
]


# A null verdict used to mean two unrelated things: "I read the page and none of the
# vocabulary matched" and "I never saw the page." _SILENT_FAILURES 212 read 53 nulls as
# the first and concluded something about all of them; 13 were actually the second --
# 8 empty responses, 3 near-empty, 2 Cloudflare interstitials. Same structural mistake
# as 206 and 199: one value standing for both a finding and the absence of one.
#
# fetch() now returns (text, outcome) and the outcomes are reported separately.
_CHALLENGE = ("just a moment", "enable javascript and cookies", "checking your browser",
              "attention required", "verifying you are human", "ddos protection by",
              "access denied", "cf-browser-verification")


def fetch(url):
    """-> (visible_text, outcome). outcome is one of: ok, empty, thin, challenge."""
    text = visible(url)
    low = text.lower()
    if not text.strip():
        return text, "empty"
    if any(c in low for c in _CHALLENGE) and len(text) < 1200:
        return text, "challenge"
    if len(text) < 400:
        return text, "thin"
    return text, "ok"


def visible(url):
    try:
        h = subprocess.run(
            ["curl", "-sL", "--compressed", "--max-time", "14",
             "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/120 Safari/537.36", url],
            capture_output=True, text=True, timeout=20, errors="replace").stdout
    except Exception:
        return ""
    if not h:
        return ""
    h = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", h)
    return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]*>", " ", h))[:6000]


def classify(text):
    low = text.lower()
    for cat, pat in RULES:
        if re.search(pat, low):
            return cat
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pending", action="store_true")
    ap.add_argument("--ids")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    doc = json.loads(CURATED.read_text())
    rows = doc["brokers"]
    by_id = {b["id"]: b for b in rows}

    targets = [b for b in rows if b.get("domain") and not b.get("category")]
    if args.ids:
        want = {i.strip() for i in args.ids.split(",")}
        targets = [b for b in rows if b["id"] in want]
    elif args.pending:
        st = json.loads(state("removal_status.json").read_text())
        st = st.get("brokers", st)
        def status(i):
            r = st.get(i)
            return (r.get("status") if isinstance(r, dict) else r) or "pending"
        targets = [b for b in targets if status(b["id"]) == "pending"]
    if args.limit:
        targets = targets[:args.limit]

    print(f"classifying {len(targets)} broker(s) from site copy\n")
    found = {}

    unread = {}

    def one(b):
        text, outcome = fetch("https://" + b["domain"])
        return b["id"], (classify(text) if outcome == "ok" else None), outcome

    with cf.ThreadPoolExecutor(12) as ex:
        for bid, cat, outcome in ex.map(one, targets):
            if outcome != "ok":
                unread[bid] = outcome
            elif cat:
                found[bid] = cat
                print(f"  {bid:<40} {cat}")

    read = len(targets) - len(unread)
    print(f"\n{len(found)}/{read} classified of {read} page(s) actually read")
    if unread:
        # NOT counted as unclassified: nothing was read, so nothing was concluded.
        print(f"{len(unread)} site(s) could not be read -- these are NOT nil results:")
        from collections import Counter as _C
        for o, n in _C(unread.values()).most_common():
            print(f"  {n:>4}  {o}")
        for bid, o in sorted(unread.items()):
            print(f"        {o:<10} {bid}")
    from collections import Counter
    for c, n in Counter(found.values()).most_common():
        print(f"  {n:>4}  {c}")

    if not args.apply:
        print("\ndry run — pass --apply to write")
        return 0

    stamp = f"site_classifier {date.today().isoformat()}"
    for bid, cat in found.items():
        b = by_id[bid]
        if b.get("category"):      # never overwrite a hand-set value
            continue
        b["category"] = cat
        b["category_source"] = stamp
    CURATED.write_text(json.dumps(doc, indent=2, ensure_ascii=False))
    print(f"\nwrote {len(found)} categories, each stamped '{stamp}'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
