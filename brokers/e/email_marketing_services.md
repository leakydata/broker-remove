# Email Marketing Services, INC

- **Email:** jonathan@listmatch.com (verified — the person actually answering)
- **Email fallback (dead):** dataprivacy@listmatch.com (CA registration address) and dataprivacy2026@listmatch.com, which itself started hard-bouncing 2026-09-01 — the year-suffixed alias rotates faster than anyone is tracking it. Write to the person, not the alias.
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** listmatch.co
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-27)
- Reference: `gmail:1a041e3313fd0e4e`
- **Note (2026-08-29):** a separate pass independently found the same original bounce (dataprivacy@listmatch.com) and, not knowing about `dataprivacy2026@listmatch.com` above, guessed `dataprivacy@listmatch.co` instead (same local part, corrected TLD to match the registry's `domain` field) and sent a duplicate letter there. Unconfirmed and superseded by the already-working address above — no action needed unless it also bounces, which would be worth recording as one more dead alias for this company.
- Note: 2026-08-27: first attempt to dataprivacy@listmatch.com (the CA registration address) hard-bounced (550, address not found). Their own privacy page publishes a YEAR-SUFFIXED address, dataprivacy2026@listmatch.com, instead. Resent the full letter there and got an EMS/CCPA auto-reply confirming receipt, which also points to a self-service portal at listmatch.com/privacy/. The letter argues THE JOIN IS THE ASSET: the valuable thing is not a row of attributes but the assertion that this record and that record are the same person, and that assertion survives a deletion aimed at attribute rows. Asked for the linkage and any persistent internal person-ID deleted, not only the fields hanging off it. Also: the match key may be a hash or an internal ID the subject cannot name, so asked them to hash the twelve addresses themselves; and the OUTPUT IS ALREADY ELSEWHERE, since every match performed was delivered to a customer, so asked which customers received a matched record and for categories and period if individual identification is impossible. Plus the standard suppression-hash question - exclude-only or match key.

## Steps

1. Email `dataprivacy2026@listmatch.com`, not the plain `dataprivacy@listmatch.com` on their CA registration — that one is dead.
2. A self-service portal also exists at listmatch.com/privacy/ per their auto-reply, unverified.

**Closed, 2026-08-31.** Follow-up questions to Jonathan (the person actually
answering, at `jonathan@listmatch.com`) got direct answers to both: **the
suppression hash applies across every company he manages, not per-entity**, and
**he manages no other registered entities** — SourceIt (a sibling suppression
hit, same address convention) was the only other one, already accounted for.
He also confirmed the California registration was voluntarily withdrawn ("we
pulled out of California") rather than lapsing, which explains why no current
CA filing shows for this company. Also reported upstream: one of his named
suppliers, `privacy@databaseusa.com`, hard-bounces — worth knowing if he ever
pushes a suppression file that way.

**Correction (2026-09-03):** `dataprivacy2026@listmatch.com`, the address this
playbook and the registry both pointed at, itself hard-bounced on 2026-09-01 —
confirming the gotcha below is not theoretical. The registry `email_to` was
still set to the now-dead alias; repointed it to `jonathan@listmatch.com`
directly, which is a named individual rather than a rotating mailbox and has
proven reliable across several threads.

## Gotchas

- **Year-suffixed address rotates while the state registry keeps the old one.** Same pattern as several other CA-registered brokers: the filed contact address ages out and the site quietly moves to a dated successor (`dataprivacy2026@`) without updating the registration. Worth checking any bounce from a CA-registered broker against the current privacy-policy page before assuming the whole channel is dead.

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
