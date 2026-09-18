# Speedeon Data

- **Opt-out:** https://optout.speedeondata.com/
- **Email:** privacy@speedeon.com (privacy function; the registry filing
  lists `accounting@speedeondata.com`, a different domain and the wrong desk)
- **Method:** web_form — Web form.
- **Domain:** speedeondata.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-25)
- Note: 2026-08-25: CONFIRMED, and the best-formed confirmation of the day. Reply came from [named individual]@speedeon.info (note: the registry contact on file is [named individual]@speedeondata.com - a different domain and an accounts mailbox, so they have a working privacy function that the filing does not point at; see SILENT_FAILURES 83). Text: 'We have fulfilled your request to delete/opt-out... we are required by law to maintain a log of your request. Also, we will retain your name and address on our Privacy Suppression file to ensure that we continue to delete your records from any new data files we receive from our vendors.' That last sentence answers UNPROMPTED the question a dozen companies have been asked and few answer straight: the suppression is FORWARD-LOOKING (applied against incoming vendor files, not a one-time clear), it states WHAT is retained and WHY so there is no guessing whether a retained identifier protects or matches, and it explains the request log as a legal requirement rather than leaving an unexplained retention to be discovered later. Worth quoting to other companies as the model wording. ONE SCOPE QUESTION SENT to privacy@speedeon.com (not a dispute, and not about sincerity - see SILENT_FAILURES 99): they describe retaining 'your name and address' SINGULAR while sixteen were supplied. A compiled file is address-history-keyed and incoming vendor records routinely carry a person under an address they left years ago, so a suppression matching only the current address lets exactly those records through. Pre-committed to closing if the answer is that the full history is keyed.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Speedeon Data LLC
- **Registered address:** 5875 Landerbrook Dr., Ste 130, Cleveland, OH,
  44124
- **Filed contact email:** [named individual]@speedeondata.com
- **Filed phone:** 866-647-9219
- **Website:** https://speedeondata.com

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
