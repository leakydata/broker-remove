# Retention Com

- **Opt-out:** https://app.retention.com/optout/
- **Email:** support@retention.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** retention.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-28)
- Note: UNPROMPTED MESSAGE 2026-08-28 01:55 UTC from support@retention.com: 'We have received your Opt-Out removal request but we previously received this request on Aug 19, 2026. 10:50am EDT. It would have already been marked for removal in our database.'

NOBODY HERE SENT A SECOND REQUEST -- a Sent-folder search shows exactly one letter to retention.com, on 19 Aug. So a duplicate reached them today from somewhere else: plausibly the concurrent peer session, a removal service, or a form. Told them so plainly, so they are not answering a duplicate they think I filed.

Used the reopened thread to press the SCOPE QUESTION that has been outstanding since the original confirmation. That confirmation named ONE email address of the twelve, and the phrase was 'marked for removal in our vendor database' rather than deleted. Scope matters more here than at an ordinary list broker because Retention.com resolves anonymous site visitors to identities: the value is the GRAPH, so suppressing one address of twelve cuts one edge and leaves the person reachable through the other eleven. Asked: (1) were all twelve searched and suppressed or only the one named -- relisted all twelve; (2) does the suppression reach HASHED forms held as match keys, since in a resolution product the hash is usually the key that does the work; (3) 'marked for removal' nine days ago -- what is the state now, noting without reading anything into it that today's wording is 'would have already been' rather than 'was'; and (4) standing suppression checked against incoming data, or a removal of what was present on the day, since the database is rebuilt from partner feeds and only the first survives. Said plainly that the second is a complete answer if true.

Status left at confirmed -- the original confirmation stands on its own terms and nothing has contradicted it; what is open is its SCOPE, not its truth.

## Steps

Email to `optouts@retention.com`; the reply came from `support@retention.com`
with `optouts@` on Cc.

> "We have processed your Opt-Out removal request. \<one address\> has been
> marked for removal in our vendor database."

## Gotchas

- **Read the scope, not the verb.** The confirmation names **one** email address
  and says "marked for removal in our vendor database" — not deleted, and not
  scoped to the twelve addresses the request listed. For a business whose product
  is resolving anonymous site visitors to identities, one address suppressed is
  one edge cut in a graph keyed on many. The question of whether the other
  eleven were searched is open, and the confirmation is silent rather than
  negative on it.
- **"Marked for removal" is a suppression flag, not a deletion.** That is not
  necessarily worse — a suppression flag is what actually stops re-acquisition —
  but it means the record still exists in some form, and it is worth asking which
  they applied rather than assuming the better reading.

## Verification

No public profile to search. The observable is indirect: whether identity-resolved
mail keyed to these addresses continues. Follow up on scope first — a one-address
confirmation against a twelve-address request is the thing to resolve before
treating this as complete.

## Follow-up, 28 Aug 2026 — the scope question, and a duplicate we did not send

Retention.com wrote **unprompted**, nine days after the original confirmation:

> "We have received your Opt-Out removal request but we previously received this
> request on Aug 19, 2026. 10:50am EDT. It would have already been marked for
> removal in our database."

**Nobody here sent a second request.** A Sent-folder search returns exactly one
letter to the domain, on 19 August. So a duplicate reached them from somewhere
else — plausibly a concurrent session, a removal service, or a form submitted
elsewhere. They were told that plainly, so they are not answering a duplicate they
believe the subject filed. Worth noting generally: **when a broker reports a
request you did not make, say so** — otherwise their dedupe logic silently
attributes someone else's submission to you, and your own follow-ups start looking
like repeats.

The reopened thread was used for the scope question this playbook already flagged
as the thing to resolve first. Four questions, each answerable in a sentence:

1. **All twelve addresses, or only the one named?** Relisted all twelve so nothing
   turns on the earlier letter being to hand.
2. **Does the suppression reach hashed forms** — MD5, SHA-1, SHA-256 — held as
   match keys? In a resolution product the hash is usually the key that actually
   does the work, so a suppression that covers only the plaintext address covers
   the wrong column.
3. **What is the state now?** "Marked for removal" was nine days ago. Marked and
   removed are different, and that is long enough for the difference to have
   resolved.
4. **Standing suppression, or a removal of what was present on the day?** The
   database is rebuilt from partner feeds, so only the first survives the next
   load — and the confirmation reads identically either way.

**One wording detail, noted without weight put on it.** Today's message says the
record *"would have already been"* marked for removal — an inference from process
rather than an assertion of fact. That was raised explicitly as a preference for
the fact over the inference, not as an accusation. It is the same distinction
§138 turns on: a claim a template could produce either way tells you nothing about
what actually happened.

**Status stays `confirmed`.** Nothing has contradicted the original confirmation.
What is open is its *scope*, not its truth — and those are different failures with
different remedies.
