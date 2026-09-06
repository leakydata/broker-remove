# Plaid

- **Opt-out:** https://my.plaid.com/data-subject-request-form
- **Method:** web_form — Web form.
- **Domain:** my.plaid.com
- **Priority: 4.**

## Status

- Current: `manual_required` (updated 2026-09-06) — never attempted; no published email, dedicated web form only
- Note: Plaid is a financial-data aggregator (bank-account linking infrastructure for other apps) rather than a people-search site — a plausible holder of financial-account-linked personal data even without a direct consumer relationship, if the subject ever used an app that itself uses Plaid underneath. No privacy-request email address is published anywhere on their site; the dedicated DSAR form is the only route on record.

## Steps

1. Go to https://my.plaid.com/data-subject-request-form and submit a data-subject request (access and/or deletion) with the standard identifier set.
2. Note in the request that this is a "no direct relationship" inquiry — the subject may never have used Plaid directly, only an app that uses Plaid as infrastructure — since Plaid's form may be built assuming a linked bank account exists.

## Gotchas

- **No email route exists to fall back on.** Unlike most entries in this registry, there is no `privacy@` or `dpo@` address published anywhere to try before resorting to the form.
- **Likely to return a nil for a "no known account" search** — worth asking explicitly whether that means no linked account exists at all, or whether Plaid holds no PII outside of a linked-account relationship in the first place.

## Verification

No self-service way to re-check short of resubmitting the form; rely on their written confirmation and stated response timeframe.
