#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Reconstruct the SUBMISSION CHANNEL for rows that never recorded one.

439 of 1,200 rows with a real status carry no `via` anywhere in their history --
they say a request was submitted and cannot say how. While the opt-out route was
alive that was untidy. Once the route rots there is nothing left to reconstruct
from, and the status becomes an assertion nobody can check. See 365.

Two fields already on the record are unambiguous evidence:

    confirmation_ref starting "gmail:"   the reference IS a mail message id
    optout_url_used starting "mailto:"   the route used was an address
    optout_url_used starting "http"      the route used was a page

Anything else is left alone. A bare ticket number like "REQ-224224" or "540175"
is a reference the broker issued and says nothing about which channel produced
it -- portals and mail desks both hand them out.

The reconstructed value is written to `via_inferred` on the RECORD, never into
the history entries. History is a log of what happened at the time; a value
worked out afterwards does not belong in it, and merging the two would make the
1,441 contemporaneous `via` records indistinguishable from these guesses.

Dry run by default. --apply writes, after taking a backup.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import state  # noqa: E402

REAL = {"submitted", "email_pending", "confirmed", "replied", "acknowledged",
        "suppressed", "not_found", "failed", "covered_by_sibling",
        "manual_required", "captcha_blocked"}


def infer(rec):
    ref = str(rec.get("confirmation_ref") or "")
    url = str(rec.get("optout_url_used") or "")
    if ref.startswith("gmail:"):
        return "email", "confirmation_ref is a mail message id"
    if url.startswith("mailto:"):
        return "email", "optout_url_used is a mailto: address"
    if url.startswith("http"):
        return "web", "optout_url_used is an http route"
    return None, None


def main():
    apply = "--apply" in sys.argv
    p = state("removal_status.json")
    st = json.loads(p.read_text())

    todo = []
    for k, rec in st.items():
        if rec.get("status") not in REAL:
            continue
        if any(h.get("via") for h in rec.get("history", [])):
            continue
        if rec.get("via_inferred"):
            continue
        via, why = infer(rec)
        if via:
            todo.append((k, via, why))

    missing = sum(1 for k, r in st.items()
                  if r.get("status") in REAL
                  and not any(h.get("via") for h in r.get("history", []))
                  and not r.get("via_inferred"))

    by = {}
    for _, via, _ in todo:
        by[via] = by.get(via, 0) + 1
    print(f"rows with no channel recorded: {missing}")
    print(f"  reconstructable from evidence on the record: {len(todo)}  {by}")
    print(f"  NOT reconstructable, left alone: {missing - len(todo)}")
    print()
    for k, via, why in sorted(todo)[:12]:
        print(f"  {k:44s} -> {via:6s} ({why})")
    if len(todo) > 12:
        print(f"  ... and {len(todo)-12} more")

    if not apply:
        print("\nDRY RUN. Re-run with --apply to write.")
        return

    backup = p.with_suffix(".json.bak-via")
    shutil.copy2(p, backup)
    for k, via, why in todo:
        st[k]["via_inferred"] = via
        st[k]["via_inferred_basis"] = why
    p.write_text(json.dumps(st, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwrote {len(todo)} via_inferred value(s); backup at {backup.name}")


if __name__ == "__main__":
    main()
