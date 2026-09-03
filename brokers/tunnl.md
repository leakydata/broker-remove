# Tunnl

- **Opt-out:** https://privacy.tunnldata.com/
- **Email:** notice@tunnldata.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** tunnldata.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-18)
- **2026-09-03 (§293):** THREE GAPS RAISED 2026-09-03 ON A COMPLETED DELETION (SILENT_FAILURES 292 sweep). The 18 August erasure stands and was exemplary -- Ethyca Privacy Center returned 'Your data has been deleted' about a minute after submission, full cycle under two minutes, no CAPTCHA and no human step. But the notes recorded two limits at the time that were never followed up, and the Choreograph case surfaced a third. (1) THE FORM TAKES ONE ADDRESS AND THERE ARE SIXTEEN. For an audience/household data company the address history IS most of the record, so a single submission covered one address of sixteen and nothing in the flow says so. Asked them to extend the existing erasure to all sixteen under the same ticket, with the standing limit restated: suppress the ASSOCIATION between a former address and me, never the address itself, and if the system can only exclude bare values then leave the former ones alone -- in an audience file a bare-address exclusion removes a stranger's household. (2) THE REQUEST TYPE WAS ERASURE ONLY, NO OPT-OUT -- the portal completes one type per submission. Argued the distinction that matters: a deletion removes what is held today, an opt-out governs what happens next, and
- Note: CONFIRMED REMOVED. Broker-issued email 'Your data has been deleted' / 'Your deletion request has been completed', arriving about one minute after the Ethyca portal submission. Full cycle - form, one-time code, submission, completion - took under two minutes with no human step and no CAPTCHA.

## Steps

1. Email `notice@tunnldata.com` if you like, but expect a redirect. Their
   autoresponder points at the Privacy Center and gives a phone alternative:

   > *"please visit our Privacy Center to submit your request. Alternatively, you
   > may make a Privacy Request by calling our dedicated toll free number at
   > 1-866-498-2784."*

2. Go to `https://privacy.tunnldata.com/`. Two cards: **Access your data** and
   **Delete your data and Opt Out of Data Sale**. Take the second — it is one
   action covering both deletion and opt-out.
3. Fill email, first name, last name, address line 1, city, state, ZIP.
   Phone is optional; **give it in `+1XXXXXXXXXX` form** (see below).
4. Press Continue. A one-time code is emailed immediately.
5. Enter the code and press Submit code. You should land on **"Request
   submitted"** with a green tick.

Corrections go to a different address: `privacy_correction@tunnldata.com`.

## This one runs end to end with no human step

Worth calling out because it is rare. No CAPTCHA anywhere in the flow, and the
only verification is a code emailed to the address you supplied — which anything
with mailbox access can read and enter. Start to finish it is fully automatable,
which makes it the cheapest kind of removal there is.

The Privacy Center is **Ethyca**-powered ("Consent powered by Ethyca" in the
footer). Expect the same flow, and the same automatability, at any other broker
running Ethyca. Recognising the platform is worth more than recognising the
broker — see `_BROKER_FAMILIES.md`.

## Gotchas

**The phone field rejects dashes, silently.** Enter a number in `NNN-NNN-NNNN`
form and the field turns red on submit with no message, no scroll-to-error and no
explanation; the form simply does not advance. `+1NNNNNNNNNN` is accepted. The field is optional,
so the fastest fix is to leave it blank — but a person who does not notice the
red outline will conclude the form is broken and give up, which is the practical
effect of a validation error that does not say anything.

**The form takes one address.** There is a single Address line 1 / City / State /
ZIP block, so a submission asserts one address. If your records span several
addresses, one submission does not obviously cover the others. Either resubmit
per address, or ask on the ticket whether the erasure is person-scoped or
address-scoped — the confirmation does not say, and the difference decides
whether you are finished.

**Deletion is stated to be irreversible:** *"Submitting a request will remove your
data from our internal database. This action cannot be undone."* That is what we
want, but it also means there is no undo if the wrong details are entered — check
before pressing Continue.

Note the scope wording: *"our internal database"*. That says nothing about data
already licensed to clients. Ask separately about downstream recipients; the form
has no field for it.

## Verification

Their success page says only *"A member of our team will review and be in contact
with you shortly"* — a receipt for a submission, not a completion.

**The completion arrived about one minute later**, by email:

> Subject: *"Your data has been deleted"*
> *"Your deletion request has been completed."*

So the whole cycle — form, one-time code, submission, completion — took under two
minutes, with no human step anywhere in it. That is the fastest confirmed removal
in this project by a wide margin, and it is worth understanding why: the request
never touched a person. Where a broker has wired its privacy portal directly to
its deletion pipeline, the removal is as cheap for them as it is for you, and
they have no incentive to make it hard.

Three emails arrive in sequence and only the third is the artifact: the one-time
code, then *"Your privacy request has been received"*, then *"Your data has been
deleted"*. Do not record the second as a confirmation — it is a receipt, and the
distinction is the whole subject of `_SILENT_FAILURES.md`.

Nothing public to search here; Tunnl sells audience data rather than publishing
profiles, so the written confirmation is the only artifact. Chase on the thread
if nothing arrives within their stated statutory period.
