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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Pipl, Inc.
- **Trading as:** Pipl
- **Registered address:** 510 S. Clearwater Loop, Suite 100, Post Falls,
  ID
- **Filed contact email:** legal@pipl.com
- **Website:** https://www.pipl.com

*Source: `data/registries/registry2024.csv`.*

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
