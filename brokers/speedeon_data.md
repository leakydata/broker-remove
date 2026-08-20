# Speedeon Data

- **Opt-out:** https://optout.speedeondata.com/
- **Email:** privacy@speedeondata.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** speedeondata.com
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-08-20)
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
