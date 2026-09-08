#!/usr/bin/env python3
"""Who to chase when the 45-day window closes, and in what order.

§421 computed the cliff: 414 open rows cross forty-five days in the week of
28 September, about a thousand within three weeks. Chasing all of them is the
volume mistake §398 refused; chasing none makes the deadline a number nobody
acted on. This produces the principled middle.

THE RULE IT APPLIES, which is §394's corroboration split put to work:

  A CORROBORATED row is not silent, it is slow. Something came back — a
  ticket, a reply, an acknowledgement. Chasing it asks a company to hurry,
  which is a request with no content.

  An UNCORROBORATED row has produced nothing at all. Silence there is
  ambiguous in the way that matters: the request may be queued, or the letter
  may never have arrived. That is answerable in one line, without touching the
  substance, and it is the only chase worth sending.

Within the uncorroborated set it orders by what a reply would settle:

  SOLE ROUTE     the channel that went unanswered is the only one known.
                 Silence and unreachability are indistinguishable here, so a
                 reply settles the most.
  ALT ROUTE      another address or a working form exists. These can be
                 RE-ROUTED rather than chased, which is better than a second
                 letter down a channel that already produced nothing.

Usage:  chase_queue.py [--as-of YYYY-MM-DD] [--limit N]

It writes nothing and sends nothing. It prints a worklist.
"""
import argparse
import datetime
import importlib.util
import json
import sys


def corroboration_classifier():
    spec = importlib.util.spec_from_file_location(
        "corr", "scripts/corroboration.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules["corr"] = m
    try:
        spec.loader.exec_module(m)
    except SystemExit:
        pass
    return m.classify


OPEN = {"submitted", "manual_required", "captcha_blocked", "failed",
        "replied", "acknowledged", "email_pending"}
WINDOW = datetime.timedelta(days=45)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--as-of", default=None,
                    help="pretend it is this date (YYYY-MM-DD)")
    ap.add_argument("--limit", type=int, default=40)
    a = ap.parse_args()
    today = (datetime.date.fromisoformat(a.as_of) if a.as_of
             else datetime.date.today())

    classify = corroboration_classifier()
    recs = json.load(open("data/removal_status.json"))
    recs = recs.get("records", recs)

    brokers = json.load(open("data/brokers.json"))
    if isinstance(brokers, dict):
        brokers = brokers.get("brokers") or list(brokers.values())
    if isinstance(brokers, dict):
        brokers = list(brokers.values())
    bi = {r["id"]: r for r in brokers if isinstance(r, dict) and "id" in r}

    # a route is "alternative" only if it is a DIFFERENT usable channel
    usable_form = set()
    try:
        for r in json.load(open("data/route_has_form.json")):
            if r["verdict"] in ("FORM", "DELEGATED", "MAILTO"):
                usable_form.add(r["id"])
    except FileNotFoundError:
        pass

    rows = []
    for k, v in recs.items():
        if v.get("status") not in OPEN:
            continue
        hist = v.get("history") or []
        first = (hist[0].get("at", "") if hist else (v.get("at") or ""))[:10]
        try:
            due = datetime.date.fromisoformat(first) + WINDOW
        except ValueError:
            continue
        if due > today:
            continue
        bucket, _ = classify(v)
        if bucket != "uncorroborated":
            continue
        b = bi.get(k, {})
        alt = bool(b.get("email_alt")) or k in usable_form
        rows.append((0 if not alt else 1, due, k, v.get("status"),
                     b.get("email_to") or "-", "alt route" if alt else "SOLE ROUTE"))

    rows.sort()
    print(f"as of {today}: {len(rows)} uncorroborated rows past 45 days\n")
    if not rows:
        print("  nothing due. The oldest open row has not reached the window.\n")
        return
    sole = sum(1 for r in rows if r[0] == 0)
    print(f"  {sole} sole-route (chase settles the most)")
    print(f"  {len(rows)-sole} have an alternative route "
          f"(RE-ROUTE rather than chase)\n")
    for _, due, k, st, em, tag in rows[:a.limit]:
        print(f"  due {due}  {k:32} {st:14} {tag:10} {em}")
    if len(rows) > a.limit:
        print(f"  ... and {len(rows)-a.limit} more")
    print("""
  A chase to one of these asks ONE question: did you receive it? Not "when
  will you answer". The second is a request with no content; the first is
  answerable in a line and settles whether the channel works at all.""")


if __name__ == "__main__":
    main()
