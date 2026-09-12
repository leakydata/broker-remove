# Openpublicrecords

- **Opt-out:** https://www.open-public-records.com/records_removal.htm
- **Method:** web_form — Web form.
- **Domain:** open-public-records.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-07)
- Reference: `open-public-records.com forms POST to /click-ad.php and /opr-bc-redirect.php`
- Note: CORROBORATED 2026-09-07 BY THE SITE'S OWN MARKUP: open-public-records.com IS NOT SEARCHABLE. Both of its apparent search forms POST to /click-ad.php and /opr-bc-redirect.php -- affiliate redirect endpoints, not a query handler. The site takes a name and hands the visitor to a paying partner; it runs no index of its own. Same structure as dobsearch_com, established the same way (SILENT_FAILURES 390: read what the site is, not what it looks like). So the earlier not_found stands for a stronger reason than 'a search returned nothing' -- there is no search, and no holding behind it. Nothing to re-verify here, and the row is excluded from the re-verification sweep accordingly.

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
