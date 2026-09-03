#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Before writing to an address, say what has already been sent to it.

_SILENT_FAILURES 309: priorityoptout@intelius.com received four near-identical
letters in 24 hours, two of them seventeen seconds apart, because four registry
rows resolved to one mailbox and nothing in the send path looked at the mailbox.
297 was the same error at a smaller scale -- Thomson Reuters got the same letter
twice because I read the last inbound without reading the last outbound.

Both are the same blind spot. The tracker is keyed by broker id, so it answers
"has THIS ROW been written to?" -- and that is the wrong question. The recipient
does not experience a row. THE UNIT OF A REQUEST IS THE MAILBOX.

So this prints, for a broker id or a bare address:

  - every other registry row that resolves to the same address, with its status
  - whether those rows were marked sent on different dates, which is the
    signature of separate letters rather than one letter covering the set
  - the verdict, phrased as the decision to make: NEW LETTER or REPLY IN THREAD

It deliberately does not check the mailbox. Sent mail is the authority on what
was actually sent (308 found a registry address that no letter ever went to),
but a script that needs credentials is a script that gets skipped. This runs on
the local files in under a second, which is the only way it gets run at all.

Usage:
    ./mailbox_guard.py fyllo                    # by broker id
    ./mailbox_guard.py privacy@example.com      # by address
    ./mailbox_guard.py --audit                  # every shared address at once
"""

import argparse
import collections
import json
import sys

from paths import ROOT, state

SENT = {"submitted", "email_pending", "confirmed", "replied", "acknowledged", "suppressed"}


def load():
    reg = json.load(open(ROOT / "data" / "curated_brokers.json"))["brokers"]
    # brokers.json carries the uncurated long tail. A row can be written to before it
    # is promoted (safeopt, SF 306), and the guard is useless if it cannot see those.
    seen = {b["id"] for b in reg}
    extra = json.load(open(ROOT / "data" / "brokers.json"))
    for b in (extra["brokers"] if isinstance(extra, dict) and "brokers" in extra else extra):
        if b["id"] not in seen:
            reg.append(b)
    st = json.load(open(state("removal_status.json")))
    return reg, st


def status_of(st, bid):
    rec = st.get(bid)
    if not rec:
        return None, None
    if isinstance(rec, str):
        return rec, None
    cur = rec.get("status")
    hist = rec.get("history") or []
    if not cur and hist:
        cur = hist[-1].get("status")
    first = next((h.get("at", "")[:10] for h in hist if h.get("status") in ("submitted", "email_pending")), None)
    return cur, first


def rows_for(reg, addr):
    return [b for b in reg if (b.get("email_to") or "").strip().lower() == addr]


def report(reg, st, addr, quiet=False):
    rows = rows_for(reg, addr)
    sent = [(b["id"], *status_of(st, b["id"])) for b in rows]
    sent = [s for s in sent if s[1] in SENT]
    dates = {s[2] for s in sent if s[2]}
    if not quiet:
        print(f"\n{addr}")
        print(f"  {len(rows)} registry row(s) resolve to this address; {len(sent)} already written to")
        for bid, cur, first in sorted(sent, key=lambda s: s[2] or ""):
            print(f"    {first or '?':10}  {cur:16}  {bid}")
        if len(dates) > 1:
            print("  ** SEPARATE SEND DATES -- this mailbox has probably had more than one letter.")
            print("     REPLY IN THE EXISTING THREAD. A new top-level letter here is 309.")
        elif sent:
            print("  One send covering these rows. A further letter must be a REPLY IN THREAD,")
            print("  not a new request, unless the scope is genuinely different -- and if it is,")
            print("  say so in the first line so the recipient can see it is not a repeat.")
        else:
            print("  Nothing sent yet. NEW LETTER is correct -- and enumerate every row above in it,")
            print("  so one letter covers the set (this is what 51 CourtRecords.us rows rest on).")
    return len(dates) > 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", help="broker id or email address")
    ap.add_argument("--audit", action="store_true", help="report every shared address")
    a = ap.parse_args()
    reg, st = load()

    if a.audit:
        by = collections.defaultdict(list)
        for b in reg:
            addr = (b.get("email_to") or "").strip().lower()
            if addr:
                by[addr].append(b)
        shared = {k: v for k, v in by.items() if len(v) > 1}
        flagged = [k for k in sorted(shared) if report(reg, st, k, quiet=True)]
        print(f"{len(shared)} shared address(es); {len(flagged)} with rows sent on more than one date")
        for k in flagged:
            report(reg, st, k)
        print("\nA flag is a QUESTION, not a fault. One letter can legitimately cover many rows and")
        print("be marked over several days. See 308: of five checked by hand, four were correct.")
        return 0

    if not a.target:
        ap.error("give a broker id or an address, or --audit")
    addr = a.target.strip().lower()
    if "@" not in addr:
        hit = next((b for b in reg if b["id"] == a.target), None)
        if not hit:
            print(f"no registry row with id {a.target!r}", file=sys.stderr)
            return 2
        addr = (hit.get("email_to") or "").strip().lower()
        if not addr:
            print(f"{a.target} has no email_to -- nothing to guard against")
            return 0
    report(reg, st, addr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
