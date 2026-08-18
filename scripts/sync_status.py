#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Share what has been done, without sharing who it was done for.

Two agents are working this project — a local session and a scheduled cloud one —
and they cannot see each other. `data/removal_status.json` holds the truth about
what has been sent, but it is gitignored for good reason: its notes quote broker
replies verbatim and carry addresses, telephone numbers and ticket references.

So each agent has been running from its own private copy of reality. Today that
produced a duplicate letter to one broker and a daily send cap counted twice, and
it will get worse: neither can tell whether a `pending` broker is genuinely
untouched or was contacted an hour ago by the other one.

The fix is a **ledger, not a copy**. This writes `data/removal_ledger.json`
containing only:

    broker id · status · date of the last status change · how it was contacted

No notes, no quotes, no identifiers, no ticket numbers. Nothing that redact.py
would object to, because there is nothing personal in it — the id and the status
are facts about a *company*, not about a person.

    ./sync_status.py            # regenerate the ledger from the private tracker
    ./sync_status.py --check    # report divergence without writing
    ./sync_status.py --merge    # fold the committed ledger back into the tracker

The --merge direction is what makes it useful to the agent that did *not* do the
work: any broker the ledger shows as contacted, but which is `pending` locally,
is adopted as `submitted` with a note saying where it came from. It never
overwrites a richer local record, because a status you established yourself with
a broker's own reply is better evidence than a line in a shared file.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIVATE = ROOT / "data" / "removal_status.json"
LEDGER = ROOT / "data" / "removal_ledger.json"

# Ranked worst-to-best. A merge never downgrades: an outcome you obtained from
# the broker outranks another agent's report that a letter went out.
RANK = ["pending", "manual_required", "captcha_blocked", "email_pending",
        "submitted", "failed", "unreachable", "still_listed", "gone",
        "not_found", "confirmed"]


def rank(s):
    return RANK.index(s) if s in RANK else 0


def last_change(rec):
    """Date the status last actually moved, as YYYY-MM-DD."""
    prev, when = None, rec.get("updated", "")
    for h in rec.get("history", []):
        if h.get("status") and h["status"] != prev:
            when, prev = h.get("at", when), h["status"]
    return (when or "")[:10]


def build(private):
    out = {}
    for bid, rec in private.items():
        status = rec.get("status", "pending")
        if status == "pending":
            continue
        vias = [h.get("via") for h in rec.get("history", []) if h.get("via")]
        out[bid] = {
            "status": status,
            "changed": last_change(rec),
            "via": vias[-1] if vias else None,
        }
    return dict(sorted(out.items()))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    ap.add_argument("--merge", action="store_true",
                    help="adopt the committed ledger into the private tracker")
    a = ap.parse_args()

    private = json.loads(PRIVATE.read_text()) if PRIVATE.exists() else {}
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}

    if a.merge:
        adopted = []
        for bid, entry in ledger.items():
            rec = private.setdefault(bid, {"status": "pending", "history": []})
            if rank(entry["status"]) <= rank(rec.get("status", "pending")):
                continue          # ours is equal or better; leave it alone
            rec["status"] = entry["status"]
            rec["updated"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            rec.setdefault("history", []).append({
                "at": rec["updated"],
                "status": entry["status"],
                "via": entry.get("via"),
                "note": (f"Adopted from the shared ledger: another agent recorded "
                         f"'{entry['status']}' on {entry['changed']}. No detail is "
                         f"carried across — re-read the broker's own reply before "
                         f"relying on this."),
            })
            adopted.append(bid)
        if adopted:
            PRIVATE.write_text(json.dumps(private, indent=2, ensure_ascii=False) + "\n")
        print(f"adopted {len(adopted)} broker(s) from the ledger"
              + (f": {', '.join(adopted[:12])}" if adopted else ""))
        return 0

    fresh = build(private)
    added = sorted(set(fresh) - set(ledger))
    changed = sorted(b for b in set(fresh) & set(ledger)
                     if fresh[b]["status"] != ledger[b]["status"])
    missing = sorted(set(ledger) - set(fresh))

    print(f"ledger: {len(ledger)} entries | tracker: {len(fresh)} acted-on")
    if added:
        print(f"  +{len(added)} not yet shared: {', '.join(added[:12])}"
              + (" ..." if len(added) > 12 else ""))
    if changed:
        print(f"  ~{len(changed)} status changed: {', '.join(changed[:12])}")
    if missing:
        print(f"  !{len(missing)} in the ledger but not in this tracker — "
              f"the other agent did these: {', '.join(missing[:12])}"
              + (" ..." if len(missing) > 12 else ""))
        print("     run --merge to adopt them, or they will be contacted twice")

    if a.check:
        return 0
    LEDGER.write_text(json.dumps(fresh, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwrote {LEDGER.relative_to(ROOT)} ({len(fresh)} entries, no personal data)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
