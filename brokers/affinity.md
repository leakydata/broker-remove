# Affinity

- **Email:** privacy@affinity.co (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** affinity.co
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-24)
- Note: 2026-08-24: first contact via the address nominated in the California data broker registration. Tailored per _CATEGORY_VARIANTS.md.

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


## Ingested from somebody else's mailbox, which changes the question

Affinity builds relationship intelligence by ingesting customers' email and
calendar histories. A person can therefore be in the product having never heard
of it — the route in is a third party's correspondence.

So the letter opens with a controller/processor scoping question and asks them to
answer it **explicitly** rather than by implication:

1. Data held for Affinity's own account, in a shared or enriched dataset — a
   consumer deletion right reaches it.
2. Data processed for a customer whose mailbox contains the subject — then
   **name the customers**, because "we are only a processor" without naming the
   controller leaves a right with nobody to exercise it against, which in
   practice is no right at all.

Three asks specific to a correspondence-derived graph:

- **What was captured** — signature-block phone numbers, message metadata,
  meeting attendance, inferred relationship-strength scores.
- **Graph edges.** An edge recording that the subject corresponded with someone
  is information about them, is indexed separately, and survives deletion of the
  contact row.
- **Re-enrichment**, and whether suppression is standing or point-in-time.
