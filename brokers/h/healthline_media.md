# Healthline Media

- **Opt-out:** https://privacyportal.onetrust.com/webform/b45407c6-ee79-4a08-912e-02ce898f9a14/6685ab48-74c4-4eed-944b-38307e40ed1a
- **Method:** web_form — Web form.
- **Domain:** healthlinemedia.com
- **Priority: 1.**

## Status

- Current: `manual_required` (updated 2026-11-10)
- Note: 2026-11-09 import from Optery seeded `contact@fullspanhealth.com` as
  the contact email, with the domain flagged `offdomain_needs_confirmation`
  because that address does not appear on healthlinemedia.com at all.
- Update (2026-11-10): Confirmed the address is wrong, not an acquisition.
  Fetched both sites directly. Healthline Media's own footer states
  "Healthline Media is an RVO Health Company." Fullspan Health's footer
  states "Fullspan Health is owned and operated by RVO Health." They are
  **siblings under the same parent, not one-is-the-other** — Fullspan Health
  is RVO Health's B2B marketing/licensing arm (its own site pitches "Put
  America's largest health information platform to work for your brands"),
  and it appears on healthlinemedia.com only as a partner-brand logo, never
  as a privacy or legal contact. Sending a consumer deletion request there
  would reach a licensing sales team at a different business unit, not
  Healthline's privacy desk. **Registry corrected**: `email_to` cleared,
  method changed to `web_form`, pointed at the OneTrust form Healthline's
  own privacy notice actually publishes (link above). Healthline's privacy
  notice page gives no email address at all for data requests — the
  OneTrust form is the only route. Not submitted this pass: a web form
  needs a browser, which this project does not have for this broker.
  **Handed off.**

## Steps

1. Open the OneTrust form above.
2. Complete it as a CCPA/CPRA deletion and opt-out-of-sale request, listing
   all known email addresses, the current address, and the DOB.
3. Watch for a confirmation email at whichever address the form requires as
   its reply-to — OneTrust forms frequently gate on a verification click.

## Gotchas

- **The registry's imported contact address was wrong.** Optery's domain
  match (`fullspanhealth.com`) picked up a sibling brand under the same
  parent company (RVO Health) rather than Healthline Media's own contact.
  Shared-parent brand families are exactly where an off-domain address needs
  confirming before sending, not assuming — see CONTRIBUTING.md.
- Healthline Media publishes **no privacy email anywhere** — only the
  OneTrust form. Do not go looking for one; there isn't one to find.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
