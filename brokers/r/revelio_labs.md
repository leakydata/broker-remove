# Revelio Labs

- **Email:** info@reveliolabs.com — live, answered by a human, replies within a day
- **Method:** email — statutory request by email. No form, no account, no ID document.
- **Domain:** reveliolabs.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-26)
- Note: 2026-08-26: CONFIRMED AND CLOSED, with five direct answers - two of them uncomfortable and given anyway. (1) Suppression: 'Fully suppressed unless someone changes their professional profile URL and we can't connect it to the old one' - so a STANDING DO-NOT-SOURCE ENTRY IS POSSIBLE and is keyed to the profile URL, which directly validates _SILENT_FAILURES.md 90. (2) Modelled fields: 'We had modeled fields, but we have deleted all of them' - an admission that inferred attributes existed, in answer to a question naming estimated compensation, inferred seniority, inferred gender or ethnicity, and departure-likelihood scores. (3) Sources: 'professional profile sites' - generic where I had asked for named platforms; the one answer that fell short. (4) Downstream: 'No, we cannot enforce downstream deletion.' Flatly stated, which is exactly what I asked for - I had written that I would rather have an uncomfortable accurate answer than a comfortable vague one, and they gave one. (5) Aggregates: 'We fully deleted the individual record; it is no longer contained in aggregates.' They ended with 'we now consider this case fully closed and will not be engaging in further correspondence.' NOT PRESSING. They answered everything asked, including the parts that reflect badly on them. Pressing after that - on the one generic answer - is how you teach a company that answering candidly invites more work. Closed.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Revelio Labs, Inc.
- **Registered address:** 860 BROADWAY FL 5, New York, NY, 10003
- **Filed contact email:** [named individual]@reveliolabs.com
- **Filed phone:** 2014216375
- **Website:** www.reveliolabs.com

*Source: `data/registries/registry.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `[named individual]@reveliolabs.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
