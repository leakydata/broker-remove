#!/usr/bin/env python3
"""Produce the next batch of statutory removal emails to send.

Sending is deliberately paced. A personal mailbox tops out around 500 recipients
a day, and a sudden burst of near-identical messages is what spam heuristics look
for -- getting the sending account limited costs more than the batch gains. Work
through the list steadily instead.

Emits JSON on stdout: [{id, name, to, subject, body}, ...]

Usage:
    ./queue_batch.py --size 15
    ./queue_batch.py --size 15 --min-priority 3
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_optout_email import TEMPLATE, CONTACT_NOTE, load_profile  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "brokers.json"
STATE = ROOT / "data" / "removal_status.json"

# Statuses meaning "already handled -- don't re-contact".
DONE = {"submitted", "confirmed", "not_found", "unreachable", "email_pending"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=15)
    ap.add_argument("--min-priority", type=int, default=1)
    ap.add_argument("--summary", action="store_true",
                    help="print a human summary instead of JSON")
    args = ap.parse_args()

    brokers = json.loads(REGISTRY.read_text())["brokers"]
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    prof = load_profile()

    pool = [
        b for b in brokers
        if b.get("email_to")
        and b.get("priority", 0) >= args.min_priority
        and state.get(b["id"], {}).get("status", "pending") not in DONE
    ]
    # Highest leverage first: aggregators before niche sites.
    pool.sort(key=lambda b: (-b.get("priority", 0), b["id"]))
    batch = pool[: args.size]

    out = []
    for b in batch:
        subject = ("Consumer Request to Delete and Opt Out of Sale of "
                   f"Personal Information — {prof['name']}")
        body = TEMPLATE.format(
            to=b["email_to"], broker=b.get("name", b["id"]),
            contact=prof["email"], contact_note="", **prof)
        # Drop the To:/Subject: header lines -- the mail tool sets those.
        body = body.split("\n", 2)[2].lstrip("\n")
        out.append({"id": b["id"], "name": b.get("name", b["id"]),
                    "to": b["email_to"], "priority": b.get("priority"),
                    "subject": subject, "body": body})

    if args.summary:
        print(f"{len(pool)} brokers still to contact by email; "
              f"showing next {len(out)}\n")
        for r in out:
            print(f"  p{r['priority']}  {r['id']:32} {r['to']}")
    else:
        json.dump(out, sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
