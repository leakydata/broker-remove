# Veripages

- **Opt-out:** https://veripages.com/optout
- **Email:** support@veripages.com (verified)
- **Method:** web_form — Web form.
- **Domain:** veripages.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Reference: `gmail:1a006815a9f66229`
- Note: Broker directs to /inner/control-privacy but requires a /profile/<Name>/<ID> URL. That format is not exposed in their public search (only /name/First/Last/, which their own email calls wrong), and the full-profile route raises a paid-trial modal. Searched current city and two prior cities: no matching profile identifiable among 214 same-name PA records. Replied asking them to process by identifiers, supply the URLs, or confirm no records.

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

## Email is answered by a human, and points at a web form

`support@veripages.com` replies quickly and usefully:

> *"Veripages has a tool to remove information on the homepage labeled Do Not Sell
> My Info. You can submit your removal request here,
> https://veripages.com/inner/control-privacy"*

## The form needs a profile URL you cannot get

The same reply insists on an exact URL format:

> *CORRECT FORMAT: `https://veripages.com/profile/Tom-Lee/HTHQAoBB`*
> *wrong format: `https://veripages.com/name/Tom/Lee/`*

**That format is not present in their public search results.** Inspecting the
result pages for every anchor, the only person links are `/name/First/Last/` — the
format the email calls wrong. "View all details" does not resolve to a
`/profile/<Name>/<ID>` address, and clicking through raises a **"$1 – 7 day trial
access"** modal before any detail appears.

So the removal route requires an identifier that the free site does not hand out.
See `_DEFLECTIONS.md` §12 for how to answer this without simply giving up.

## Search notes

- `/inner/profile/search?fname=<First>&lname=<Last>&state=<ST>` works, and accepts
  `&city=<City>`. The city filter is loose: results include people who merely
  *lived* in that city at some point, so unrelated records from other states
  appear.
- Result cards show aliases, cities, relatives and partial phone numbers, but
  **no date of birth**, and age is missing on some. With a common name that leaves
  very little to disambiguate on.
- A common first-and-last-name search returned **214 people in one state** over 20
  pages.

## Scope note

Cards are labelled "Data provided by Veripages" alongside sponsored panels for
TruthFinder and BeenVerified. Removal here does not touch those services — they
are separate brokers with their own opt-out routes.

