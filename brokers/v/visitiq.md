# VisitIQ LLC

- **Email:** [named individual]@visitiq.io (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** visitiq.io
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-09-07)
- Reference: `outbox/staged/visitiq_ketch.txt`
- Note: EMAIL REFUSED OUTRIGHT 2026-09-03 by [named individual]@visitiq.io: 'we do not process data requests via email... Please do not reply to this email as it is not monitored.' A designated-method refusal from an address that also disclaims being read, so there is no channel to argue with. ROUTE: https://visitiq.io/data-rights-and-privacy/ is a KETCH privacy widget rendered entirely in JavaScript, carrying a CAPTCHA -- nothing is visible to a plain fetch and no fields can be filled without a browser. Staged for a human at outbox/staged/visitiq_ketch.txt and queued. INCIDENTAL: the page leaks raw PHP into its own HTML -- the string wp_body_open(); ?> appears as visible text -- so a WordPress template is broken there. Harmless to this request; recorded only because there is no reply channel to mention it through. WHY THE ORDERING MATTERS FOR THIS ONE: VisitIQ is a website-visitor identification product, so its business is resolving anonymous site traffic to named people. A deletion alone is undone the next time the subject loads a page carrying their pixel; the OPT-OUT and the SUPPRESSION are the parts that persist. Same shape as LeadPost. The staged file says so and tells the operator to take every right the widget offers rather than deletion alone, and to supply no MAID, cookie id, device id or IP whatever is asked -- those being exactly the identifiers this product runs on.

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
