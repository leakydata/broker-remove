#!/usr/bin/env python3
"""Which requests are approaching or past the period a company would apply?

948 rows sit at `submitted` with no reply. Until now there was no way to tell
which of those are simply young and which have gone quiet past the point where a
response was due -- so follow-ups went out when something reminded me, which is
not a schedule.

TWO CAUTIONS BUILT INTO THE OUTPUT, because getting this wrong would mean
accusing companies of breaches they have not committed:

  1. The subject is a PENNSYLVANIA resident and Pennsylvania has no comprehensive
     consumer privacy statute. So the 45-day CCPA period is not automatically a
     legal deadline for this requester -- it is the period the company would apply
     to a Californian, and which many have said in writing they apply to everyone.
     This tool says "past the period" and never "in breach".

  2. The clock runs from RECEIPT, not from sending. A letter that bounced, sat in
     a spam folder (SILENT_FAILURES 281) or was never delivered has no clock at
     all. Rows whose only evidence is a send are marked accordingly.

Periods used:
  CCPA  Cal. Civ. Code 1798.130(a)(2): 45 days, extendable once by a further 45
        with notice to the consumer.
  GDPR  Art 12(3): one month, extendable by two further months for complex
        requests, with notice within the first month.
"""
import argparse, json, sys, datetime, collections
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ROOT  # noqa: E402

STATE = ROOT / "data" / "removal_status.json"

# Statuses where a response is still owed. `replied` and the terminal outcomes
# are excluded: the company has answered, whatever the answer was.
AWAITING = {"submitted", "acknowledged", "email_pending"}

CCPA_DAYS = 45
CCPA_EXTENDED = 90
GDPR_DAYS = 30


def sent_date(rec):
    """Earliest history entry that looks like the request going out."""
    for h in rec.get("history", []):
        if h.get("status") in ("submitted", "acknowledged") and h.get("at"):
            return h["at"][:10]
    h = rec.get("history") or []
    return (h[0].get("at") or "")[:10] if h else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--today", default="", help="YYYY-MM-DD, for testing")
    ap.add_argument("--window", type=int, default=10,
                    help="days before the CCPA period to start flagging")
    ap.add_argument("--limit", type=int, default=40)
    a = ap.parse_args()

    today = (datetime.date(*map(int, a.today.split("-"))) if a.today
             else datetime.date.today())
    st = json.loads(STATE.read_text())

    rows = []
    for bid, rec in st.items():
        if rec.get("status") not in AWAITING:
            continue
        d = sent_date(rec)
        if not d:
            continue
        try:
            when = datetime.date(*map(int, d.split("-")))
        except ValueError:
            continue
        age = (today - when).days
        rows.append((age, bid, rec.get("status"), d))

    rows.sort(reverse=True)
    tally = collections.Counter()
    for age, *_ in rows:
        tally["past-extended" if age > CCPA_EXTENDED
              else "past-45" if age > CCPA_DAYS
              else "past-30" if age > GDPR_DAYS
              else "due-soon" if age > CCPA_DAYS - a.window
              else "young"] += 1

    print(f"awaiting a response: {len(rows)} row(s), as at {today}")
    for k, label in (("past-extended", f"past {CCPA_EXTENDED}d (CCPA extended)"),
                     ("past-45", f"past {CCPA_DAYS}d (CCPA)"),
                     ("past-30", f"past {GDPR_DAYS}d (GDPR one month)"),
                     ("due-soon", f"within {a.window}d of the CCPA period"),
                     ("young", "still inside every period")):
        if tally[k]:
            print(f"  {label:<38} {tally[k]:4}")

    actionable = [r for r in rows if r[0] > GDPR_DAYS - a.window]
    if not actionable:
        oldest = rows[0][0] if rows else 0
        print(f"\nNothing is chaseable yet -- the oldest request is {oldest} days "
              f"old.\nThe earliest rows reach the {CCPA_DAYS}-day mark on "
              f"{(today + datetime.timedelta(days=CCPA_DAYS - oldest)).isoformat()}.")
        return 0

    print(f"\n=== chase list, oldest first")
    for age, bid, status, d in actionable[:a.limit]:
        print(f"  {age:4}d  {bid:<34} {status:<14} sent {d}")
    if len(actionable) > a.limit:
        print(f"  ... and {len(actionable) - a.limit} more")

    print("\n  note: the subject is a Pennsylvania resident and PA has no "
          "comprehensive statute.\n  These are the periods a company would apply "
          "to a Californian or an EU resident,\n  not deadlines this requester can "
          "enforce -- and the clock runs from RECEIPT,\n  which a bounce or a spam "
          "folder (SF 281) means may never have started.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
