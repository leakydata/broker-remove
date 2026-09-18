# IDEngine

- **Email:** privacy@idengine.com — **do not send.** The domain publishes a null MX.
- **Method:** none available by email.
- **Domain:** idengine.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-25)
- Note: 2026-08-25: found by the null-MX sweep, NOT by a bounce - no letter was wasted. idengine.com publishes a lone '0 .' MX record, an explicit RFC 7505 refusal of all mail. IMPORTANT CORRECTION TO EARLIER WORK: this row was one of the five 'repairable typos' I corrected in the domain sweep, changing idengine.ai to idengine.com. The .ai domain did not resolve, so the correction looked right - but it pointed the address at a domain that refuses mail outright. The typo fix was not a fix. Recorded rather than quietly amended, because a correction that produces a dead target is indistinguishable from a correction that worked unless someone checks.

## Why it is unreachable

`idengine.com` publishes a single MX record of priority 0 pointing at the root:

```
idengine.com   MX -> 0 .
```

That is a **null MX** (RFC 7505) — the domain owner stating explicitly, in DNS,
that this domain accepts no mail. A send would be refused at once.

Found by the null-MX sweep rather than by a bounce, so unlike `crawlbee` no
letter was wasted here.

## Gotchas

**The address in this row is the result of an earlier correction that was wrong.**

The registry filing gave `idengine.ai`. That domain did not resolve, so the
domain sweep treated it as a typo and "repaired" it to `idengine.com`. The
correction looked obviously right — same brand, live TLD — and it pointed the
address at a domain that refuses all mail.

Recorded rather than quietly reverted, because a correction that produces a dead
target is indistinguishable from one that worked unless somebody checks. See
`_SILENT_FAILURES.md` §92.

## Steps

Nothing to do by email. If this broker is worth pursuing:

1. Look for a privacy page or web form on any live property under either domain.
2. Check the state registry filings for a **postal** address — a filing that
   gives no working email may still give a real one for mail.
3. Check whether the company was acquired; `scripts/mx_family_scan.py` finds
   parents by shared mail tenant, and `_FAMILIES.md` appendix six explains how.

Do **not** re-add an email route without re-running
`scripts/check_email_domains.py` on the domain first.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** idEngine LLC
- **Registered address:** 1309 Coffeen Avenue STE 5325, Sheridan, WY
- **Filed contact email:** [named individual]@idengine.ai
- **Filed phone:** 858 999 7195
- **Website:** https://idengine.com/

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
