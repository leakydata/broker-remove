# Dobsearch Com

- **Opt-out:** https://www.dobsearch.com/people-finder/block-record-request.php
- **Method:** web_form — Web form.
- **Domain:** dobsearch.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-07)
- Reference: `dobsearch.com/contact -- 'does not hold any customer data nor do we have a database of people's data'`
- Note: RESOLVED 2026-09-07 ON THE SITE'S OWN PUBLISHED STATEMENT, using the SILENT_FAILURES 390 test -- read what the site says it is. Their contact page carries this, verbatim and unprompted: 'Note: As of January 2022, DOBSearch.com does not hold any customer data nor do we have a database of people's data. All data has been removed already.' Their privacy policy adds: 'Please be advised we DO NOT SELL YOUR PERSONAL INFORMATION to third parties and have never sold your personal information.' AND THE STRUCTURE CORROBORATES IT: every search box on the site -- name, phone, email, address, eight forms in all -- POSTs to https://htrk1.beenverified.com/aff_c carrying offer_id, aff_id and aff_sub. DOBSearch runs no searches. It hands the query to BeenVerified and takes a commission. That is the affiliate front-end pattern from 390, confirmed by the markup rather than inferred. THE UPSTREAM IS ALREADY WORKED: BeenVerified is covered by three rows plus freephonetracer -- beenverified (legal@ltvco.com), beenverified_llc (privacy@ltvco.com, ticket 28963990), and beenverified_inc (privacy@moneybot5000.com). So the data this site surfaces is already the subject of live requests at the company that actually holds it. THE RECORDED OPT-OUT URL WAS A REDIRECT-AWAY (SILENT_FAILURES 354): /people-finder/block-record-request.php returns HTTP 200 and lands on a blog article, 'How To Find Information On Someone Online (7 Ways)'. It resolves, it returns 200, and there is no form behind it -- which is why every automated check passed it. THE MAIL DEFERRALS ARE EXPLAINED RATHER THAN MYSTERIOUS: info@dobsearch.com has been deferring since 2026-09-05 with no bounce and no delivery -- MX is privateemail.com, a small host -- and a site that holds no data and runs on affiliate links has little reason to maintain a mailbox. NOT ESCALATING and not waiting for the deferral to resolve: there is no target for the request here. Directory-sourced row, not on a state register, so no registration duty is asserted.

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
