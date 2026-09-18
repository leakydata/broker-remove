# Cadent

- **Email:** privacy@cadent.tv (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** cadent.tv
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-09-03)
- Reference: `tracking code on file`
- Note: THE LOOP IS NOW DEMONSTRATED RATHER THAN INFERRED (SILENT_FAILURES 290). Sequence: 17 Aug portal request dies at a 24-hour verification window -> 2 Sep re-filed by email -> autoresponder points at the same verify-email form -> 3 Sep letter explaining the loop and asking only for the no-verification 1798.120 opt-out -> THE IDENTICAL AUTORESPONSE AGAIN, pointing at the same form. Four steps, two of them mine, and the machine returned the same sentence to a letter that was entirely about that sentence. Nothing here suggests bad faith: an autoresponder cannot distinguish an argument from a request, which is exactly why a company whose only route is a form needs one human-monitored address for correspondence ABOUT the process. Form queued for handoff with the operative instruction -- do not start unless you can click the confirmation within the hour.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@cadent.tv`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

## Email is refused, politely, with a working route

`privacy@cadent.tv` is answered from `privacy@cadent.com`:

> *"We have received your email. To submit a data rights request, please complete
> the form which can be found here: https://privacy.cadent.tv/privacy/#/verify-email"*

## Delete is gated behind a device ID; opt-out is not

The most useful sentence on the form, and the reason to read it before choosing:

> *"For **access and deletion** requests, you must provide both your household
> address **and one or more device IDs** that belong to you... For **opt-out
> requests**, you need only to provide your household address, after which we will
> opt-out that household accordingly."*

Almost nobody can produce the advertising or device identifier for their own TV or
phone. So the deletion route is effectively closed to an ordinary consumer, while
the **opt-out of sale/share (including targeted advertising and sensitive PI) is
available on address alone** and covers the whole household.

Someone who picks "Delete", hits the device-ID field, and gives up has walked past
the one request they could actually complete. Pick the opt-out; note in your
tracker that deletion remains unexercised and why.

## Route

1. `/privacy/#/verify-email` → "Are you a US based user?" → **Yes**
2. Enter email → **Send Email Verification Link**
3. Click the link in the mail from `support@cadent.app` (**valid 24 hours**) —
   this opens the actual request form, pre-filled with the verified address
4. Household address, city, state, ZIP
5. Tick **Opt-Out of "Sale"/"Share" of Personal Information**
6. Tick both certifications — they are "under penalty of perjury" and assert only
   that the details are your own, truthful and accurate, and that the request is
   not fraudulent. Read them; they are reasonable, but they are sworn statements.
7. **reCAPTCHA + Submit** — a human is needed for this step only.

Stated turnaround: *"we aim to resolve your request within forty-five (45) days."*

## Notes

- The verification step is genuinely automatable: the link arrives by email and
  opens the form. Only the final CAPTCHA needs a person.
- The form does not scroll conventionally — it renders inside a container. Address
  fields by element reference rather than trying to scroll to them.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Cadent LLC
- **Registered address:** 1675 Broadway 22nd Floor, New York, NY, 10019
- **Filed contact email:** privacy@Cadent.tv
- **Filed phone:** 2127961960
- **Website:** www.cadent.tv

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
