# DMAchoice (direct mail)

- **Opt-out:** https://dmachoice.thedma.org/
- **Method:** account_required — Requires an account or profile claim.
- **Domain:** dmachoice.thedma.org
- **Priority: 4.**

## Status

- Current: `manual_required` (updated 2026-09-06) — never attempted; requires an account this project's rules forbid creating on the subject's behalf
- Note: DMAchoice is the DMA's own direct-mail preference service — a legitimate, industry-run suppression list rather than a scraped data broker, and one of the few opt-outs that genuinely reduces future postal mail volume rather than just one company's copy of a record. It charges a $6 processing fee and requires creating a personal account/profile on their site to register the preference.

## Steps

1. Go to https://dmachoice.thedma.org/ and register a personal consumer account (their own account, not a third-party login).
2. Add the subject's name and current mailing address to the "do not mail" preference list; the $6 fee is paid at registration.
3. Renews periodically per their published terms — check the confirmation email for the exact renewal window.

## Gotchas

- **This project's own rule — "never create an account with a broker" — is exactly why this sits in `manual_required` rather than `submitted`.** An account is a new record, and DMAchoice's flow has no account-free path. This is a legitimate exception where the human must do it directly rather than the removal project creating a proxy account.
- **Requires a small payment ($6).** No automated or free-tier path exists for the online registration.

## Verification

No verification possible until the account is created and the preference registered. Direct-mail volume drop is the practical signal, over the following 1–3 months per their own published timeline.
