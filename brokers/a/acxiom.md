# Acxiom

- **Opt-out:** https://www.acxiom.com/optout/  (isapps.acxiom.com/optout/optout.aspx redirects here)
- **Method:** web_form in a cross-origin iframe + reCAPTCHA at submit
- **Phone fallback:** (877) 774-2094 — full opt-out by voice, no CAPTCHA
- **Postal fallback:** Acxiom LLC, Consumer Care Advocate, CWY0301-026,
  Attn: Consumer Rights Requests, PO Box 2000, Conway, AR 72033
- **Priority: 5.** Upstream aggregator — its data feeds many downstream brokers,
  so this one has outsized leverage.

## Steps
1. Dismiss the cookie banner with **X**, not "OK" (OK accepts optional cookies).
2. "Select opt out segment" is a **multi-select** — add all three:
   Mailing Addresses, Phone Numbers, Email Addresses.
3. "Who is opting out?" → **Me**.
4. Fill First / Last / Area code / Phone / Email / Street / City / State / Zip.
   Title and Middle are optional — leave blank rather than guessing.
5. **Critical:** click the small blue **+** beside each of name, phone, email,
   and address. Values typed but not "+"-added are silently dropped and the
   form fails validation with "Please add at least one ...".
6. The address "+" opens a USPS normalization picker — take the RECOMMENDED form.
7. reCAPTCHA appears only after Submit is first clicked. Hand off to the human here.

## Gotchas
- The form is inside a cross-origin iframe (`isapps.acxiom.com`), so `read_page`
  and `form_input` return nothing for it — drive it with coordinates instead.
  Navigating to the iframe URL directly just redirects back to the parent page.
- The native `<select>` elements do not respond reliably to clicking an option in
  a stale screenshot. Click the select, then **type the option text** and press Return.
- Acxiom also offers Right to Know / Right to Delete separately from Opt Out.
  Deletion is stronger than opt-out and is worth filing as a second request.
