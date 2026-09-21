# Nativo, Inc.

- **Email:** privacy@nativo.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** nativo.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-21)
- Note: Emailed privacy@nativo.com 2026-08-29 (CA registry 2020-2025). Native advertising platform. Standard ad-tech concession up front (cookie/MAID/page-context keyed, so a name search returns nothing and that is a real answer), then three asks, one of which is specific to this format. (1) Identity layer: hashed emails, alternative IDs (UID2, RampID, ID5), or any device-to-person graph -- and if so, hash the twelve addresses themselves and search. (2) THE ONE THAT IS PARTICULAR TO NATIVE ADVERTISING: native measures what an individual READ and for how long, so an article-level engagement history is a materially more revealing record than an impression count -- it can indicate a health concern, a financial difficulty, a legal problem or a belief purely from which articles were opened and how long they held attention. Asked whether reading and engagement events are retained at individual or device level after a campaign ends, for how long, and whether they feed interest or intent segments; deletion asked for, and use-and-disclosure restriction asked separately. (3) Where the opt-out lives (cookie vs server-side) and whether GPC is recorded durably or honoured only in-session. Plus supplier and recipient categories. No IP and no device ID sent, reasons stated.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@nativo.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

## Nativo is a Life360 brand — reply came from privacy-nativo@life360.com

**Reply (2026-09-09):** "We are confirming that we did not locate your information in our system" — a clean nil on the identity-keyed search, sent from `privacy-nativo@life360.com`. Life360 (the family-safety/location app company) evidently now owns or operates the Nativo ad platform under its own privacy program; this is worth cross-referencing against any direct Life360 entry, since a shared privacy team can mean a shared underlying data store even when the products look unrelated.

**The pseudonymous-data offer is browser-only and was not completed.** The same reply says Nativo/Life360 "may have additional 'pseudonymous' personal information about you, such as a Cookie ID, IP address, and associated reference data," and offers two routes to reach it:

1. Visit `https://ads.life360.com/legal/interest-based-ads` and click an "Opt Out" button — a client-side action that sets a cookie in the visiting browser. Not something a non-browser channel can do or verify.
2. Alternatively, retrieve the "Visitor ID" cookie stored under the `postrelease.com` domain from your own browser and email it back for a manual match-and-delete.

Both routes require a browser [FIRST] controls; neither is completable by email alone. **Do not send a cookie/Visitor ID here without deciding it's worth it** — handing over the exact identifier that links a browser to this profile is the same trade-off the letter to Nativo's own ad-tech peers argues against (see the identity-layer question in the original letter). Flagged as a browser-only follow-up for a human, not attempted.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Nativo, Inc.
- **Registered address:** 222 Pacific Coast Highway, Floor 10, El
  Segundo, CA
- **Filed contact email:** privacy@nativo.com
- **Website:** https://www.nativo.com

*Source: `data/registries/registry2024.csv`.*

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
