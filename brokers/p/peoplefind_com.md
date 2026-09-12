# Peoplefind Com

- **Opt-out:** https://www.intelius.com/privacy-center
- **Method:** web_form — Web form.
- **Domain:** peoplefind.com
- **Priority: 2.**

## Status

- Current: `covered_by_sibling` (updated 2026-09-07)
- Reference: `peopleconnect family suppression 2026-08-27; key set extended 2026-08-31`
- Note: RESOLVED 2026-09-06 AS AN INTELIUS-BRANDED FRONT END. The site says so itself, on its own About page: the service is described as "powered by Intelius", and the search, the report format and the FCRA disclaimer are Intelius. It is not an independent holder of records. THE PARENT IS ALREADY SUPPRESSED: PeopleConnect confirmed a family-wide suppression on 2026-08-27, applied in ONE ACTION across Intelius.com, InstantCheckmate.com, TruthFinder.com and USSearch.com, and Intelius extended the key set on 2026-08-31 to cover four further email addresses, six prior addresses including two PO boxes, and three prior phone numbers. THE CAVEATS THAT CAME WITH IT CARRY OVER TO THIS ROW UNCHANGED, and they matter more than the closure: (1) it is a DISPLAY SUPPRESSION, NOT A DELETION, and they explained why in architectural terms -- "background reports are compiled in real time via live calls to data providers... Because we do not retain reports, we cannot delete them"; (2) the suppression is keyed to a NAME SEARCH, so a lookup by phone, address or email may still surface a report; (3) PeopleConnect scoped it to "the people search sites within our corporate family that we control", and a powered-by brand is within that scope on the plain reading, but nobody at PeopleConnect has confirmed THIS domain by name. METHOD, so this is not mistaken for a bulk close: checked individually against the SILENT_FAILURES 390 test -- read what the site says it is. Three sites in this cluster say "powered by Intelius" on their own pages and are closed on that. The others sharing the same recorded route do NOT, and have been left open with their findings recorded rather than swept up in the same verdict.

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
