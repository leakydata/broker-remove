# Pipl

- **Opt-out:** https://pipl.com/personal-information-removal-request
- **Email:** privacy@pipl.com (verified)
- **Method:** web_form — Web form.
- **Domain:** pipl.com
- **Priority: 4.**

## Status

- Current: `confirmed` (updated 2026-09-12)
- Note: Adopted from the shared ledger: another agent recorded 'confirmed' on 2026-09-04. No detail is carried across — re-read the broker's own reply before relying on this.

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

Recorded `not_found` at the time because the negative was real and there was no
basis to dispute it, but see below — the caution turned out to matter.

**A "no profiles" answer is scoped to the consumer-facing product, not to all
personal information the company holds.** If a company sent marketing or service
email to an address, that is direct proof of a broader relationship — account,
billing, support, mailing-list — that a "profile" search will never touch. Check
old newsletters/service mail from the broker itself before accepting a nil at
face value; it's the only external check available.

**A model exchange for how a company should handle being shown its first answer
was incomplete.** Pipl didn't defend the "no profiles" reply — it searched a
different system, found something, disclosed it including the *reason* it
couldn't be deleted (audit retention of disabled accounts) rather than a bare
"not allowed," and confirmed no query logs survive. Worth citing back to other
brokers who give a defensive or partial answer to a challenged nil.

## Verification

Profile index: no public profile page exists, so re-send identifiers in six
months as the only signal. Account-level finding is closed — a permanently
disabled account with no logs and no customer-facing use needs no further check.
