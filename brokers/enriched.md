# Enriched

- **Email:** admin@getconversiondata.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** getenriched.io
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-25)
- Note: 2026-08-25: contact domain publishes no MX and no A record - nothing can be delivered. The broker's own domain is equally dead, so there is no alternative route by mail. Never written to; marked before spending a send. Re-check if the domain is ever reinstated.

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


## Unreachable: no mail route exists

Both the contact address published in their California data broker registration
**and** the company's own domain have no MX record and no A record. There is
nowhere to deliver a message, so no letter was ever sent.

Found by `check_email_domains.py`, which asks whether a contact domain can
receive mail at all before a send is spent on it. See `_SILENT_FAILURES.md` §86.

**Why this is `unreachable` rather than `failed`.** Nothing was attempted and
nothing was refused. A domain with no mail records produces a *delayed delivery*
notice and roughly 48 hours of retries before it finally fails, so writing here
would have shown `submitted` for two days and taught nobody anything.

**Re-check rather than treating this as final.** A dead domain can mean a lapsed
registration, a company that has wound up, or a rebrand that left the filing
behind. If the domain is ever reinstated, or a successor entity appears in a
later state registration under the same legal name, the route reopens.
