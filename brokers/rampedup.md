# RampedUp

- **Email:** contact@rampedup.io (site-published — unverified until a reply arrives)
- **Email fallback (dead):** privacy@rampedup.io — the address on their CA data broker registration, but it is a restricted Google Workspace group that rejects outside mail
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** rampedup.io
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-27)
- Note: 2026-08-26: emailed privacy@rampedup.io. Used the B2B variant: noted a personal-email search will likely return a false negative, asked them to search phone numbers and name variants instead, asked which customers received a copy of any record, and asked for a standing do-not-add suppression entry even on a null result.
- Note: 2026-08-27: privacy@rampedup.io hard-bounced — "the group you tried to contact (privacy) may not exist, or you may not have permission to post messages to the group" (a Google Workspace group, not a mailbox). Found contact@rampedup.io published on their own site and resent the same letter there, explaining the redirect. Registry corrected to use contact@rampedup.io as primary.

## Steps

1. Email `contact@rampedup.io`, not `privacy@rampedup.io` — the latter is a restricted Google Group and will bounce regardless of message content.

## Gotchas

- **The CA registration address is a Google Group, not a mailbox.** This is the recurring "internal-only distribution group" bounce class: it looks like any other 550 but Gmail's own delivery-failure text names it explicitly ("group you tried to contact ... may not exist, or you may not have permission to post"). The fix is the same every time — find a second address on the broker's own site, not a variant guess.

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
