# Speedeon Data

- **Opt-out:** https://optout.speedeondata.com/
- **Email:** privacy@speedeon.com (privacy function; the registry filing
  lists `accounting@speedeondata.com`, a different domain and the wrong desk)
- **Method:** web_form — Web form.
- **Domain:** speedeondata.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-25)

### 2026-08-25 — CONFIRMED

Reply from `DoNotReply@speedeon.info`, subject "CCPA Request Processed":

> *"We have fulfilled your request to delete/opt-out. As you have asked to be
> deleted/opted-out please note that we are required by law to maintain a log of
> your request. Also, **we will retain your name and address on our Privacy
> Suppression file to ensure that we continue to delete your records from any new
> data files we receive from our vendors.**"*

The best-formed confirmation received in this project, and worth quoting to other
companies as the model. In three sentences it establishes that the suppression is
**forward-looking** (applied to incoming vendor files, not a one-time clear), says
**what is retained and why** so nobody has to ask which of the two lists it sits
on, and **explains the request log** as a legal requirement rather than leaving an
unexplained retention to be found later.

**Note the contact:** the reply came from `speedeon.info`, while the registry
filing lists `accounting@speedeondata.com` — a different domain and an accounts
mailbox. They run a working privacy function their own filing does not point at.
That is `_SILENT_FAILURES.md` §83 seen from the inside: the letter arrived only
because an accounts mailbox forwarded it.

### Open: the suppression is probably keyed to the current address only

They wrote "your name and address" — **singular**. Sixteen were supplied.

This is not speculation. **Their own form says so:** *"Only one name and address
may be included on this form."* (See the staged-form note below.) So the
suppression entry almost certainly covers **the current address only**, and
nothing else.

That matters because a compiled consumer file is **address-history keyed**, and
incoming vendor records routinely carry a person under an address they left years
ago — precisely the records the suppression exists to catch. A scope question has
been sent to `privacy@speedeon.com` (the confirmation came from a no-reply
address) asking whether the entry covers the full history, with a commitment to
close it if the answer is yes.

**Anyone reusing this playbook: submit the form once per prior address**, or ask
in writing for the full history to be added to one suppression entry. One
submission is not a complete removal here, and their confirmation will not tell
you that.
- Note: Autoreply redirected to optout.speedeondata.com. Form staged with all three boxes ticked. TWO UNUSUALLY HONEST DISCLOSURES ON THE PAGE, both worth quoting: (1) 'To be transparent, the process is largely the same whether you have asked to OPT-OUT or have your information deleted. We will have your name and address added to a suppression file that will ensure, going forward, that your data will not be sold.' -- so deletion here IS suppression, stated plainly, which is the answer most brokers leave ambiguous. (2) 'Speedeon Data does not collect or maintain most categories of Sensitive Data. We do collect data regarding religious affiliation, ethnicity, and self-reported ailment data. If you would like to limit the use of this data, please fill out the form and check the sensitive data checkbox.' -- a named admission that they hold religion, ethnicity and health-adjacent inferences, with an opt-out for it. Ticked. LIMIT: 'Only one name and address may be included on this form' -- so each prior address needs a separate submission. reCAPTCHA handed off.

## Steps

1. Email `privacy@speedeondata.com`. It auto-replies with the form URL, which
   redirects to `optout.speedeondata.com`.
2. **Tick all three boxes**: DELETION, OPT-OUT and **SENSITIVE DATA**. They are not
   alternatives — see Gotchas for why the third one matters.
3. Fill first / last / email / phone / street / city / state / zip. The State
   control is a custom dropdown, not a `<select>`; click it and pick from the list.
4. Solve the reCAPTCHA and submit.
5. **Repeat for each prior address you care about** — the form takes one name and
   address per submission.

## Gotchas

- **One address per form.** *"Only one name and address may be included on this
  form. If you would like information for another name and address combination, you
  will need to complete and provide a separate form."* A single submission covers
  the current address only.
- **Tick SENSITIVE DATA even though it sounds like a niche extra.** They state
  plainly what falls under it, and it is not niche: *"We do collect data regarding
  religious affiliation, ethnicity, and self-reported ailment data."*
- The State field is a custom button-and-list widget with no `<select>` element, so
  setting a value directly does nothing — it needs a click on the option.
- The life-event trigger products (new mover, new parent, new homeowner) are not
  mentioned anywhere on the opt-out form. Raise those by email if you want them
  addressed explicitly.

## Verification

No public lookup — a B2B marketing data compiler, so nothing to search yourself in.

**Their own description of the outcome is the useful artifact**, and it is more
candid than most:

> "To be transparent, the process is largely the same whether you have asked to
> OPT-OUT or have your information deleted. We will have your name and address
> added to a **suppression file** that will ensure, going forward, that your data
> will not be sold."

That answers the suppression-versus-deletion question before it is asked, and it
answers it honestly: what you get is a standing suppression keyed to name and
address, not an erasure. Record it that way rather than as a deletion.

Which also sets the re-check: a suppression keyed to **name + address** is only as
good as the spelling and the address it was filed under, so it is worth repeating
for prior addresses and for name variants.
