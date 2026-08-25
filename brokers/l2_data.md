# L2 Data

- **Opt-out:** https://www.l2-data.com/optout1-667457/
- **Email:** privacyrequests@l2political.com (published on the opt-out page)
- **Method:** email, or a web form behind a CAPTCHA
- **Domain:** l2-data.com (privacy mail on l2political.com)
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-20)

## How this broker was found

Not from a broker list. **Sourceit Marketing named L2 Data as one of the
suppliers its email lists came from**, in answer to "if you licensed my
information from a supplier, please tell me which one."

That question is worth asking every reseller, and this is why: a deletion at a
reseller that leaves the record intact upstream is undone on their next ingest.
The supplier disclosure turns a guess into a letter to the source, and in this
case it surfaced a 250-million-record broker that the registry did not contain
at all.

Of the seven suppliers named, five were already tracked, one was LinkedIn (a
platform the subject has an account with, not a broker to write to), and this
one was new.

## Gotchas

**The opt-out page is at a non-guessable path.** It is
`/optout1-667457/`. Meanwhile `/opt-out/`, `/privacy/` and `/privacy-policy/`
all return **404** — and the 404 body is 199 KB of the ordinary site chrome, so
a scraper that only checks for an email address in the response will find
`info@` and `support@` on the 404 page and report success. Nothing about that
response says "wrong URL".

The real page is linked from the homepage as `/optout1-667457/` and carries the
privacy address, a form and a CAPTCHA. Found only by reading the homepage source
for links matching `privacy|opt-?out|ccpa|rights`, which is the general fix:
**never conclude a route is absent from guessed paths returning 404** — harvest
the links the site actually publishes.

**Three product lines, three different arguments.** The site sells voter data,
constituent data, and "more than 250 million national consumer records". Ask
which the subject appears in and make the request cover all three, because a
reply scoped to one is indistinguishable from a complete answer.

**On the voter file, concede the public-record point first.** A state voter file
is genuinely public at source. Asking them to alter a government record invites a
correct refusal. Ask instead that L2 stop republishing, licensing and selling the
registration data, and ask which state or county file it came from and when it
was last refreshed — the source is where a durable fix has to happen.

**The do-not-source entry decides whether any of it lasts.** Their sources are
continuous. Re-ingest the same state file next quarter and today's deletion was a
pause. Ask directly, and pre-accept "we cannot do that" as a useful answer.

**Ask about modelled attributes by name** — partisanship and propensity scores,
ethnicity or religion models, income and household estimates. These are
inferences drawn about a person, are personal information in their own right, and
are what actually gets used. A deletion that clears source fields and leaves the
score is not a deletion.

## Verification

No public person-search page to re-run. Verification is the written answer.
Watch specifically for whether the reply addresses the do-not-source entry or
goes quiet on it, and whether it names which of the three product lines the
record sat in.

> **Correction (2026-08-25):** A duplicate-detection error in that day's run sent an unnecessary second request to `lauren.pembo@l2political.com`, on top of the already-open thread documented above. The exclusion check matched only exact addresses seen in a partial Sent-folder scan, and this broker's registry `email_to` had drifted from the address actually used historically — so it looked unsent when it wasn't. No new information was requested; treat the status above as authoritative. **Lesson: check this playbook's own `Current:` status before treating a registry email_to as evidence a broker is unsent — it is not reliable on its own.**
