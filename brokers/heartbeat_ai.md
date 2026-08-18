# Heartbeat Ai

- **Opt-out:** https://heartbeat.ai/optout
- **Email:** contact@heartbeat.ai — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** heartbeat.ai
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Supplies personal mobile numbers and private email addresses for individuals, notably in healthcare - so the personal contact details ARE the product and the request is aimed squarely at them, including hashed forms. Asked for per-contact-point sourcing (the part not discoverable any other way), the customer list, permanent suppression, and do-not-contact entries held independently of the record so deletion does not remove the protection.

## Steps

1. Email `contact@heartbeat.ai`.
2. Name the personal contact details directly — they are the product.
3. Ask for **per-contact-point sourcing**: where each number and address came
   from.
4. Ask which customers received them.
5. Ask that do-not-contact entries survive the deletion.

## Gotchas

A service whose value is supplying a stranger with somebody's **personal mobile
number and private email address** is holding precisely the data a deletion request
is about. There is no need to reason about what might be in scope: say which
numbers and addresses, ask them to confirm which they hold, and ask for all of
them — including hashed forms.

**Per-contact-point sourcing is the ask worth insisting on.** Not "where did you
get my data" but *where did each number and each address come from, individually*.
These records are assembled from several upstream suppliers, and a single answer
names one of them. The itemised answer is the only way to reach the rest, and it is
information no amount of searching from outside will produce.

Suppression entries must be held **independently of the record** — otherwise
deleting the record removes the do-not-contact protection with it, which is the
perverse case in `_SILENT_FAILURES.md` §16.

**The exported copy is the one that matters.** These platforms exist to be
exported: a user runs a search, saves or downloads a record, and it lands in a CRM
or applicant-tracking system the platform cannot reach. Deleting the source record
removes the least consequential copy — the exported one is what actually contacts
you.

So ask for the recipient list in the same breath as the deletion. Without it there
is no way to pursue the copies, and a company that will not delete should at
minimum say who can. See `_DEFLECTIONS.md` §21.

## Verification

Nothing public to search. Ask the confirmation to list which of your contact points
they held, where each came from, and which customers received them. A reply that
says only "your data has been deleted" has answered none of those.

## They confirmed the opt-out and said nothing about the deletion

Within eight minutes, three times over, identically:

> *"Your request to opt out of the sale or sharing of your personal information has
> been received and successfully processed."*

The letter asked for two things — **delete**, and opt out of sale. The reply
confirms the second and is silent on the first, and the silence is easy to miss
because the message reads as a completion.

**Why the distinction matters especially here.** Heartbeat.ai's product is
supplying a stranger with somebody's personal mobile number and private email
address. An opt-out stops them *selling* that while they continue to *hold* it: it
remains available to existing customers, and exposed to any future change of
policy, breach or acquisition. Deletion removes it. For a company whose entire
inventory is personal contact points, "we have stopped selling it" is a
materially weaker outcome than it sounds.

This is `_SILENT_FAILURES.md` §12 arriving by email rather than through a form —
a request for several rights, an accurate confirmation of one, and nothing marking
the gap.

**Check every confirmation against the list you sent.** Not "did they reply
positively" but *which of my numbered requests does this sentence actually
address*. Where one is missing, say so and ask again; it is usually granted,
because nobody refused it in the first place.

## An operational note worth reporting back

Three identical confirmations and two ticket acknowledgements arrived for a single
message — an autoresponder firing per inbound rather than per ticket. Harmless
here, but worth mentioning to them: a privacy desk that cannot tell one request
from three is a privacy desk whose request counts are wrong, and those counts are
what some jurisdictions require companies to publish.

