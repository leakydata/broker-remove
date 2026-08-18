#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Find brokers that share a privacy contact, and say what that means for work.

A broker whose published privacy address lives on *another* broker's domain is
telling you something it did not mean to: the two are run by the same people, or
at least handled by the same desk. `sheriffsdepartment.net` publishing an address
at `truthfinder.com` is not a coincidence, and neither is a state-by-state
network of fifty-one sites all pointing at one mailbox.

Why this is worth automating rather than noticing by eye:

  - **It saves letters.** Fifty-one separate requests to one desk is fifty-one
    tickets, fifty-one identity verifications, and fifty-one chances to be told
    no. One letter naming all fifty-one is a single ticket with an unambiguous
    scope. The daily send cap makes this the difference between a week of work
    and an afternoon.
  - **It finds the ones already covered.** A pending broker whose contact belongs
    to a broker you have already written to is probably not pending at all -- but
    only if your letter named it. That distinction is the whole point, and it is
    the thing this script will not decide for you.
  - **It surfaces the gaps.** A sibling nobody named is a sibling nobody removed,
    and it looks identical to one that was.

The output groups by the contact address and marks each member with its status,
so a group where the parent is `submitted` and a sibling is `pending` is visible
at a glance. That is the case worth acting on: reply on the existing ticket
naming the sibling, rather than opening a new one.

    ./family_scan.py                 # every shared-contact group
    ./family_scan.py --actionable    # only groups with an uncovered sibling
    ./family_scan.py --min-size 3
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "brokers.json"
STATE = ROOT / "data" / "removal_status.json"

# Statuses meaning a request has reached the desk that handles this contact.
REACHED = {"submitted", "confirmed", "not_found", "email_pending"}


def norm(d):
    return (d or "").strip().lower().removeprefix("www.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--actionable", action="store_true",
                    help="only groups where some member is still pending")
    ap.add_argument("--min-size", type=int, default=2)
    a = ap.parse_args()

    brokers = json.loads(REGISTRY.read_text())["brokers"]
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    owner_of = {}
    for b in brokers:
        d = norm(b.get("domain"))
        if d:
            owner_of.setdefault(d, b["id"])

    groups = defaultdict(list)
    verified = {}
    for b in brokers:
        email = (b.get("email_to") or "").strip().lower()
        if "@" not in email:
            continue
        groups[email].append(b["id"])
        # Any member's verification evidence describes the shared address.
        if b.get("email_verified"):
            verified[email] = True
        verified.setdefault(email, False)

    rows = []
    for email, members in groups.items():
        if len(members) < a.min_size:
            continue
        statuses = {m: state.get(m, {}).get("status", "pending") for m in members}
        pending = [m for m, s in statuses.items() if s not in REACHED]
        reached = [m for m, s in statuses.items() if s in REACHED]
        if a.actionable and not (pending and reached):
            continue
        rows.append((email, owner_of.get(email.split("@")[1]), members,
                     statuses, pending, reached, verified.get(email, False)))

    rows.sort(key=lambda r: (-len(r[4]), -len(r[2])))
    for email, owner, members, statuses, pending, reached, ok in rows:
        head = f"{email}  ({len(members)} broker(s)"
        head += f", contact domain owned by '{owner}'" if owner else ""
        print(f"\n{head})")
        if not ok and len(members) > 1:
            # Consolidating is a force multiplier in both directions. An address
            # nobody has confirmed, shared by a dozen brokers, turns one bad
            # contact into a dozen requests that were never received -- and every
            # one of them looks submitted.
            print(f"  UNVERIFIED CONTACT: {len(members)} broker(s) route here and "
                  f"nothing confirms this address works.")
            print("  Verify it before consolidating: scripts/verify_emails.py --ids "
                  + ",".join(sorted(members)[:3]) + " ...")
        if pending and reached:
            print(f"  ACTIONABLE: {len(reached)} already written to, "
                  f"{len(pending)} not covered unless your letter named them.")
            print(f"  Reply on the existing ticket naming: {', '.join(sorted(pending))}")
        for m in sorted(members):
            mark = " " if statuses[m] in REACHED else "*"
            print(f"   {mark} {m:34} {statuses[m]}")

    total_pending = sum(len(r[4]) for r in rows)
    unverified = sum(len(r[2]) for r in rows if not r[6])
    print(f"\n{len(rows)} shared-contact group(s) | "
          f"{total_pending} member(s) still pending | "
          f"{unverified} member(s) behind an unverified contact")
    print("* = pending. A sibling your letter did not name is a sibling nobody removed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
