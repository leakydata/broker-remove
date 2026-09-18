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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Acxiom LLC
- **Registered address:** 301 E Dave Ward Drive, Conway, AR, 72032
- **Filed contact email:** askprivacy@acxiom.com
- **Filed phone:** 5013421000
- **Website:** www.acxiom.com

*Source: `data/registries/registry.csv`.*

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
