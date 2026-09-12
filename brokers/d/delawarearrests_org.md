# Delaware Arrests

- **Method:** web_form — Web form.
- **Domain:** delawarearrests.org
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-09-08)
- Note: CORRECTED 2026-09-08, SAME DAY, BEFORE ANY TIME WAS SPENT ON IT. This row was briefly set to 'pending' with a /ccpaOptOut/ route on the strength of an HTTP 200. That was wrong. A negative control -- requesting /zzz-not-a-real-page-9137/ on the same host -- also returns 200, with byte-identical content. Nine of these domains serve a 114-byte parking stub for every path; four serve a ~32KB generic landing page for every path. THERE IS NO ROUTE AND NO SECOND FAMILY. The contrast is decisive: every real InfoTracer sibling (california, nevada, pennsylvania, texas, ohio, alabama, georgia, wyoming) returns 404 on the same nonsense path while returning 200 on its genuine /ccpaOptOut/ or /contact-form. So the network is 33 operating InfoTracer front-ends plus these parked domains, not two operations. Recorded unreachable: the domain resolves and answers, and there is nothing behind it a consumer can use. See _SILENT_FAILURES 427.

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
