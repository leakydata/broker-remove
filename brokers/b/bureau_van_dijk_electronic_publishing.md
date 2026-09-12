# Bureau van Dijk Electronic Publishing Ltd.

- **Email:** privacy@moodys.com (verified — replaces privacy@bvdinfo.com, which bounced)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** bvdinfo.com (privacy operations now run through moodys.com)
- **Priority: 2.**
- **Family:** canonical entry for the Moody's group — `moody_s` and
  `moody_s_analytics` are held out of the send queue as `duplicate_of` this
  entry (same mail tenant; see `data/broker_families.json`). Raise any sibling
  question in this thread, not a second one.

## Status

- Current: `failed` (updated 2026-08-25)
- Note: 2026-08-25: privacy@bvdinfo.com bounced 550 5.1.1 'address not found' - the registered contact in the CA filing is dead. Domain resolves fine and has valid MX, so no domain-level deliverability check could have caught this; only sending did. REQUEST IS NOT ABANDONED: bvdinfo.com sits in Proofpoint tenant 00520701 alongside moodys.com and reis.com, so BvD was folded into the family letter to privacy@moodys.com, which explicitly names Bureau van Dijk and asks them to correct the stale filing. Track the outcome under moody_s.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

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
