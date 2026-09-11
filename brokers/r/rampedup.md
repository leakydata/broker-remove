# RampedUp

- **Email:** contact@rampedup.io (site-published — unverified until a reply arrives)
- **Email fallback (dead):** privacy@rampedup.io — the address on their CA data broker registration, but it is a restricted Google Workspace group that rejects outside mail
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** rampedup.io
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-28)
- Note: 2026-08-26: emailed privacy@rampedup.io. Used the B2B variant: noted a personal-email search will likely return a false negative, asked them to search phone numbers and name variants instead, asked which customers received a copy of any record, and asked for a standing do-not-add suppression entry even on a null result.
- Note: 2026-08-27: privacy@rampedup.io hard-bounced — "the group you tried to contact (privacy) may not exist, or you may not have permission to post messages to the group" (a Google Workspace group, not a mailbox). Found contact@rampedup.io published on their own site and resent the same letter there, explaining the redirect. Registry corrected to use contact@rampedup.io as primary.
- Update 2026-08-27: contact@rampedup.io auto-replied that the inbox is unmonitored, and that CCPA/GDPR/do-not-sell requests must go through their web portal, which authenticates identity first. Queued for a human.

## Steps

1. Do not email at all. `contact@rampedup.io` is an unmonitored inbox that
   auto-replies to everything; `privacy@rampedup.io` is a restricted Google
   Group that bounces regardless of message content.
2. Use `https://basic.rampedup.io/app/donotsell` directly.

## Gotchas

- **The CA registration address is a Google Group, not a mailbox.** This is the recurring "internal-only distribution group" bounce class: it looks like any other 550 but Gmail's own delivery-failure text names it explicitly ("group you tried to contact ... may not exist, or you may not have permission to post"). The fix is the same every time — find a second address on the broker's own site, not a variant guess.
- **Neither published email address is actually monitored.** One is a dead
  Google Group, the other auto-replies "not a monitored inbox" to everything
  including a properly formatted opt-out letter. The portal is not a
  fallback here — it's the only route.

## Verification

No confirmation yet — pending the do-not-sell portal submission. No stated
timeframe found; ask when submitting.
