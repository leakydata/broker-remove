# Open People Search

- **Email:** none that works. `info@openpeoplesearch.com` is the only address they
  publish and it hard-bounces.
- **Method:** self-service opt-out at `/Consumer` — no email, no account, no CAPTCHA
- **Domain:** openpeoplesearch.com
- **Operator:** The Open Data People, Inc., PO Box 890370, Temecula, CA
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Opt-out completed with an on-page artifact: **"OPT-OUT SUCCESS! Your data has
  been blocked from future sharing!"** Submitted 5 name variants, 15 Pennsylvania
  addresses, 12 telephone numbers and 12 email addresses.

## Steps

**Skip the email entirely.** The only address published anywhere on the site is
`info@openpeoplesearch.com`, printed in their own privacy policy, and it
hard-bounces with "address not found" — on a domain with healthy Google MX
records. The published contact and the dead contact are the same string.

The working route is self-service and needs nothing from them:

1. `/Consumer` — "Remove My Info". Also linked from the footer of every page and
   from the privacy policy as *"Do No Share or Sell My Personal Information"*.
   Both links go to the same place.
2. **START** → `/Consumer/State`. Choose a state, **CONTINUE**.
3. If the state has no comprehensive privacy law you get an interstitial saying
   so (see Gotchas — it is not a refusal). **GOT IT, CONTINUE**.
4. `/Consumer/OptOut` — a repeatable form: add any number of names, addresses,
   phone numbers and email addresses, each through its own modal.
5. **OPT-OUT MY INFO** → `/Consumer/Confirmed`.

## Gotchas

**The state you pick at step 2 locks the address modal for the whole run.** The
Address modal's State selector contains exactly one option — the state chosen on
the first screen — so a person with addresses in three states cannot enter them
in one pass. Worse, re-entering the flow immediately after a successful
submission would not advance past the state screen at all, which looks like a
one-completion-per-session guard. Addresses in other states need a fresh session
each.

**The modal's State field silently loses its default after the first use, and Add
then fails with no error.** On the first address the selector is pre-filled;
after the first commit it is blank. A blank required field makes the Add button
do nothing — no message, no red outline, the modal just sits there. Four
addresses were typed and lost this way before the cause was visible. **Set State
explicitly on every single address.**

**How to tell whether a row actually committed** — this is the useful trick, and
it generalises to any add-a-row modal:

> After clicking Add, re-open the modal and write the next value. If the tool
> reports the previous field content as **empty**, the modal was freshly opened,
> which means the last one committed. If it reports the **previous item's text**,
> the modal never closed — the last Add silently failed and you are about to
> overwrite it.

That single signal caught two losses in this flow that would otherwise have gone
unnoticed: four names early on, and `225 Buckhout St` later. Reading the
committed table with a text extraction after every few rows is the belt to that
braces, and costs one call.

**Do not batch these without waits.** Rapid-fire click-fill-Add sequences fail
almost every time; the modal needs a beat to close and reopen. Two seconds after
opening, three after Add.

## The jurisdiction interstitial — the honest version

Pennsylvania produces this page:

> *"This state has no applicable data privacy law (Source: International
> Association of Privacy Professionals. If you believe otherwise, let us know!)
> **but you can still Opt-out your information.**"*

This is the same fact that three other people-search sites used to refuse the
request outright (see `_DEFLECTIONS.md` §27), handled the opposite way: stated
plainly, sourced, open to correction, and then set aside. Their opt-out list
offers all fifty states plus DC, Guam and Puerto Rico.

Worth holding onto as the counter-example. "Your state has no privacy law" is a
true statement that does not, on its own, decide anything — and here is a broker
who agrees.

## What their privacy policy admits

Read it before writing to anyone in this family; it is unusually candid.

- **They claim a blanket public-records exemption in five states** — California
  (§1798.140(v)(2)), Virginia, Colorado, Connecticut and Utah — each with the
  same formula: *"All data shared at this website is publicly available
  information and is exempt from [the statute]. However, we recognize that some
  people may still want to remove their information, so we allow them to do so."*
  Note the structure: the right is denied and the remedy is offered anyway, as
  grace rather than obligation. Grace can be withdrawn; take it while it is there.
- **An explicit admission of sale:** *"We have sold information to third parties
  for a business or commercial purpose in the preceding 12 months."*
- **They do not honor Do Not Track**, and say so: *"California law requires that
  we disclose whether we acknowledge 'do not track' signals... We do not do so."*
- Data categories collected include date of birth, employer and occupation, plus
  *"Name of public data source"* and *"Date of record collected"* — meaning
  provenance is recorded per row and could be disclosed on request.

## Verification

Re-run the opt-out search, or search the site for the name. Their confirmation
says *blocked from future sharing*, which is suppression language rather than
one-time deletion — the stronger of the two, and worth testing at the 7-day mark
rather than assuming.
