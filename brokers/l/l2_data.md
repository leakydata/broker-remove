# L2 Data

- **Opt-out:** https://www.l2-data.com/optout1-667457/
- **Email:** privacyrequests@l2political.com (published on the opt-out page)
- **Method:** email, or a web form behind a CAPTCHA
- **Domain:** l2-data.com (privacy mail on l2political.com)
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: SUPPLEMENT AFTER THREE UNANSWERED LETTERS (20, 25 and 29 Aug to three different published addresses) -- but NOT a chase: new information from a third party that narrows the request to one thing. Also sent to the LABELS & LISTS, INC contact from the register, since that is the registered entity name and the earlier letters may have reached only the trading name. WHAT LEIDOS VOLUNTEERED: 'Leidos Digital Solutions is a reseller of voter data and DOES NOT ITSELF RETAIN THIS DATA which is provided DIRECTLY TO OUR CUSTOMERS FROM L2, INC... WE REPURCHASE VOTER DATA FROM L2 EACH TIME our customers purchase this data from us.' Customers are elected officials and government offices on Intranet Quorum. TWO CONSEQUENCES, BOTH POINTING AT L2 RATHER THAN THE RESELLER: (1) L2 IS THE ONLY PLACE A SUPPRESSION CAN ATTACH -- Leidos retains nothing, the file goes from L2 straight to the customer, so there is no intermediate copy to delete and no intermediate step at which anyone else can exclude me; if L2 does not suppress, NOBODY IN THE CHAIN CAN. (2) THE RE-PURCHASE MODEL DEFEATS A ONE-TIME DELETION BY DESIGN -- data is bought fresh on every order, so a deletion at L2 today is undone the moment their voter file is next rebuilt from state rolls, and the next order exports me again with every step working correctly. SO THE ASK NARROWS TO ONE THING: a STANDING EXCLUSION APPLIED AT EXPORT, checked when a file is generated for a customer and surviving the next rebuild -- not a deletion of today's row. RESTATED THE ORIGINAL DISTINCTION BRIEFLY: not asking them to alter a voter roll, which is a state record maintained for election administration. THE MODELLED LAYER IS A DIFFERENT OBJECT -- partisanship and turnout scores, ETHNICITY AND RELIGION MODELS, income and education estimates, household inferences -- none of which comes from any government record, all computed, and inferences are personal information in their own right under 1798.140(v)(1)(K). A publicly-available exclusion CANNOT REACH A VALUE THE PUBLIC RECORD DOES NOT CONTAIN. Several are also sensitive PI on their face -- 1798.140(ae) names racial/ethnic origin and religious beliefs -- so 1798.121 exercised as a direction rather than a lookup. Asked whether any exclusion covers the MODELLED layer or only the name-and-address row, and which modelled attributes exist, with 1798.106 correction in mind: 'an inference about someone's religion, computed from a surname and a postcode and sold to political campaigns, is a claim about me I have never seen.' SF 193 stated at its sharpest for a voter file -- an address is a household and households turn over -- and SF 256 applied to my own letter: reply only to the correspondence address, the others are search keys.

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

> **Correction (2026-08-25):** A duplicate-detection error in that day's run sent an unnecessary second request to `[named individual]@l2political.com`, on top of the already-open thread documented above. The exclusion check matched only exact addresses seen in a partial Sent-folder scan, and this broker's registry `email_to` had drifted from the address actually used historically — so it looked unsent when it wasn't. No new information was requested; treat the status above as authoritative. **Lesson: check this playbook's own `Current:` status before treating a registry email_to as evidence a broker is unsent — it is not reliable on its own.**
