# Addresssearch Com

- **Opt-out:** https://www.addresssearch.com/remove-info.php
- **Method:** web_form — Web form.
- **Domain:** addresssearch.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-09-05)
- Note: SUBMITTED 16 TIMES 2026-09-05 (current address plus 15 prior addresses, one per submission -- the form takes a single address). EVERY SUBMISSION RETURNED HTTP 500 WHILE DISPLAYING 'Your information has successfully been removed.' Verified directly: status 500, body 2748 bytes, contains the success sentence, contains no PHP error text, and is TRUNCATED -- no closing html tag. So the script prints the success line and then dies before finishing the page. A browser renders that as a clean success page and shows no error at all; the first two submissions were made through the browser and looked perfect. Whether the removal was written before or after the point of failure cannot be determined from outside. Recorded FAILED rather than submitted because the server said the request failed, and not not_found because a record may well exist. The on-screen confirmation here is worth nothing: it is emitted before the thing that broke. Addresses submitted: the current one plus fifteen prior street addresses from the profile -- eleven in Pennsylvania, one in Maryland, one in Alabama, spanning seven towns. They are not listed here because this file is public. The two PO boxes were deliberately omitted: this is a residential street directory and a PO box would match whoever holds it now. NEXT: write to them about the 500, and re-check the directory by name/address in a few days -- that search is the only thing that can settle whether any of it took effect.

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
