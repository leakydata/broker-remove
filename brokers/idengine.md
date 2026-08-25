# IDEngine

- **Email:** privacy@idengine.com — **do not send.** The domain publishes a null MX.
- **Method:** none available by email.
- **Domain:** idengine.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-25)
- No letter was ever sent to this address, and none should be.

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
