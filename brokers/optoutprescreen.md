# OptOutPrescreen (credit offers)

- **Opt-out:** https://www.optoutprescreen.com/
- **Method:** web_form — Web form.
- **Domain:** optoutprescreen.com
- **Priority: 4.**

## Status

- Current: `manual_required` (updated 2026-09-06) — never attempted; browser-only, no email/no-CAPTCHA route
- Note: OptOutPrescreen is the official joint Equifax/Experian/TransUnion/Innovis site for opting out of pre-screened ("firm offer of credit") mail and marketing lists — a genuine, high-value suppression since it covers all four major credit bureaus in one action.

## Steps

1. Go to https://www.optoutprescreen.com/ and choose the electronic 5-year opt-out (no SSN required) rather than the permanent postal option.
2. The permanent (lifetime) opt-out requires mailing a signed form that includes the last 4 digits of the SSN — **do not use this option**; the CPRA/CCPA `never submit more than a form requires` rule and this project's own no-SSN policy both point to the 5-year electronic option, which needs only name and address.
3. Renew again in 5 years, or repeat sooner as a reminder.

## Gotchas

- **Two very different options on the same page, one of them SSN-gated.** The 5-year electronic opt-out asks only for identity details already in this letter set; the permanent postal opt-out asks for a partial SSN. Always take the electronic option — the recurring 5-year renewal costs far less than handing a partial SSN to a form.
- **No CAPTCHA reported on this form as of the last check**, but it has not been attempted in this project yet — confirm before assuming a one-click completion.

## Verification

Re-run the credit-offer opt-out check by watching for a drop in prescreened credit-offer mail volume over the following 1–2 months; no online status page to query.
