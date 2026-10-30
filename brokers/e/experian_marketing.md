# Experian Marketing

- **Opt-out:** https://www.experian.com/privacy/
- **Email:** ca_drop_fsd@experian.com (verified)
- **Method:** web_form — Web form.
- **Domain:** experian.com
- **Priority: 4.**

## Status

- Current: `manual_required` (updated 2026-10-30) — now the single highest-
  priority handoff item in this project; see the case-flood note below.
- Note: 2026-08-24: the 21 Aug letter to [named individual]@experian.com has had no reply in 3 days, and the sibling ca_drop_audigent@ auto-replies that it is unmonitored - so that request was almost certainly never read. Resent via optout@experian.com with a fault report on both registered addresses.
- 2026-10-26 and 2026-10-27: CCPA@experian.com sent two separate "Your
  Experian Consumer Privacy Report is complete" notices, for two different
  case numbers (964193712 and 656487694) -- evidently two requests were
  processed (the second addressed to a name variant supplied in some
  letters, so likely a distinct submission rather than a duplicate
  send of the same case). Both require clicking a link to
  consumerprivacy.experian.com and answering security questions again
  before the report can be viewed or downloaded -- a browser step this
  project cannot complete by email. **Flagged for handoff**: a human needs
  to open both links, re-verify identity, and read what the reports say
  before this can be marked `confirmed` or `not_found` with evidence. Do
  not assume either outcome from the notice text alone -- "report is
  complete" says nothing about what it contains.
- 2026-10-28: A THIRD "report is complete" notice arrived, case number
  938509602 -- again from CCPA@experian.com, again gated behind
  https://consumerprivacy.experian.com/security-questions/938509602 and a
  fresh identity re-verification. Same handoff as the other two: added to
  the queue rather than guessed at. Three separate case numbers in three
  days suggests Experian is processing each letter sent to it as its own
  case rather than consolidating by requester -- worth asking, once a human
  is in the portal, whether the three can be merged so future replies don't
  keep fragmenting.
- 2026-10-28/10-30 (escalated): **The fragmentation above was not three
  cases -- it kept going.** Across 2026-10-28 18:57 through 2026-10-30
  05:49, roughly 140 more distinct "Your Experian Consumer Privacy Report
  is complete" notices arrived, each with its own unique case number, each
  gated behind its own `consumerprivacy.experian.com/security-questions/<case>`
  re-verification link. Only **four** emails were ever sent to an
  `@experian.com` address by this project. A ratio of ~140 generated cases
  to 4 letters sent is not consolidation-by-letter (the 10-27/10-28 theory)
  -- something in Experian's CCPA case-management pipeline is generating
  new cases at a rate completely disconnected from actual incoming
  requests, and the rate is still climbing as of the last check (new
  notices arriving hours apart, still arriving at time of writing). **Do
  not open and re-verify each one by hand; that does not scale and may not
  even be the right response.** This looks more like a backend fault
  (duplicate case creation, a retry loop, or cases spun up from some
  unrelated bulk process that happens to be keyed to this requester's name)
  than a sign that ~140 separate searches were run. Flagging as the
  priority handoff item: a human should (a) open 2-3 of the case links to
  confirm what they actually contain (same report? empty? an error?) before
  assuming any pattern, and (b) consider emailing CCPA@experian.com asking
  directly why dozens of cases are being opened per letter, since that
  question is more useful than manually triaging each one. Do not mark any
  of these `confirmed` or `not_found` without that check -- "report is
  complete" says nothing about content, and at this volume guessing is a
  real risk of misrecording the outcome.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.experian.com/privacy/
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `optout@experian.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Experian Information Solutions, Inc
- **Registered address:** 475 Anton Blvd, Costa Mesa, CA, 92626-7037
- **Filed contact email:** [named individual]@experian.com
- **Filed phone:** 714-830-7000
- **Website:** https://www.experian.com

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
