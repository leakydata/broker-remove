#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""A work queue for the steps a human has to do.

Some removal routes need exactly one human action -- a CAPTCHA, a click on a
confirm button, a phone call. Everything either side of that can be automated:
finding the route, filling the form, reading the confirmation email, recording
the result.

Handling those one at a time means interrupting a person per item, which is the
most expensive way to spend the one resource that is genuinely scarce here. This
queues them instead, so a batch can be cleared in one sitting.

Each entry stands on its own: broker, URL, and exactly what to do. It does NOT
depend on a browser tab still being open, because tabs do not survive the wait.

    ./handoff.py add spokeo --url https://... --action captcha \\
        --steps "Solve the reCAPTCHA, then press Continue"
    ./handoff.py list                 # what's waiting
    ./handoff.py list --brief         # one line, for a notification
    ./handoff.py done spokeo          # cleared
    ./handoff.py done spokeo --failed "form errored again"
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
from paths import state, outbox  # noqa: E402
QUEUE = state("handoff_queue.json")

ACTIONS = {
    "captcha":  "solve a CAPTCHA, then submit",
    "click":    "click one button",
    "phone":    "make a phone call",
    "postal":   "print, sign and post",
    "id":       "decide whether to supply an identity document",
    "decision": "make a judgement call",
}


def load():
    return json.loads(QUEUE.read_text()) if QUEUE.exists() else {"open": [], "closed": []}


def save(q):
    QUEUE.parent.mkdir(parents=True, exist_ok=True)
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False) + "\n")


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def cmd_add(a):
    q = load()
    q["open"] = [e for e in q["open"] if e["broker"] != a.broker]
    q["open"].append({
        "broker": a.broker, "url": a.url, "action": a.action,
        "steps": a.steps, "note": a.note, "staged_at": now(),
        "minutes": a.minutes,
    })
    save(q)
    print(f"queued: {a.broker} ({ACTIONS.get(a.action, a.action)})")


def cmd_done(a):
    q = load()
    hit = [e for e in q["open"] if e["broker"] == a.broker]
    if not hit:
        sys.exit(f"{a.broker} is not in the open queue")
    for e in hit:
        e["closed_at"] = now()
        e["outcome"] = "failed" if a.failed else "done"
        if a.failed:
            e["failure"] = a.failed
        q["closed"].append(e)
    q["open"] = [e for e in q["open"] if e["broker"] != a.broker]
    save(q)
    print(f"{a.broker}: {'failed - ' + a.failed if a.failed else 'done'}")


def cmd_list(a):
    q = load()
    open_ = q["open"]
    if not open_:
        print("nothing waiting on you" if not a.brief else "")
        return 0

    total = sum(e.get("minutes") or 1 for e in open_)
    if a.brief:
        kinds = {}
        for e in open_:
            kinds[e["action"]] = kinds.get(e["action"], 0) + 1
        bits = ", ".join(f"{v} {k}" for k, v in sorted(kinds.items()))
        print(f"{len(open_)} waiting on you ({bits}) - about {total} min")
        return 0

    print(f"\n{len(open_)} item(s) waiting on you - roughly {total} minute(s) total\n")
    for i, e in enumerate(open_, 1):
        waited = ""
        try:
            mins = int((datetime.now(timezone.utc)
                        - datetime.fromisoformat(e["staged_at"])).total_seconds() // 60)
            waited = f"  (staged {mins} min ago)"
        except Exception:
            pass
        print(f"{i}. {e['broker']}  -  {ACTIONS.get(e['action'], e['action'])}{waited}")
        if e.get("url"):
            print(f"   {e['url']}")
        if e.get("steps"):
            print(f"   what to do: {e['steps']}")
        if e.get("note"):
            print(f"   note: {e['note']}")
        print()
    print("clear one with:  uv run scripts/handoff.py done <broker>")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("add")
    p.add_argument("broker")
    p.add_argument("--url", required=True)
    p.add_argument("--action", required=True, choices=sorted(ACTIONS))
    p.add_argument("--steps", required=True, help="exactly what the human does")
    p.add_argument("--note", help="anything else worth knowing")
    p.add_argument("--minutes", type=int, default=1, help="rough time cost")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("done")
    p.add_argument("broker")
    p.add_argument("--failed", help="it did not work; what happened")
    p.set_defaults(func=cmd_done)

    p = sub.add_parser("list")
    p.add_argument("--brief", action="store_true", help="one line, for a notification")
    p.set_defaults(func=cmd_list)

    a = ap.parse_args()
    return a.func(a) or 0


if __name__ == "__main__":
    sys.exit(main())
