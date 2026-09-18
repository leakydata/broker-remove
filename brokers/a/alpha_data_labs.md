# Alpha Data Labs

- **Email:** privacy@alphadatalabs.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** alphadatalabs.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-09-18)
- Note: Not previously in this registry. Added and contacted the same day it
  surfaced: hireEZ's data-subject reply (2026-09-17, see `hireez.md`) named
  Alpha Data Labs as one of the third parties it sources candidate contact
  data from, and gave this address as the opt-out contact. That is the only
  provenance for the address -- it has not been confirmed against Alpha Data
  Labs' own site or a state filing, so `email_verified` is left false until a
  reply or bounce settles it. Sent the standard B2B contact-enrichment letter
  (identifiers led with name/phone/institutional email forms, not personal
  email) the same day, since a company that supplies candidate contact data
  to a recruiting tool is exactly the kind of B2B index a generic
  people-search letter under-asks.

## Steps

1. Email `privacy@alphadatalabs.com` with the standard consumer
   deletion/opt-out/suppression request. Use the B2B contact-enrichment
   variant per `_CATEGORY_VARIANTS.md` -- ask what upstream/downstream
   customers (recruiting and sourcing tools like hireEZ) received a copy,
   since a deletion at Alpha Data Labs does not reach copies already exported
   into a customer's ATS or CRM.
2. If this bounces or goes unanswered, the fallback route is through hireEZ
   or any other customer that discloses Alpha Data Labs as a source --
   ask the downstream customer to confirm it directed the deletion upstream.

## Gotchas

- This is an UPSTREAM SUPPLIER discovered through a DOWNSTREAM CUSTOMER's
  disclosure, not through a state registry or the company's own site. The
  general pattern worth repeating elsewhere: when a recruiting/sourcing/
  enrichment tool answers a data-subject request, ask it explicitly who it
  sources FROM. The supplier is usually less visible (no consumer-facing
  product, no privacy-policy SEO footprint) and often bigger than the tool
  asking about it.
- No confirmation yet that `privacy@` is the right mailbox -- if it bounces,
  check whether Alpha Data Labs publishes a different contact on its own
  site before concluding the route is dead.

## Verification

No reply yet. Re-check via `verify_removals.py` after 7 days from the
2026-09-18 send.
