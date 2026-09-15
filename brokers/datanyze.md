# Datanyze

- **Email:** privacy@datanyze.com (discovered 2026-09-12 — not yet verified by a reply)
- **Method:** email
- **Domain:** datanyze.com — technographic/B2B contact data; some sources
  describe Datanyze records as now administered under ZoomInfo.
- **Priority: 1.**

## Status

- Current: `submitted` (2026-09-15)
- **Reply (2026-09-14):** *"We have added your information to the removal
  queue, which will be completed within 24-72 hours. Third parties who may
  have had access to these details have also been notified."* Doesn't say
  whether a record actually existed, and doesn't answer the ZoomInfo
  administration question either way — a queue-and-ETA acknowledgement, not
  yet a completion. Left at `submitted`; re-check with `verify_removals.py`
  once the 24-72h window has passed.
- Note: registry previously carried only a bare Optery stub with no domain
  or contact — the address above was found and used directly. The letter
  asked that, if Datanyze records are now held or administered by
  ZoomInfo, the request be applied there too rather than treated as
  out of scope.

## Steps

1. Email `privacy@datanyze.com`.
2. If the reply says the brand has been folded into ZoomInfo, check whether
   a ZoomInfo registry entry already exists and cross-reference rather than
   opening a fresh request there — see the cience_technologies playbook for
   the pattern of a brand folding into a differently-named operator.

## Gotchas

- Reply gives a specific 24-72h ETA rather than a vague "in progress" —
  worth checking back within that window rather than waiting the full 7 days.

## Verification

Queue acknowledgement received 2026-09-14 with a 24-72h ETA. Re-check after
that window (well before the standard 7-day `verify_removals.py` cycle).
