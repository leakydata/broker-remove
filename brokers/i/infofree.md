# Infofree

- **Opt-out:** https://privacycompliance.biz/other-infofree/
- **Email:** info@infofree.com — **verified (privacy_policy)**. `privacy@infofree.com` hard-bounces.
- **Method:** web_form — Web form.
- **Domain:** infofree.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: privacy@infofree.com hard-bounced (550). Their site links its privacy route to privacycompliance.biz/other-dbusa/ - a DatabaseUSA portal - so Infofree and DatabaseUSA share an opt-out mechanism. Completed that portal end to end: email+name+state, emailed verification link, then a full form with SEPARATE TOGGLES for opt-out of sale, delete, and disclosure of categories. All three enabled. Stated timelines: opt-out 15 days, deletion 45 days.

## Steps

1. Email `info@infofree.com` (**not** `privacy@infofree.com` — that address hard-bounces with a 550, address not found; `info@` is the only address the site's own privacy policy publishes).
2. Lead with the **export problem** — which subscribers already downloaded the
   record.
3. Ask for permanent suppression, and for do-not-call entries held independently.
4. Ask about sensitive and modelled attributes by name.

## Gotchas

**A subscription search product is an export product.** Customers pay to search and
download; that is the whole service. So by the time a deletion request arrives, the
record may exist in dozens of subscribers' own systems, and those copies are
entirely beyond the reach of a deletion at source. They are also the copies that
produce the call or the mailing.

Ask which subscribers received the record. It is the only route to the rest, only
they have the list, and a company that will not delete downstream should at least
name who holds it.

The rest is the compiled-file shape: permanent suppression rather than deletion
because these files rebuild on a cycle (`dmdatabases_com.md`), do-not-call entries
held independently of the record so that deletion does not remove the protection
(`_SILENT_FAILURES.md` §16), and sensitive or modelled attributes named explicitly
and asked for as **deletions** rather than contact-suppressions
(`_CATEGORY_VARIANTS.md`).

## Verification

No public listing. Ask the confirmation to state separately: the record deleted,
the suppression entry added, the telephone numbers suppressed as standalone
entries, and the subscribers notified. One sentence covering "your request has been
completed" answers none of those individually.

## The bounce found a broker that was not on any list

`privacy@infofree.com` hard-bounced with a 550. `info@infofree.com` is what the
site actually publishes.

But the more useful thing was on the page. Infofree's privacy link points at
**`privacycompliance.biz/other-dbusa/`** — a **DatabaseUSA** portal. So the two
share an opt-out mechanism, and DatabaseUSA was not in any of the source lists
this project started from.

**That is the pattern worth taking away.** A bounce forces you to read the site
properly instead of trusting the registry, and reading the site turns up routes
and relationships a scraped list never had. The failure was productive: it cost
one wasted send and produced a new broker, a working portal, and a documented
family link.

The portal was completed end to end — see `databaseusa.md` for the flow and for
their unusually candid disclosure of what they collect. All three rights were
enabled in one submission: opt-out of sale (15 days), deletion (45 days), and
disclosure of categories.

**Whether that covers Infofree's own file is not established.** A shared portal is
evidence of a shared operator, not proof of a shared database, and nobody will
volunteer that a submission was narrower than you assumed. Worth asking
`info@infofree.com` directly whether the DatabaseUSA submission reaches Infofree's
records, or whether a separate request is needed.

