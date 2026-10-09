# Client Command

- **Email:** privacy@ClientCommand.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** clientcommand.com
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-10-09)
- Note: STAGED 2026-10-09 on the OneTrust DSAR form, blocked only by an 'I am not a robot' reCAPTCHA. Client Command refuses email outright ('email is not a mechanism used by Client Command for privacy rights requests'), so this form is the only route. FILLED: relationship 'Other' (he is not a customer, applicant, employee or vendor -- Other is the only honest option and, as at EAB, the one that fits the people a data-broker registration actually concerns), [EMAIL] in both email fields, [PERSONAL], [PERSONAL], [PERSONAL], Pennsylvania, [PERSONAL], [PHONE]. TWO LIMITS WORTH RECORDING. (1) NO REQUEST-TYPE SELECTOR AND NO FREE-TEXT BOX AT ALL. The form collects identity and nothing else -- there is no way to say whether this is a deletion, an opt-out, an access request or a correction, and no way to ask for a forward-looking suppression or for the 1798.105(c) direction to recipients. Whatever Client Command infers from a bare identity submission is what the request becomes. Same structural shape as Adstra; third form in this project that cannot carry the ask. (2) ONE ADDRESS, ONE EMAIL, ONE PHONE, and the address field says in capitals 'DO NOT ENTER CITY, ST. OR ZIP, HERE' -- so the eleven other emails, eleven prior numbers and fifteen prior addresses cannot be supplied at all. For a company whose business is automotive-marketing audience data keyed to households, that is a material gap. THE ACKNOWLEDGEMENT IS UNUSUALLY CLEAR and worth quoting back if they later equivocate: 'A request to delete my personal information/data is irreversible'. Their postal fallback, if the form proves unusable, is Summit Resources, LLC d/b/a Client Command, Attn: Privacy Inquiry, 13560 Morris Rd, Suite 4250, Alpharetta, GA 30004.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `legal@clientcommand.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

> **Correction (2026-08-25):** A duplicate-detection error in that day's run sent an unnecessary second request to `legal@clientcommand.com`, on top of the already-open thread documented above. The exclusion check matched only exact addresses seen in a partial Sent-folder scan, and this broker's registry `email_to` had drifted from the address actually used historically — so it looked unsent when it wasn't. No new information was requested; treat the status above as authoritative. **Lesson: check this playbook's own `Current:` status before treating a registry email_to as evidence a broker is unsent — it is not reliable on its own.**

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Summit Resources, LLC
- **Trading as:** Client Command
- **Registered address:** 13560 Morris Rd, Suite 4250, Alpharetta, GA,
  30004
- **Filed contact email:** legal@clientcommand.com
- **Filed phone:** 7707770122
- **Website:** clientcommand.com

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
