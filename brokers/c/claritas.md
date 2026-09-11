# Claritas

- **Opt-out:** https://privacyportal.onetrust.com/webform/68582716-6ce4-4f6e-bf08-78371b5f3292/6c7dc52d-0e2b-481f-9256-0755179e3783.html
- **Email:** privacyinfo@claritas.com (verified)
- **Method:** web_form — Web form.
- **Domain:** claritas.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: EVIDENCE OF SUBMISSION: the browser tab that held the staged Claritas OneTrust form was later found on privacyportal.onetrust.com/trust-center-portal/#/verify/success?verificationId=9c1cb809-68fd-4289-a989-bcda9d7166d6 -- a OneTrust verification-success page. So the form was submitted and the email verification link clicked. NO REQUEST ID CAPTURED and no confirmation email seen in the inbox yet; watch for one and record the ID. Downgraded from manual_required to submitted on that basis, but treat as provisional until a broker-issued artifact with an ID arrives.

## Steps

1. Email `privacyinfo@claritas.com`. A named Privacy Office replies within about
   two days and redirects to a OneTrust webform — but **keep the email thread**,
   because it is where the scoping statements below are recorded.
2. Open the webform (also reachable from "Do Not Sell or Share My Personal
   Information" at the foot of their site).
3. Fill name, address 1, city, **state as a two-letter uppercase code**, zip,
   email, phone. All accept normal input.
4. Put the segment/cluster ask and every prior address into the free-text box —
   see "The ask this category needs" below. It is the only place they fit.
5. **Click the request type by hand: "Request to be Deleted from Database".**
   Automation cannot drive this control; see Gotchas.
6. Submit and watch for a confirmation carrying a request ID.

## Gotchas

- **The request-type listbox is inert to synthetic clicks.** `role="option"` divs
  whose `aria-selected` never leaves `"false"`, by ref or by coordinate. No
  selected class appears either. Everything else on the form works normally.
- **A hover tooltip overlays the middle button** and intercepts the pointer. Move
  the cursor away before clicking, and even then expect to click manually.
- **State must be the uppercase two-letter code** — the placeholder says so
  explicitly (`example "OH" for Ohio`).
- Check whether the control allows more than one request type before assuming it
  does; see [[_SILENT_FAILURES]] §49.
- Their own page collapses three rights into one option: sensitive-information
  limitation and correction requests are both **treated as deletions**. Choosing
  Delete loses nothing.

## Verification

No public lookup — this is a B2B segmentation and household-data business, so there
is nothing to search yourself in and the written confirmation is the only evidence.

What to check when it arrives, because a generic OneTrust completion notice will
not address either:

1. Whether the **segment or cluster assignment** was deleted, not just a source
   contact record. That inference is the product.
2. Whether any **address-level** assignment was removed for every prior address
   supplied — a name-keyed deletion leaves an address-keyed classification intact.

If the confirmation is silent on both, reply quoting them. Keep the request ID and
the original email thread together; the thread carries their statement that
correction and sensitive-information requests are treated as deletions.

## The listbox that cannot be clicked (updated 2026-08-19)

Email redirects to a OneTrust webform. Every text field on it fills normally. The
**request-type control does not.**

It is an Angular CDK listbox — `role="option"` `<div>`s, not buttons or inputs:

    <div tabindex="0" role="option" aria-selected="false"
         class="… dsar-webform__label-button text-pointer …"
         aria-label="Request to be Deleted from Database">

`aria-selected` stays `"false"` after a click by element reference, after a click by
computed screen coordinates, and after clicking a second option. No `selected` or
`active` class ever appears. The control is simply inert to synthetic input while
every other field on the same form accepts it.

**A second obstacle sits on top of the first.** A dark hover tooltip — *"If you wish
to have your information removed from Claritas offline marketing database, you may
make your request here"* — renders directly over the middle button and intercepts
the pointer. Moving the cursor away first is necessary but was not sufficient.

> **When one control on a form refuses input and the rest accept it, stop trying
> and hand off that control alone.** Fill everything else, write down exactly which
> element needs a real click and why, and let a human spend three seconds on it. A
> handoff of one click is cheap; a quarter-hour of coordinate arithmetic is not.

Recorded `manual_required` rather than `captcha_blocked` — there is no bot gate
here, just a control that automation cannot drive.

## Which option to choose, in their own words

The page is unusually explicit that **Delete is the superset**, and it is worth
quoting because it removes a judgement call:

> "If you wish Claritas to **limit the use of your sensitive personal
> information**, please select 'request to be deleted.' Claritas will treat a
> request limit your use of sensitive personal information as a request to
> delete."

> "…you may submit a **request to correct** your information by emailing
> privacyinfo@claritas.com. **Claritas will treat correction requests as a request
> to delete.**"

So three distinct rights all collapse into the delete option. Choose *Request to be
Deleted from Database*, and check whether the control permits a second selection
(*Opt Out From Sale of Information*) — see [[_SILENT_FAILURES]] §49 on option grids
that look multi-select and behave otherwise.

## The ask this category needs

Claritas sells geodemographic segmentation, so the request has to name the
inference explicitly or the deletion misses the product:

> **The segment assignment is the personal information.** A cluster placing a
> household in a lifestyle, income, life-stage or behavioural category is an
> inference generated about an identifiable person. It is what is actually licensed
> to clients, and it survives the deletion of a source record.

And the question specific to household data:

> **Does the assignment attach to the address rather than to the name?** If so,
> deleting a name-keyed record while leaving the address classified leaves the
> substance of the profile intact. Ask for the address-level assignment to be
> removed and suppressed too, and supply every prior address — segmentation is
> keyed to the address held at the time of assignment.

Both are in the staged request-details box. See [[_CATEGORY_VARIANTS]].
