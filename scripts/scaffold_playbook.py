#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Scaffold brokers/<id>.md from what the registry and status log already know.

Writing playbooks by hand is the step that gets skipped when a batch of requests
goes out, which is precisely when the knowledge is freshest. This turns the
boring half into one command so only the genuinely learned part is left to write.

Never overwrites an existing playbook. Existing files are the hand-written ones.

Usage:
    ./scaffold_playbook.py --missing        # every acted-on broker lacking a file
    ./scaffold_playbook.py mylife epsilon
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from redact import redact  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "brokers.json"
STATE = ROOT / "data" / "removal_status.json"
ALIASES = ROOT / "data" / "playbook_aliases.json"
OUT = ROOT / "brokers"

ACTED = {"submitted", "email_pending", "captcha_blocked", "manual_required", "failed"}

METHOD_NOTE = {
    "email": "Statutory request by email. No web form needed.",
    "web_form": "Web form.",
    "web_form_captcha": "Web form with a CAPTCHA — see where it sits (page load vs submit).",
    "account_required": "Requires an account or profile claim.",
    "postal": "Postal mail only.",
    "phone": "Telephone only.",
    "unknown": "Route not yet established.",
}


def scaffold(bid, reg, st):
    b = reg.get(bid)
    if not b:
        return f"  skip unknown broker: {bid}"
    path = OUT / f"{bid}.md"
    if path.exists():
        return f"  keep existing: {bid}.md"

    rec = st.get(bid, {})
    name = b.get("name", bid)
    lines = [f"# {name}", ""]

    if b.get("optout_url"):
        lines.append(f"- **Opt-out:** {b['optout_url']}")
    if b.get("email_to"):
        verified = " (verified)" if b.get("email_verified") else " — **unverified, may bounce**"
        lines.append(f"- **Email:** {b['email_to']}{verified}")
    lines.append(f"- **Method:** {b.get('method','unknown')} — "
                 f"{METHOD_NOTE.get(b.get('method'), '')}")
    if b.get("domain"):
        lines.append(f"- **Domain:** {b['domain']}")
    lines.append(f"- **Priority: {b.get('priority', '?')}.**")
    lines.append("")

    lines += ["## Status", ""]
    lines.append(f"- Current: `{rec.get('status', 'pending')}`"
                 + (f" (updated {rec.get('updated','')[:10]})" if rec.get("updated") else ""))
    if rec.get("confirmation_ref"):
        lines.append(f"- Reference: `{redact(rec['confirmation_ref'])}`")
    if rec.get("note"):
        # Tracker notes are gitignored and may contain personal data; this file
        # is tracked and public. Redact on the way across that boundary.
        lines.append(f"- Note: {redact(rec['note'])}")
    lines.append("")

    lines += [
        "## Steps",
        "",
        "<!-- Replace once the route is confirmed. What actually worked, in order. -->",
        "",
        "## Gotchas",
        "",
        "<!-- Fill in from their reply. Recurring things worth capturing:",
        "     - Do they refuse email and point at a form? Which form?",
        "     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?",
        "     - Does the form silently drop values not committed with an Add/+ button?",
        "     - Do they gate on state of residence? Does their own form contradict that?",
        "     - What does the removal NOT cover — name search only? FCRA-exempt products?",
        "     - Any upsell to a paid removal service? -->",
        "",
        "## Verification",
        "",
        "<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->",
        "",
    ]
    path.write_text("\n".join(lines))
    return f"  wrote {bid}.md"


def status_block(bid, rec):
    """The generated `## Status` section, current as of the tracker."""
    lines = ["## Status", ""]
    lines.append(f"- Current: `{rec.get('status', 'pending')}`"
                 + (f" (updated {rec.get('updated','')[:10]})" if rec.get("updated") else ""))
    if rec.get("confirmation_ref"):
        lines.append(f"- Reference: `{redact(rec['confirmation_ref'])}`")
    if rec.get("note"):
        lines.append(f"- Note: {redact(rec['note'])}")
    return "\n".join(lines) + "\n"


def refresh(bid, st):
    """Rewrite an existing playbook's Status block in place, leaving the prose.

    The generated header goes stale the moment the tracker moves, and it is the
    first thing a reader sees -- a file whose top says `submitted` while the
    request has since hard-bounced is actively misleading. Hand-written sections
    are never touched."""
    path = OUT / f"{bid}.md"
    if not path.exists():
        return f"  no playbook: {bid}"
    text = path.read_text()
    new = status_block(bid, st.get(bid, {}))
    # Replace from the Status heading up to the next heading, and nothing else.
    out, n = re.subn(r"## Status\n.*?(?=\n## )", new, text, count=1, flags=re.S)
    if not n:
        return f"  no Status block: {bid}"
    if out == text:
        return f"  current: {bid}.md"
    path.write_text(out)
    return f"  refreshed {bid}.md"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--missing", action="store_true",
                    help="scaffold every acted-on broker with no playbook")
    ap.add_argument("--refresh", action="store_true",
                    help="update the Status block of existing playbooks in place")
    args = ap.parse_args()

    reg = {b["id"]: b for b in json.loads(REGISTRY.read_text())["brokers"]}
    st = json.loads(STATE.read_text()) if STATE.exists() else {}
    OUT.mkdir(exist_ok=True)

    if args.refresh:
        ids = args.ids or sorted(bid for bid in st
                                 if (OUT / f"{bid}.md").exists())
        for bid in ids:
            print(refresh(bid, st))
        print(f"\n{len(ids)} checked")
        return

    if args.missing:
        # Some brokers share one playbook under a family name; don't fragment it.
        aliases = (json.loads(ALIASES.read_text()).get("aliases", {})
                   if ALIASES.exists() else {})
        have = {p.stem for p in OUT.glob("*.md")}
        ids = [bid for bid, rec in st.items()
               if rec.get("status") in ACTED
               and bid not in have
               and aliases.get(bid) not in have]
    else:
        ids = args.ids
    if not ids:
        raise SystemExit("nothing to do — pass broker ids or --missing")

    for bid in sorted(ids):
        print(scaffold(bid, reg, st))
    print(f"\n{len(ids)} processed")


if __name__ == "__main__":
    main()
