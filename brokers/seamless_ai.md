# Seamless Ai

- **Opt-out:** https://login.seamless.ai/personalDataRequest
- **Email:** privacy@seamlessleads.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** seamlessleads.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: LODGED AND ACKNOWLEDGED. After the hCaptcha and email verification, DataGrail sent: 'We have received your Deletion request. If you did not submit this request, please notify us immediately. Otherwise, no action is necessary. You will receive another email once your [request is processed].' So the full chain completed: form -> hCaptcha -> verify link -> Identity Verified -> receipt. Still no numeric request ID exposed; the saidsar.com verification token (d=...) is the only handle. Their stated clock is 45 days CCPA / 30 days GDPR. Watch for the completion email and check it against the three questions in the comments box -- provenance, recipients, and whether a mobile or direct-dial number is held -- since a generic completion notice will address none of them.

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
