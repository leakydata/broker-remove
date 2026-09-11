# Belardi Wong

- **Opt-out:** https://privacyportal.onetrust.com/webform/3d2d5e0c-bd98-46b8-906c-ede68a6f6a80/400f54ed-fcbb-4749-ab5b-32f491c72390
- **Email:** privacy.officer@belardiwong.com (verified)
- **Method:** web_form — Web form.
- **Domain:** belardiwong.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Reference: `OneTrust request ID on file`
- Note: Deletion request submitted via OneTrust webform and the two-step email verification completed: 'Your request is confirmed!'. Broker-issued Request ID on file.

## Steps

1. Email `privacy.officer@belardiwong.com`. Do not expect a person: it is an
   unmonitored auto-responder.
2. Its reply supplies **three OneTrust webform UUIDs** — opt-out, deletion and
   access. Pick deletion; they are separate requests and submitting one does not
   imply the others.
3. Fill the OneTrust form. A text-image CAPTCHA sits at submit, so this is a
   hand-off point, not an automation point.
4. **Complete the email verification.** OneTrust sends a confirmation link; the
   request is not filed until you have seen *"Your request is confirmed!"*.
5. Record the broker-issued Request ID.

## Gotchas

The published privacy address is a dispatcher, not a mailbox. Writing to it
produces an auto-reply and no ticket — the request only exists once a OneTrust
form has been submitted and verified.

**Three separate UUIDs is the thing to notice.** Opt-out, deletion and access are
three requests at this broker, and a consumer who submits "the privacy form"
submits one of them. If deletion is what you want, the opt-out form will
cheerfully accept you and confirm success, and nothing will be deleted. Read the
UUID's own label before filling it.

OneTrust's two-step is genuine and easy to half-complete: form submission is
followed by an emailed verification link, and an unclicked link means no request.
See `_SILENT_FAILURES.md` §2. Take the link from the **HTML** part of the mail,
not the plaintext part — plaintext quoted-printable wrapping has been observed
eating characters out of these URLs.

Both steps done here; a Request ID was issued and is on file.

## Verification

OneTrust request IDs are quotable back to the broker, so verification is a matter
of asking rather than searching: reply on the confirmation with the ID and ask
for the outcome and its date.

Re-check ~30 days after confirmation. If nothing arrives, the Request ID is what
makes a follow-up concrete rather than a repeat.
