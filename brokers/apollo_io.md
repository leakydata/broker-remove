# Apollo.io

- **Opt-out:** https://www.apollo.io/privacy-policy/remove
- **Email:** privacy@apollo.io (verified)
- **Method:** web_form — Web form.
- **Domain:** apollo.io
- **Priority: 4.**

## Status

- Current: `submitted` (updated 2026-08-21)
- Note: 2026-08-20: first contact, sent to the address discovered by the verify_emails sweep. Tailored per _CATEGORY_VARIANTS.md.

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

## Category: B2B contact & sales prospecting

See `_CATEGORY_VARIANTS.md`, section "B2B contact & sales prospecting databases",
and `_DEFLECTIONS.md` §44 for the deflection to expect ("which email format is it
under?" / "we can search under your LinkedIn URL").

**Address discovered, not curated.** `privacy@apollo.io` came from the
`verify_emails.py --no-email` sweep on 2026-08-20; Apollo had a live domain and
no route in the registry until then.

**What the letter asks that the standard one does not:**

- states up front that a search over personal webmail will return nothing even
  if a record exists, because the index is keyed to work addresses that are
  frequently pattern-generated or captured by a customer's browser extension —
  identifiers the subject never chose and cannot reproduce;
- redirects the search to **telephone numbers and name variants**; the phone
  number is the most person-shaped field a prospecting database holds, because a
  direct dial follows someone between jobs;
- asks **which mechanism created the record** — supplier feed or extension
  capture. This matters because supplier suppression does not stop the second
  one: any customer repeating the action recreates it;
- asks which customers exported the record into a CRM or sequencer, since that
  copy is beyond Apollo's deletion and is what produces the calls;
- asks for a **do-not-add suppression entry that survives a null result**, citing
  SourceIT's SHA-1/SHA-256 practice as precedent — naming another firm's
  practice moves the ask from favour to norm;
- **declines to supply a LinkedIn URL, with the reason given.** A profile URL is
  a stable, unique, employer-linked key; supplying one to a contact database
  furnishes an identifier they may not hold plus a link to everything else in the
  letter. If no record exists, that search assembles the match it claims to test.

**A null result here is not `not_found`.** It is a search run on the wrong keys
with the suppression request outstanding.
