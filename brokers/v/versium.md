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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Versium
- **Registered address:** 7530 164th Ave NE, A204, Redmond, WA 98052,
  United States
- **Filed contact email:** privacy@versium.com
- **Website:** http://www.versium.com
- **Opt-out route they filed:** Consumers may opt out via email to
  optout@versium.com, webform at https://versium.com/ccpa-opt-out, or by
  calling 1-800-395-0164.
- **Route for protected individuals:** Consumers may demand deletion of
  information via email to optout@versium.com, webform at
  https://versium.com/ccpa-opt-out, or by calling 1-800-395-0164. (Cal.
  Gov. Code 6208.1(b) / 6254.21(c)(1) — for survivors of domestic
  violence, stalking and similar, a stronger and faster route than the
  ordinary consumer request)
- **What they say they collect:** For information on data collecting
  practices, please see our Privacy Notice for California Residents at
  https://versium.com/ccpa-privacy-policy.

*Source: `data/registries/complete-reg-data-brokers.csv`.*

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
