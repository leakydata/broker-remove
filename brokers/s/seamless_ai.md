# Seamless Ai

- **Opt-out:** https://login.seamless.ai/personalDataRequest
- **Email:** privacy@seamlessleads.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** seamlessleads.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-17)
- Note: 2026-09-17 SUBSTANTIVE CLOSE. Reply to the 2026-08-20 letter (sent separately by email, not just the web form) itemised the full assembled profile before erasure -- every prior job title/employer going back to a paper route, a dozen phone numbers, and ~40 email addresses including many the subject never supplied (aliases of the pattern `[first]-[last]@[employer-domain]` and `[initial][last]@[employer-domain]` at multiple past employers -- addresses INFERRED from name+employer patterns he never gave them, i.e. Seamless assembled these itself rather than merely storing what was submitted). States personal data is erased; retains only name+email "for recordkeeping...and to support your suppression request." Named upstream sources only by category (third parties, service providers, public sources, CRM/professional-network/social platforms), declined to itemise recipients citing "impossible or disproportionate effort" -- a real limit, not obviously a dodge, for a subscription re-sale business with an unbounded customer count. Letter explicitly states it "serves as a record of completion of your opt-out and suppression requests."
- Note: REVERTED 2026-09-02, SAME DAY (SILENT_FAILURES 287). I moved this row to email_pending an hour earlier on the strength of an unconfirmed-looking verification email sitting in the inbox. THE ROW'S OWN HISTORY ALREADY SAID THE VERIFICATION WAS COMPLETED -- variously 'email verification clicked', 'Your request is confirmed!', 'successfully verified', or a later substantive reply that could only have followed confirmation. A verification mail stays in the inbox forever because nobody archives it; ITS PRESENCE IS NOT EVIDENCE THAT IT WAS NEVER USED. Nine of the ten rows I downgraded were already verified. Restored to submitted, which is what the evidence supports.

## Steps

1. Email `privacy@seamlessleads.com` first. It will not process the request, but the
   autoresponder is worth having: it names the portal **and** offers an explicit
   email fallback (see Gotchas).
2. Go to `preferences.seamless.ai` — a **DataGrail** Privacy Request Center.
3. Pick country **United States**, then state. The state picker defaults to
   *Virginia*; change it. Pennsylvania is accepted and does not reduce the options.
4. Choose **Start Delete My Information/Opt-Out of the Sale or Sharing** — the
   broadest card.
5. Fill first name, last name, email, phone. A phone number is required: *"please
   include a phone number or a direct line (general corporate phone numbers not
   applicable)."*
6. **Relationship**: Business Contact / Customer / Employee / Former Employee / Job
   Applicant / **Other**. Pick Other if none is true.
7. **Request type**: Deletion request, or Opt-out. Deletion is broader.
8. Put everything the form has no field for into **Additional comments** — the
   other identifiers, suppression, and the provenance and recipient questions.
9. Review Request → tick the **hCaptcha** → Submit Request.

## Gotchas

- **The state picker silently defaults to Virginia.** Change it before anything
  else; the choice is carried in the URL as `locationCode=US-PA` and shapes what
  the form will accept.
- **Pennsylvania is accepted here**, and all five request types remain available —
  worth noting, because PA is the usual trigger for a jurisdiction refusal.
- **Do not misstate the relationship to satisfy the dropdown.** "Other" is honest
  for a compiled record; "Business Contact" or "Customer" implies a relationship
  that does not exist.
- **hCaptcha at submit** — but this form behaves well: it renders an explicit
  *"Complete the Captcha"* error rather than failing silently. Contrast
  [[_SILENT_FAILURES]] §59.
- **There is a documented email fallback**, which is rare and worth keeping:
  *"If you are unable to complete the Privacy Request Center, kindly respond to
  this email with the following information so that we may process your request"* —
  full name, country and state, city, email, phone.

## Verification

No public lookup — this is a B2B contact database, so nothing to search yourself in.

They state their own clock: *"generally 45 days under the California Consumer
Privacy Act or 30 days under the General Data Protection Regulation, unless we need
to extend that timeframe as permitted by applicable law."*

Keep the request ID from the confirmation email; the portal issues one and it is
the only artifact. When a response arrives, check it against the three questions
put in the comments box — provenance, recipients, and whether a mobile or
direct-dial number is held — because a generic completion notice will address none
of them.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Seamless Contacts, Inc.
- **Trading as:** Seamless.AI
- **Registered address:** 7652 Sawmill Road, Suite 341, Dublin, OH
- **Filed contact email:** privacy@seamlessleads.com
- **Website:** https://www.seamless.ai

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
