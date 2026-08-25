#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Track data broker opt-out progress.

Usage:
    ./tracker.py list [--status STATUS] [--tier TIER]
    ./tracker.py show BROKER_ID
    ./tracker.py set BROKER_ID STATUS [--note "..."] [--url URL] [--ref REF]
    ./tracker.py next [N]          # highest-priority brokers not yet done
    ./tracker.py stats
    ./tracker.py report            # markdown progress report
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
from paths import state, outbox  # noqa: E402
REGISTRY = ROOT / "data" / "brokers.json"
STATE = state("removal_status.json")

STATUSES = [
    "pending",           # not started
    "not_found",         # searched, no record of me exists
    "submitted",         # opt-out request sent, awaiting processing
    "email_pending",     # blocked: needs a confirmation link in the user's inbox
    "captcha_blocked",   # blocked: needs a human to solve a CAPTCHA
    "manual_required",   # blocked: needs ID upload, phone call, or postal mail
    "confirmed",         # broker confirmed removal
    "failed",            # attempted, broker rejected or site broken
    "unreachable",       # site dead / domain parked
]



# Outcomes that represent real, hard-won progress. Moving away from one of these
# is almost always an accident (see cmd_set), so it needs an explicit flag.
TERMINAL_WINS = {"confirmed", "not_found"}
def load(path, default):
    if path.exists():
        return json.loads(path.read_text())
    return default


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def get_state():
    return load(STATE, {})


def get_registry():
    reg = load(REGISTRY, {"brokers": []})
    return {b["id"]: b for b in reg["brokers"]}


def cmd_list(args):
    reg, st = get_registry(), get_state()
    for bid, b in sorted(reg.items(), key=lambda kv: (-kv[1].get("priority", 0), kv[0])):
        rec = st.get(bid, {})
        status = rec.get("status", "pending")
        if args.status and status != args.status:
            continue
        if args.tier and b.get("tier") != args.tier:
            continue
        print(f"{status:16} p{b.get('priority',0):<2} {bid:28} {b.get('name','')}")


def cmd_show(args):
    reg, st = get_registry(), get_state()
    b = reg.get(args.broker_id)
    if not b:
        sys.exit(f"unknown broker: {args.broker_id}")
    print(json.dumps({"registry": b, "state": st.get(args.broker_id, {})}, indent=2))


def cmd_set(args):
    if args.status not in STATUSES:
        sys.exit(f"status must be one of: {', '.join(STATUSES)}")
    reg, st = get_registry(), get_state()
    if args.broker_id not in reg:
        sys.exit(f"unknown broker: {args.broker_id}")
    rec = st.setdefault(args.broker_id, {"history": []})

    # Don't let a later note quietly undo an earlier win.
    #
    # A confirmed removal is the most expensive fact in this file: it took a
    # letter, usually a follow-up, and a broker willing to say plainly that the
    # data is gone. New activity on an already-confirmed broker is normally a
    # FOLLOW-UP ticket, not a reversal -- MyLife acknowledged a fresh ticket a
    # week after confirming deletion, and recording that as `submitted` silently
    # erased the confirmation from the totals.
    #
    # Downgrades are still allowed: a broker can genuinely re-add someone, and
    # refusing to record that would be its own kind of lie. But it must be
    # deliberate, so it requires --regressed and says so out loud.
    prior = rec.get("status")
    if prior in TERMINAL_WINS and args.status != prior and not args.regressed:
        sys.exit(
            f"refusing to move {args.broker_id} from '{prior}' to "
            f"'{args.status}'.\n"
            f"  '{prior}' is a recorded outcome that cost real work. New "
            f"activity on a settled broker is usually a follow-up, not a "
            f"reversal -- record it with:\n"
            f"      tracker.py set {args.broker_id} {prior} --note \"...\"\n"
            f"  If the broker really has re-added the data or withdrawn the "
            f"confirmation, pass --regressed to say so deliberately."
        )
    if args.regressed and prior:
        print(f"NOTE: {args.broker_id} regressed from '{prior}' to "
              f"'{args.status}'", file=sys.stderr)

    rec["status"] = args.status
    rec["updated"] = now()
    if args.url:
        rec["optout_url_used"] = args.url
    if args.ref:
        rec["confirmation_ref"] = args.ref
    entry = {"at": now(), "status": args.status}
    if args.via:
        entry["via"] = args.via
    if args.note:
        entry["note"] = args.note
        rec["note"] = args.note
    rec.setdefault("history", []).append(entry)
    save(STATE, st)
    print(f"{args.broker_id} -> {args.status}")


