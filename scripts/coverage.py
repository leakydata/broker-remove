#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Which rows need a human, and is anyone actually going to do them?

A status of `manual_required` means the automated route is closed and a person
has to act. The handoff queue is where that person looks. Nothing has ever
checked that the two agree.

They frequently do not, and not because work is missing -- because COVERAGE
LIVES UNDER A DIFFERENT NAME. `cappex_com` is done by the `eab` item, because
EAB owns Cappex. `hivestack` is done by `perion`, because Perion answers for the
group. `lotame` is done by `lotame_via_epsilon`, because Lotame was merged into
Epsilon in October 2025. Three mtalley brands are done by one FastPeopleSearch
form filed under `mississippi_tornado_alley`. Querying a row's own id finds none
of that, and on 2026-09-11 I nearly reported seven abandoned rows of which six
were covered (SILENT_FAILURES 434).

So this asks the question the way the answer is actually shaped: for each row
needing a human, is there an open item HERE, or somewhere a note explicitly
points, or in the same registry family?

DELIBERATELY CONSERVATIVE ABOUT THE NEGATIVE. A row with no match is reported as
"no coverage found", never as "abandoned". Coverage can be recorded in prose this
script cannot parse, or implied by a relationship nobody wrote down. The list is
a place to look, not a verdict -- which is the whole lesson of 427 and 428.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Statuses that mean a person still owes an action.
NEEDS_HUMAN = {"manual_required", "captcha_blocked", "email_pending"}

# "queued under `perion`", "handoff item 'eab'", "see mississippi_tornado_alley"
POINTER = re.compile(
    r"(?:queued|covered|handled|filed|done)\s+(?:as|by|under|via)?\s*"
    r"(?:the\s+)?(?:handoff\s+item\s+)?['\"`]?([a-z0-9_]{4,})['\"`]?|"
    r"handoff\s+item\s+['\"`]([a-z0-9_]{4,})['\"`]",
    re.I)


def load(name):
    return json.loads((ROOT / "data" / name).read_text())


def main():
    st = load("removal_status.json")
    q = load("handoff_queue.json")
    openq = {e["broker"]: e.get("action")
             for e in q.get("open", []) if isinstance(e, dict) and e.get("broker")}

    # registry family: rows sharing a statutory contact domain
    fam_of = {}
    try:
        fams = load("broker_families.json").get("families", {})
        for domain, members in fams.items():
            for m in members:
                if m.get("domain"):
                    fam_of[m["domain"]] = domain
    except Exception:
        pass
    dom_of = {}
    try:
        for b in load("brokers.json")["brokers"]:
            if b.get("domain"):
                dom_of[b["id"]] = b["domain"]
    except Exception:
        pass
    family_members = defaultdict(list)
    for bid, dom in dom_of.items():
        if dom in fam_of:
            family_members[fam_of[dom]].append(bid)

    covered, uncovered = [], []
    for bid, rec in st.items():
        hist = rec.get("history") or []
        cur = (hist[-1] if hist else {}).get("status")
        if cur not in NEEDS_HUMAN:
            continue
        note = rec.get("note") or ""

        if bid in openq:
            covered.append((bid, cur, f"own item [{openq[bid]}]"))
            continue

        # a note that names another row, where that row really is queued
        named = {g for m in POINTER.finditer(note) for g in m.groups() if g}
        hit = sorted(n for n in named if n in openq and n != bid)
        if hit:
            covered.append((bid, cur, f"note points at `{hit[0]}` [{openq[hit[0]]}]"))
            continue

        # same registry family as something queued
        fam = fam_of.get(dom_of.get(bid, ""), "")
        sibs = [s for s in family_members.get(fam, []) if s in openq]
        if sibs:
            covered.append((bid, cur, f"registry family {fam} -- `{sibs[0]}` is queued"))
            continue

        uncovered.append((bid, cur, note))

    print(f"rows whose status says a human must act: {len(covered) + len(uncovered)}\n")
    print(f"  coverage found      {len(covered)}")
    print(f"  no coverage found   {len(uncovered)}\n")

    by_reason = defaultdict(int)
    for _, _, why in covered:
        by_reason[why.split(" --")[0].split(" [")[0]] += 1
    for why, n in sorted(by_reason.items(), key=lambda x: -x[1]):
        print(f"    {n:4}  {why}")

    print(f"\n=== NO COVERAGE FOUND ({len(uncovered)})")
    print("    A place to look, not a verdict. Coverage may be recorded in prose")
    print("    this cannot parse, or implied by a relationship nobody wrote down.")
    for bid, cur, note in sorted(uncovered):
        first = re.sub(r"\s+", " ", note).strip()[:96]
        print(f"  {bid:44s} {cur:16s} {first}")

    out = ROOT / "data" / "coverage.json"
    out.write_text(json.dumps(
        {"covered": [{"id": b, "status": s, "why": w} for b, s, w in covered],
         "no_coverage_found": [{"id": b, "status": s} for b, s, _ in uncovered]},
        indent=1) + "\n")
    print(f"\nwrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
