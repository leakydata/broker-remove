# PublicRecordsNow

- **Opt-out:** https://www.publicrecordsnow.com/optout/
- **Method:** web_form — Web form.
- **Domain:** publicrecordsnow.com
- **Priority: 3.**

## Status

- Current: `unreachable` (updated 2026-09-05)
- Note: NO ROUTE OF ANY KIND, verified 2026-09-05. The site advertises '120+ Billion Records', '6,000 data sources' and '30+ Years Experience'. It has: (1) no opt-out -- the recorded /optout/ path does not 404, it silently 302s to the homepage, so a checker that tests for HTTP 200 on the opt-out URL scores this site as compliant; (2) no privacy policy -- the footer 'Privacy Policy' link is href='#', and navigating to /privacy-policy directly returns '404 Page Not Found. Did you forget to add the page to the router?', a developer-facing message shipped to production; (3) no contact -- the footer 'Contact' link is also href='#'; (4) no email -- publicrecordsnow.com publishes NO MX record, so the domain cannot receive mail at all; (5) no published postal address anywhere on the site. Every 'Legal' and 'Company' footer link is a dead anchor to the top of the same page. There is nothing to write to and nothing to submit. Recording unreachable rather than failed: failed would imply a route was attempted and rejected.

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
