# Deluxe

- **Email:** privacy@deluxe.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** deluxe.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Note: Statutory delete/opt-out emailed to privacy@deluxe.com. Tailored for a company with both a customer-facing business and a marketing-data arm: asked them to treat it as a request against BOTH systems and to say which held a record, and to search hashed/pseudonymised identifier forms.

## Steps

1. Email `privacy@deluxe.com` with the two-arm framing described below.
2. Ask explicitly **which system held a record**. A single "we have deleted your
   information" from a company with several data estates does not tell you how
   many of them were searched.
3. Ask them to search hashed and pseudonymised forms of each identifier.

## Gotchas

Deluxe is two businesses wearing one name: a customer-facing services company
(cheques, payments, business services) **and** a marketing-data and data-services
arm that licenses audience data. A deletion request that does not say so gets
answered by whichever team owns the mailbox.

That is the general problem with any broker whose brand is better known for
something else. The customer-service reading of "delete my data" is *close my
account and remove my customer record* — a truthful, complete-sounding answer
that leaves the marketing database untouched, because the person answering never
had access to it and did not know to ask.

**Write the request against each estate by name**, and ask which ones held a
record. The answer is also intelligence: it tells you whether the marketing arm
holds you at all, which no amount of searching from outside will reveal.

Hashed identifiers matter here for the same reason they matter in adtech: a
company that "has no record of your email address" may hold its MD5 or SHA-256
digest, which is the same record under a different key. Ask for those forms to be
searched explicitly (`_CATEGORY_VARIANTS.md`).

<!-- Further notes from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
