#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Decide what to send next, across two competing queues.

There are two backlogs and they are not interchangeable:

  NEW brokers      -- never contacted. Each letter opens a whole unexplored
                      holding, but the contact address is unproven and may bounce.
  SUPPLEMENTS      -- already contacted before the identifier list grew, so their
                      "no records found" answered a narrower question than we
                      thought (see _SILENT_FAILURES.md #103). The address is known
                      good and the thread already exists.

Naive orderings get this wrong in both directions. Doing all supplements first
stalls new coverage for days. Doing all new brokers first leaves the largest
compilers holding records under the four identifiers that BDEX demonstrated are
the ones that actually match.

The policy encoded here:

  1. HIGH-PRIORITY SUPPLEMENTS FIRST (priority >= 3). Only ~28 exist, and they
     are the aggregators -- Epsilon, LexisNexis, Intelius, BeenVerified and the
     like. A record surviving at a supplier propagates downstream to everyone it
     sells to, so these are worth more per letter than anything else in either
     queue.
  2. THEN INTERLEAVE the rest, alternating supplement / new. Neither backlog
     starves, and a bad run in one does not stop the other.
  3. LOW-PRIORITY NEW BROKERS LAST (priority <= 1).

Usage:
    ./send_plan.py --size 12            # JSON-ish plan for the next 12
    ./send_plan.py --size 12 --summary  # human-readable
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from paths import state  # noqa: E402

REGISTRY = ROOT / "data" / "brokers.json"
CUTOVER = "2026-08-20"          # first contact before this used the short list
SUPPLEMENTABLE = {"submitted", "not_found", "confirmed"}
ACTED = {"submitted", "confirmed", "not_found",
         "manual_required", "captcha_blocked", "failed"}


def first_contact(rec):
    ds = [(e.get("at") or "")[:10] for e in (rec.get("history") or [])
          if e.get("status") in ACTED]
    ds = [d for d in ds if d]
    return min(ds) if ds else None


def build():
    reg = {b["id"]: b for b in json.loads(REGISTRY.read_text())["brokers"]}
    sp = state("removal_status.json")
    st = json.loads(sp.read_text()) if sp.exists() else {}

    supplements, new = [], []
    for bid, b in reg.items():
        if not b.get("email_to") or b.get("duplicate_of"):
            continue
        rec = st.get(bid, {})
        status = rec.get("status", "pending")
        pri = b.get("priority") or 0

        if status == "pending":
            new.append((pri, bid, b, "new"))
        elif (status in SUPPLEMENTABLE
              and not rec.get("supplemented")
              # A broker can be covered by a letter sent to a sibling brand or to
              # a shared contact address. Recording that as a skip is a decision,
              # not a gap -- without this the planner re-offers it every tick and
              # the same judgement gets made again, or worse, a duplicate goes out.
              and not rec.get("supplement_skipped")):
            d = first_contact(rec)
            if d and d < CUTOVER:
                supplements.append((pri, bid, b, "supplement"))

    supplements.sort(key=lambda t: (-t[0], t[1]))
    new.sort(key=lambda t: (-t[0], t[1]))

    hi_supp = [t for t in supplements if t[0] >= 3]
    lo_supp = [t for t in supplements if t[0] < 3]
    mid_new = [t for t in new if t[0] >= 2]
    lo_new = [t for t in new if t[0] < 2]

    plan = list(hi_supp)                      # 1. aggregators, supplemented
    for a, b_ in zip(lo_supp, mid_new):       # 2. interleave, neither starves
        plan += [a, b_]
    tail = lo_supp[len(mid_new):] + mid_new[len(lo_supp):]
    plan += tail
    plan += lo_new                            # 3. long tail of low-priority new
    return plan, len(hi_supp), len(supplements), len(new)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=12)
    ap.add_argument("--summary", action="store_true")
    args = ap.parse_args()

    plan, n_hi, n_supp, n_new = build()
    print(f"{n_supp} supplement(s) outstanding ({n_hi} high-priority), "
          f"{n_new} new broker(s) never contacted", file=sys.stderr)

    batch = plan[: args.size]
    if args.summary:
        for pri, bid, b, kind in batch:
            print(f"  {kind:10} p{pri}  {bid:38} {b['email_to']}", file=sys.stderr)
        return
    print(json.dumps([{"id": bid, "kind": kind, "priority": pri,
                       "name": b.get("name", bid), "to": b["email_to"]}
                      for pri, bid, b, kind in batch], indent=2))


if __name__ == "__main__":
    main()