def cmd_next(args):
    reg, st = get_registry(), get_state()
    done = {"confirmed", "submitted", "not_found", "unreachable"}
    todo = [
        b for bid, b in reg.items()
        if st.get(bid, {}).get("status", "pending") not in done
    ]
    todo.sort(key=lambda b: (-b.get("priority", 0), b["id"]))
    for b in todo[: args.count]:
        print(f"p{b.get('priority',0)} {b['id']:28} {b.get('optout_url','')}")


def _tally(reg, st):
    counts = {}
    for bid in reg:
        s = st.get(bid, {}).get("status", "pending")
        counts[s] = counts.get(s, 0) + 1
    return counts


def cmd_stats(args):
    reg, st = get_registry(), get_state()
    counts = _tally(reg, st)
    total = len(reg)
    print(f"total tracked brokers: {total}")
    for s in STATUSES:
        if counts.get(s):
            print(f"  {s:16} {counts[s]:4}")


def cmd_report(args):
    reg, st = get_registry(), get_state()
    counts = _tally(reg, st)
    lines = [
        "# Data Broker Removal Report",
        "",
        f"_Generated {now()}_",
        "",
        "## Summary",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    for s in STATUSES:
        if counts.get(s):
            lines.append(f"| {s} | {counts[s]} |")
    lines += ["", "## Detail", "",
              "| Broker | Status | Updated | Note |", "|---|---|---|---|"]
    for bid, b in sorted(reg.items(), key=lambda kv: (-kv[1].get("priority", 0), kv[0])):
        rec = st.get(bid, {})
        if rec.get("status", "pending") == "pending":
            continue
        note = (rec.get("note", "") or "").replace("|", "\\|")
        lines.append(
            f"| {b.get('name', bid)} | {rec.get('status')} | "
            f"{rec.get('updated','')[:10]} | {note} |"
        )
    out = "\n".join(lines) + "\n"
    (ROOT / "docs" / "REMOVAL_REPORT.md").write_text(out)
    print(out)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    lp = sub.add_parser("list"); lp.add_argument("--status"); lp.add_argument("--tier")
    lp.set_defaults(func=cmd_list)

    sp = sub.add_parser("show"); sp.add_argument("broker_id"); sp.set_defaults(func=cmd_show)

    stp = sub.add_parser("set")
    stp.add_argument("broker_id"); stp.add_argument("status")
    stp.add_argument("--note"); stp.add_argument("--url"); stp.add_argument("--ref")
    stp.add_argument("--regressed", action="store_true",
                     help="allow moving away from a confirmed/not_found outcome")
    # 'email' is a fresh outbound letter and counts against the daily send cap.
    # 'reply' is a message into an existing thread -- answering a deflection,
    # recording a ticket acknowledgement -- and does not. Conflating them lets a
    # busy inbox day exhaust a cap that no new broker ever benefited from.
    stp.add_argument("--via", choices=["email", "reply", "web", "phone", "postal"],
                     help="channel used, so the daily send cap can count accurately")
    stp.set_defaults(func=cmd_set)

    np = sub.add_parser("next"); np.add_argument("count", nargs="?", type=int, default=10)
    np.set_defaults(func=cmd_next)

    sub.add_parser("stats").set_defaults(func=cmd_stats)
    sub.add_parser("report").set_defaults(func=cmd_report)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
