# FamilyTreeNow

- **Working route:** https://www.familytreenow.com/privacy-rights  ← use this
- **Bot-gated:** https://www.familytreenow.com/optout (Cloudflare hangs on load)
- **Email: refused.** support@familytreenow.com replies that privacy requests are
  not processed by email.
- **Priority: 4.** Genealogy angle means relatives and address history are exposed.

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
