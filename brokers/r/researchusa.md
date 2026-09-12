# ResearchUSA

- **Email:** ~~privacy@researchusallc.com~~ — **hard-bounces 550, do not use.** It is
  the address in their own California registry filing; the mailbox does not exist.
- **Method:** web — the `privacycompliance.biz` portal is the only working route.
- **Opt-out:** https://privacycompliance.biz/other-researchusallc/
- **Domain:** researchusallc.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-09-07)
- Reference: `550 x3: 2026-08-26, 2026-09-03, 2026-09-07`
- Note: THREE SENDS, THREE HARD BOUNCES, TWELVE DAYS. privacy@researchusallc.com -- the address on their California register filing -- returns 550 'address not found' every time: the consumer request on 2026-08-26, the form defect report on 2026-09-03, and the escalation on 2026-09-07. THIS CORRECTS AN EARLIER NOTE OF MINE. The 3 September entry said the portal defect had been 'reported to the one sibling that does have an address (researchusa)'. It had not. The send happened; the delivery did not; the bounce was in the mailbox and went unread. So four days of apparent inaction on their part were four days of nobody knowing -- the same recording-the-send-not-the-receipt error that SILENT_FAILURES 393 catches in the ledger, made here by hand in a note. DIAGNOSIS: researchusallc.com has a live A record and live MX on Intermedia exch028 -- the same mail platform as databaseusa.com, infofree.com and privacycompliance.biz, which confirms one operation behind all four. The domain and its mail infrastructure are healthy. THE MAILBOX SIMPLY DOES NOT EXIST. Compare SILENT_FAILURES 88: a domain-level deliverability check would pass this address; only sending reveals it. WHAT THIS MEANS TOGETHER WITH 406: this family's designated WEB FORM cannot send mail on any page for any brand, and the register-listed EMAIL for this brand has never existed. A consumer following either published route reaches nothing, and neither route reports its own failure back to the company. TODAY'S LETTER DID LAND at the two CC'd addresses, info@databaseusa.com and info@infofree.com, neither of which has bounced -- the first time anything about this defect has reached anyone. Any further correspondence for this brand should go there, not to the register address.

## Steps

**Use the portal, not email.** See `_PRIVACYCOMPLIANCE_FAMILY.md` for the full
picture; the short version:

1. Open `https://privacycompliance.biz/other-researchusallc/`. Enter email address and full name.
2. Open the link emailed by `OptOut@privacycompliance.biz`. It expires.
3. Enable **all three** toggles — opt-out of sale, delete, disclosure of categories.
   They are independent.
4. Opt-out lands in 15 days, deletion in 45.

## Gotchas

ResearchUSA is one of fourteen brands run through a single compliance portal by one
operator in Omaha. A suppression recorded under one brand and not the others is not
a suppression if the underlying file is shared — ask whether it is.

Eight of the fourteen brands have no opt-out page for residents of states without a
comprehensive privacy statute. Not a refusal; the page was never built
(`_SILENT_FAILURES.md` §110).

Do not write to the address in the registry filing. The two we tested in this family
both return 550 while their domains and MX records look perfectly healthy
(`_SILENT_FAILURES.md` §111).

## Verification

Stated timelines are 15 days for the opt-out and 45 for the deletion. The portal
emails a confirmation at submission; keep it, because it is the only receipt.
