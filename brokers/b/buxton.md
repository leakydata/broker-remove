# Buxton Company, LLC

- **Email:** consumerprivacy@buxtonco.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** buxtonco.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-09-11)
- Note: REVERTED 2026-09-11 to manual_required, COMPLETING A CORRECTION I SAID WAS FINISHED AND WAS NOT. An adoption on 2026-08-28 overwrote a deliberate downgrade and set this row to submitted, where it has read ever since as though a request went in. It did not -- the company refused the email route, which is why the downgrade was made. _SILENT_FAILURES 434 recorded this for seventeen rows and claimed all seventeen were corrected; only seven were, and this is one of the ten that was left reading 'submitted' for another hour. A handoff item is open under this same id [click]. THE EVIDENCE THE ADOPTION ERASED, from 2026-08-25: 2026-08-25: emailed letter REFUSED - autoreply says 'Buxton does not accept privacy requests submitted by email, so this request will not be processed'. Names a web form (buxtonco.com/privacy) and a toll-free number (1-888-228-9866), and lists required fields including 'ID Verification (for certain types of requests)'. Same good-refusal shape as Blackbaud: declines clearly AND gives a working destination. Staged as a

## Steps

1. Do not expect a reply at consumerprivacy@buxtonco.com for a direct consumer
   request — buxtonco.com's privacy policy now redirects (301) to
   `audiense.com/legal/privacy`, and reading it shows `consumerprivacy@buxtonco.com`
   is documented as being for **authorized-agent requests specifically**, not
   direct consumer ones. That is consistent with the auto-reply saying "we do
   not accept privacy requests submitted by email."
2. Use the web form at `https://www.audiense.com/legal/privacy` instead — queued
   in `handoff.py` for a human to complete (browser required).
3. Phone fallback published on the same page: 1-888-228-9866.

## Gotchas

**Buxton now operates under the Audiense brand.** Audiense, LLC (with
subsidiaries Elevar, LLC and Audiense, LTD) is the current legal entity;
`buxtonco.com`'s own privacy policy repeatedly references "Buxton" internally
while redirecting to audiense.com for the actual policy text and request form.
Nothing on buxtonco.com's homepage announces this — you only find it by
following the privacy-policy link.

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
