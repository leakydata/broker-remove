# Mightyrep

- **Email:** privacy@MightyRep.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** mightyrep.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: privacy@mightyrep.com hard-bounced 'address not found'. Only contact published anywhere on their site is a NAMED INDIVIDUAL at their own domain, in the site footer beside the privacy policy - which is different from the stranger's-personal-address case verify_emails guards against, because this is the company's own published contact. Wrote to it, apologised for using a named address, and asked him to pass it on and to get the privacy mailbox fixed.

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

## The bounced address is the state-registered one

MightyRep's CA data broker registration (oag.ca.gov/data-broker/registration/564387,
approved 2023-03-16) lists `privacy@mightyrep.com` as the contact - the exact
address that hard-bounces "address not found". So the earlier note about writing
to a named individual in the footer was working around a genuinely dead official
channel, not a wrong guess. Fallback web route: `https://www.mightyrep.com/contact`
(untested; needs a human, no CAPTCHA info known).
