# Babel Street, Inc.

- **Email:** privacy@babelstreet.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** babelstreet.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-09-10)
- Note: 2026-09-06 sent the full access/deletion/opt-out/sources letter to privacy@babelstreet.com. Babel Street sells location, mobile-audience and open-source (social/handle-keyed) intelligence products, so the letter stated up front what identifiers would never be supplied — no MAID, device ID, IP, cookie ID or social handle — and asked them to say plainly whether "no record" means a genuine negative search or an admission that their data isn't indexed in a way a consumer can query at all. Also asked for sources by category (open web / licensed vendor / mobile location supply / public records) since deletion here does nothing about an upstream copy.
- **Reply (2026-09-10, auto):** directed to a OneTrust Data Subject Rights Portal, but offered an email-only path: reply "CONFIRM" if declining the portal. Replied CONFIRM, explicitly opting out of the portal since it would only ask for identifiers already in the letter.
- **Reply (2026-09-10, human):** Babel Street proceeded anyway via the OneTrust portal ("since you have already provided the necessary verification information") and said two MFA prompts would follow — one by email, one by SMS.
- **This is the CAPTCHA-equivalent stopping point:** SMS MFA to Nathan's phone cannot be completed by this project (no browser, no phone access). Queued for handoff — see `scripts/handoff.py`.

## Gotchas

Babel Street's intake email accepts "CONFIRM" as an alternative to the OneTrust portal for the *initial* verification step, but that does not prevent them from routing the underlying request through the portal anyway once a ticket is opened — the email opt-out only avoids the *first* portal touchpoint, not all of them. Expect SMS MFA even after declining the portal.

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
