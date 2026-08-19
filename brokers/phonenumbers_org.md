# Phonenumbers Org

- **Opt-out:** https://phonenumbers.org/optout/
- **Email:** privacy@privacy.phonenumbers.org — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** privacy.phonenumbers.org
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Reverse phone lookup. Contact is privacy@privacy.phonenumbers.org - a privacy SUBDOMAIN with its own MX (aironmail.webair.com) separate from the apex, which is unusual and worth noting: mail to the apex and mail to the privacy subdomain land in different places, so an address guessed at the apex would not reach this desk. Standard reverse-lookup asks: every prior number, both directions, enrichment fields, suppression-vs-one-time, and stored-index-vs-pass-through.

## Steps

1. Write to **`privacy@privacy.phonenumbers.org`** — note
   the privacy *subdomain*, not the apex.
2. Standard reverse-lookup framing; see `numberguru.md` and `numlookup.md`.

## Gotchas

**The privacy subdomain has its own mail exchanger, separate from the apex.**
`phonenumbers.org` routes to Google; `privacy.phonenumbers.org` routes to
`aironmail.webair.com`. Those are different mail systems, so a plausible-looking
address guessed at the apex — `privacy@phonenumbers.org` — would land somewhere
else entirely, or nowhere.

> Where a broker publishes an address on a subdomain, use the subdomain exactly.
> The extra label is not decoration; it is a different destination.

Otherwise the standard reverse-lookup asks apply: search every prior number, not
the current one; remove the association in both directions; strip carrier,
line-type and location enrichment; suppression versus one-time removal; and
whether the lookup is answered from a stored index or resolved live against a
supplier at query time.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
