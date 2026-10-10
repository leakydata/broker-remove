# Seamless Ai

- **Opt-out:** https://login.seamless.ai/personalDataRequest
- **Email:** privacy@seamlessleads.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** seamlessleads.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-10-10)
- Note: AUTO-REPLY DEFLECTED AN INCIDENT REPORT TO A REQUEST FORM, 2026-10-10. Seamless answered the 464 follow-up with an automated message -- it says so itself, 'This email was sent by an automated service' -- directing all access, correction, deletion and opt-out requests to preferences.seamless.ai and stating 'Seamless does not respond to initial access, correction, deletion, or opt-out at this email address.' THE LETTER WAS NOT A REQUEST AND THE FORM CANNOT CARRY IT. His own request is FINISHED: they completed it on 17 September with erasure confirmed, the pre-erasure data supplied and the retention basis explained. There is nothing outstanding about his data. The follow-up raised two things a rights-request form has no field for. (1) THEIR ACCESS RESPONSE DISCLOSED THIRD PARTIES' PERSONAL DATA to an unrelated requester -- at least two addresses in the file belong to identifiable other people, present because the matching logic built a composite of several people sharing the name. That is an incident arising from the access PROCESS, not a consumer rights request. (2) A REQUEST TO NARROW THEIR SUPPRESSION, which cuts against his own interest: if the suppression is keyed to everything in the deleted record rather than to his name and email, it would block strangers from a database on a decision that was never his. REPLIED, FIRMLY AND WITHOUT ESCALATING. Pointed out the channel objection does not apply -- this was not an initial anything, it was a reply on the thread where their team sent a detailed substantive answer from this same address three weeks ago, so the address demonstrably reaches people who engage when a human reads it. Asked for a better route if one exists -- DPO, legal, incident address -- and for two concrete things: whether access responses are reviewed for identifiers that do not match the requester before they go out, and whether the suppression is keyed to his two identifiers or the whole record. STATUS LEFT AT confirmed because the deletion genuinely is complete; the open items are about other people and about their process, not about his data.

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
