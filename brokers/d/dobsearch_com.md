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

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.dobsearch.com/people-finder/block-record-request.php
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
