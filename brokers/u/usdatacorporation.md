# US Data Corporation

- **Opt-out:** —
- **Email:** privacy@usdatacorporation.com (kept — verification found
  `info@usdatacorporation.com` published, but a generic mailbox is not an
  improvement on a purpose-named privacy one; `info@` recorded as fallback)
- **Method:** email
- **Domain:** usdatacorporation.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)

## Gotchas

**Never trade a privacy address down to a generic one.** `verify_emails.py`
returns KEEP_BETTER here: `info@` is definitely real because it is published,
and `privacy@` might bounce. Send to `privacy@` anyway. A deletion request
landing in a sales inbox is worse than one that bounces, because a bounce at
least tells you it failed.

**The suppression entry matters more than the deletion.** This is list
compilation and rental. Ask for five standing entries by name, not a single
"remove me":

- do not sell
- do not rent
- do not append
- **do not re-onboard** — so the record is not re-acquired from a compiler on
  the next ingest
- do not mail, and do not call

State why re-onboarding is the one that counts: a record deleted today and
refilled from the same upstream compiler next quarter is not deleted, and nothing
in the confirmation distinguishes the two.

**Ask about modelled attributes as well as source fields** — income, household,
life-event and interest attributes are inferences about the person and are
personal information in their own right.

**Suppress against every historical address and phone.** A match on an old
address is exactly how a deleted record gets restored under a slightly different
key, so a suppression keyed only to the current address does not hold.

**Ask which compiler or co-operative the data was licensed from.** In a rental
business that is where the fix has to happen.

## Verification

No public search page to check against, so verification depends on their written
answer. If the reply confirms deletion but says nothing about re-onboarding, ask
that single question again.
