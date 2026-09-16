# The privacycompliance.biz family — fourteen brands, one Omaha operator

One compliance portal, `privacycompliance.biz`, runs the consumer opt-out flow for
fourteen brands. We found DatabaseUSA and Infofree the ordinary way, by following
their privacy policies. We found the other twelve by reading the portal's own
navigation menu.

## The brands

| Brand | Non-CA route | Registry? |
|---|---|---|
| AtoZdatabases | `/other-atozdatabases/` | no |
| DatabaseUSA (DBUSA) | `/other-dbusa/` | **yes** |
| HDML | `/other-hdml/` | no |
| Infofree | `/other-infofree/` | **yes** |
| ResearchUSA | `/other-researchusallc/` | **yes** |
| Salesflower | `/other-salesflower/` | no |
| AtoZacademics | — | no |
| DatabaseUSA Gov | — | no |
| EmailUSA | — | no |
| FreeSalesLeads | — | no |
| ListProGuru | — | no |
| NewBusinessListsUSA | — | no |
| NewHomeownerListsUSA | — | no |
| ReferenceGuru | — | no |
| SalesLeads101 | — | no |

"Registry?" is whether the brand appeared in our broker list before this — a list
built from every state data-broker registry plus a commercial removal service's
catalogue. Three of fifteen entries did. Twelve did not exist in it anywhere.

The Omaha connection is on the filings: DatabaseUSA at 11211 John Galt Blvd and
ResearchUSA at 11133 O Street, both Omaha NE 68137. Their mail is on the same
Intermedia Exchange tenant (`exch028.serverdata.net`), which on its own is only a
weak signal — that is a shared host — but here it corroborates evidence that is
already strong.

## The working route

This flow has been completed end to end twice (DatabaseUSA and Infofree, both
2026-08-18). No CAPTCHA, no account.

1. Open `https://privacycompliance.biz/other-<brand>/`. It asks for **email address
   and full name only.**
2. A link arrives from `OptOut@privacycompliance.biz`. It expires — use it promptly.
3. The form that opens has **three separate toggles**: opt-out of sale, delete, and
   disclosure of categories collected. Enabling one does not enable the others.
   Enable all three.
4. Stated timelines: opt-out 15 days, deletion 45 days.

## Do not email the filed addresses

`privacy@databaseusa.com` and `privacy@researchusallc.com` both return
550 "user unknown." These are the addresses in the California registry filings.
Domain and MX are healthy; the mailboxes are not there, so no domain-level check
catches it (`_SILENT_FAILURES.md` §111).

ResearchUSA's 2020 filing also lists `ccpa-optout.com/rsusa/`, which 404s. Of the
three consumer routes it has filed with a regulator over time, one works.

`OptOut@privacycompliance.biz` demonstrably sends mail. Whether it reads incoming
mail is untested — we wrote to it on 2026-08-26.

## The form itself is broken, portal-wide (2026-09-03 → 2026-09-07)

The "Other" (non-covered-state) request page — same Contact Form 7 instance,
id 705, embedded across every brand's page on the site (AtoZdatabases,
DatabaseUSA, DBUSA LLC, DBUSAgov, EmailUSA, Infofree, ResearchUSA, Salesflower,
SalesLeads101, HDML, ListProGuru, AtoZacademics, NewBusinessListsUSA,
NewHomeownerListsUSA, ReferenceGuru, FreeSalesLeads, Marketing.AtoZdatabases —
roughly fifty state-specific pages total) — has failed two different ways in
two tests four days apart:

- **2026-09-03:** the submit button was disabled, gated on an "Disabled! To
  enable, check the acceptance field" message with **no acceptance checkbox
  rendered anywhere on the page** to check. On the HDML and Salesflower pages
  the checkbox existed in the markup but was invisible. Nothing a consumer
  does can submit the form in this state.
- **2026-09-07 retest:** the button now submits, but the send itself fails —
  "There was an error trying to send your message. Please try again later."
  (Contact Form 7's standard mail-transport-failure string, meaning the
  plugin reaches the send step and the mail transport rejects it — likely an
  SMTP credential or From-address problem, not a form-logic bug.) The stale
  "Disabled!" text is still present in the markup with still no checkbox.

**Net effect: no request submitted through the "Other" page on any brand, for
any non-covered-state resident, on either date, has been recorded.** The
`other-infofree` and `other-dbusa` pages are the two known exceptions — both
completed a real email-verification round trip in earlier tests, so whatever
mail configuration those two use still works; it has not been extended (or
has broken) on the rest of the portal.

This was reported directly to the operator (sent to `privacy@researchusallc.com`,
cc `info@databaseusa.com` and `info@infofree.com` — the first bounces, per
above; the cc's do not) with reproduction steps and a request to check the CF7
mail config. Re-test before relying on any brand's "Other" page.

## The eight brands with no route

Eight brands have pages only for California, Colorado, Connecticut, Delaware,
Indiana, Iowa, Maryland, Montana, Utah and Virginia — the states with
comprehensive privacy statutes. For anyone else the URL simply 404s.

That is not a refusal, it is a missing row in a matrix, and it cannot be appealed
because nobody decided it. See `_SILENT_FAILURES.md` §110. The response is to write
to the operator rather than the brand, ask what a non-covered resident is supposed
to do, and ask them to honour the request as company policy if the honest answer is
that nothing exists.

## What to ask for

Compiled-file shape, so the emphasis is suppression rather than deletion — these
files rebuild on a cycle and a clean deletion just means re-acquisition on the next
ingest. Ask for a forward-looking exclude-only entry, for the identifiers searched
to be enumerated, for **modelled** attributes (income, homeownership, age, household
composition, net worth, purchase propensity) to be deleted rather than merely
suppressed from contact, and for upstream suppliers and downstream purchasers to be
named.

Infofree's own page is unusually candid about what the file contains — worth reading
before writing (`infofree.md`). And these are subscription search products, which
means they are export products: by the time a request arrives, subscribers may hold
their own copies, entirely beyond the reach of a deletion at source.
