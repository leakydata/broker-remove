# FamilyTreeNow

- **Working route:** https://www.familytreenow.com/privacy-rights  ← use this
- **Bot-gated:** https://www.familytreenow.com/optout (Cloudflare hangs on load)
- **Email: refused.** support@familytreenow.com replies that privacy requests are
  not processed by email.
- **Priority: 4.** Genealogy angle means relatives and address history are exposed.

## Status

- Current: `submitted` (updated 2026-08-18)
- Reference: `FTN Right to Know ticket`
- Note: STAGE TWO CONFIRMED on-screen: 'Request Successfully Submitted - The following information was submitted to our system successfully... Expect your information to be fully removed in 3 days or less.' Names the record back: 'Submitted: [name] - [PERSONAL], PA [PERSONAL] | [email]'. Sidebar states 'No further action needed'. Same two-doors pattern as TruePeopleSearch.

## Same platform as TruePeopleSearch

FamilyTreeNow and TruePeopleSearch run the same privacy-request system: identical
form structure, identical auto-reply wording, and FamilyTreeNow's footer links to
TruePeopleSearch.com. **The same workaround applies to both** — see
`brokers/truepeoplesearch.md`.

Their confirmation page even leaks an unrendered template variable
("Thank you for sending your Context.Request"), which is a good tell that these
are one codebase.

## Route
`/privacy-rights` → *access, delete, or correct* → **Right to Know** (not Delete —
Delete renders no form) → *no direct relationship* → First/Last/Email/
*subject of this request*/Phone/Street/City/State/Zip → Submit.
Confirms at `privacy/privacyrightsconfirmation?success=True`.

## Gotchas
- Ask separately about **family-tree records**, which expose relatives and address
  history beyond a standard listing.
- State dropdown includes all 50 states — don't be deterred by the "if you live in a
  state with an applicable privacy law" preamble.

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

## The self-service door worked where the statutory one was refused

The Right to Know submission was refused on jurisdiction -- Pennsylvania has no
comprehensive consumer privacy law (see `_DEFLECTIONS.md` §27). The self-service
opt-out, which never asks what state you live in, went through the same afternoon.

The confirmation page is a real artifact rather than a pleasantry, because it **names
the record back**:

> *"The following information was submitted to our system successfully. We will locate
> and remove your record based on the information you provided. Expect your
> information to be fully removed in 3 days or less."*

followed by the submitted name, city, ZIP and email. That distinguishes a completed
submission from a form that merely accepted a POST.

**Three stages, and only the last one counts.** Name and email plus a captcha; then an
emailed link that expires in 24 hours; then the fuller form carrying date of birth,
telephone, address, city, state and ZIP. Stopping after stage one looks like progress
and achieves nothing.

Their own warning explains why completeness matters here: *"If we receive new data
connected to a record that we were unable to identify based on your original request,
information you submit here may appear on our site in the future."* Partial
identifiers buy a removal that does not stick.

## How to verify, and how not to

The confirmation page carries an unusually candid instruction about checking the work:

> *"Please make sure you clear your browser cache before attempting to confirm
> removal, or your device may pull up an old, stored version of our website. Also make
> sure you initiate a new search. Please do not attempt to verify removal by clicking
> on a saved link."*

Fresh search, clean session, live site. See `_SILENT_FAILURES.md` §31 -- a cached page
can report the removal failed when it succeeded, and a stale search-engine result can
report the opposite.
