# BDEX, LLC

- **Email:** privacy@bdex.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** bdex.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-17)
- Note: 2026-09-17 CLOSED THE OUTSTANDING QUESTIONS. "When we remove/opt-out a consumer, we remove and opt out ALL of the data we have about them including other devices (MAIDs, CTV, etc...) When we license our graph we license it as a complete refresh so that we do not need to send any signals to our customers about your opt-out, instead you are deleted and then when our clients get the refresh your data is no longer there." This answers both items left open on 8/25: deletion DOES reach linked device/identifier edges (not just the matched email rows), and propagation to exchange partners happens automatically via the refresh-licensing model rather than needing an explicit per-partner signal -- a genuinely better architecture than most identity graphs, which either don't propagate at all or rely on partners to honour a signal they may ignore. The one thing still unanswered across both replies: whether hashed-email forms are covered by the same removal (asked twice, never addressed) -- worth a fresh, single-question follow-up if this row is revisited.
- Note: 2026-08-25: ITEMISED. 4 of 12 emails matched - [EMAIL], [EMAIL], [EMAIL], [EMAIL] - each removed with associated data, and ALL TWELVE opted out from future use in the platform, i.e. standing suppression applied to addresses they did not hold. NOTABLE: all four matches are long-dead addresses (gateway.net and iwon.com are defunct ISPs); zero current addresses matched. Hashed-forms, edges and exchange-propagation questions still outstanding.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@bdex.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

BDEX has no consumer-facing lookup page (it is a backend identity graph/
exchange, not a directory), so there is no URL to re-check. Confirmation
rests on the company's own written replies: the 8/25 itemised match list and
the 9/17 statement that removal covers linked devices/identifiers and
propagates via the refresh-licensing model. If this needs re-verifying,
re-send the same 12 email addresses and ask whether any now match again.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** BDEX, LLC
- **Registered address:** 18117 Biscayne Suite #2575, Miami, FL, 33160
- **Filed contact email:** privacy@bdex.com
- **Filed phone:** 917 410-6616
- **Website:** www.bdex.com

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
