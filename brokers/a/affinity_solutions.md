# Affinity Solutions

- **Email: refused.** *"For privacy and security reasons, Affinity Solutions does
  not accept privacy requests via email."*
- **Working route:** OneTrust web form, linked from
  <https://www.affinity.solutions/data-privacy-notice/>
- **Method:** web form + **text CAPTCHA** at submit, then email verification
- **Priority: 2.** Consumer purchase / card transaction data via bank partners.

## Route
1. Their auto-reply supplies a OneTrust webform URL. It is **not** gated on load.
2. Choose: *on behalf of* → **Myself**; then the right you want.
   **Only ONE right is selectable per submission** — pick Delete, and state in
   Request Details that it also constitutes Do Not Sell, or file twice.
3. Fields: address, city, country, state, zip, first/last, email, phone, **DOB**,
   Request Details (5000 chars), acknowledgement, **text CAPTCHA**, submit.
4. An email verification link follows. **The request is not processed until it is
   clicked** — point the email at a mailbox you can actually read.
5. Success page: `/trust-center-portal/#/verify/success`. Keep the **Request ID**.

## What to ask for
Bank-sourced transaction data. Use Request Details to widen scope beyond the
name-and-address record:

- transaction records, merchant-level purchase history, spend categories
- segments, scores and inferences derived from them
- **ask them to search hashed forms** of your email — identifier matching here is
  routinely done on hashed email, so a plaintext-only search can return nothing
  while they hold plenty
- ask **which financial institution or data partner supplied** your information;
  that names an upstream relationship you probably don't know exists

## Gotchas
- Request Details says "please refrain from entering any personal information" —
  odd on a privacy form. Use it for scope and instructions, not identifiers.
- Two valid domains for their mail: `affinitysolutions.com` and `affinity.solutions`.

## Email is refused; the web form is the only route

Auto-reply, verbatim:

> *"Please note that for privacy and security reasons, Affinity Solutions does not
> accept privacy requests via email. You can submit a privacy request via our
> interactive web form."*

No human appears to read the mailbox, so unlike some refusals this one is not
worth arguing — go to the form.

## The request is not filed until you click the emailed link

The form is OneTrust-hosted. On submission it issues a Request ID by email and
then requires a second step: an emailed **"Confirm email"** button. Only after
clicking does the portal say *"Your request is confirmed!"*

A request submitted here sat unverified for roughly a day and was indistinguishable
from a completed one. Do not close the loop until you have seen the confirmation
page. See `_SILENT_FAILURES.md` §2.

## Status

- Current: `submitted` (updated 2026-09-03)
- **2026-09-03 (§294):** SECOND RIGHT PRESSED BY EMAIL 2026-09-03 (SILENT_FAILURES 293/290). The OneTrust deletion is filed and email-verified (X4SPXJY2DR, right selected: Delete My Information) but THE FORM ALLOWS ONE RIGHT PER SUBMISSION, so the do-not-sell request went into the free-text details field -- and a note in a text box is not a filed request. Asked them to record the 1798.120 opt-out from the email, on the ground that it requires no verification: there is nothing to verify, a wrongly-honoured opt-out discloses nothing and harms no one, which is why it is treated differently from deletion where a mistaken match destroys the wrong person's record. Their form has already verified the address for the deletion; the opt-out needs less than that. TWO COMPANY-SPECIFIC POINTS: Affinity works with CARD-TRANSACTION DATA SOURCED FROM FINANCIAL INSTITUTIONS, so (a) the derived layer IS the product -- spend categories, merchant affinities, income and lifestyle inferences, audience segments -- and a deletion clearing an identity row while keeping the segments is a half-deletion; and (b) I never had a relationship with them, so if a record exists it arrived from a bank or card issuer I DID deal with, which ma
