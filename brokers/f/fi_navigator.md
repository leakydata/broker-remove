# FI Navigator Corporation

- **Email:** privacy@fi-navigator.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** fi-navigator.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-08-31)
- Note: PROOF, not inference (SF 209). At 00:35:57 I sent a re-ask whose entire content was the question 'did a search actually run?'. It contained NO identifiers -- no emails, no addresses, no phone numbers, nothing to search against. Thirty seconds later, at 00:36:26 and 00:36:27, trustsuperset returned the identical template twice: 'We were unable to find any matching records given the information provided in your right to erasure request' and the same for opt-out. A no-match verdict on a message that supplied nothing to match. Combined with the 2026-08-31 00:05 RevOptimal result (two completions, including a right never exercised, 55s after a defect report), this reproduces across two independent tenants: the outcome is generated from RECEIPT OF MAIL, not from a query. Email does not reach a person at any trustsuperset tenant. Queued for a non-email route.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@fi-navigator.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**Their privacy mail runs through a third-party vendor, trustsuperset.com, and
the vendor appears unreliable.** Two "no matching records" replies arrived
2026-08-27 (erasure and opt-out-of-sale). A follow-up letter (2026-08-31) noted
that the SAME platform, acting for a different company that same week, sent an
internal end-to-end test fixture ("this is the 404-not-found email (e2e test)")
to a real inbox, followed by two unrequested "request completed" confirmations
sent 55 seconds after a message that contained no request at all. That's
evidence the pipeline can emit a "no matching records" outcome with no search
behind it. The follow-up asked three closing questions — did a search actually
run, which fields were searched (12 emails / 16 addresses / 11 phones were
supplied, most a search on current details alone would miss), were hashed forms
checked — and got back **the same templated "no matching records" text**,
unresponsive to any of it. Treat FI Navigator's nil result as *unconfirmed*
rather than closed; a human reply engaging with the specifics never arrived.
Worth flagging trustsuperset.com's reliability generically if it turns up as
the vendor behind other brokers' privacy mail.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** FI Navigator Corporation
- **Registered address:** 50 Glenlake Parkway NE, #395, Atlanta, Georgia,
  30328
- **Filed contact email:** privacy@fi-navigator.com
- **Filed phone:** (770) 837-9974
- **Website:** https://www.fi-navigator.com

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
