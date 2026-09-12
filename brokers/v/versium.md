# Versium

- **Opt-out:** —
- **Email:** optout@versium.com (CONFIRMED — the address is published on their own page and matched exactly)
- **Method:** email
- **Domain:** versium.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-11)
- Note: CORRECTED 2026-09-11 FROM A 'confirmed' THAT HAD ALREADY BEEN CORRECTED ONCE AND WAS SILENTLY RESTORED -- the same defect as plunge_digital on the same two days. History: confirmed 2026-08-20 on a THREE-SECOND autoresponder; DOWNGRADED 2026-08-27 to submitted with full evidence; then 'confirmed' AGAIN on 2026-08-28 by an adoption citing the stale record, with the note 'No detail is carried across'. The correction was overwritten the next day by a mechanism that never checked whether the row had moved on. See _SILENT_FAILURES 433. WHY THE DOWNGRADE WAS RIGHT AND STILL IS: optout+noreply@versium.com replied three seconds after the letter -- 'We have processed your request to optout/delete your record from Versium data. Please consider this response your confirmation.' On 27 Aug a HUMAN at optout@versium.com wrote: 'If we do not receive a reply to this email within 10 days, we will process the opt-out request.' Future tense. The opt-out had therefore NOT been processed on 20 Aug; the autoresponder fires on receipt and describes queued work in the past tense. THE TRAP in their 27 Aug message, unchanged: silence triggers the opt-out and a reply SUSPENDS it, so a consumer who engages is left worse off than one who ignores them. The reply sent 2026-08-27 led with an explicit unconditional instruction to process the deletion and opt-out now, severable from everything else. NOW OVERDUE: the 10-day window from 2026-08-27 expired around 2026-09-06 and no further inbound mail has arrived from versium.com. Next move is to ask them to confirm the opt-out was processed at the end of that window, quoting their own sentence back.

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
