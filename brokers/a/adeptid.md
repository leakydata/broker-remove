# AdeptID, Inc.

- **Email:** privacy@adept-id.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** adept-id.com
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


## Ask for the derived layer, not the contact fields

AdeptID predicts suitability for work. A deletion scoped to name and email leaves
the consequential part intact, so the letter asks specifically for:

- skills inference, competency mapping, role-transition prediction
- employability, retention or attrition scores
- **inferred demographics** — gender, ethnicity, age band, socioeconomic class —
  including where inferred for bias measurement rather than targeting
- the employment and education history the above is derived from, **and where
  each element came from**

These are model outputs, not facts anyone supplied, and they are the elements a
person can least easily discover while employers act on them.

**The customer-upload question is the one that decides who to write to next.** If
an employer or staffing customer supplied the record, deleting AdeptID's copy
does not reach theirs. Asked them to name the customer or confirm they directed
deletion.


## 2026-08-24: the form will not open for a Pennsylvania resident

The email was received and routed to an Osano form (`my.datasubject.com`) with
*"you must fill out the following form"*. The form detects the jurisdiction and
renders **nothing** — no fields, no submit control:

> *"We have detected that you are attempting to submit a request from a
> jurisdiction that does not currently support privacy rights."*

Full write-up in `_DEFLECTIONS.md` §45. Three things to carry forward:

- **The gate is Osano's, not AdeptID's.** Any broker whose rights link lands on
  `my.datasubject.com` will do this to a requester in a state without a
  comprehensive privacy law. Check for it before spending time on the form.
- **The jurisdiction is a dropdown and it must not be changed.** Setting it to
  California would open the form and would be a false statement of residency made
  while asserting a legal right. Declined, and said so in the reply — naming it is
  what makes it fixable.
- **The email channel works.** Replied there asking them to treat the original
  message as the request, honour it under their published privacy policy, and
  raise the vendor gate with Osano.

**Status stays `submitted`**, not `failed` — a reply is outstanding on a live
channel. Recorded that the web route is closed to this requester so nobody
retries the form.

The substance of the request is unchanged and never depended on the form: the
derived layer, not the contact fields.
