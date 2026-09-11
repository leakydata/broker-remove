# Salesflower

- **Opt-out:** https://privacycompliance.biz/other-salesflower/
- **Method:** web — 
- **Domain:** salesflower.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-26)
- Note: 2026-08-26: routed to the privacycompliance.biz portal, staged as a handoff. Part of a fourteen-brand family run by one Omaha operator, enumerated from the portal's own navigation menu. Filed registry email for ResearchUSA (privacy@researchusallc.com) hard-bounces 550, as does DatabaseUSA's; the portal is the only working route.

## Steps

**Use the portal, not email.** See `_PRIVACYCOMPLIANCE_FAMILY.md` for the full
picture; the short version:

1. Open `https://privacycompliance.biz/other-salesflower/`. Enter email address and full name.
2. Open the link emailed by `OptOut@privacycompliance.biz`. It expires.
3. Enable **all three** toggles — opt-out of sale, delete, disclosure of categories.
   They are independent.
4. Opt-out lands in 15 days, deletion in 45.

## Gotchas

Salesflower is one of fourteen brands run through a single compliance portal by one
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
