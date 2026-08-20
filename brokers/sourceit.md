# Sourceit

- **Email:** dataprivacy@sourceitmarketing.com — verified against their own published page
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** sourceitmarketing.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
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
  (CORRECTED: not rotation - a botched WordPress edit, fixed by them 2026-08-20. Record when
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

## Outcome: confirmed, and the most complete answer in the project so far

The operator replied personally within hours, and answered every question asked.

**The removal.**

> "We only had the record of [one old webmail address] which has been removed."

One old webmail address out of twelve supplied — which is itself the argument for
listing every historical address rather than the current one. A search of the
current details would have found nothing and closed the file.

**The hashed-email question, answered voluntarily and correctly.**

> "We keep a SHA1/SHA256 hash, and your other email records are hashed to not be
> added again."

This is the *right* use of a hash and it should be accepted rather than argued
with. A suppression list that forgets you cannot suppress you. The distinction to
hold onto is between a hash kept so a record is never re-added, and a hash kept
as saleable match inventory — the first is compliance, the second is the product
wearing a disguise. Asking the question as a fork ("confirm these are covered or
tell me plainly which are not") is what makes the good answer easy to give.

**The broken link was real, and they fixed it.**

> "Thanks for letting us know. We corrected the page, it was failed change in
> wordpress."

See `_SILENT_FAILURES.md` §66, including the correction — the year stamp was not
a rotation policy, it was a botched WordPress edit. Reporting the fault plainly
in the letter cost two sentences and bought a same-morning fix plus a full
answer to everything else.

**They named their suppliers, unprompted by anything but the standard ask.**

> "The email contact lists that we have is from other third parties/data brokers,
> which include L2 Data, Apollo, DatabaseUSA, Zoominfo, LinkedIn, GetProspects,
> ExactData. We do not operate websites that collect consumer email lists."

Five were already tracked. One (LinkedIn) is a platform the subject has an
account with rather than a broker to write to. **L2 Data was not in the registry
at all** — a 250-million-record voter and consumer broker, surfaced only because
a reseller was asked where its data came from. See `brokers/l2_data.md`.

**"We go by email addresses for all our records"** confirms the join key, and
"we do not operate websites that collect consumer email lists" places them as a
pure reseller — which is exactly why the supplier question mattered more here
than the deletion did.

## What to reuse

Ask every reseller, in the first letter: *if you licensed my information from a
supplier, please tell me which one.* It costs a sentence. When it is answered it
converts one confirmed removal into a list of upstream sources, and the upstream
is where the record actually originates. A deletion at the reseller is undone by
the next ingest; a deletion at the source is not.
