# Growbots

- **Email:** privacy@growbots.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** growbots.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-18)
- Note: Opt-out form submitted for [EMAIL]. THEIR FORM STATES THE TRAP OUTRIGHT: 'if you would like to request deleting all information we may have connected to your email, we may not be able to keep a record of your opt-out preference and add information to the database again.' So at Growbots deletion is the WORSE outcome - the opt-out keeps the address purely as a suppression key, which is the correct design. They also refuse gmail/yahoo and require a professional address. Confirmation link goes to the psu.edu mailbox, which I cannot read - handed off.

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


## 2026-08-20: the confirmation address died with the affiliation

The opt-out submitted on the institutional address can never be confirmed — that
mailbox is closed; the requester has left the institution. The request is
submitted, permanently unverifiable, and from Growbots' side indistinguishable
from an abandoned one.

**This is a design fault, not bad luck, and it is worth stating in the letter.**
Two individually sensible rules combine into a dead end:

1. *Refuse public-domain addresses,* because a gmail address does not identify a
   person in a B2B contact database. Reasonable.
2. *Send the confirmation link to the address entered.* Also reasonable.

Together they can only be satisfied by someone who still controls the
professional mailbox the record was built around — which excludes exactly the
people most likely to want out. A stale B2B record is stale *because* the role
ended. The population the form cannot serve is the population it most needs to.

The fix costs a field: key the suppression to the professional address, send the
confirmation to a separate contact address the requester nominates. The
identifier and the proof-of-reachability do not have to be the same string.

**Reopened by email to `privacy@growbots.com`**, asking them to honour the
submitted opt-out without the confirmation, or re-issue it to a readable
address, and to suppress the personal address, name and telephone number as
well so a supplier ingest under different details is also caught.

**Still asking for opt-out and not deletion**, deliberately, for the reason
their own form gives — deletion would destroy the record of the opt-out
preference and permit re-adding. That remains the right call and it did not
change with the mailbox.

## Handoff item closed

Removed from the human queue. No click can rescue it, so leaving it there would
have been a permanent no-op sitting in a list of things a person is asked to do.

## 2026-08-21: routed through their own "other privacy rights" channel

privacy@growbots.com auto-replied again pointing at the Google Form for opt-out,
but also named a second route for anything else: `customers@growbots.com`, with
name, jurisdiction and request in the body. Used that instead of the form (which
this project cannot complete without a browser) to ask them to either honor the
already-submitted opt-out without the dead-mailbox confirmation, or re-issue the
confirmation to a reachable address. Framed it as opt-out/suppression, not
deletion — consistent with the earlier finding that deletion is the worse
outcome here.
