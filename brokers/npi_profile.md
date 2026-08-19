# NPI Profile

- **Email:** none published anywhere. Contact form only.
- **Method:** web form — an opt-out tool keyed to a 10-digit NPI number
- **Domain:** npiprofile.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-08-19)
- Settled at the source rather than with the broker. No matching record exists in
  the dataset they republish, so there is nothing here to remove.

## Steps

**This one is answerable without writing to them at all**, and that is the
point worth taking away.

Their privacy policy states the scope in one sentence: *"The provider information
displayed on this site comes entirely from the official NPPES public data release
published by the Centers for Medicare & Medicaid Services (CMS) under the Freedom
of Information Act."*

A site that republishes exactly one dataset and nothing else has a checkable
claim. NPPES is the federal NPI registry, it is public, and **it has a free API
with no key**:

    https://npiregistry.cms.hhs.gov/api/?version=2.1&first_name=X&last_name=Y&state=PA

If the subject has no NPPES record, the republisher cannot hold one either. That
is a stronger negative than anything the broker could send back, because it comes
from the authoritative source rather than from a search somebody else ran.

Run it across every state the subject has lived in, and use a `first_name`
wildcard to catch the longer form of a shortened given name.

## Gotchas

**The published contact address was on the wrong domain and could never have
worked.** The registry carried `contact@nprofile.com` — `npiprofile` minus the
`i`. That domain publishes a **null MX record** (`0 .`), which under RFC 7505 is
an explicit declaration that the domain accepts no mail at all. So a letter there
would not have bounced because of a full mailbox or a typo'd local part; it would
have been refused by design, on a domain that is not theirs.

Two separate lessons, both of which look like a working contact in a tracker:
a one-character domain error, and a null MX that a plain "does it resolve" check
reads as healthy.

**The opt-out is keyed to an NPI number, so it must not be guessed.** The tool
takes a 10-digit NPI, shows you the matching record, and removes it. Entering a
number you do not own removes a stranger's listing. The temptation is real here:
the search turned up a similarly-named provider in a city the subject has a prior
address in. Name plus city is not identity. Do not use it.

**They are honest about what an opt-out does and does not reach**, and the
distinction is the right one: *"Opting out removes your profile from our site
only and has no effect on your official government NPI record."* Corrections must
go to NPPES; removal from the republisher is a separate, narrower thing. That is
the same hosting-versus-findability split that applies to every public-record
republisher, stated plainly by the republisher itself.

## Verification

Re-run the NPPES API query. If a record ever appears, the removal route is the
opt-out tool with that record's own NPI — and only then.
