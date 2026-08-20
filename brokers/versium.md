# Versium

- **Opt-out:** —
- **Email:** optout@versium.com (CONFIRMED — the address is published on their own page and matched exactly)
- **Method:** email
- **Domain:** versium.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)

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

## Outcome

Confirmed **three seconds** after the request, from `optout+noreply@versium.com`:

> "Thank you for contacting Versium Analytics. We have processed your request to
> optout/delete your record from Versium data. Please consider this response
> your confirmation."

**Read the timestamp before reading the words.** A three-second turnaround is an
autoresponder; nobody searched a database in that interval. The message is a real,
quotable, unconditional written confirmation — it says "processed", past tense,
and explicitly offers itself as the confirmation — and it is simultaneously
zero evidence that a lookup happened.

Both things are true and neither cancels the other. Record it as confirmed,
because that is what they put in writing and it is the artifact a complaint would
rest on. But treat it as the weakest class of confirmation and re-verify on the
normal cadence rather than trusting it. A confirmation whose latency is shorter
than a database query is a **policy statement about what they do**, not a report
about what they did.

None of the edge questions was answered, which is consistent with an automated
reply and not worth pursuing as a refusal.
