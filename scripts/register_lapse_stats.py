#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Does a lapsed data-broker registration predict anything about the outcome?

_SILENT_FAILURES 357 suggested it should: eMerges deregistered in California
after 2024, wound the business down, and kept receiving removal requests from
directories built out of the stale register. The obvious inference was that a
lapsed registration marks a company that has stopped answering.

This measures that instead of assuming it, because the inference turns out to be
half wrong -- and the wrong half is the one that would have changed behaviour.

Two rates, split on whether the most recent filing on record is the latest
register year or the one before it:

    ANSWER RATE       of the rows actually written to, how many produced any
                      substantive response at all (replied / acknowledged /
                      confirmed / not_found / suppressed / covered_by_sibling)
    DEAD-ROUTE RATE   how many of the whole cohort ended up unreachable or failed

Run it after any register refresh. If the answer rates ever diverge materially,
that is new information and 359 needs rewriting.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import state  # noqa: E402

ANSWERED = {"replied", "acknowledged", "confirmed", "not_found",
            "suppressed", "covered_by_sibling"}
SENT = ANSWERED | {"submitted", "email_pending"}
DEAD = {"unreachable", "failed"}


def main():
    prof = json.loads((ROOT / "data" / "register_profiles.json").read_text())
    st = json.loads(state("removal_status.json").read_text())

    years = {}
    for k, filings in prof.items():
        ys = [f.get("year") for f in filings if f.get("year")]
        if ys:
            years[k] = max(ys)
    if not years:
        sys.exit("no filing years on record")

    latest = max(years.values())
    prior = str(int(latest) - 1)
    cohorts = {
        f"lapsed (last filed {prior})": {k for k, y in years.items() if y == prior},
        f"current (filed {latest})": {k for k, y in years.items() if y == latest},
    }

    print(f"register snapshot: latest filing year on record is {latest}\n")
    rows = []
    for label, group in cohorts.items():
        sent = [k for k in group if (st.get(k) or {}).get("status") in SENT]
        ans = [k for k in sent if st[k]["status"] in ANSWERED]
        dead = [k for k in group if (st.get(k) or {}).get("status") in DEAD]
        rows.append((label, len(group), len(sent), len(ans), len(dead)))

    print(f"{'cohort':32s} {'n':>5} {'written':>8} {'answered':>9} {'rate':>7} "
          f"{'dead route':>11} {'rate':>7}")
    for label, n, sent, ans, dead in rows:
        ar = f"{100*ans/sent:.1f}%" if sent else "-"
        dr = f"{100*dead/n:.1f}%" if n else "-"
        print(f"{label:32s} {n:5d} {sent:8d} {ans:9d} {ar:>7} {dead:11d} {dr:>7}")

    print()
    print("  Read it this way: a lapsed registration predicts a DEAD ROUTE, not a")
    print("  dead company. The companies that lapse are far likelier to have lost")
    print("  their domain or mailbox -- which is what lapsed_scan.py exists to")
    print("  catch. But the ones still reachable answer about as often as anyone")
    print("  else. Deregistering is not the same act as ceasing to reply, and it is")
    print("  emphatically not the same act as ceasing to hold the data: eMerges")
    print("  deregistered, wound down, and still holds twenty-five years of records")
    print("  under a legal preservation obligation. See 357, 359.")


if __name__ == "__main__":
    main()
