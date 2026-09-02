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

# Keep this in step with what the queue actually contains. `form` and `verify`
# were in use for weeks before they were in this dict: add() rejected them while
# list() rendered them fine, because list() falls back to the raw string. The
# validator and the data disagreed and the data was right -- filling a web form
# is the commonest handoff there is after a CAPTCHA.
ACTIONS = {
    "captcha":  "solve a CAPTCHA, then submit",
    "form":     "fill in and submit a web form",
    "click":    "click one button",
    "verify":   "complete a verification step",
    "phone":    "make a phone call",
    "postal":   "print, sign and post",
    "id":       "decide whether to supply an identity document",
    "decision": "make a judgement call",
    "none":     "nothing to do -- recorded so it is not re-planned",
}


def load():
    return json.loads(QUEUE.read_text()) if QUEUE.exists() else {"open": [], "closed": []}


def save(q):
    QUEUE.parent.mkdir(parents=True, exist_ok=True)
    QUEUE.write_text(json.dumps(q, indent=2, ensure_ascii=False) + "\n")


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def cmd_add(a):
    # A queued item is read days later by someone who does not have the session
    # that staged it. Steps written as "already filled in the open tab" are worse
    # than useless then: the URL opens an empty form and the note says the work is
    # already done. Thirteen items broke this rule while the rule was in the
    # docstring above. Refuse them at the point of writing, where the fix is free.
    # See _SILENT_FAILURES 283.
    _STALE = ("open tab", "already open", "open in chrome", "fully filled",
              "already filled", "already prefilled", "tab is open",
              "tab is staged", "in the open tab")
    _steps = (a.steps or "").lower()
    if any(t in _steps for t in _STALE) and "if the tab is gone" not in _steps:
        sys.exit(
            "refusing: these steps assume a browser tab that will not exist when "
            "someone reads them.\n"
            "  Write the field VALUES to enter, not 'already filled'.\n"
            "  If the item does describe a live tab AND also carries the values, "
            "include the words\n  'IF THE TAB IS GONE' and it will be accepted. "
            "See _SILENT_FAILURES 283.")

    q = load()
    # Replacing silently is how contradictory items survive. `add` has always
    # dropped any existing entry for the same broker -- which is right when the
    # new item supersedes the old, and wrong when a broker legitimately needs two
    # (a phone route and a portal fallback, say). Either way the person staging it
    # should be told which happened. A queue audit found two brokers carrying an
    # old item beside a newer one that CONTRADICTED it: one said "submit this
    # OneTrust form", the newer said "hold, that URL is a draft". See
    # _SILENT_FAILURES 284.
    prior = [e for e in q["open"] if e["broker"] == a.broker]
    if prior and not getattr(a, "also", False):
        print(f"  replacing {len(prior)} existing open item(s) for {a.broker} "
              f"(pass --also to keep them alongside)")
        for e in prior:
            print(f"    dropped: [{e.get('action')}] "
                  f"{(e.get('steps') or '')[:80]}")
    if not getattr(a, "also", False):
        # Archive what is replaced rather than discarding it. Testing this very
        # function destroyed two real items -- a phone route and its portal
        # fallback -- which had to be reconstructed from a tracker note, because
        # the replace path dropped them with no copy anywhere and this file is
        # gitignored, so there was no history to recover from either.
        for e in prior:
            e["closed_at"] = now()[:10]
            e["closed_reason"] = ("replaced by a newer item for the same broker "
                                  "(handoff.py add). Archived rather than "
                                  "discarded -- see _SILENT_FAILURES 284.")
            q.setdefault("closed", []).append(e)
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
    p.add_argument("--also", action="store_true",
                   help="keep any existing open items for this broker rather than "
                        "replacing them -- for a route and its fallback")
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
