# Affinity

- **Email:** privacy@affinity.co (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** affinity.co
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-24)
- Note: 2026-08-24: first contact via the address nominated in the California data broker registration. Tailored per _CATEGORY_VARIANTS.md.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@affinity.co`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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


## Ingested from somebody else's mailbox, which changes the question

Affinity builds relationship intelligence by ingesting customers' email and
calendar histories. A person can therefore be in the product having never heard
of it — the route in is a third party's correspondence.

So the letter opens with a controller/processor scoping question and asks them to
answer it **explicitly** rather than by implication:

1. Data held for Affinity's own account, in a shared or enriched dataset — a
   consumer deletion right reaches it.
2. Data processed for a customer whose mailbox contains the subject — then
   **name the customers**, because "we are only a processor" without naming the
   controller leaves a right with nobody to exercise it against, which in
   practice is no right at all.

Three asks specific to a correspondence-derived graph:

- **What was captured** — signature-block phone numbers, message metadata,
  meeting attendance, inferred relationship-strength scores.
- **Graph edges.** An edge recording that the subject corresponded with someone
  is information about them, is indexed separately, and survives deletion of the
  contact row.
- **Re-enrichment**, and whether suppression is standing or point-in-time.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Project Affinity, Inc.
- **Trading as:** Affinity
- **Registered address:** 182 Howard St, PMB#3, San Francisco,
  California, 94105
- **Filed contact email:** privacy@affinity.co
- **Filed phone:** 6282633645
- **Website:** affinity.co

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
