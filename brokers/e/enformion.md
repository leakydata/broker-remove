# Enformion

- **Opt-out:** https://www.enformion.com/privacy-policy/
- **Email:** compliance@enformion.com (verified)
- **Method:** web_form — Web form.
- **Domain:** enformion.com
- **Priority: 5.**

## Status

- Current: `captcha_blocked` (updated 2026-10-09)
- Note: CORRECTION TO THIS MORNING'S NOTE, AND A BROKEN LOOP IN THEIR FLOW. I recorded the Right to Delete form as 'staged, blocked only by a reCAPTCHA' and did not click Submit. It nevertheless went through: support@enformion.com emailed 'Enformion - Complete Your Request' at 17:44 carrying TICKET 15417940. So the request exists and my note was wrong about it being unsubmitted -- recorded here rather than quietly amended. THE EMAILED LINK DOES NOT DO WHAT IT SAYS. It promises 'the final steps... Click here to complete your request' and a form where 'you will receive a confirmation email'. Following it lands on enformion.com/opt-out with the token and ticketid in the query string -- but the page renders the ORIGINAL request-a-link step again, First/Last/Email plus a visible 'I am not a robot' reCAPTCHA, not the token-filled delete form it promises. Re-selecting Right to Delete and Member of the public does not change that. So the flow returns the consumer to the beginning, and a second submission would presumably mail a second link to the same dead end. The 24-hour link expiry quoted in the mail makes that worse, not better. STATE: form re-staged with name, email and the authorisation box; the reCAPTCHA checkbox is the only blocker and it is a real one this time. Needs one human solve, and someone should watch whether submitting from the tokenised URL behaves differently from the bare portal.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.enformion.com/privacy-policy/
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `compliance@enformion.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

- **Legal entity:** Enformion, LLC
- **Trading as:** Tracers; Enformion; Endato
- **Registered address:** 1915 21st St, Sacramento, CA
- **Filed contact email:** [named individual]@enformion.com
- **Website:** https://www.enformion.com

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
