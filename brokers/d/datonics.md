# Datonics LLC

- **Email:** accounting@datonics.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** datonics.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-28)
- Note: ANSWERED 2026-08-28 by a human at privacy@datonics.com, two days after the letter reached them via Accounting. 'We have used all of the email addresses you provided to opt-out and delete it from our services.'

That is a claim about THIS request rather than a fact about the company, so it corroborates under 138 as corrected. But it is UNENUMERATED -- they did not list which addresses -- so 139's caveat applies: a confirmation that does not name its inputs may be reporting on a subset that cannot be seen from outside. Recorded confirmed on the strength of the past-tense completion claim, with that caveat explicit.

THE MOST USEFUL SENTENCE IS THE ONE ABOUT MY OWN METHOD: 'We do not process telephone numbers, physical addresses or dates of birth in our services, so we never had that information until you chose to send it to us.' Second company to say this after Fog Data Science. Acted on rather than noted -- see _SILENT_FAILURES 144 and the change to make_optout_email.py.

Cookie and MAID opt-out routed to their privacy-choices page. Replied explaining why that page cannot do what they hope -- a browser opt-out dies with cleared storage or a replaced device, and a MAID cannot be supplied by the person it identifies -- and asked the one question they can answer from their own side: DOES THE EMAIL-KEYED OPT-OUT PROPAGATE to cookie/MAID/CTV identifiers already linked to those hashed addresses in their graph, or are the two mechanisms independent so the device side survives the email side.

STILL OPEN, re-asked: (1) the SUPPRESSION HASH question -- if they retain a hash to keep him excluded that is fine, but which of two lists does it sit on, exclusion or match, since the same string does opposite work depending on the answer; (2) upstream suppliers, categories rather than names.

NOT ACKNOWLEDGED: the registry-filing correction. [named individual]@datonics.com has been the filed CPPA contact for 2024, 2025 and 2026 while privacy@ is the working desk, so every consumer who looks up the registered contact lands in Accounting. They did not respond to that. Worth re-raising once if nothing else comes back.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `[named individual]@datonics.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

- **Legal entity:** Datonics LLC
- **Registered address:** 250 broadway 24 fl, ny, NY, 10007
- **Filed contact email:** [named individual]@datonics.com
- **Filed phone:** 6468670647
- **Website:** https://www.datonics.com

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
