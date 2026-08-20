# Mugshotlook

- **Opt-out:** https://www.mugshotlook.com/api/helper/optOutLight/search
- **Email:** support@mugshotlook.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** mugshotlook.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: CONFIRMED, 28-36 minutes after the consolidated 16-brand family letter went out: 'From the information you provided, we have removed your information from our database at <this site>.' Identical template to the privaterecords confirmation of 2026-08-19, which the letter had cited as precedent -- so citing a sibling's granted request appears to have worked. Same volunteered common-name hedge: 'it is possible we were unable to distinguish your listing across multiple similar listings, based on the information provided' -- so re-verify rather than closing. Phone support 8am-11pm EST if a listing survives. STILL UNANSWERED by every member: suppression vs one-time, multiple records, related-person entries, criminal/inmate/sealed-record/mugshot entries and their sources, FCRA scoping, and which of the sixteen sites were actioned.

## Steps

1. Email `support@mugshotlook.com`. You get a template reply within minutes — the
   SAME template InmatesSearcher sends. It will not answer your questions.
2. Opt-out is at `/api/helper/optOutLight/search` — first name, last name, city
   (required) and state. A text-image CAPTCHA blocks the SEARCH itself.
3. Submit an email address against the listing, then **REPLY** to the
   acknowledgement email. Clicking is not enough and there is nothing to click.
4. Fallback if the web route fails: they offer a phone line, 8am–11pm EST.

## Gotchas

Same operator as InmatesSearcher, same flow, same reply-not-click confirmation — and
the template answers none of the questions actually asked. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Same operator as InmatesSearcher

The reply is **word for word** the one InmatesSearcher sends: *"It's my pleasure to help
you out today"*, the reply-to-confirm instruction with **NOT** capitalised, the
browser-cache advice, and the closing line that *"all information contained in our
database is public information, so you may need to perform a similar action with other
non-affiliated data providers also"*. Only the signature name, the street address
(Woodland Hills rather than Glendale) and the telephone number differ.

The decisive tell is not the template but the URL: both brands run their opt-out at
`/api/helper/optOutLight/search`. Nobody white-labels an internal API helper route. See
`_BROKER_FAMILIES.md`.

## The template does not answer the letter

The request asked two specific things — is the opt-out a **standing suppression** applied
to future booking feeds, and is **de-indexing** available if deletion is refused. The
reply addresses neither. It is dispatched on receipt, not written in response.

**Read that as a property of the desk, not a refusal.** There is no point re-arguing the
same points into the same template; the useful moves are the self-service flow, and the
telephone line they volunteer for when it fails.

## The flow's own hazards, inherited from the sibling

  - the **CAPTCHA is on the search**, so you cannot even learn whether a listing exists
    without a human clearing it;
  - **city is required** despite the instructions implying name and state suffice;
  - the confirmation is a **REPLY**, not a click — *"If you do not respond to the email,
    your listing will NOT be removed"*;
  - their cache advice is real: verify with a fresh search in a clean session, never a
    saved link. See `_SILENT_FAILURES.md` §31.

Their stated definition of a negative is also worth keeping: *"If you are unable to
locate your listing then it means your information was never collected, or has already
been removed."*


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
