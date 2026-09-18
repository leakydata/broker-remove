# Xverum (Operia)

- **Opt-out:** https://www.xverum.com/dontusemydata/
- **Method:** web_form — Web form.
- **Domain:** xverum.com
- **Priority: 3.**

## Status

- Current: `manual_required` (added 2026-09-18)
- Note: Not previously in this registry. hireEZ's data-subject reply
  (2026-09-17, see `hireez.md`) named "Operia/Xverum" as one of the third
  parties it sources candidate contact data from and pointed to this
  dedicated opt-out form -- no email address is published anywhere for this
  route. Browser-gated: **needs a human** to load the form and submit it.
  Nothing sent yet.

## Steps

1. Open https://www.xverum.com/dontusemydata/ in a real browser.
2. Fill in name, and whatever identifiers the form requests (do not
   over-supply beyond what the form asks for).
3. If the form has a CAPTCHA, stage everything else and hand off only the
   CAPTCHA click -- never solve it automatically.
4. Record the confirmation (a ticket number or confirmation screen/email) in
   this file.

## Gotchas

- Discovered as an UPSTREAM SUPPLIER via a downstream customer's (hireEZ's)
  disclosure, not via Xverum's own site or a state filing -- the same pattern
  as `alpha_data_labs`. Worth checking hireEZ's reply again if this company
  changes its opt-out route, since hireEZ is the only source for it here.
- No email route at all as far as has been found -- if the form breaks or is
  CAPTCHA-gated at page load (not just at submit), there is currently no
  documented fallback. Check the privacy policy for a `dpo@` or `privacy@`
  address before assuming email is not an option.

## Verification

Not yet submitted.
