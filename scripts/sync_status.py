#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Share what has been done, without sharing who it was done for.

Two agents are working this project — a local session and a scheduled cloud one —
and they cannot see each other. `data/removal_status.json` holds the truth about
what has been sent, but it is gitignored for good reason: its notes quote broker
replies verbatim and carry addresses, telephone numbers and ticket references.

So each agent has been running from its own private copy of reality. Today that
produced a duplicate letter to one broker and a daily send cap counted twice, and
it will get worse: neither can tell whether a `pending` broker is genuinely
untouched or was contacted an hour ago by the other one.

The fix is a **ledger, not a copy**. This writes `data/removal_ledger.json`
containing only:

    broker id · status · date of the last status change · how it was contacted

No notes, no quotes, no identifiers, no ticket numbers. Nothing that redact.py
would object to, because there is nothing personal in it — the id and the status
are facts about a *company*, not about a person.

    ./sync_status.py            # regenerate the ledger from the private tracker
    ./sync_status.py --check    # report divergence without writing
    ./sync_status.py --merge    # fold the committed ledger back into the tracker

The --merge direction is what makes it useful to the agent that did *not* do the
work: any broker the ledger shows as contacted, but which is `pending` locally,
is adopted as `submitted` with a note saying where it came from. It never
overwrites a richer local record, because a status you established yourself with
a broker's own reply is better evidence than a line in a shared file.

**A ledger only works if both agents write to it, and that cannot be assumed.**
The first time this ran, the other agent had not yet adopted the convention, so
--merge reported "0 adopted" and the local tracker still showed twelve brokers as
`pending` that had already been written to. Nothing was wrong with the merge; it
faithfully reported an empty ledger, and "0 adopted" read as "we are aligned".

So --merge also reads the **committed playbooks**, which are shared whether or not
anyone remembers to publish a ledger. A `brokers/<id>.md` in git means somebody
acted on that broker: validate.py hard-fails on an acted-on broker without one, so
their presence is enforced. That makes the playbook set a lower bound on what has
been done, available from the same git pull, and independent of the other agent's
cooperation.

Belt and braces on purpose: the ledger carries the *status*, the playbooks carry
the *fact that something happened*. Either alone leaves a gap.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
from paths import state, outbox  # noqa: E402
PRIVATE = state("removal_status.json")
LEDGER = state("removal_ledger.json")
PLAYBOOKS = ROOT / "brokers"
ALIASES = ROOT / "data" / "playbook_aliases.json"

# Ranked worst-to-best. A merge never downgrades: an outcome you obtained from
# the broker outranks another agent's report that a letter went out.
#
# "acknowledged", "replied" and "covered_by_sibling" were added to tracker.py's
# STATUSES vocabulary (see the comment there) but never added here -- any status
# missing from this list falls through rank()'s `else 0`, the same rank as
# "pending". That silently made "acknowledged" indistinguishable from
# "pending" during a merge: an already-answered broker's ledger entry looked
# no better than an untouched one, so --merge skipped adopting it and
# queue_batch.py (which has the same gap in its own DONE set) queued a fresh
# "Consumer Request" letter into a thread that already had a reply sitting in
# it. Keep any status added to tracker.py's STATUSES in sync with this list.
RANK = ["pending", "manual_required", "captcha_blocked", "email_pending",
        "submitted", "acknowledged", "replied", "failed", "unreachable",
        "still_listed", "gone", "not_found", "suppressed", "confirmed",
        "covered_by_sibling"]


# A playbook that says, in its own Status block, that nothing has been done.
# Matches "- Current: not yet acted on." and "- Current: not acted on. **Blocked
# ...**" and "- Current: `pending`". Anything else is treated as evidence of
# action, which is the safe direction for a lower bound. See 451b.
NOT_ACTED_RE = re.compile(
    r"^- Current:\s*(?:`pending`|not (?:yet )?acted on|nothing (?:has been )?sent)",
    re.M | re.I)


def rank(s):
    return RANK.index(s) if s in RANK else 0


def last_change(rec):
    """Date the status last actually moved, as YYYY-MM-DD."""
    prev, when = None, rec.get("updated", "")
    for h in rec.get("history", []):
        if h.get("status") and h["status"] != prev:
            when, prev = h.get("at", when), h["status"]
    return (when or "")[:10]


