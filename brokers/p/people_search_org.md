# People Search Org

- **Opt-out:** https://www.people-search.org/privacy-policy
- **Method:** web_form — Web form.
- **Domain:** people-search.org
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-19)
- Note: No email route exists at all. The registry carried support@peoplesearch.org - note the missing hyphen, a DIFFERENT domain from their actual people-search.org, and the same one-character trap as npi_profile. Neither spelling publishes an MX record, so both would have bounced silently. Their site publishes no address anywhere. The only route is per-record and URL-keyed: 'If you wish to have your information removed from our database, please press the removal request removal button on the record widget' - meaning you must locate your own record page first. That makes it the Lookups.io pattern: acting on the wrong record removes a stranger's listing, so the record must be positively identified before touching it. Queued rather than guessed.

## Steps

1. **Do not try to email them.** There is no address on
   the site and no MX record on the domain. The registry's
   `support@peoplesearch.org` was on a *different domain* — the real site is
   `people-search.org`, with a hyphen — and neither spelling accepts mail.
2. The only route is per-record, from their privacy policy: *"If you wish to have
   your information removed from our database, please press the removal request
   removal button on the record widget."*
3. So: search the site, find the record, press the button on that record.

## Gotchas

**Two traps in one contact string.** `support@peoplesearch.org` differs from
the operating domain by a single hyphen, and neither domain publishes an MX
record. A letter there would have vanished twice over — wrong domain, and no mail
on either. Compare `npi_profile`, where the published address was `npiprofile`
minus one letter. **A contact whose domain does not exactly match the site is a
contact to verify before using, not after.**

**Removal is URL-keyed, so it must not be guessed.** The button lives on a record
page, which means identifying the right record first. On a common name this is
the `lookups_io` problem: press the button on the wrong record and you have
removed a stranger's listing while leaving your own in place. Positively match on
the distinguishing details — an unusual former address, the date of birth — before
acting.

**They are candid about what the site is**, which is useful when writing to
siblings: *"People-Search.org aggregates information from publicly available
sources."* Policy effective September 14 2025, with the standard
continued-use-is-acceptance clause.

**Cloudflare fronts the domain** (A records in the Cloudflare range), so expect
an interstitial. It cleared on its own elsewhere in this project — wait before
concluding the page is blocked.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
