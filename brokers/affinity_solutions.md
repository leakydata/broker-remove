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
