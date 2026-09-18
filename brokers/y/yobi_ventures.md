# Yobi Ventures, LLC

- **Email:** privacy@yobi.ai (per current CPPA registry filing)
- **Email fallback (dead):** admin@yobi.ventures — hard-bounced 2026-09-02
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** yobi.ai (yobi.ventures redirects to www.yobi.ai/ventures)
- **Priority: 2.**

## Status

- Current: `covered_by_sibling`
- Note: BOUNCED, PREMISE WRONG, AND THE ROW IS A PREDECESSOR. admin@yobi.ventures no longer exists. The letter had argued from 'filings run 2020-2023 and then stop' -- THAT WAS WRONG. Checking the other registry files shows YOBI VENTURES, INC. filed for 2025 and 2026 at YOBI.AI with a live privacy@yobi.ai and a published opt-out URL. Same operation, one legal form later, and there is already a separate curated row -- yobi_ai -- which is SUBMITTED. So the company is covered and this row is its predecessor, not a gap. NEITHER SF 251 CHECK WOULD HAVE PAIRED THEM: different legal form, different domain, different contact, no shared free text, non-overlapping metrics years. THE STREET ADDRESS PAIRS THEM INSTANTLY -- both filings give the same New York suite number. That produced SF 258 and a new detector in register_profile.py: clustering by normalised street+postcode gives 93 CLUSTERS COVERING 209 ROWS, against 29 and 66 for prose-and-metrics. Marked covered_by_sibling rather than unreachable, since the live entity has an open request.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@yobi.ai`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

- **Legal entity:** Yobi Ventures, LLC
- **Registered address:** 136 e 76th st, 4B, NYC, NY 10021, United States
- **Filed contact email:** admin@yobi.ventures
- **Website:** http://yobi.ventures

*Source: `data/registries/complete-reg-data-brokers.csv`.*

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
