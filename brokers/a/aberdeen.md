# Aberdeen

- **Opt-out:** https://www.aberdeen.com/do-not-sell-my-personal-information/
- **Email:** privacy@spiceworks.com — **off-domain, corporate relationship unconfirmed**
- **Method:** web_form — Web form.
- **Domain:** aberdeen.com
- **Priority: 2.**

## Status

- Current: `email_pending` (updated 2026-08-29)
- Note: Sent 2026-08-29 to privacy@spiceworks.com. **This should not have gone out yet.** The registry already flags this address `email_verified_by: offdomain_needs_confirmation` — `privacy@spiceworks.com` is not on `aberdeen.com`, and the note on the entry says explicitly: "confirm the corporate relationship before sending: the letter carries a full identifier set." A stale local copy of the registry used for this batch didn't carry that hold flag, so the send went out without the check `queue_batch.py` normally applies (it excludes anything flagged `offdomain_needs_confirmation` from an auto-sent batch — see its `HOLD` set).

## Steps

1. **Before treating this as resolved, confirm the relationship.** Aberdeen
   and Spiceworks both plausibly sit under the same media/B2B-data parent
   (Foundry/Ziff Davis-adjacent), which would make this a legitimate shared
   privacy inbox — but that is a plausible story, not confirmed fact. If a
   reply comes back with no sign of actually knowing who Aberdeen is, that is
   itself the answer: this letter went to an unrelated company.
2. If a reply confirms the relationship, treat this as a normal submission.
   If not, do not repeat this mistake for other `offdomain_needs_confirmation`
   entries — check that flag before adding a broker to a send batch, not
   just whether `email_to` is populated.

## Gotchas

- **A registry hold flag is only useful if the send path actually reads it.**
  This project's `queue_batch.py` has a `HOLD` set specifically for this
  situation (see its comment on `DISCOVERED_OFFDOMAIN` /
  `firstadvantage.com`-style mistakes) — the failure here wasn't a missing
  safeguard, it was a batch built by hand from a copy of the registry that
  predated the flag being set, which bypassed it entirely.

## Verification

Sent 2026-08-29. When a reply arrives, read it specifically for evidence of
the corporate relationship before recording anything further.
