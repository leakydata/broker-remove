# Graze Social PBC

- **Email:** legal@graze.social (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** graze.social
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-03)
- Note: THE BEST HANDLING OF A REQUEST IN THE PROJECT, and it contains something no other company has done (SILENT_FAILURES 289). Follow-up answered 2026-09-02. (1) A POSITIVE CONTROL, UNPROMPTED: 'a query that is silently broken returns zero for everything, which looks identical to a true negative. So we ran the same query with a control -- an address we know is present in the account table. The control returned one row; your twelve returned none. That is the difference between we found nothing and our lookup was not working.' THAT IS THE 138 PROBLEM SOLVED FROM THE INSIDE. Every nil result is unfalsifiable from outside -- a careful search and a silently broken query produce the identical sentence -- and I had concluded it was unsolvable from my side, because it is. It is trivially solvable from theirs, at the cost of one extra query, and they are the first of over a thousand to do it. (2) THEY ADMITTED AN INTAKE DEFECT THEY DID NOT HAVE TO: 'our intake had taken the first address from your letter rather than all of them... HAD YOU NOT PRESSED, ELEVEN OF YOUR ADDRESSES WOULD HAVE GONE UNSEARCHED. The fault was ours.' They could have re-run quietly and reported the same nil; it would have read identically. And the fix is systemic rather than personal -- a request listing multiple identifiers now has each searched and logged separately, which changes it for everyone who writes afterwards. (3) TWELVE SEARCHES, EACH ITS OWN DATED LOG ENTRY, both the account and billing/subscription tables, all twelve addresses including [EMAIL]: no match in either store. Opt-out of sale/sharing recorded against all twelve; they state they do not sell personal information and do not run targeted advertising. NEW TOOL FROM THIS: ask every company returning a nil whether they ran a POSITIVE CONTROL. It is cheap for them and it is the only thing that converts an unfalsifiable nil into a demonstrated one. STILL OPEN, AND IT IS OURS NOT THEIRS: the Bluesky handle. They confirmed a handle can be appended to the existing logged request later, the original receipt date stands, and 'there is no account' is a perfectly good close.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `legal@graze.social`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

- **Legal entity:** Graze Social PBC
- **Registered address:** 2562 NE 48th Ave, Portland, OR, 97213
- **Filed contact email:** [named individual]@graze.social
- **Filed phone:** (503) 319-2931
- **Website:** www.graze.social

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
