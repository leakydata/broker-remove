# Sourceit

- **Email:** dataprivacy@sourceitmarketing.com — verified against their own published page
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** sourceitmarketing.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Sent 2026-08-20 05:36 UTC to dataprivacy@sourceitmarketing.com (confirmed on their own site). List/marketing data. Standard row-vs-person framing plus the source question, and deliberately offered them an exit on it: if naming the source is something they will not do, say so explicitly - a clear refusal is a useful answer and I will not press further. That construction has worked before (MightyRep); an unanswered question invites silence, a question with a stated acceptable refusal invites an answer.

## Steps

1. **Do not click the contact link on their privacy policy.** Its `mailto:` href
   and its visible text are different mailboxes, and the href is dead
   (`_SILENT_FAILURES.md` §66).
2. Mail the **year-stamped** address that appears in the policy's running text —
   the same local part with the current year appended. Three plain-text
   occurrences in the policy use it; only the anchor's href is stale.
3. Use the subject line their policy requires for opt-outs:
   **`CCPA Opt-out`**.
4. Second routes worth trying: their self-service portal at `/privacy`, and the
   "Do Not Sell My Info" link on the home page. Both are named in the policy.

## Gotchas

- **The address has an expiry date.** A year stamp in a privacy mailbox means a
  rotation: last year's is gone and next year's does not exist yet. Record when
  you verified it, not only that you did.
- **Automated verification will confirm the wrong address.** Both mailboxes
  appear in the fetched HTML — one in the href, one in the link text — so an
  extractor that pools everything on the page will happily confirm the dead one
  and stop looking. Compare href against text explicitly.
- **The bounce is mailbox-level, not domain-level.** Office 365 answers with
  "Recipient Unknown" while the domain, MX and site are all healthy, so the
  failure reads like a typo on your side.

## Verification

No public profile. The observables are their answer on suppression-vs-deletion,
and whether they name the compiler that supplied the record — the request asked
for both separately and offered an explicit exit on the source question.
