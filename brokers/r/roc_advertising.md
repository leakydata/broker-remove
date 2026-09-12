# Roc Advertising

- **Email:** dataprivacy_rocadvertising@simpleoptoutcompliance.com — verified against their own published page
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** simpleoptoutcompliance.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Resent 2026-08-20 to first-party privacy@rocadvertising.com after the published vendor address at simpleoptoutcompliance.com hard-bounced 550 5.1.1. Subject line 'Data Removal Request' as their policy requires.

## Steps

1. **Do not use the address in the aggregator listings.**
   `dataprivacy_rocadvertising@simpleoptoutcompliance.com` hard-bounces
   `550 5.1.1`. The domain resolves and has an SES inbound MX, so the bounce is
   mailbox-level, not domain-level — it looks like a typo and is not one.
2. Fetch `https://www.rocadvertising.com/privacy-policy/` and **decode HTML
   entities before extracting addresses** (see `_SILENT_FAILURES.md` §64). The
   live address is `privacy@` their own domain, written entirely as character
   entities, twice, with different decimal/hex mixes each time.
3. Send with the exact subject line their policy requires:
   **`Data Removal Request`**.
4. Ask for suppression, not only deletion — their policy states they buy
   one-time mailing lists from a data broker, so the record is re-acquirable by
   construction.

## Gotchas

- **The corporate name is not the brand name.** The policy attributes the
  list-rental business to "Results Only Consulting", not to ROC Advertising.
  Address the letter to both; a mailbox that files by legal entity will not
  match a letter addressed only to the trading name.
- **They publish their own answer.** Their policy says consumers "may delete
  their record, opt-out or unsubscribe from having their data rented or sold"
  by writing with that subject line. Quote it rather than arguing statute — the
  ask is theirs, and there is nothing left to dispute.
- **A stated mailing lead time.** The policy warns that advertising prepared in
  advance may continue for "up to 10-days after unsubscribing, and 45-days after
  opting-out or deleting their record". Treat 45 days, not the confirmation
  date, as the point at which to judge whether it worked.

## Verification

No public profile to re-check — this is a mail-list business, so the observable
is mail volume, not a search result. Their own policy sets the window: judge at
**45 days after confirmation**, not before. If mail continues past that, quote
the 45-day figure back at them; it is their number.
