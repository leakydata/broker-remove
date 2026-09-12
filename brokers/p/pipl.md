# Pipl

- **Opt-out:** https://pipl.com/personal-information-removal-request
- **Email:** privacy@pipl.com (verified)
- **Method:** web_form — Web form.
- **Domain:** pipl.com
- **Priority: 4.**

## Status

- Current: `replied` (updated 2026-08-30)
- Note: PRESSED, AND THEY FOUND IT (SF 255). Pipl's 21 Aug answer was 'we did not find any profiles in our system that match the data points provided' -- true, and the SF 205 shape in its purest form. The follow-up put SPECIFIC evidence rather than general doubt: five of Pipl's own 2018-19 marketing and service emails still in the mailbox, addressed 'Dear API customer', several saying 'Go to your account', one sent from privacy@pipl.com itself. So a commercial relationship existed, with account/billing/ticketing/mailing-list/API-log data attached -- NONE OF WHICH IS A 'PROFILE', which is exactly why a profile search returned nothing while the data existed. Asked them to search beyond the profile index AND TO NAME WHICH SYSTEMS WERE SEARCHED. THEY DID: 'After looking through our INTERNAL (NON-PUBLIC) FACING SYSTEM, we did find an account associated with [the address]. This account had been PERMANENTLY DISABLED, as we no longer allow individuals with no business association to access our data... We cannot remove this account from our internal system, as it's not allowed.' Searched a different system, found the thing, said so, did not defend the first answer, required no proof. Credited strongly. TWO FOLLOW-UPS. (1) 'NOT ALLOWED BY WHAT?' -- asked genuinely, noting 1798.105(d) expressly permits retention to detect security incidents, comply with a legal obligation, or for internal uses aligned with expectations, and that a record kept SO A DISABLED ACCOUNT CANNOT BE SILENTLY RE-ENABLED is squarely the first. If that is the basis it closes the point and I record a LAWFUL RETENTION rather than a refusal -- materially different. 'Not allowed' could mean a statute, a security policy, or simply that the system has no delete function, and those are three different facts. (2) THE ONE THAT IS NOT ABOUT ME: does the retained record include API OR SEARCH QUERY LOGS? A search history at a people-search company is not data about the account holder alone -- IT IS A LIST OF OTHER PEOPLE'S NAMES. Asked for those specifically to be deleted or minimised on two grounds: personal information about me (a record of what I looked at is as revealing as a profile), and personal information about THIRD PARTIES WHO NEVER DEALT WITH PIPL AT ALL, retained for no operational purpose on an account permanently disabled and unusable. 'There are no such logs' accepted as a one-line close. Recorded the profile nil as ITS OWN FINDING rather than folding it into the account result -- for a company whose business is building profiles, 'we have no profile of this person' is genuinely good news -- and re-stated that the exclude-only suppression applies to the profile index precisely because a nil now is not a nil next quarter.

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
