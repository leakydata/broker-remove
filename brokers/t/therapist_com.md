# Therapist Com Llc

- **Opt-out:** https://therapist.com/privacy-notice/
- **Email:** info@therapist.com (verified)
- **Method:** unknown — Route not yet established.
- **Priority: 1.**

## Status

- Current: `replied` (updated 2026-09-22)
- Reference: `gmail:1a0bb20784b3eba2`
- Note: 9/21, two identical auto-replies from
  support@therapistdirectory.zendesk.com (subject prefixed `[PESI]` — the
  parent company/CE-training platform behind Therapist.com). Both reframed
  the request as **closing a customer account**: offered account deletion
  (with a warning about losing purchase/attendance/certificate history),
  removal from the promotional mailing list, or merging duplicate accounts —
  none of which is a CCPA-style data deletion, and none acknowledged a
  privacy-statute basis at all. This is the "delete your account" deflection,
  distinct from the identity-verification and no-email-route deflections in
  `_DEFLECTIONS.md` but the same shape: answer a narrower, easier request than
  the one that was made. Replied 9/22 clarifying there is no account to close,
  this is a statutory/policy privacy request independent of any account, and
  asking them to process it as such. The underlying mailbox lands on Zendesk
  (ticket ref `2Z2G9D-33GKR`), so expect a support-desk turnaround rather than
  a dedicated privacy team.
- Older note (9/19), for the letter that produced this reply: first contact. Standard consumer deletion/opt-out/suppression letter. Address sourced from an Optery-directory import; `email_verified_by` had been set to `"optery_directory"`, which only means a commercial directory listed the company, not that the mailbox was ever confirmed to accept mail -- three addresses from the same 2026-09-18 batch hard-bounced (see ct_company_directory.md, ibegin.md, native_american_netroots.md). Watch for a bounce on the next pass before treating this as delivered.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://therapist.com/privacy-notice/
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `info@therapist.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**A privacy deletion request lands on a customer-support Zendesk queue and
gets answered as an account-support ticket.** The auto-reply offers account
deletion, promo-list removal, or account merge — three different, narrower
asks than a CCPA-style deletion/opt-out/suppression request, and it never
mentions a privacy statute or policy. If you don't have an account, say so
explicitly and re-state the request as one that doesn't depend on account
status — otherwise the ticket may get closed as "no account found," which
would wrongly read as a completed removal.

**Therapist.com is a PESI brand** (the reply is Zendesk-branded
`therapistdirectory.zendesk.com` and subject-prefixed `[PESI]`) — PESI is a
continuing-education platform for therapists. If Therapist.com comes back
empty, consider whether PESI itself (course purchase/attendance records)
holds a separate record worth its own request.

## Verification

Watch for a substantive answer to the 9/22 clarification. If they again treat
it as an account question, escalate by naming the statutory basis explicitly
(state consumer privacy law or, failing that, their own published privacy
policy at the URL above) rather than repeating the account framing.

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
