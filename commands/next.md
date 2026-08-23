---
description: Run one removal pass — inbox, verification, a batch of letters, playbooks
---

Run a full removal pass, in this order. Do the work; do not describe it.

1. **Inbox first.** Bounces before replies. For each reply: what does it *quote*?
   A broker answering a superseded message is answering the quoted one. Handle
   deflections using `${CLAUDE_PLUGIN_ROOT}/brokers/_DEFLECTIONS.md`.
2. **Click any pending verification links.** An unconfirmed request does not
   exist, and these expire — often in 30 minutes.
3. **`verify_removals.py`** for anything submitted more than 7 days ago.
4. **Send the next batch** within the daily cap, tailored per
   `${CLAUDE_PLUGIN_ROOT}/brokers/_CATEGORY_VARIANTS.md`.
5. **Work browser forms.** Never solve a CAPTCHA — stage the form fully and queue
   a one-click handoff.
6. **Write the playbooks**, quoting the broker rather than paraphrasing. Run
   `playbook_audit.py`.
7. **Run `validate.py` and `redact.py`, check they passed, then commit.** Not
   chained beside the commit — before it.

Report briefly at the end: what moved, what is blocked, what needs the user.
