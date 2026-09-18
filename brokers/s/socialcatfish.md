# Socialcatfish

- **Method:** unknown — Route not yet established.
- **Domain:** socialcatfish.com
- **Priority: 1.**

## Status

- Current: `manual_required` (updated 2026-09-06)
- Note: ROUTE FOUND AND FULLY MAPPED; NEEDS A BROWSER TO SUBMIT. socialcatfish.com/opt-out/?id=request_optout was discovered 2026-09-05. CORRECTION TO A FIRST READ: an earlier glance at the page's fields showed an email-and-password pair and I took the opt-out to be behind a login. It is not -- that is a site-wide login modal, and the opt-out is a separate form, id=request_optout_form, posting to /opt-out/?id=request_optout#step2. No account is required. FIELDS: firstname, lastname, email, and ccpa_url[] ('Enter profile URL here'), with an optional expandable section for ccpa_middle_name, ccpa_age as a RANGE (the subject falls in 45-53), ccpa_emails[] and ccpa_phones[], each repeatable, plus an image upload. Not submitted from a script: the submit control and csrf_token are injected by JavaScript and are not in the served markup, so a blind POST would be exactly the unverifiable submission today's failures warn about. Two browser attempts ended with the extension refusing script injection on this 245KB page. THEIR POLICY IS BETTER THAN MOST AND DESERVES SAYING SO: 'If you are a California, Colorado, Connecticut, Florida, Nevada, Oregon, Texas, Utah, or Virginia resident you may have specific rights related to privacy requests. However, Social Catfish is committed to extending the highest level of privacy rights offered under U.S. law to all U.S. residents. As such, we accept and honor requests from residents of all U.S. states.' That is the exact opposite of the state-gating seen at Whitepages and noon.ai -- they name the states with statutes and then explicitly decline to use that list to narrow who they will help. They also commit to a fifteen-day deadline. Pennsylvania residency is therefore not an obstacle here.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `[named individual]@socialcatfish.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Social Catfish, LLC
- **Registered address:** 38770 sky canyon dr, ste a, MURRIETA, CA, 92563
- **Filed contact email:** [named individual]@socialcatfish.com
- **Filed phone:** 8444228347
- **Website:** https://socialcatfish.com

*Source: `data/registries/registry.csv`.*

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
