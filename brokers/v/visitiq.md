# VisitIQ LLC

- **Email:** [named individual]@visitiq.io (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** visitiq.io
- **Priority: 2.**

## Status

- Current: `replied` (updated 2026-10-19)
- Reference: `outbox/staged/visitiq_ketch.txt`; case #01066705
- Note (2026-10-19): A REPLY ARRIVED, BUT IT DOES NOT SAY WHETHER A SEARCH
  ACTUALLY RAN. "I have added the requested info to be processed. If any
  matching profiles are found in our database they will be deleted." That
  is consistent with either the search having already run and found
  nothing, or the request merely being queued -- the two read identically
  from outside, which is exactly the ambiguity this project exists to
  close. Sent a short follow-up asking three things: (1) has the search
  against the 13 October identifier set already run or is it still
  pending; (2) if it ran, which identifiers matched, if any; (3) whether a
  forward-looking suppression is now applied against those identifiers.
  Framed "nothing matched" as a completely acceptable answer to pre-empt
  any reluctance to give a plain nil. Awaiting that reply.
- Prior note (2026-10-14): **THE NARROW QUESTION WORKED.** The 2026-10-11 probe to support@visitiq.io asked one factual question with no personal data in it — does the address on your California registration accept privacy requests? Two days later (2026-10-13): "At this time we only allow processing of opt-outs through the website for most cases, **however we can accommodate your request via email as an exception.** Please reply to this email with the information you'd like to opt-out of our ID graph and I will ensure it is processed." A route that did not exist now exists. **FULL IDENTIFIER SET SENT THE SAME DAY** (2026-10-13 23:47): twelve email addresses, eleven former phone numbers, sixteen former addresses, name and DOB. This is deliberately different from the usual rule of thumb — VisitIQ's whole business is an identity graph keyed on (usually hashed) email, so supplying the full set hands over search keys for a profile they almost certainly hold, not identifiers for a profile they don't (contrast the AutoWeb/Buyerlink nil, where the same move would be the wrong trade — see `brokers/a/autoweb.md`). **Mobile advertising IDs, device IDs, cookie IDs and IP addresses were explicitly withheld**, with the reasoning stated in the letter: supplying a current device/cookie ID to get removed creates a fresh, dated link to that device at the exact moment of the request. The letter also asked them to suppress any OTHER identifiers already linked to him in their graph (device/cookie IDs included) without needing to be told what they are — asking for suppression of a link costs nothing even when the identifier itself is never disclosed. Awaiting their substantive reply.
- Prior (2026-10-11, superseded): THE FILED ADDRESS WORKS, AND THE SEPTEMBER EMAIL REFUSAL WAS NOT THE COMPANY'S POSITION. Thirty-two minutes after the no-data probe to support@visitiq.io: 'Thank you for contacting VisitIQ Support. We have received your request and created CASE #01066705. A member of our team is reviewing the details and will follow up with you shortly.' So the registered contact accepts mail AND OPENS A CASE. Compare what this row recorded on 2026-09-03, from [named individual]@visitiq.io: 'we do not process data requests via email... Please do not reply to this email as it is not monitored.' BOTH MESSAGES COME FROM THE SAME NOTIFICATION ADDRESS -- the one that called itself unmonitored -- and they say opposite things. THE GENERALISABLE LESSON: an email refusal is evidence about the address that sent it, not about every address the company has. Check the REGISTERED contact separately before recording a company as email-refusing.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `[named individual]@visitiq.io`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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

- **Legal entity:** VisitIQ LLC
- **Registered address:** 729 North Washington Avenue #600, Minneapolis,
  NM, 55401
- **Filed contact email:** [named individual]@visitiq.io
- **Filed phone:** 5405536133
- **Website:** visitiq.io

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
