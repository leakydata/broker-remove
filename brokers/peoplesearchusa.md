# Peoplesearchusa

- **Opt-out:** https://www.peoplesearchusa.org/api/helper/optOutLight/search
- **Email:** support@peoplesearchUSA.org — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** peoplesearchusa.org
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: FAMILY CONFIRMED -- 13 brands, one platform. Evidence is rank-1 (identical non-obvious URL path), because DNS is useless here: all sit on Namecheap's shared dns1/dns2.registrar-servers.com defaults, which is NOT a family signal. What IS conclusive: every one of the 13 serves the same non-obvious opt-out route /api/helper/optOutLight/search (HTTP 200 or 429 under rate limiting, never 404), and five replied within THREE MINUTES of each other with a byte-identical template ('Thank you for taking the time to contact us at <brand>. It's my pleasure to help you out today.') carrying the same no-account line, the same 'if you are unable to locate your listing then it means your information was never collected' definition, and the same reply-to-the-acknowledgement-email requirement. Twelve cluster on three adjacent IPs 146.235.220.52 / .225.48 / .230.19; peoplesearchusa.org sits elsewhere but serves the same path and template. Signers and postal addresses DIFFER per brand (Orlando FL vs Woodland Hills CA), so the fronts are separately presented. Members: backgroundcheckers.net, mugshotlook.com, peoplesearch123.com, peoplesearcher.com, peoplesearchusa.org, personsearchers.com, privaterecords.net, privatereports.com, publicsearcher.com, secretinfo.org, truthrecord.org, truthviewer.com, weinform.org. PRECEDENT TO CITE: privaterecords already CONFIRMED a removal on 2026-08-19, actioned from the email thread without the form.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

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
