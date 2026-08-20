# Staircase

- **Email:** optout@staircase.co — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** staircase.co
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-20)
- Note: NO CONTACT ROUTE. optout@staircase.co hard-bounces 550 5.1.1 (it came from a broker listing, not from their site - which the letter said openly). The site has NO privacy page and no legal pages at all: /privacy-policy/, /privacy, /legal, /legal/privacy-policy, /terms, /privacy-notice and /company/privacy all 404, the sitemap contains no legal URLs, and rendering the site in a browser finds zero mailto links, zero links matching privacy/legal/terms/ccpa/opt-out, and zero email addresses in the rendered text. What staircase.co actually is: developer documentation for a mortgage data platform - the navigation is a data model listing person, person_credit, person_income, credit, employment, employment_income, property, property_tax and so on. So they are a B2B infrastructure vendor who would hold consumer data as a processor for lenders rather than a consumer-facing broker, which explains the absence of a consumer privacy page without excusing it. No further route without a business contact.

## Steps

**No contact route exists.** `optout@staircase.co` hard-bounces 550 5.1.1, and
that address came from a broker listing rather than from Staircase.

Everything else was checked and came back empty:

| checked | result |
|---|---|
| `/privacy-policy/`, `/privacy`, `/legal`, `/legal/privacy-policy`, `/terms`, `/privacy-notice`, `/company/privacy` | all 404 |
| `sitemap.xml` | no legal URLs |
| rendered page, `a[href^="mailto:"]` | none |
| rendered page, links matching privacy/legal/terms/ccpa/opt-out | none |
| rendered page, addresses in visible text | none |

## Gotchas

- **Render before concluding.** `staircase.co` is a JavaScript application and
  `curl` sees almost nothing, so the absence of links in the fetched HTML proves
  nothing. Only the browser check makes "no legal pages at all" a finding rather
  than a guess.
- **Read what the site is before writing again.** The navigation is a published
  data model — `person`, `person_credit`, `person_income`, `credit`,
  `employment`, `employment_income`, `property`, `property_tax`. This is
  developer documentation for a mortgage data platform, i.e. a B2B vendor
  holding consumer data as a processor for lenders, not a consumer-facing
  broker. That explains the missing consumer privacy page without excusing it.
- **The letter that bounced said so openly** — that the address came from a
  broker listing and that the first question was simply whether they hold
  anything at all. Keep that framing if a route is ever found; asserting a
  business model you inferred is the mistake `_SILENT_FAILURES.md` §67 records.

## Verification

Nothing to verify. Reopen only if a business contact surfaces — a lender's
vendor list, a state registry filing, or a named privacy officer.
