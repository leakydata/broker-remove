# PeopleSearchNow

- **Working route:** https://www.peoplesearchnow.com/privacy-rights
- **Also:** `/opt-out`, `/do-not-sell`
- **Email: REFUSED.** *"This email address is dedicated to customer service
  inquiries... We do not process privacy requests received via email."*
- **Priority: 3.**

## Status

- Current: `captcha_blocked` (updated 2026-08-18)
- Note: statutory route refused on jurisdiction; the self-service opt-out is
  staged and needs a captcha. See below.


## Third member of the TruePeopleSearch platform family

The refusal email is **word-for-word identical** to TruePeopleSearch's and
FamilyTreeNow's, and `/privacy-rights` presents the same form. Everything in
`brokers/truepeoplesearch.md` applies:

- Select **"Right to Know"**, not "Right to Delete" — Delete renders no form.
- Context: *"I have no direct relationship with the company"*.
- The state dropdown lists **all 50 states including Pennsylvania**, despite the
  preamble implying only "covered" states qualify.

Known family members so far: **TruePeopleSearch, FamilyTreeNow, PeopleSearchNow**.
When a refusal email matches one you have seen before, try the sibling's route
straight away rather than re-deriving it.

## Form-filling notes

The form **collapses back to its initial state** if the top-level category dropdown
loses its value — which hides every field below it and looks like a total reset.
The lower dropdowns usually retain their values in the DOM even when hidden, so
re-selecting only the top dropdown restores the rest rather than requiring a full
refill. Check before retyping everything.

Fill in stages with a screenshot after each, rather than chaining a long batch: a
chained sequence reported success on every step here while the form silently reset.

## Gotchas
- **A Google vignette ad overlay can hijack the page mid-fill and reset every
  field.** It appeared here after the form was fully populated and wiped it. Fill
  quickly, screenshot to verify, and expect to redo it.

## Refused on jurisdiction; the opt-out route is a different door

The statutory "Right to Know" was refused because Pennsylvania has no comprehensive
consumer privacy law -- see `_DEFLECTIONS.md` §27 for the wording and for why
appealing that is a bad trade. The refusal arrived in the same minute, in the same
words, from TruePeopleSearch, FamilyTreeNow and PeopleSearchNow, which is the family
confirmation by itself.

Their self-service opt-out is a **separate mechanism** that never asks what state
you live in. It is an email-link flow: name and email plus a captcha, then a link
that **expires in 24 hours**, then a fuller form where the record details actually
go. Submitting only the first step achieves nothing while looking like progress.
