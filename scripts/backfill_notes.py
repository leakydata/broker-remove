#!/usr/bin/env python3
"""Recover evidence for statuses adopted from the ledger without any.

The shared ledger (§268) carries only id, status, date and method -- deliberately,
because notes quote broker replies and carry identifiers. So when this agent adopts
the other agent's work, it gets a status and a placeholder:

    "Adopted from the shared ledger: another agent recorded 'submitted'...
     No detail is carried across."

That is honest and it is also an unfalsifiable claim. 113 rows in this tracker
asserted a status with no evidence anywhere in their history -- 109 of them
`submitted`, which is the status the entire coverage figure rests on. validate.py
already refuses a TERMINAL status with no note ("an unfalsifiable claim"), but
`submitted` is not terminal, so those rows sailed past it.

The evidence is not lost, though: the playbooks ARE committed, and the other agent
writes its note there. This lifts `- Note:` out of brokers/<id>.md and files it as
a history entry, so the claim in this tracker is backed by something a reader can
check in git.

It never overwrites a substantive note and never changes a status. Recovery only.
"""
import argparse, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ROOT  # noqa: E402

STATE = ROOT / "data" / "removal_status.json"
NOTE_RE = re.compile(r"^- Note[^:]*:\s*(.+?)(?=\n- |\n\n|\n## |\Z)", re.S | re.M)
# Last-resort evidence: the playbook's own status line. Weaker than a note, but a
# committed "- Current: `submitted` (updated 2026-08-18)" is still a dated,
# checkable assertion in git -- which is more than the ledger placeholder it
# replaces. Recorded as minimal so it is never mistaken for a real account of
# what was sent.
CUR_RE = re.compile(r"^- Current: `([a-z_]+)`(?:\s*\(updated ([0-9-]+)\))?", re.M)


def is_placeholder(note):
    return (note or "").startswith("Adopted from")


def substantive(rec):
    """Does any history entry carry a real note?"""
    return any((h.get("note") or "") and not is_placeholder(h.get("note"))
               for h in rec.get("history", []))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write; otherwise report only")
    ap.add_argument("--min-chars", type=int, default=60,
                    help="ignore playbook notes shorter than this")
    a = ap.parse_args()

    st = json.loads(STATE.read_text())
    recovered, no_playbook, too_thin, conflicts = [], [], [], []

    for bid, rec in st.items():
        if not rec.get("history") or substantive(rec):
            continue
        pb = ROOT / "brokers" / f"{bid}.md"
        if not pb.exists():
            no_playbook.append(bid)
            continue
        body = pb.read_text()
        m = NOTE_RE.search(body)
        text = (m.group(1).strip() if m else "")

        # A DISAGREEMENT IS NOT A GAP. If the playbook asserts a different status
        # than the tracker, recovering its note would attach evidence for one
        # claim to a row making another. Report it and leave the row alone --
        # somebody has to decide which is right, and it is not this script.
        cm = CUR_RE.search(body)
        if cm and cm.group(1) != rec.get("status"):
            conflicts.append((bid, rec.get("status"), cm.group(1)))
            continue

        if len(text) < a.min_chars:
            # A short note is still evidence: "Statutory opt-out/deletion email
            # sent 2026-08-22" says what was sent and when, which is exactly what
            # a `submitted` claim asserts. Take it, and mark it minimal.
            if text:
                recovered.append((bid, text + "  [minimal: this is the whole of "
                                  "what the playbook records]"))
            elif cm and cm.group(2):
                recovered.append((bid, f"No note in the playbook; its status line "
                                  f"records `{cm.group(1)}` as of {cm.group(2)}. "
                                  f"That is the whole of the evidence for this row."))
            else:
                too_thin.append(bid)
            continue
        recovered.append((bid, text))

    print(f"rows asserting a status with no evidence: "
          f"{len(recovered) + len(no_playbook) + len(too_thin)}")
    print(f"  recoverable from a committed playbook : {len(recovered)}")
    print(f"  playbook exists but the note is thin  : {len(too_thin)}")
    print(f"  no playbook at all                    : {len(no_playbook)}")
    if no_playbook:
        print("     " + ", ".join(sorted(no_playbook)[:10]))
    if conflicts:
        print(f"\n  !! {len(conflicts)} row(s) where the PLAYBOOK DISAGREES with "
              f"the tracker -- left untouched, these need a decision:")
        for bid, tr, pb in conflicts:
            print(f"     {bid:<34} tracker={tr:<12} playbook={pb}")

    if not a.apply:
        print("\n(report only -- pass --apply to write)")
        return 0

    for bid, text in recovered:
        rec = st[bid]
        last = rec["history"][-1]
        rec["history"].append({
            "at": last.get("at"),          # the ledger's date, not now: this is
                                           # recovery of an existing fact, not a
                                           # new event. Stamping it today would
                                           # make the send look like it happened
                                           # today -- the §268 bug the other agent
                                           # fixed in sync_status for the same
                                           # reason.
            "status": rec.get("status"),
            "via": last.get("via"),
            "note": ("Recovered from the committed playbook brokers/"
                     f"{bid}.md, because the ledger carries no notes and this "
                     "row's status had no evidence behind it: " + text),
        })
        rec["note"] = rec["history"][-1]["note"]
    STATE.write_text(json.dumps(st, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwrote {len(recovered)} recovered note(s) to "
          f"{STATE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
