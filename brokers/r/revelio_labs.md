# Revelio Labs

- **Email:** info@reveliolabs.com — live, answered by a human, replies within a day
- **Method:** email — statutory request by email. No form, no account, no ID document.
- **Domain:** reveliolabs.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Disclosure received. **Deletion not yet confirmed.**

## What happened

Three exchanges over two days.

**1. The request.** Workforce-intelligence framing: no relationship exists, so any
record they hold was compiled. Asked for disclosure *before* deletion, on the
ground that an inaccurate employment or compensation record circulating to
investors and employers does real harm and deleting it unseen removes the only
chance to correct it.

**2. The verification demand.**

> "Our records include many individuals with the same name as the person
> referenced in your request. Under the CPRA, if there are reasonable doubts about
> the identity of the person making the request, additional information may be
> requested.
>
> Please provide this person's LinkedIn URL. If this individual does not have the
> LinkedIn URL, please provide the names of this individuals' last 3 employers."

Reasonable in kind — the name is common and the dataset is keyed to employment —
and it asks for personal information the company does not yet have.

**3. They dropped it and sent the data.**

> "Please find the raw data we hold attached."

Four CSV files. No LinkedIn URL and no employment history were supplied.

## Gotchas

**What made them drop it** is set out in `_DEFLECTIONS.md` §38. In short: concede
that the demand is reasonable in kind, then make the narrow statutory point —
CPRA verification information must be *necessary*, and the business should not
collect more personal information than the purpose requires — and, critically,
**hand over a better identifier than the one being demanded.** Here that was the
twelve email addresses already supplied, with a specific argument for the `.edu`
one: a university address in a standard institutional format is both a likelier
join key for a workforce dataset and far less likely to collide with a different
person of the same name than current webmail.

A proportionality objection with nothing behind it is just a refusal to verify.
One that supplies a sharper identifier leaves nothing to argue about.

**Refuse the LinkedIn URL separately from the employer question.** They are not
the same ask. A profile URL is a live, third-party, continuously-updated
identifier that would let a workforce-data company join the request to a public
profile and enrich from it — which is adjacent to the product itself. Say that;
it is a specific objection, not a general reluctance.

**Offer the fallback genuinely.** The reply agreed to provide employer names if
the email search came back empty, conditional on written confirmation that they
would be used solely to locate and delete, deleted if no match was found rather
than kept as a "requested but not found" log row, and that the request would stay
a deletion rather than being converted to access-only. Offering it is what made
the refusal credible. It never had to be honoured.

**Ask for the schema in the same breath as the data.** The export arrived as
`data_1.csv` through `data_4.csv` with no column dictionary. For a workforce
record the whole question is which fields are *sourced* and which are *modelled* —
estimated compensation, inferred seniority, inferred gender or ethnicity,
departure-likelihood scores — and a raw table does not distinguish them. Requested
after the fact; should have been requested up front.

**Disclosure is not deletion.** They answered the first half of "disclose then
delete". Replied asking them to proceed with deletion, opt-out, and a standing
do-not-source entry, and re-asking the four questions that never depended on
identification: inferred attributes, sources, downstream licensee retention, and
whether individual-level records persist where only aggregates are sold.

**The do-not-source entry is the one that decides whether any of it lasts.**
Sourcing here is continuous. If the name reappears on a professional network next
month and a new record is built, today's deletion was a pause.

## Verification

The CSVs need a human to read them — check whether the employment history is
accurate, and whether modelled fields are present. That is queued as a handoff.
Deletion is unconfirmed until they say so in writing; watch for whether the reply
addresses the do-not-source entry or goes quiet on it.
