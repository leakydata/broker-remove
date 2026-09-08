#!/usr/bin/env python3
"""What the ledger has already told itself to do.

Notes in removal_status.json routinely end with a commitment: "next move is X",
"diarise for October", "watch for the completion notice". Nothing surfaces
those. They are a to-do list written into prose and then never read again —
which is how one row sat with a next-step that had already been carried out,
and another sat nineteen days past the trigger its own note had set.

This is the ledger's half of what handoff.py does for the human queue. It does
NOT decide anything: every line is a lead pointing at a note to read, in the
row's own words.

ON WHAT IT CANNOT DO, because four keyword classifiers over free text
over-reported in one day (SF 410): this matches the LANGUAGE OF COMMITMENT, not
the state of the world. A row whose next step was done yesterday still says
"next move is" until somebody rewrites the note. So treat every line as "go
read this row", never as "this is outstanding". The count at the bottom is
deliberately absent.
"""
import json
import re
import sys
from datetime import date

OPEN = {"submitted", "manual_required", "captcha_blocked", "failed",
        "replied", "acknowledged", "email_pending"}

# a sentence that commits to something later
TRIGGER = re.compile(
    r"[^.]*\b(next (?:move|step)\s*(?:is|:)|diaris\w+|re-?check\b|"
    r"watch for|follow up (?:in|when|after|on)|worth (?:a )?re-?test|"
    r"when (?:they|it) (?:answer|repl)|if (?:that|this) goes unanswered)"
    r"\b[^.]*\.", re.I)

# rough month words, so October items can be held back until October
MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], 1)}
MONTH_RE = re.compile("|".join(MONTHS), re.I)

WAITING = re.compile(r"watch for|when (?:they|it) (?:answer|repl)|"
                     r"if (?:that|this) goes unanswered", re.I)


def main():
    data = json.load(open("data/removal_status.json"))
    recs = data.get("records", data)
    today = date.today()

    due, later, waiting = [], [], []
    for k, v in sorted(recs.items()):
        if v.get("status") not in OPEN:
            continue
        note = v.get("note") or ""
        m = TRIGGER.search(note)
        if not m:
            continue
        sentence = re.sub(r"\s+", " ", m.group(0)).strip()
        month_hit = MONTH_RE.search(sentence)
        row = (k, v.get("status"), sentence)
        if WAITING.search(sentence):
            waiting.append(row)
        elif month_hit:
            mo = MONTHS[month_hit.group(0).lower()]
            (due if mo <= today.month else later).append(row + (month_hit.group(0),))
        else:
            due.append(row)

    def show(title, rows, note=""):
        if not rows:
            return
        print(f"\n=== {title}")
        if note:
            print(f"    {note}")
        for r in rows:
            k, st, sent = r[0], r[1], r[2]
            when = f"  [{r[3]}]" if len(r) > 3 else ""
            print(f"\n  {k}  ({st}){when}")
            print(f"    {sent[:300]}")

    show("READ THESE — a commitment with no date, or a date now past",
         due, "Go read the row. The note may already have been acted on.")
    show("WAITING ON THEM — nothing to do until something arrives", waiting)
    show("DIARISED FOR LATER", later)
    print("\n  Every line is a pointer to a note, not a verdict. See SF 420.\n")


if __name__ == "__main__":
    main()
