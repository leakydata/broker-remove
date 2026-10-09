# Xverum (Operia)

- **Email:** privacy@xverum.us (verified — found on their published privacy policy)
- **Opt-out (fallback):** https://www.xverum.com/dontusemydata/
- **Method:** email — statutory request by email, avoiding the browser-gated form.
- **Domain:** xverum.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-10-09)
- Reference: `gmail:1a120329d4b9ee8d`
- 2026-10-09: found `privacy@xverum.us` on their own privacy policy via
  `verify_emails.py` — the browser-gated form is no longer the only route.
  Sent the B2B contact/candidate-data variant (see Steps and `
  _CATEGORY_VARIANTS.md` "B2B contact & sales prospecting databases"): asked
  them to search name and phone rather than personal email, asked whether
  their index is keyed to observed or pattern-generated addresses, and asked
  the four category-specific questions (exported CRM copies, browser-
  extension capture, re-verification vs. standing suppression, and a
  do-not-add suppression that survives a null result, citing SourceIT's
  hash-retention practice as precedent). Awaiting reply.
- Prior (2026-09-18): `manual_required`. Not previously in this registry.
  hireEZ's data-subject reply (2026-09-17, see `hireez.md`) named
  "Operia/Xverum" as one of the third parties it sources candidate contact
  data from and pointed to the opt-out form above — no email address was
  known at the time. Superseded by the email route found above.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@xverum.us`** rather than fighting the browser-gated form.
   Ask for the four statutory things explicitly — deletion, opt-out,
   third-party direction, and forward-looking suppression.
2. **Search keys matter more here than at a people-search site.** This is a
   candidate-sourcing/contact-finding product: a search over personal
   webmail addresses will likely return nothing even if a record exists,
   because the index is built on work addresses and phone numbers. Ask them
   to search name and phone, and ask whether the index is keyed to observed
   or pattern-generated addresses.
3. **Ask for a do-not-add suppression even on a null result**, so a future
   enrichment pass from an upstream supplier doesn't recreate the record.
4. If the email route ever goes dark, fall back to
   https://www.xverum.com/dontusemydata/ — browser-gated, needs a human, and
   if it has a CAPTCHA, stage everything and hand off only the click.

## Gotchas

- Discovered as an UPSTREAM SUPPLIER via a downstream customer's (hireEZ's)
  disclosure, not via Xverum's own site or a state filing -- the same pattern
  as `alpha_data_labs`. Worth checking hireEZ's reply again if this company
  changes its opt-out route, since hireEZ is the only source for it here.
- The email route (`privacy@xverum.us`) was published on their privacy
  policy, not on the opt-out form itself — the form reads as the only route
  until you check the policy page.

## Verification

Submitted 2026-10-09. Watch for: which identifiers matched (if any),
whether the index is observed- or pattern-keyed, and confirmation of a
standing do-not-add suppression distinct from a one-time deletion.
