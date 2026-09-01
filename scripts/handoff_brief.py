#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Turn the handoff queue into something a person can actually start.

The queue reached 143 open items and roughly fourteen hours of estimated work. As a flat
list that is not a plan, it is a wall -- and the natural response to a wall is to do
nothing, which is the worst outcome available since some of these items EXPIRE.

So this sorts by what would be lost by not doing it, not by when it was added:

  1. EXPIRING      confirmation links and verification tokens. The request does not
                   start until clicked and the token dies. Nothing else in the queue
                   has a deadline.
  2. PUBLIC        people-search and public-records sites. A listing anybody can read
                   is the only category where the harm is ongoing and visible, so a
                   minute here removes more than a minute anywhere else.
  3. CAPTCHA       blocked on a challenge. We will not solve these (standing rule), so
                   a human is the only route and no amount of waiting changes that.
  4. DECISION      needs judgement rather than hands -- an account, an ID document, a
                   payment, a trade-off only the subject can make.
  5. REST          forms and portals where the request is already made by email and
                   this is belt-and-braces.

Within each tier, cheapest first: the point is to make the next twenty minutes obvious,
not to schedule fourteen hours.

    ./handoff_brief.py                # the whole brief
    ./handoff_brief.py --minutes 20   # what fits in twenty minutes
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from paths import state  # noqa: E402

PUBLIC = {"people_search", "public_records", "local_crime_news"}

# A deadline is a PHRASE, not the word "expire" appearing anywhere. The first version
# matched the bare word and swept seven CAPTCHA items into the top tier because their
# steps mentioned an expiring link in passing -- the same failure as 196 (the classifier
# firing on "cookie") and 224a (the succession scan firing on "a ... business").
DEADLINE = ("expires in", "expires -", "one-time access", "access code", "15 minutes",
            "use it promptly", "token")

# Work already done that will be LOST rather than merely delayed: a form filled in an
# open browser tab, waiting on one human action. These decay silently -- a closed tab or
# a session timeout throws the staging away -- so they rank above things that will still
# be there next week.
STAGED = ("already filled", "fully filled", "fully staged", "already open",
          "staged in the open tab", "in the open tab")


def tier(item, cat):
    a = (item.get("action") or "").lower()
    note = ((item.get("note") or "") + " " + (item.get("steps") or "")).lower()
    if a in ("confirm link", "confirm domains") or any(w in note for w in DEADLINE):
        return 1, "EXPIRING -- has a deadline"
    if any(w in note for w in STAGED):
        return 2, "STAGED -- filled in, one action left"
    if cat in PUBLIC:
        return 3, "PUBLIC LISTING -- visible harm"
    if a == "captcha":
        return 4, "CAPTCHA -- human only"
    if a in ("decision", "id", "postal"):
        return 5, "DECISION -- needs your judgement"
    return 6, "REST -- already requested by email"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=int, default=0,
                    help="only show what fits in this many minutes")
    args = ap.parse_args()

    q = json.loads((ROOT / "data" / "handoff_queue.json").read_text())["open"]
    cats = {b["id"]: b.get("category") for b in
            json.loads((ROOT / "data" / "curated_brokers.json").read_text())["brokers"]}

    rows = []
    for i in q:
        t, label = tier(i, cats.get(i.get("broker")))
        rows.append((t, label, int(i.get("minutes") or 5), i))
    rows.sort(key=lambda r: (r[0], r[2]))

    budget, spent, shown = args.minutes, 0, 0
    last = None
    for t, label, mins, i in rows:
        if budget and spent + mins > budget:
            continue
        if label != last:
            print(f"\n=== {label} ===")
            last = label
        print(f"  [{mins:>2}m] {i['broker']}")
        if i.get("url"):
            print(f"        {i['url']}")
        steps = (i.get("steps") or "").strip()
        if steps:
            print(f"        {steps[:300]}")
        spent += mins
        shown += 1

    total = sum(r[2] for r in rows)
    print(f"\n{shown} of {len(rows)} item(s), {spent} min shown of {total} min "
          f"({total/60:.1f} h) queued")
    if budget:
        print("Cheapest-first within each tier, so this is the next best use of the time "
              "rather than the front of the list.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
