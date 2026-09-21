# Heartbeat Ai

- **Opt-out:** https://heartbeat.ai/optout
- **Email:** contact@heartbeat.ai — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** heartbeat.ai
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-21)
- Note: Replied three times with an IDENTICAL confirmation covering only the OPT-OUT: 'your request to opt out of the sale or sharing of your personal information has been received and successfully processed.' Silent on deletion, which was the first half of the request. Pressed for deletion specifically, plus which identifiers they hold (including hashed), per-contact-point sourcing, the customer list, and a do-not-contact entry held independently of the record. Also flagged their autoresponder firing per inbound rather than per ticket.
- **2026-09-02 reply (sat unread until this 2026-09-21 pass — check for stale unread mail on any thread that got a follow-up letter):** answers the deletion-vs-suppression gap above. Records tied to name, email addresses, LinkedIn profile and Facebook profile have been suppressed and are "not disclosed, processed, or made available to any customer," and identifiers were added to a suppression list meant to survive future data refreshes or enrichment. They said they are not aware of additional hashed/pseudonymized records beyond what was suppressed. Declined the itemized asks: source given only as a general category ("online sources"), recipients given only as a general category ("customers on our platform who use this information for contact discovery purposes") — no supplier-by-supplier or per-customer breakdown. This is the same reply text, nearly verbatim, that Swordfish AI sent under its own name for the same identifiers (see swordfish_ai.md) — the two run on one shared backend.

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

## A substantive reply sat unread for 19 days

The 2026-09-02 suppression confirmation above was sitting in the inbox,
marked unread, through at least two later passes before this one read it. It
was not a bounce and not boilerplate — it was the actual answer to the
deletion-vs-opt-out gap raised on 2026-08-18 — and the ledger kept showing
`submitted` from August the whole time, understating real progress. Whatever
inbox query a pass runs first should not be scoped so narrowly (e.g. to a
short `newer_than:` window, or only to threads matching a broker's most
recent send) that it can skip an older unread message sitting in a thread
that already looked "closed" after the 08-18 exchange. Worth an occasional
`is:unread` sweep with no date bound at all, not just the recent-window one.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Heartbeat.AI Inc
- **Trading as:** Heartbeat AI
- **Registered address:** 8 THE GREEN, STE 4000, Dover, DE, 19901
- **Filed contact email:** contact@heartbeat.ai
- **Filed phone:** (855) 512-9715
- **Website:** www.heartbeat.ai

*Source: `data/registries/registry.csv`.*

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
