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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Staircase, Inc.
- **Registered address:** 2093AÂ Philadelphia Pike, Suite 452, Claymont,
  DE 19703, United States
- **Filed contact email:** optout@staircase.co
- **Website:** https://staircase.co/
- **Opt-out route they filed:** 1) Internet web page: Customers will be
  able to identify themselves and claim profile with full update, edit,
  delete capabilities, , 2) Email: optout@staircase.co,
- **Route for protected individuals:** 1) Internet web page: Customers
  will be able to identify themselves and claim profile with full update,
  edit, delete capabilities, , 2) Email: optout@staircase.co (Cal. Gov.
  Code 6208.1(b) / 6254.21(c)(1) — for survivors of domestic violence,
  stalking and similar, a stronger and faster route than the ordinary
  consumer request)

*Source: `data/registries/complete-reg-data-brokers.csv`.*

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
