#!/usr/bin/env python3
"""Before asserting something about the corpus, ask the corpus.

Five times in one session I wrote a claim -- into an entry, a letter, or a status
change -- that my own notes already contradicted:

  267a  a finding I had already made twice, met as though new
  278   "the template cannot name the right", with four counterexamples in my notes
  282   a worry about 948 rows that one arithmetic check dissolved
  287   nine live requests downgraded because a mail sat in an inbox
  288   "one of these rows misattributes a ticket ID" -- neither did

Every one had the same shape: a signal observed, a conclusion drawn, the evidence
in `removal_status.json` not consulted. The rule adopted at 267a -- grep the notes
first -- did not hold, because it is a rule about remembering, and the tracker
guard that DID hold is mechanical.

So this makes checking one command instead of a decision:

    ./claimcheck.py L7JE3RVPKK              # which rows mention this?
    ./claimcheck.py 'verification.*clicked'  # regex, case-insensitive
    ./claimcheck.py --count 'suppression list'

It searches every note in every row's history, and prints the row, its status, and
the surrounding text -- which is exactly what I keep failing to look at.
"""
import argparse, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ROOT  # noqa: E402

STATE = ROOT / "data" / "removal_status.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern", help="regex, case-insensitive")
    ap.add_argument("--count", action="store_true", help="row names only")
    ap.add_argument("--context", type=int, default=140)
    ap.add_argument("--limit", type=int, default=25)
    a = ap.parse_args()

    try:
        rx = re.compile(a.pattern, re.I)
    except re.error as e:
        sys.exit(f"bad pattern: {e}")

    st = json.loads(STATE.read_text())
    hits = []
    for bid, rec in sorted(st.items()):
        notes = " || ".join((h.get("note") or "") for h in rec.get("history", []))
        m = rx.search(notes)
        if m:
            hits.append((bid, rec.get("status"), notes, m))

    print(f"{len(hits)} row(s) mention /{a.pattern}/")
    if a.count or not hits:
        if hits:
            print("  " + ", ".join(b for b, *_ in hits))
        return 0

    for bid, status, notes, m in hits[: a.limit]:
        lo = max(0, m.start() - a.context)
        hi = min(len(notes), m.end() + a.context)
        print(f"\n### {bid}  [{status}]")
        print("    ..." + notes[lo:hi].replace("\n", " ") + "...")
    if len(hits) > a.limit:
        print(f"\n  ... and {len(hits) - a.limit} more (raise --limit)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
