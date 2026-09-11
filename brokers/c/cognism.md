# Cognism

- **Opt-out:** https://www.cognism.com/data-opt-out
- **Email:** privacy@cognism.com (verified)
- **Method:** web_form — Web form.
- **Domain:** cognism.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-30)
- Note: 2026-08-30 reply, 13 days after the original: "unable to locate a user account associated with the information you provided," and asked for a work email, phone number, and LinkedIn URL to help match. Declined the LinkedIn URL -- if they don't already hold one linked to my name, sending it creates a link that did not previously exist, which is the opposite of a deletion request. Pointed out the framing error instead: this was never an account-based request, and a search against an account table will always return nothing for a B2B contact-database record. Re-sent the already-provided phone number (plus 8 priors) and all 8 email addresses, asked them to run the search against the prospecting/contact database rather than an account lookup, and said plainly that "not found" is an acceptable answer if that broader search genuinely returns nothing.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

- The "no account found" deflection at a data-compiler (not a consumer service) is usually a mismatched search, not a real negative: their support tooling often only queries an account/login table, which a prospecting-database record was never in. Worth naming that distinction explicitly rather than just resending identifiers.
- They will ask for a LinkedIn URL or work email as a "match aid." Refuse the LinkedIn URL specifically if one isn't already on file — it's an identifier that creates a link between an anonymous B2B record and a named identity rather than testing an existing one.

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
