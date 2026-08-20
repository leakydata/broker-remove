# Merkle

- **Opt-out:** https://www.merkle.com/en/privacy-policy/data-product-privacy-notice/control-your-personal-information.html
- **Email:** americas.dpo@dentsu.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** dentsu.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Reference: `8N6KVXVA3C`
- Note: Email confirmation clicked; OneTrust returned 'Your email has been confirmed! Your request has been received and will be reviewed by our Privacy Team.' Reference 8N6KVXVA3C on the privacyportal-de (EU) tenant, acknowledged from assessments@dentsu.com. Confirmation page exposes a further direct contact: dpous@merkleinc.com. Dentsu's footer lists the brands this desk covers: iProspect, Carat, dentsu x, dentsu Creative, tag and Merkle.

## Steps

1. Email `americas.dpo@dentsu.com` — the Dentsu Americas DPO desk answers for
   Merkle. A named Data Protection Manager replies, not an autoresponder.
2. The reply redirects to a OneTrust webform and volunteers two commitments worth
   keeping (see below). **Save that email** — it is better evidence of scope than
   anything the form returns.
3. On the form: request type **Delete My Information**, "Yes, myself", brand
   **Merkle**, then name / address / city / state / zip / email.
4. The State control is a OneTrust type-ahead. Click it, type the full state name,
   then click the option in the dropdown; setting the value directly will not
   commit it.
5. Solve the BotDetect image CAPTCHA and submit.
6. **Then watch the inbox.** A confirmation link arrives and must be clicked
   within 3 days or the request is void.

## Gotchas

- **The request-type grid looks multi-select and is single-select.** Clicking a
  second option silently replaces the first, with no visual warning that anything
  was lost. Check `aria-selected` across the group before submitting — exactly one
  should be `true`.
- **The free-text box is mislabelled.** It reads "Correct My Information Request
  Details" no matter which right you selected.
- **Two clocks:** 3 days to click the email confirmation, and the statutory period
  only starts after that.
- **A failed verification does not mean nothing happens** — the form states the
  deletion is converted to a do-not-sell and the submitted identifiers are added
  to their suppression files. Which also means those identifiers are retained
  either way.
- The tenant is the German instance (`privacyportal-de`), so request IDs are not
  interchangeable with the US OneTrust tenant.

## Verification

No public lookup page — this is an identity-resolution and consumer-data business,
so there is nothing to search yourself in.

Verification is documentary, and the two sentences from the DPO's covering email
are the strongest part of the file:

> "It doesn't matter which identifier you enter once you click the link. We will
> find all that matches to you so only submit one form."

> "Selecting Deletion will obviously opt you out of everything and put you on
> suppression."

If a later confirmation is narrower than that — scoped to one email address, or
silent on suppression — quote both lines back and ask which one governs.

## The redirect that came with two commitments worth having (updated 2026-08-19)

Dentsu's Americas DPO answers for Merkle and redirects to a OneTrust webform. An
ordinary form deflection — except the covering note volunteered two things that
are normally extracted only after several rounds:

> "It doesn't matter which identifier you enter once you click the link. **We will
> find all that matches to you** so only submit one form. **Selecting Deletion will
> obviously opt you out of everything and put you on suppression.**"

Both sentences are load-bearing.

> **The first is an identity-resolution commitment.** For an identity-graph
> company, the usual worry is that a deletion keyed to one email leaves every
> other identifier — hashed addresses, MAIDs, cookie and CTV IDs, household
> associations — untouched. This says the match runs the other way: one identifier
> in, everything that resolves to you out. Quote it back if a later confirmation
> looks narrower than that.

> **The second collapses three requests into one.** Deletion here is asserted to
> carry the opt-out *and* a standing suppression entry. That is precisely the
> distinction most confirmations leave ambiguous, stated in advance and in writing.

Get it in writing before submitting, because after submission the only artifact is
a request ID.

### Choose Delete, and then do not touch the other buttons

The request-type control is a grid of seven buttons: Access, Delete, Do Not Share
or Sell, Correct, Limit Use of Sensitive Information, Opt-Out of Targeted
Advertising, Opt-Out of Profiling.

They render as toggles. They behave as a **radio group**.

Selecting Delete and then clicking "Do Not Share or Sell" to be thorough does not
add it — it *replaces* Delete. Do it three more times and the form is submitted as
the narrowest right on the grid, with nothing to indicate anything was lost. The
DOM tells the truth where the styling does not: `aria-selected` is `true` on
exactly one.

> **Before submitting any button-styled option grid, read `aria-selected` across
> the whole group.** Buttons that look like checkboxes and act like radios are
> common in these portals, and "I selected everything I wanted" is the one belief
> the interface will not correct.

Given Merkle's own statement, Delete is the right single choice anyway.

### Two clocks and a downgrade path

The form's own text carries three things worth knowing before you start:

> "If you do not verify your email address within **3 days**, we will not be able
> to complete your request."

> "If Merkle is unable to validate your request to delete, Merkle will **convert
> the deletion request to a do not sell request and will add the personal
> information you have submitted to our suppression files**."

That second one is unusually good faith: a verification failure degrades to an
opt-out plus suppression rather than to nothing. It also means the identifiers you
type are retained either way — worth knowing before deciding how many to give.

A **BotDetect image CAPTCHA** sits above Submit, so the flow stages to the last
click and stops. Fields: request type, self/agent, brand, first, last, address,
address 2, city, state, zip, email, and a free-text box that is labelled
"Correct My Information Request Details" regardless of which right you chose.

The State control is a OneTrust type-ahead — `form_input` will not commit it.
Click, type the full state name, then click the option in the dropdown list.

See [[_SILENT_FAILURES]] and [[_DEFLECTIONS]].
