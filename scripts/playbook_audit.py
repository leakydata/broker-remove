#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Are the playbooks actually current, or just present?

`validate.py` already hard-fails when a broker we have acted on has no
`brokers/<id>.md`. That catches absence, which is the cheap half of the problem.
It says nothing about a file that exists but has not been touched since something
happened -- a bounce, a reply, a refusal, a confirmation. A playbook that stops
at "request sent" while the tracker has since recorded a hard bounce is worse
than a missing one: it reads as settled knowledge and is wrong.

Four things get flagged, in descending severity:

    MISSING     acted on, and no playbook covers it
    STALE       the tracker recorded something well after the playbook last
                changed, so the file predates the outcome it should explain
    SCAFFOLD    still essentially the generated file, for a broker that has
                since produced a real outcome
    UNFILLED    real knowledge was written, but a generated section was left as
                an empty placeholder -- so a reader hits "Steps" and finds a
                comment, with the actual route further down under a heading
                they were not looking for
    THIN        acted on, has a reply or an outcome, and under N useful lines

Two kinds of gap are not staleness, and flagging them buries the real findings:

  - Writing the playbook and then recording the send is the normal order of a
    single pass, so anything inside --min-gap-hours is left alone.
  - A tracker entry that only appends a note, leaving the status where it was,
    does not date the playbook. What dates a playbook is a **status change** it
    predates -- a request that has since bounced, been confirmed, or been
    refused. So the comparison is against the last time the status actually
    moved, and a file whose own header already agrees with the current status is
    not reported at all.

"Last changed" is the git commit date when the file is tracked, falling back to
filesystem mtime. Do not use mtime alone: a checkout or a bulk reformat touches
every file and would silently mark the whole set fresh.

    ./playbook_audit.py                 # everything worth looking at
    ./playbook_audit.py --stale-only
    ./playbook_audit.py --limit 20
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
from paths import state, outbox  # noqa: E402
STATE = state("removal_status.json")
ALIASES = ROOT / "data" / "playbook_aliases.json"
BOOKS = ROOT / "brokers"

# Outcomes where the playbook is expected to say more than "we sent a letter".
INTERESTING = {"failed", "confirmed", "not_found", "unreachable",
               "captcha_blocked", "manual_required", "still_listed", "gone"}

PLACEHOLDER = re.compile(r"<!--\s*(Replace once the route|Fill in from their reply)")


def git_mtime(path):
    """Commit date of the file's last change, or None if untracked."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, timeout=15).stdout.strip()
        return datetime.fromisoformat(out) if out else None
    except Exception:
        return None


def last_changed(path):
    return git_mtime(path) or datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)


def parse(s):
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def last_status_change(rec):
    """When the status last actually moved, ignoring note-only updates.

    Appending a note to an unchanged status is bookkeeping, not news. Treating it
    as news marks a correct playbook stale every time the tracker is touched."""
    prev, when = None, None
    for h in rec.get("history", []):
        s = h.get("status")
        if s and s != prev:
            when, prev = parse(h.get("at", "")) or when, s
    return when


def header_status(text):
    """The status the playbook's own generated header claims, if it has one."""
    m = re.search(r"^- Current: `([a-z_]+)`", text, re.M)
    return m.group(1) if m else None


def last_event(rec):
    """Most recent thing the tracker knows, as an aware datetime."""
    stamps = [h.get("at") for h in rec.get("history", []) if h.get("at")]
    if rec.get("updated"):
        stamps.append(rec["updated"])
    best = None
    for s in stamps:
        try:
            d = datetime.fromisoformat(s.replace("Z", "+00:00"))
            if d.tzinfo is None:
                d = d.replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if best is None or d > best:
            best = d
    return best


def useful_lines(text):
    """Prose lines, ignoring headings, bullets of generated metadata and comments."""
    n = 0
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith(("#", "<!--", "-->", "- **", "|")):
            continue
        n += 1
    return n


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stale-only", action="store_true")
    ap.add_argument("--min-gap-hours", type=int, default=2,
                    help="ignore a tracker update this soon after the playbook "
                         "changed; that is just the write order of one pass")
    ap.add_argument("--thin-lines", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()

    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    aliases = (json.loads(ALIASES.read_text()).get("aliases", {})
               if ALIASES.exists() else {})
    findings = []

    for bid, rec in state.items():
        if rec.get("status") == "pending":
            continue
        path = BOOKS / f"{bid}.md"
        if not path.exists():
            # A family document may cover it. Read that instead of reporting a
            # gap that does not exist -- but audit it under this broker's own
            # events, since the shared file has to stay current for all of them.
            covered = aliases.get(bid)
            if not (covered and (BOOKS / f"{covered}.md").exists()):
                findings.append(("MISSING", bid, "acted on, no playbook"))
                continue
            path = BOOKS / f"{covered}.md"

        text = path.read_text()
        changed = last_changed(path)
        # A header that already names the current status is not stale, however
        # long ago it was written.
        claimed = header_status(text)
        event = None if claimed == rec.get("status") else last_status_change(rec)

        if event and changed:
            gap = (event - changed).total_seconds() / 3600
            if gap > a.min_gap_hours:
                where = f" (covered by {path.stem}.md)" if path.stem != bid else ""
                was = f" (header says `{claimed}`)" if claimed else ""
                findings.append(("STALE", bid,
                                 f"status changed {int(gap)}h after the playbook last "
                                 f"changed{where}{was} - now `{rec.get('status')}`"))
                continue
        if a.stale_only:
            continue
        n = useful_lines(text)
        if PLACEHOLDER.search(text) and rec.get("status") in INTERESTING:
            # Distinguish "nobody wrote this" from "somebody wrote a lot of it
            # underneath the empty sections". Both need work; they need
            # different work.
            kind = "SCAFFOLD" if n < 20 else "UNFILLED"
            left = len(PLACEHOLDER.findall(text))
            findings.append((kind, bid,
                             f"{left} generated section(s) still empty, status "
                             f"`{rec.get('status')}`"
                             + (f" - {n} lines of prose sit below them"
                                if kind == "UNFILLED" else "")))
            continue
        if n < a.thin_lines and rec.get("status") in INTERESTING:
            findings.append(("THIN", bid,
                             f"{n} line(s) of prose for a `{rec.get('status')}` outcome"))

    order = {"MISSING": 0, "STALE": 1, "SCAFFOLD": 2, "UNFILLED": 3, "THIN": 4}
    findings.sort(key=lambda f: (order[f[0]], f[1]))
    shown = findings[: a.limit] if a.limit else findings

    for kind, bid, why in shown:
        print(f"  {kind:9} {bid:30} {why}")

    tally = {}
    for kind, _, _ in findings:
        tally[kind] = tally.get(kind, 0) + 1
    acted = sum(1 for r in state.values() if r.get("status") != "pending")
    print(f"\n{acted} acted-on broker(s) | "
          + ("  ".join(f"{k}={v}" for k, v in sorted(tally.items())) or "all current"))
    if a.limit and len(findings) > a.limit:
        print(f"({len(findings) - a.limit} more not shown -- raise --limit)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
