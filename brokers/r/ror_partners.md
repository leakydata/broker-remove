# ROR Partners

- **Email:** privacy@rorpartners.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** rorpartners.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-23)
- Reference: `L7JE3RVPKK`
- Note: OneTrust intake exists (Request ID L7JE3RVPKK, origin unknown — no corresponding sent letter found in Gmail Sent), requiring an email-confirmation click before processing starts. WebFetch on the confirmation link returns only a bare JS shell ('Trust Center Portal') — the confirm action needs a real browser (JS/POST), which this agent does not have. Needs a human to open the email and click Confirm; link may expire.

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


## Verified 2026-08-23 — and the fetch could not tell me so

OneTrust request `L7JE3RVPKK`. The emailed confirmation link, fetched over plain
HTTP, returned a page whose entire readable content was the words "Trust Center
Portal": no confirmation, no error, nothing to record.

Opened in a real browser it showed a green tick and *"Your request is confirmed!
We will review your request and contact you shortly."*

The portal is a JavaScript app and the fetch got the shell. **A verification link
whose fetch returns no confirmation text is unverified, not verified** — the two
outcomes are indistinguishable from the fetch alone, and an unconfirmed request
does not exist. See `_SILENT_FAILURES.md` §79.
