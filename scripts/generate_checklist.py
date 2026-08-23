#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Generate a human do-it-yourself checklist for every broker that automation
cannot finish: CAPTCHA gates, account signups, ID uploads, phone/postal-only flows.

These are the steps a human has to perform. Grouping them into one document means
they can be cleared in a single sitting instead of one interruption at a time --
which matters because reCAPTCHA tokens expire in about two minutes.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
from paths import state, outbox  # noqa: E402
BLOCKED = {"captcha_blocked", "manual_required", "email_pending", "failed"}

REASON = {
    "captcha_blocked": "Solve the CAPTCHA and click submit. The form is already filled.",
    "manual_required": "Needs an account, a photo ID, a phone call, or postal mail.",
    "email_pending": "Click the confirmation link in the inbox. Unconfirmed requests are void.",
    "failed": "Attempt failed - needs a look.",
}


def main():
    reg = {b["id"]: b for b in
           json.loads((ROOT / "data" / "brokers.json").read_text())["brokers"]}
    state_path = state("removal_status.json")
    state = json.loads(state_path.read_text()) if state_path.exists() else {}

    items = [(bid, rec, reg.get(bid, {})) for bid, rec in state.items()
             if rec.get("status") in BLOCKED]
    items.sort(key=lambda t: (-t[2].get("priority", 0), t[0]))

    lines = [
        "# Manual Action Checklist",
        "",
        "Steps automation cannot legitimately complete. Everything else is already done.",
        "",
        "> Work top to bottom - the list is ordered by how much each broker's data",
        "> spreads to other brokers, so the early entries have the widest effect.",
        "",
    ]

    if not items:
        lines.append("_Nothing blocked. All attempted brokers went through cleanly._")
    else:
        by_status = {}
        for bid, rec, b in items:
            by_status.setdefault(rec["status"], []).append((bid, rec, b))

        for status, group in by_status.items():
            lines += [f"## {status.replace('_', ' ').title()}", "",
                      f"_{REASON.get(status, '')}_", ""]
            for bid, rec, b in group:
                url = rec.get("optout_url_used") or b.get("optout_url", "")
                lines.append(f"- [ ] **{b.get('name', bid)}** — <{url}>")
                if rec.get("note"):
                    lines.append(f"      - {rec['note']}")
                pb = ROOT / "brokers" / f"{bid}.md"
                if pb.exists():
                    lines.append(f"      - Playbook: `brokers/{bid}.md`")
            lines.append("")

    out = ROOT / "docs" / "MANUAL_CHECKLIST.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out} ({len(items)} items needing a human)")


if __name__ == "__main__":
    main()
