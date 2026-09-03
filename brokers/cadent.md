# Cadent

- **Email:** privacy@cadent.tv (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** cadent.tv
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- **2026-09-02 (§291):** AUTORESPONDER ROUTES BACK TO THE FLOW THAT FAILED. Replying to my 2026-09-02 re-file, privacy@cadent.com (note: a different domain from the cadent.tv address I wrote to) returned a form letter: 'To submit a data rights request, please complete the form which can be found here: https://privacy.cadent.tv/privacy/#/verify-email. We aim to resolve your request within 45 days.' That is THE SAME verify-email flow the 17 August request died in -- the one whose confirmation mail gives 24 hours -- and the letter it answers was specifically about that window. THE LOOP, put to them without complaint attached: the only route they accept has a one-day expiry, and the channel that could bypass it answers by pointing at the route, so a person who misses the window twice has no third option. Not deliberate; it is what two reasonable rules produce when they meet. THE WEDGE USED: asked them to action the 1798.120 SALE/SHARING OPT-OUT FROM EMAIL ALONE, since that right REQUIRES NO IDENTITY VERIFICATION -- the CCPA regulations are explicit that a business shall not require verification as a condition of
- Reference: `tracking code on file`
- Note: Household opt-out of sale/share (incl. targeted advertising and sensitive PI) submitted and acknowledged by email with a tracking code. Access and Delete remain unexercised because both require a device ID the consumer cannot produce. Stated turnaround 45 days.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

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

