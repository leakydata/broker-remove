# Rhode Island Arrests

- **Opt-out:** https://infotracer.com/optout/
- **Email:** privacy@infotracer.com (verified)
- **Method:** web_form — Web form.
- **Domain:** riarrests.org
- **Priority: 2.**

## Status

- Current: `covered_by_sibling` (updated 2026-09-07)
- Reference: `infotracer ticket 544087 -- zero records, suppression on each ingestion`
- Note: RESOLVED 2026-09-06 AS AN AFFILIATE FRONT-END, NOT A BROKER. This row is one of 53 that share a single recorded route, infotracer.com/optout/. Investigated properly tonight rather than left as a shared URL. WHAT THESE SITES ARE, from their own footer, verbatim: 'The owners of this site do not own the records found on this site or any public records database. All records presented on this site are gathered from third party databases that are not controlled by the owners of this site... The website owners receive compensation if you complete a registration through our website.' So the site is a search box and a commission. It holds no records; the records are InfoPay's. THE UPSTREAM IS ALREADY CLOSED. InfoPay (ticket 544087) confirmed zero records under the subject's identifiers, named the identifiers and record categories searched, and applied SUPPRESSION RE-APPLIED ON EACH SUBSEQUENT INGESTION -- the durable form. Their stated reason for scope was checkable rather than an assurance: 'a record cannot appear on a redirect or sibling brand without first existing on InfoPay.' These sites are downstream of exactly that. WHAT THE SWEEP OF ALL 53 DOMAINS FOUND: 22 publish their own /privacy-request-portal, a WPForms form with a CAPTCHA; 27 return 404 on that path; 3 return a page with no form. The family is NOT uniform, and the single route recorded against all 53 was an inference, not an observation. TWO THINGS THAT MATTER MORE THAN THE COUNT. First, the portals that exist are about USER ACCOUNT DATA -- their own text lists 'your email address, search history, payment records, and other data from using the site' -- NOT about the published arrest records. For someone who never used the site, that portal is the wrong instrument: it governs the visitor, not the subject. Second, the subject's OWN STATE SITE, pennsylvaniaarrests.org, is one of the 27 with no portal at all. The site publishing Pennsylvania arrest records offers a Pennsylvanian nothing but a privacy policy. See SILENT_FAILURES 390. Not writing to these individually: there is nobody at the other end holding a record, and the one entity that was has already answered completely.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://infotracer.com/optout/
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@infotracer.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
