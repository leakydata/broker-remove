# Versium

- **Opt-out:** —
- **Email:** optout@versium.com (CONFIRMED — the address is published on their own page and matched exactly)
- **Method:** email
- **Domain:** versium.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)

## Steps

1. `verify_emails.py` returns CONFIRMED for `optout@versium.com` — a
   purpose-built removal mailbox, published, matching. No form, no account.
2. Send the identity-graph variant of the letter.

## Gotchas

**Ask for the edges, not the rows.** Versium sells identity resolution and data
append. In that business the graph *is* the product, so a deletion that clears
the endpoint records while leaving the linkage means the profile reassembles on
the next match. The letter names four things explicitly and asks them to confirm
each or say which is excluded:

- hashed forms of the email addresses (MD5, SHA-1, SHA-256) held as match keys
- mobile advertising identifiers, cookie IDs, CTV identifiers
- **the edges** between those identifiers and name / address / phone
- household-level association derived from IP address

**Suppression, not a one-time delete.** Append businesses re-ingest from
suppliers continuously. Ask for do-not-sell, do-not-rent, do-not-append and
do-not-re-onboard as standing entries, and say why: a record deleted today and
refilled from the same source next month is not deleted, and the confirmation
email reads identically either way.

**Ask for supplier and customer names.** A deletion at the compiler that leaves
copies in a customer's CRM is a deletion in name only.

## Verification

Watch for a reply. If it confirms deletion without addressing the edges, push
once on that specific point — it is the difference between removal and a pause.
