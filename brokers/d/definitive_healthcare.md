# Definitive Healthcare

- **Email:** populidrop@definitivehc.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** definitivehc.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-10-02)
- Note: 2026-08-25: emailed [named individual]@definitivehc.com. Healthcare commercial intelligence, split into two scopes. (1) Provider/prescriber/KOL data compiled ABOUT individuals rather than collected FROM them - NPI-linked records, affiliation history, referral-pattern metrics, influence and tier scores. (2) The careful one: much of this sector's raw material is claims data described as de-identified or as HIPAA Limited Data Sets. Rather than disputing that, asked the narrow answerable question - do you or any product you sell RE-LINK such data to identified individuals or identity-graph keys, by your own processing or a partner's? Pre-committed to accepting a plain no as complete. The reasoning given: 'it is de-identified' is a statement about a dataset rather than a guarantee about what is done with it downstream.
- Note: 2026-08-29: a second, shorter letter was also sent to the same address (apparently by a separate session, unaware of the 8/25 letter — worth checking for a duplicate-send before mailing this address again).
- Note: 2026-10-02: both the 8/25 and 8/29 emails got the identical auto-reply: they do not process privacy requests received by email at all, full stop, and route to two OneTrust-hosted web forms instead (see Gotchas). Downgraded from `submitted` to `manual_required` — the email was never actually accepted as a request, it was bounced to a form. Queued to `handoff.py` for a human to fill in and submit, since this project's channel is email-only.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `[named individual]@definitivehc.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

- **Email is refused outright, not deflected.** The reply doesn't dispute
  scope or ask a verification question — it states flatly that requests
  must go through their "designated methods": a general privacy-request
  form at `https://preferences.definitivehc.com/privacy`, a separate
  do-not-sell/opt-out form at `https://preferences.definitivehc.com/dont_sell`,
  or a phone line (1-866-679-6461). No alternate ungated email address is
  published anywhere in the reply or on `definitivehc.com/privacy-center/notices`.
  This is an email-only project's genuine dead end — it goes to `handoff.py`,
  not a resend.
- **Two separate letters, same outcome.** Both the detailed 8/25 letter
  (with the de-identification/re-linking questions above) and a shorter
  8/29 letter got byte-identical auto-replies, so the refusal isn't
  content-sensitive — it triggers on arriving by email at all.
- The legal entity is Swedish (Monocl AB, trading as Definitive Healthcare),
  filed with the CA registry under a Gothenburg address — don't be thrown by
  the EU-looking registered address when the product and the forms are
  plainly US-facing.

## Verification

No subject-search page. The only verification available is whichever
confirmation the OneTrust form itself issues after a human submits it —
watch for a ticket/request ID in the resulting email.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Monocl AB
- **Trading as:** Definitive Healthcare
- **Registered address:** Hvitfeldtsplatsen 7, 411 20 Gothenburg,
  Gothenburg, GB, 411 20
- **Filed contact email:** [named individual]@definitivehc.com
- **Filed phone:** 31 20 20 53
- **Website:** account.monocl.com; https://www.definitivehc.com

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
