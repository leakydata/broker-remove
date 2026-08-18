# Governmentregistry Org

- **Opt-out:** https://www.governmentregistry.org/opt-out
- **Email:** privacy@governmentregistry.org (verified)
- **Method:** web_form — Web form.
- **Domain:** governmentregistry.org
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Public-records aggregator. Framed the ask as stopping REPUBLICATION of the name-to-record association rather than altering a government record - the latter invites a reasonable refusal, the former is within their control and is the substance. Plus disclosure and source of any criminal/court entry, suppression vs one-time given the re-ingest cycle, relatives-and-associates listings, and a request to name any sibling site sharing the index.

## Steps

1. Email `privacy@governmentregistry.org`.
2. Frame the request as stopping **republication of the association**, not
   altering a government record.
3. Ask for disclosure and source of any criminal or court entry.
4. Ask suppression versus one-time, given the re-ingest cycle.
5. Ask them to name any sibling site sharing the index.

## Gotchas

**Do not ask a public-records aggregator to delete a public record.** They cannot,
they know they cannot, and the request invites a refusal that sounds entirely
reasonable and then colours everything else in the reply.

What they *can* do — and what actually matters — is stop republishing **your
association with those records in a form that is searchable by name**. Say that is
what you are asking for. It is both more likely to be granted and more useful when
it is, because the harm is not that a court file exists; it is that typing a name
into a search box returns it.

Everything else is the public-records shape covered in `fastbackgroundcheck.md`
and `courtrecords_us.md`: disclosure and source before deletion on anything
criminal or court-derived, suppression rather than one-time removal because source
data is re-ingested on a cycle, and relatives-and-associates listings, which a
profile-scoped deletion leaves untouched.

Ask them to name sibling properties. A `.org` records site is often one skin over
an index shared with several others, and `family_scan.py` finds those only when
they are already in the registry — asking the operator finds the ones that are
not.

## Verification

Re-run the public search on the name and on **each** former address. Then check a
relative's listing for the subject's name in the related-persons block. Re-check
after a source refresh if the reply confirmed deletion but not suppression.
