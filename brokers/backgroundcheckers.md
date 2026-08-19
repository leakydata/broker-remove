# Backgroundcheckers

- **Opt-out:** https://www.backgroundcheckers.net/api/helper/optOutLight/search
- **Email:** support@backgroundcheckers.net (verified)
- **Method:** web_form — Web form.
- **Domain:** backgroundcheckers.net
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Note: Three localities now searched via their self-service tool (current city, one former borough, one former college town): all three returned no results. Their form requires city+state so each answer is locality-scoped. Awaiting written record-level answer to the emailed request covering all eight.

## Steps

1. Email `support@backgroundcheckers.net`. They answer, and answer usefully.
2. They will point you at the self-service search below. Run it for your current
   city — the first search of a session carries no CAPTCHA.
3. From the second search onward you need a person to read a distorted-text
   CAPTCHA. **Do not spend one per former address.** Go back to the email thread
   and ask for suppression at the record level, listing every locality at once.
4. If a listing is found: submit an email address to prove ownership, then
   **reply to the acknowledgement email**. Without that reply nothing is removed.
5. Ask for the outcome in writing. An empty search you ran yourself is not the
   same artifact as "we hold no record" from the operator.

Phone fallback: **(833) 714-0641**, 8am–11pm EST.

**Result so far:** three localities searched — the current city, a former
borough, and a former college town, chosen to span the address history rather
than cluster in one county. All three returned nothing. That is good evidence and
still not an index-wide answer; the written reply is what closes it.

## Gotchas

The CAPTCHA is positioned to make address history expensive: city and state are
both **required** fields, so an index that is address-keyed can only be searched
one locality at a time, and every locality after the first costs a human.
Somebody with eight former addresses pays eight times. The way out is not to
automate around the CAPTCHA — it is to stop using the search and put the list of
localities in an email, where one message covers all of them.

Their "no results" wording is name-shaped — *"unable to find any search results
for <name>"* — but the query was city-scoped. Do not read it as an index-wide
answer. See `_SILENT_FAILURES.md` on results whose phrasing is broader than the
query that produced them.

<!-- Further notes from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## A self-service route, and a second step that is automatable

Support answers email helpfully and points at a removal tool:

> *"If you are unable to remove your listing from
> https://www.backgroundcheckers.net/api/helper/optOutLight/search please call us
> between 8am and 11pm EST"*

The flow they describe is worth quoting in full, because the second step is the
one that gets missed:

> *"When you locate your listing, submit your email address to validate your
> ownership of the information. An acknowledgement email will be sent to you
> immediately. **Respond to the acknowledgement email to authorize removal of your
> listing. If you do not respond to the email, your listing will NOT be
> removed.**"*

Not a link to click — a **reply to send**. Anyone treating the acknowledgement as
a receipt has an unremoved listing and a mailbox that says otherwise. See
`_SILENT_FAILURES.md` §2; this is that trap in an unusual form.

Good news for automation: replying to an email is something a helper with mailbox
access can do unattended. Only the search itself needs a person.

## The CAPTCHA arrives on the second search

The **first** search runs clean. A text-image CAPTCHA — *"Please enter the
characters exactly as shown above"* — appears from the **second** onward. That
matters when you have address history: one city is free, the rest are gated.

Search by `first / last / city / state`, with optional ZIP, phone and email. No
account needed — they say so explicitly:

> *"You do not need to have an account with us to remove your listing."*

## Reading an empty result

> *"If you are unable to locate your listing then it means your information was
> never collected, or has already been removed."*

Useful, and unusually honest. But treat it per-city: a search of the current city
returning nothing says nothing about a former one, and this is a broker whose
index is address-keyed. Work the prior-address list before recording `not_found`.

They also warn that a stale result can be a cache:

> *"you may need to clear your browser cache or try your search a few days later"*

## Same operator as CheckSecrets

CheckSecrets replied to a separate request with a **word-for-word identical**
template on the same afternoon — same opening line, same paragraphs, same closing.
Two brands, one support desk. Expect the same tooling and the same two-step
acknowledgement flow, and treat a lesson learned on one as applying to both.

Phone: **(833) 714-0641**, 8am–11pm EST. Postal address published in Orlando, FL.


## One platform, thirteen brands (updated 2026-08-19)

Five of these sites replied within **three minutes of each other** with a
byte-identical template:

> "Thank you for taking the time to contact us at `<brand>`. It's my pleasure to
> help you out today. ... You do not need to have an account with us to remove your
> listing. If you are unable to locate your listing then it means your information
> was never collected, or has already been removed. ... **Respond to the
> acknowledgement email to authorize removal of your listing. If you do not respond
> to the email, your listing will NOT be removed.**"

### The evidence, and why the usual test was no help

**DNS gave nothing.** All thirteen sit on `dns1`/`dns2.registrar-servers.com` —
Namecheap's shared default, used by every Namecheap customer on earth. Per
[[_BROKER_FAMILIES]], a shared *registrar default* is not a signal at all, and
treating it as one would have produced a confident false positive.

**The URL path settled it.** Every brand serves the same non-obvious route:

    /api/helper/optOutLight/search

Probed across all thirteen: HTTP 200, or 429 under rate limiting — never 404. A
hand-rolled path like `optOutLight` under `/api/helper/` is not a coincidence
between unrelated companies. That is the rank-1 signal, and it carries the case
alone.

**Co-location corroborates.** Twelve cluster on three adjacent addresses —
`146.235.220.52`, `146.235.225.48`, `146.235.230.19`. One sits elsewhere and still
serves the same path and template, which is the useful reminder: shared hosting
supports the finding but is not required by it.

> **When rank 2 is unavailable, rank 1 still decides.** A shared nameserver pair is
> the easiest family signal to collect, but registrar defaults make it useless for
> a whole class of operators. An unusual URL path costs one HEAD request per domain
> and cannot be explained away.

### The thirteen

    backgroundcheckers.net   mugshotlook.com      peoplesearch123.com
    peoplesearcher.com       peoplesearchusa.org  personsearchers.com
    privaterecords.net       privatereports.com   publicsearcher.com
    secretinfo.org           truthrecord.org      truthviewer.com
    weinform.org

**The fronts are separately presented.** Different signer names, different phone
numbers, and genuinely different postal addresses per brand — one in Orlando FL,
another in Woodland Hills CA. Asked directly whether they operate a named sibling,
neither of the two that were asked said yes, or said no. The question was simply
not addressed.

### What to do with that

**Cite the precedent.** `privaterecords.net` **confirmed a removal** on 2026-08-19,
and did it from the email thread without the form — *"From the information you
provided, we have removed your information from our database."*

> **A confirmed removal at one brand is the most useful thing you can put in a
> letter to its siblings.** It is not an accusation, it costs them nothing to
> match, and it makes refusal conspicuous: the same operator, the same platform,
> the same request, already actioned once.

The flow, the caveats and the reply-to-acknowledge trap are identical across all
thirteen — see [[privaterecords]] for the worked example, including the silently
refusing search form ([[_SILENT_FAILURES]] §59).

> **Update 2026-08-19: the family is SIXTEEN, not thirteen.** Mining the A-record
> sweep found `checksecrets.com`, `inmatessearcher.com` and `sealedrecords.net`
> sharing an address with an already-confirmed member, and the path test then held
> for all three. Note that these three are branded around **inmate searches, sealed
> records and mugshots** — so the criminal-record question in the standard letter
> stops being boilerplate for this family. See [[_BROKER_FAMILIES]].