def build(private):
    out = {}
    for bid, rec in private.items():
        status = rec.get("status", "pending")
        if status == "pending":
            continue
        vias = [h.get("via") for h in rec.get("history", []) if h.get("via")]
        out[bid] = {
            "status": status,
            "changed": last_change(rec),
            "via": vias[-1] if vias else None,
        }
    return dict(sorted(out.items()))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="report only, write nothing")
    ap.add_argument("--merge", action="store_true",
                    help="adopt the committed ledger into the private tracker")
    a = ap.parse_args()

    private = json.loads(PRIVATE.read_text()) if PRIVATE.exists() else {}
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}

    if a.merge:
        # A committed playbook is evidence that somebody acted, even when no
        # ledger entry exists — see the note at the top about one-sided ledgers.
        aliases = (json.loads(ALIASES.read_text()).get("aliases", {})
                   if ALIASES.exists() else {})
        covered = set(aliases)
        # RECURSIVE. brokers/ was sharded into 27 subdirectories on 11 September
        # and this glob was not updated (_SILENT_FAILURES 451a). A flat "*.md"
        # matched 11 files afterwards -- README plus the _-prefixed digests, all
        # of which this loop then skips -- so the playbook arm of --merge adopted
        # NOTHING for a day, and reported it as "0 adopted", which is what it
        # also says when there is genuinely nothing to adopt.
        #
        # AND THE EXISTENCE OF A PLAYBOOK IS NOT EVIDENCE OF A SEND (451b).
        # The note above argues: validate.py hard-fails on an acted-on broker
        # with no playbook, therefore a playbook means somebody acted. That is
        # the converse and it does not follow. It held only by accident, while
        # playbooks happened to be written after acting -- and it broke the
        # same hour the glob was repaired, because validate ALSO warns about a
        # high-priority broker with no playbook, so playbooks now get written
        # for brokers nobody has contacted. Two checks, two meanings for the
        # same file. On the first run after the fix this adopted `plaid` and
        # `dmachoice` as `submitted`; both playbooks say in their own first
        # line that nothing has been sent, and dmachoice is blocked on a
        # decision that is the subject's to make.
        #
        # So read what the playbook SAYS. The test is for an explicit DENIAL,
        # not for a positive claim -- because most of the older playbooks
        # (spokeo, whitepages, acxiom, beenverified) were hand-written before
        # the scaffold existed and carry no "- Current:" line at all. Requiring
        # a positive claim dropped 57 genuinely-acted brokers from the lower
        # bound, which trades a small false-positive for a large false-negative
        # and is the wrong way round for a set whose whole job is to be a floor.
        for f in PLAYBOOKS.glob("**/*.md"):
            if f.stem.startswith("_") or f.stem == "README":
                continue
            if NOT_ACTED_RE.search(f.read_text(errors="replace")):
                continue
            covered.add(f.stem)
        for bid in sorted(covered):
            if bid in ledger:
                continue          # the ledger is the better source; use it below
            rec = private.get(bid)
            if rec and rec.get("status", "pending") != "pending":
                continue          # we already know
            ledger[bid] = {
                "status": "submitted", "changed": "", "via": None,
                "_from": "playbook",
            }

        adopted = []
        skipped_newer = []
        for bid, entry in ledger.items():
            rec = private.setdefault(bid, {"status": "pending", "history": []})
            if rank(entry["status"]) <= rank(rec.get("status", "pending")):
                continue          # ours is equal or better; leave it alone

            # RANK IS NOT THE WHOLE COMPARISON, because a status can move
            # DOWN on purpose. _SILENT_FAILURES 451c: greenhouse_software was
            # set to manual_required deliberately -- the email route
            # manufactures a completed deletion request out of any message, so
            # the portal is the only honest path and the row was moved back to
            # say so, with tracker.py's --regressed flag, twice, on two days.
            # The shared ledger still carried `submitted` from 27 August.
            # `submitted` outranks `manual_required`, so a rank-only merge
            # silently reverted a decision made an hour earlier and pointed the
            # next send straight back at the mailbox the decision existed to
            # avoid.
            #
            # Rank answers "which status is further along". It cannot answer
            # "which of these two people knew more", and when the local entry
            # is NEWER than the ledger's, that second question is the one that
            # matters. A deliberate downgrade is always newer than the thing it
            # downgrades.
            ours_at = last_change(rec)
            theirs_at = (entry.get("changed") or "")[:10]
            if ours_at and theirs_at and ours_at > theirs_at:
                skipped_newer.append(
                    f"{bid} ({rec.get('status')} here {ours_at}, "
                    f"{entry['status']} in the ledger {theirs_at})")
                continue
            rec["status"] = entry["status"]
            rec["updated"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            # The history "at" is what queue_batch.py's daily-send-cap counter reads.
            # Stamping it with datetime.now() backdated nothing -- it FRONT-dated
            # every adopted row to the moment the merge ran, so a merge adopting
            # hundreds of old sends made the cap counter see them all as sent today.
            # Use the ledger's own "changed" date when there is one; only a
            # playbook-only adoption (no ledger date at all) has no real date to
            # fall back to, so that case alone uses now().
            at = (entry.get("changed") or "") or rec["updated"]
            note = (
                f"Adopted from a committed playbook: brokers/{bid}.md exists in "
                f"git but this tracker had nothing, so another agent acted and "
                f"did not publish a ledger entry. Status is a floor, not a "
                f"finding — read the playbook and the broker's own reply before "
                f"relying on it."
                if entry.get("_from") == "playbook" else
                f"Adopted from the shared ledger: another agent recorded "
                f"'{entry['status']}' on {entry['changed']}. No detail is "
                f"carried across — re-read the broker's own reply before "
                f"relying on this.")
            rec.setdefault("history", []).append({
                "at": at, "status": entry["status"], "via": entry.get("via"),
                "note": note,
            })
            # validate.py's TERMINAL-status check (and a human skimming this
            # file) both read the top-level `note`, not history -- tracker.py's
            # own `set` command writes both, but this adoption path used to
            # write only history, which is how a merge could adopt hundreds of
            # `confirmed`/`not_found` rows and have every one of them fail
            # validate.py's "TERMINAL status needs a note" check afterwards.
            rec["note"] = note
            adopted.append(bid)
        if adopted:
            PRIVATE.write_text(json.dumps(private, indent=2, ensure_ascii=False) + "\n")
        from_pb = [b for b in adopted if ledger[b].get("_from") == "playbook"]
        print(f"adopted {len(adopted)} broker(s)"
              + (f" ({len(from_pb)} from committed playbooks with no ledger entry)"
                 if from_pb else "")
              + (f": {', '.join(adopted[:12])}" if adopted else ""))
        if from_pb:
            print("  the other agent is not publishing a ledger yet — its work was "
                  "recovered from git, but statuses are a floor, not a finding")
        if skipped_newer:
            print(f"\nHELD BACK {len(skipped_newer)} higher-ranked ledger status(es) "
                  f"because ours is NEWER (451c):")
            for line in skipped_newer:
                print(f"  {line}")
            print("  A status can move DOWN on purpose. Rank says which is further "
                  "along;\n  it cannot say which of us knew more, and the newer "
                  "entry usually did.\n  If the ledger is right, the other agent "
                  "should re-publish it with today's date.")
        return 0

    # ACTIVITY THE LEDGER STRUCTURALLY CANNOT CARRY.
    #
    # The ledger holds id, status, date and method -- and nothing else, because
    # notes quote broker replies and carry identifiers, and this repo is public.
    # That trade is right (§268) and it has a blind spot: A LETTER THAT DOES NOT
    # CHANGE A STATUS IS INVISIBLE HERE. A follow-up to a company already recorded
    # as `manual_required`, an opt-out wedge to a row already `submitted`, a
    # correction sent to fix my own error -- all real work, none of it a status
    # move, so the other agent never learns it happened.
    #
    # On 2 September two such letters went out and `git commit` reported nothing
    # to commit. The fix is not to widen the ledger; it is to say out loud which
    # rows moved WITHOUT their status moving, so the substance can be pushed into
    # the playbook, which is the durable channel. See _SILENT_FAILURES §291.
    today = datetime.now(timezone.utc).date().isoformat()
    quiet = []
    for bid, rec in private.items():
        hist = rec.get("history") or []
        touched = [h for h in hist if (h.get("at") or "")[:10] == today]
        if touched and last_change(rec) != today:
            quiet.append(bid)
    if quiet:
        print(f"\n  {len(quiet)} row(s) had activity today that DID NOT move a status,")
        print(f"  so the ledger cannot carry it: {', '.join(sorted(quiet)[:10])}"
              + (" ..." if len(quiet) > 10 else ""))
        print(f"  If any of that was a letter or a finding, put it in the playbook "
              f"-- brokers/<id>.md --\n  or the other agent will never see it.")

    fresh = build(private)
    added = sorted(set(fresh) - set(ledger))
    changed = sorted(b for b in set(fresh) & set(ledger)
                     if fresh[b]["status"] != ledger[b]["status"])
    missing = sorted(set(ledger) - set(fresh))

    print(f"ledger: {len(ledger)} entries | tracker: {len(fresh)} acted-on")
    if added:
        print(f"  +{len(added)} not yet shared: {', '.join(added[:12])}"
              + (" ..." if len(added) > 12 else ""))
    if changed:
        print(f"  ~{len(changed)} status changed: {', '.join(changed[:12])}")
    if missing:
        print(f"  !{len(missing)} in the ledger but not in this tracker — "
              f"the other agent did these: {', '.join(missing[:12])}"
              + (" ..." if len(missing) > 12 else ""))
        print("     run --merge to adopt them, or they will be contacted twice")

    if a.check:
        return 0

    # THE LEDGER WRITE IS A UNION, NOT A REPLACEMENT.
    #
    # This used to write `fresh` -- this agent's whole view -- straight over the
    # file. Which meant every sync silently deleted whatever the other agent had
    # added since the last merge. On 2 September it dropped three brokers the
    # cloud agent had written to that morning (subsplash, wealthminder,
    # h1bdata_info); they reverted to looking `pending`, and the next queue_batch
    # run would have sent each of them a second letter.
    #
    # The bitter part: the block above ALREADY PRINTS the warning -- "!N in the
    # ledger but not in this tracker ... run --merge to adopt them, or they will
    # be contacted twice" -- and then the next line did exactly what it warned
    # against. A diagnostic that names a hazard and an action that causes it, four
    # lines apart. See _SILENT_FAILURES §270.
    #
    # A row present only in the ledger is not stale, it is the other agent's work.
    # Keep it. On conflict the higher-ranked status wins; on equal rank the later
    # change date does.
    merged = dict(ledger)
    for bid, rec in fresh.items():
        prev = merged.get(bid)
        if prev is None:
            merged[bid] = rec
            continue
        # RECENCY DECIDES, NOT RANK -- and this was wrong for one tick.
        #
        # The first version of this merge kept the higher-ranked status, on the
        # assumption that a status only ever improves. It does not. A bounce, a
        # discovered mis-send, or a playbook correction all move it DOWN, and
        # those are exactly the corrections that matter, because they deflate an
        # overclaim. Ranking made them unpublishable: `aberdeen` (submitted ->
        # email_pending) and `outlogic` (submitted -> manual_required) were
        # corrected locally and silently refused by the ledger, so the other
        # agent would have kept acting on `submitted`.
        #
        # Fixing deletion-by-omission had introduced monotonic optimism instead:
        # the shared file could no longer be told that something got worse. See
        # _SILENT_FAILURES §275.
        #
        # The later assertion wins, whichever direction it points. Rank breaks a
        # same-day tie only, where "further along" is the better guess.
        d_new = rec.get("changed") or ""
        d_old = prev.get("changed") or ""
        if d_new > d_old or (
                d_new == d_old
                and rank(rec["status"]) >= rank(prev.get("status", "pending"))):
            merged[bid] = rec
    merged = dict(sorted(merged.items()))
    kept = len(set(merged) - set(fresh))

    LEDGER.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwrote {LEDGER.relative_to(ROOT)} ({len(merged)} entries, no personal data)")
    if kept:
        print(f"  {kept} entry(ies) preserved from the other agent rather than "
              f"overwritten -- run --merge to adopt them locally")
    return 0


if __name__ == "__main__":
    sys.exit(main())
