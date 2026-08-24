# Pipl

- **Opt-out:** https://pipl.com/personal-information-removal-request
- **Email:** privacy@pipl.com (verified)
- **Method:** web_form — Web form.
- **Domain:** pipl.com
- **Priority: 4.**

## Status

- Current: `not_found` (updated 2026-08-24)
- Note: privacy@pipl.com replied 2026-08-21: 'We did not find any profiles in our system that match the data points provided.'

## Steps

1. Email `privacy@pipl.com`. Answered in about 18 hours.
2. Supply every identifier — Pipl is an identifier-to-identity lookup, so the
   email addresses and phone numbers *are* the record keys, not search hints.

## Gotchas

The reply is short and unqualified:

> *"We did not find any profiles in our system that match the data points
> provided."*

**Note what it says and what it does not.** "Data points provided" is correctly
scoped and honestly stated — but it does not address the reverse-lookup question
the letter asked, namely whether each address and number still *resolves* to the
subject in either direction. Nor does it address suppression: a null result today
says nothing about the next index refresh, and Pipl rebuilds from upstream
sources.

Recorded `not_found` because the negative is real and there is no basis to
dispute it. But it is a **point-in-time negative from a continuously rebuilt
index**, which is the weakest kind, and a recheck is worth more here than at a
broker that confirmed a deletion.

## Verification

Re-send the same identifiers in six months. There is no public
profile page, so the only signal is whether the answer changes.
