# GRIN Technologies Inc.

- **Email:** legal@grin.co (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** grin.co
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-10-12)
- Reference: request FLCMX7I6, `gmail:1a12e79d408108dd`
- Note: CONFIRMED DELETED 2026-10-12. The web-form route (`https://grin.co/data-privacy-form/`, run through the Saymine privacy portal at `grin.privacy.saymine.io`) worked where email had been refused. Sequence: form submission → an identity-verification email with a `verifyUser?jwToken=...` link (plain GET, no CAPTCHA, states a 7-day expiry) → an auto-reply acknowledging receipt ("we will answer it as soon as possible") → roughly 7 hours later, a substantive reply: "we would like to confirm that your personal data has been effectively and completely deleted from our systems. All of our service providers were [instructed to do likewise]." This is a genuine broker-issued confirmation, not a submission receipt — closes the loop EMAIL REFUSED opened on 2026-08-27.
- Prior: EMAIL REFUSED 2026-08-27, four seconds after sending. Auto-reply from legal+noreply@grin.co: 'If you are writing to make a request regarding your privacy or data, we need to verify the request, before taking action or releasing information. Please use Grin's [form].' The +noreply subaddress on a legal@ mailbox is the tell -- mail is accepted and answered by a machine that will not accept the request.

## Steps

Email is not the working route. Use `https://grin.co/data-privacy-form/`
directly — it runs through the Saymine privacy portal (`*.privacy.saymine.io`)
and verifies identity by email link (plain click, no CAPTCHA seen) before Grin
will act. If the link is unreachable, `privacy.support@grin.co` is the stated
fallback.

## Gotchas

Standard "email gets an identity-verification gate" shape — the letter itself
doesn't get read for content before being redirected to the form. The
verification step itself is a simple emailed link, not a form — no identity
document was requested.

## Verification

Confirmed deleted 2026-10-12, with downstream service providers stated as
notified too. Nothing public to re-search (a B2B prospecting database, not a
listing site); the written confirmation is the artifact. Re-check if a listing
resurfaces.

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
