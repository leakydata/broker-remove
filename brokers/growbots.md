# Growbots

- **Email:** privacy@growbots.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** growbots.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Outbound-prospecting platform. Beyond the contact record, asked for CAMPAIGN AND ENGAGEMENT HISTORY - messages sent, opens, clicks, replies, bounce status - which is personal data about the recipient and is routinely missed by a deletion framed as being about a 'contact'. Plus copies in customer sequences, and a global suppression entry held independently so deletion does not make the address mailable again.

## Steps

1. Email `privacy@growbots.com`.
2. Search professional identifiers and hashed forms.
3. Ask for **campaign and engagement history**, not just the contact record.
4. Ask which customers hold exported copies.
5. Ask for a global suppression entry that survives the deletion.

## Gotchas

**Ask for the engagement log, not just the contact.** An outbound platform holds
more than an address: messages sent, opens, clicks, replies, bounce status. That
is a record of what was sent to a person and how they behaved — personal
information about them — and it is routinely missed, because a deletion framed as
being about a "contact" reads as being about the contact row.

**The suppression-survives-deletion point is acute here** (`_SILENT_FAILURES.md`
§16). If an address is on a global do-not-contact list and that entry is a property
of the contact record, deleting the record makes the address mailable again — the
consumer becomes reachable *because* they asked to be deleted. Ask for the
suppression entry to be held independently, and ask the confirmation to state it
separately.

**The exported copy is the one that matters.** These platforms exist to be
exported: a user runs a search, saves or downloads a record, and it lands in a CRM
or applicant-tracking system the platform cannot reach. Deleting the source record
removes the least consequential copy — the exported one is what actually contacts
you.

So ask for the recipient list in the same breath as the deletion. Without it there
is no way to pursue the copies, and a company that will not delete should at
minimum say who can. See `_DEFLECTIONS.md` §21.

## Verification

Nothing public to search. The practical check is negative and slow: if mail keeps
arriving from their customers, the exported copies were never addressed. Ask for
the customer list so that becomes actionable rather than merely annoying.
