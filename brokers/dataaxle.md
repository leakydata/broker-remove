# Data Axle (infoUSA)

- **Opt-out:** https://www.data-axle.com/privacy-rights-request/
- **Email:** privacyteam@data-axle.com — **unverified, may bounce**
- **Method:** web_form_captcha — Web form with a CAPTCHA — see where it sits (page load vs submit).
- **Domain:** data-axle.com
- **Priority: 5.**

## Status

- Current: `manual_required` (updated 2026-08-18)
- Note: Form staged at data-axle.com/privacy-rights-request/, reCAPTCHA on submit. Privacy Choice is a single-select so deletion and opt-out of sale need TWO separate submissions. Their privacy policy also claims deemed consent: by agreeing to the policy you consent to commercial use of your data 'now, and at all times in the future, regardless of when or how Data Axle acquired' it, unless you opt out.

## Steps

1. Use the **Consumer Privacy Rights Request** form at
   `https://www.data-axle.com/privacy-rights-request/`. Do not use the
   Authorized Agent form — that is for agents acting for someone else, and this
   is a first-party request.
2. Fill first/last name, address, city, state, ZIP, email and phone. All are
   required.
3. Choose the **Privacy Choice**. It is a single-select — see below.
4. Tick the attestation box, then submit. A reCAPTCHA sits on the submit.
5. **Submit the form a second time** with a different Privacy Choice, for the
   second right you want.

One form covers Exact Data as well; it runs on the same domain and publishes the
same privacy address.

## Gotchas

**The Privacy Choice dropdown is a single-select, and its options are rights, not
categories:**

    Request to opt out of sale/sharing
    Request to correct inaccuracies
    Request to delete
    Request to access
    Request to limit use/disclosure of sensitive personal information

So one submission buys **one right**. A consumer who wants their data deleted
*and* wants to stop it being sold has to submit twice, and nothing on the page
says so. Pick "Request to delete", submit, then do the whole thing again with
"Request to opt out of sale/sharing".

This is the same shape as Belardi Wong's three separate OneTrust form UUIDs, and
it is worth treating as a general rule: **wherever a form asks you to choose a
right, assume the others were not requested.** The confirmation will be accurate
and will cover only what you picked. See `_SILENT_FAILURES.md`.

## The consent clause

Their privacy policy contains a claim worth reading twice:

> *"By agreeing to this privacy policy, you hereby consent to Data Axle using your
> personal information for commercial purposes now, and at all times in the
> future, regardless of when or how Data Axle acquired your personal information,
> unless and until you opt out."*

Read plainly: a person who has never visited the site, never agreed to anything,
and whose data was acquired from a third party is deemed to have consented —
permanently, and to any future use — with an opt-out as the only exit.

Whatever its legal weight, it tells you how the business is structured, and it is
the reason the opt-out submission matters as much as the deletion. Deletion
removes what they hold today; the opt-out is what addresses the standing
permission they assert for tomorrow. **Do both.**

The policy also states outright that the entity maintaining the site is a data
broker — useful, since a self-declaration forecloses the "we are not a data
broker" deflection before it is offered.

## Verification

Nothing public to search. Ask the confirmation to state **which right** was
actioned, and keep both confirmations separately — one per submission. Two
confirmations that both say "your request has been processed" are not
interchangeable, and only the pair together shows deletion and opt-out were both
requested.
