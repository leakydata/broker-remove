---
description: Show the steps that need a human, batched into one sitting
---

Show what is waiting on the user:

```bash
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/handoff.py" list
```

Present it as a short worklist with a realistic total time. Group by kind —
CAPTCHAs, single clicks, phone calls, decisions — because a batch of ten
identical CAPTCHAs is one sitting and ten scattered interruptions are not.

For each item make sure the instruction stands alone: broker, URL, exact steps.
Never rely on a browser tab still being open; tabs do not survive the wait.

If an item can no longer be completed at all — a confirmation sent to a mailbox
the user cannot access, a form that has since changed — take it off the queue and
say so. A permanent no-op sitting in a list of things someone is asked to do
makes the whole list easier to ignore.

Offer to stage the CAPTCHA items into tabs so they can be cleared in one run.
Solve-then-submit must be adjacent: a solved CAPTCHA token goes stale in about
two minutes, so never queue a second solve before the first is submitted.
