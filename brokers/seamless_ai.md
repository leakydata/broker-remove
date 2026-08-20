# Seamless Ai

- **Opt-out:** https://login.seamless.ai/personalDataRequest
- **Email:** privacy@seamlessleads.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** seamlessleads.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Stage complete 2026-08-20. DataGrail flow finished end to end: email-verification link at 02:37 UTC, then a broker-issued confirmation at 02:50 UTC from noreply@saidsar.com - 'We have received your Deletion request... You will receive another email once your request has been completed.' Two separate senders are involved and they mean different things: privacy@seamlessleads.com sends a human deflection pointing at the Privacy Request Center, while noreply@saidsar.com is the DataGrail transactional address that issues the actual request artifacts. Only the second constitutes evidence a request exists. Awaiting the completion email.

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
