# Pacificeast

- **Opt-out:** https://www.pacificeast.com/contact-us-privacy/
- **Email:** privacy@pacificeast.com (verified)
- **Method:** web_form — Web form.
- **Domain:** pacificeast.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Identity resolution and contact-data append. Framed around edges rather than rows: phone-to-name, name-to-phone, email-to-anything, and the linkage between current and former numbers and addresses - each independently queryable, so removing one direction leaves the fact retrievable from the other. Also asked for line-type, carrier, portability, connect/disconnect status, subscriber-name verification and any contactability or confidence score, which are personal information that survives a name-and-address deletion. Plus the two standing questions for this category: which identifier types did you match on, and which parts do you hold as a service provider rather than controller.

## Steps

1. Write to `privacy@pacificeast.com` (verified against their
   published page).
2. Frame the request around **edges**, not rows.

## Gotchas

**An append service holds relationships, and each one is separately
queryable.** Ask for removal in every direction the data can be asked for:
phone→name-and-address, name-and-address→phone, email→anything, and the linkage
between current and former numbers and between numbers and former addresses.
Removing one direction leaves the same fact retrievable from the other, and no
confirmation will say which was done.

**Ask for the telephony metadata by name**: line type, carrier, portability,
connect/disconnect status, subscriber-name verification, and any contactability
or confidence score. These are personal information about the subject, they are a
large part of what the product actually sells, and they survive a deletion scoped
to name-and-address.

**Suppression matters more than usual.** An append database is continuously
refreshed from upstream sources; without a standing suppression the record
returns at the next refresh.

Standing questions for the category: which identifier types did you match on, and
which parts are held as a service provider for clients rather than as controller.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
