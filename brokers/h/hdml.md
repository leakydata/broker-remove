# HDML

- **Opt-out:** https://privacycompliance.biz/other-hdml/
- **Method:** web — 
- **Domain:** hdml.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-09-07)
- Reference: `gmail:1a07c938add3710c`
- Note: RETESTED IN A BROWSER 2026-09-07, FOUR DAYS AFTER THE DEFECT WAS REPORTED. STILL BROKEN, AND THE FAILURE HAS MOVED. On 3 September the form refused to submit at all -- 'Disabled! To enable, check the acceptance field', with no acceptance checkbox rendered anywhere on the page. Today the form ACCEPTS the click and attempts the send, and the send fails: 'There was an error trying to send your message. Please try again later.' Movement without progress: somebody touched the submit path, the outcome for the consumer is identical, and the orphaned 'Disabled!' string is still in the markup with still no checkbox to go with it. Filled with a real email, full name and PA selected from the state dropdown before pressing Send, so this is an observed failure rather than an inferred one. THE BLAST RADIUS: Contact Form 7 form id 705 is embedded on EVERY request page on privacycompliance.biz. The site menu lists AtoZdatabases, DatabaseUSA, DBUSA LLC, DBUSAgov, EmailUSA, Infofree, ResearchUSA, Salesflower, SalesLeads101, HDML, ListProGuru, AtoZacademics, NewBusinessListsUSA, NewHomeownerListsUSA, ReferenceGuru and FreeSalesLeads across roughly fifty state-specific pages covering nineteen states plus an 'Other' page. One mail misconfiguration stands between every consumer who reaches any of those pages and the request they came to make. SELF-CONCEALING: the page returns a POLITE ERROR inviting the consumer to try again later, so the natural response is to assume a transient glitch -- which produces no signal on the company's side either. From inside the business, a form that cannot send mail looks exactly like nobody asking. See SILENT_FAILURES 406. ESCALATED 2026-09-07 to privacy@researchusallc.com, copying info@databaseusa.com and info@infofree.com -- the register-listed addresses for three brands in the family, rather than the vendor -- with reproduction steps, the CF7 diagnosis (the error string is CF7's standard mail-send failure, so the plugin reaches the send step and the transport refuses it), and three fixes: check the mail configuration behind form 705; remove or restore the orphaned acceptance text; and point the other brands at the confirmation flow that demonstrably works on other-infofree and other-dbusa. No bad faith alleged and the letter says so. THE CONSUMER REQUEST WAS MADE IN THE SAME LETTER, since the designated route cannot carry it. CREDIT WHERE DUE: the portal publishes an explicit 'Other' page for residents of states with no statute, which is better design than most -- it is just wired to a form that cannot send.

## Steps

**Use the portal, not email.** See `_PRIVACYCOMPLIANCE_FAMILY.md` for the full
picture; the short version:

1. Open `https://privacycompliance.biz/other-hdml/`. Enter email address and full name.
2. Open the link emailed by `OptOut@privacycompliance.biz`. It expires.
3. Enable **all three** toggles — opt-out of sale, delete, disclosure of categories.
   They are independent.
4. Opt-out lands in 15 days, deletion in 45.

## Gotchas

HDML is one of fourteen brands run through a single compliance portal by one
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
