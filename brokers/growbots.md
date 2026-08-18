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

## They publish the deletion trap themselves

`privacy@growbots.com` auto-replies with a Google Form. The form's preamble
contains the clearest statement of `_SILENT_FAILURES.md` §16 anyone has put in
writing:

> *"Please note that if you would like to request deleting all information we may
> have connected to your email, we may not be able to keep a record of your opt-out
> preference and **add information to the database again**."*

Read that plainly: **asking for deletion here makes you re-addable.** The opt-out
keeps your address purely as a suppression key —

> *"we will remove the profile and business information linked to this email from
> our database, keeping the email address for purposes of respecting your opt-out
> preference in the future"*

— which is the correct design, and is exactly what §16 says to ask for. Growbots
have simply built it that way and said so.

**So at this broker, opt-out is the better outcome and deletion is the worse one.**
That inverts the usual advice, and it is only safe to invert because they told you.
Do not generalise it: at a broker that does *not* maintain a persistent suppression
list, deletion is still the stronger request. The lesson is to **read what the
route says before choosing which right to exercise**, not that opt-out is
preferable in general.

Worth keeping as the clean counter-example to `dataaxle.md`, where the interface
makes you pick a right and says nothing about the consequences of the choice.

## They refuse public-domain addresses

> *"Since our product is strictly business-oriented we do not process, in general,
> public domain email addresses such as '@gmail.com' or '@yahoo.com'. For this
> reason please use your professional email here."*

A B2B database, so a consumer address is not a usable key. Submit the work or
university address; here that meant the `.edu` one. If you have no professional
address at all, that is itself worth writing to `privacy@growbots.com` about,
because it means their self-service route cannot serve you.

## The confirmation goes to the address you typed

Submitting the form produces:

> *"We've sent an email to your address. Please open your inbox and click the
> confirmation link in our message to continue with your request."*

**The link goes to the professional address, not to your usual mailbox.** For
anyone running this at arm's length — an assistant with access to one inbox — that
is a hand-off, and an unavoidable one. Without the click nothing happens, and
nothing will say so. See `_SILENT_FAILURES.md` §2.

