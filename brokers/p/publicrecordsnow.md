# PublicRecordsNow

- **Opt-out:** https://www.publicrecordsnow.com/optout/
- **Method:** web_form — Web form.
- **Domain:** publicrecordsnow.com
- **Priority: 3.**

## Status

- Current: `unreachable` (updated 2026-09-05)
- Note: NO ROUTE OF ANY KIND, verified 2026-09-05. The site advertises '120+ Billion Records', '6,000 data sources' and '30+ Years Experience'. It has: (1) no opt-out -- the recorded /optout/ path does not 404, it silently 302s to the homepage, so a checker that tests for HTTP 200 on the opt-out URL scores this site as compliant; (2) no privacy policy -- the footer 'Privacy Policy' link is href='#', and navigating to /privacy-policy directly returns '404 Page Not Found. Did you forget to add the page to the router?', a developer-facing message shipped to production; (3) no contact -- the footer 'Contact' link is also href='#'; (4) no email -- publicrecordsnow.com publishes NO MX record, so the domain cannot receive mail at all; (5) no published postal address anywhere on the site. Every 'Legal' and 'Company' footer link is a dead anchor to the top of the same page. There is nothing to write to and nothing to submit. Recording unreachable rather than failed: failed would imply a route was attempted and rejected.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.publicrecordsnow.com/optout/
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
