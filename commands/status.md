---
description: Where the removal campaign stands
---

Report progress. Run these and summarise:

```bash
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/tracker.py" stats
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/queue_batch.py" --summary --size 1
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/handoff.py" list --brief
```

Lead with what actually changed since last time and what is blocked on the user.
Do not pad with a list of everything checked.

Be honest about what the numbers mean: `submitted` is a letter sent, not a
removal. `confirmed` is the only status that means the data is gone, and it will
always be the smallest number. Say so rather than letting the total imply
progress it has not made.
