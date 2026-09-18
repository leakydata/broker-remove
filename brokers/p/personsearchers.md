# PersonSearchers

- **Opt-out:** https://personsearchers.com/optout
- **Email:** support@personsearchers.com (verified)
- **Method:** web_form — Web form.
- **Domain:** personsearchers.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Sent 2026-08-20 07:20 UTC as ONE letter to the eleven optOutLight brands that have not confirmed, citing the five that have. This is the _DEFLECTIONS.md 40 move executed: the four same-template confirmations of 20 August, plus privaterecords on 19 August, quoted verbatim with their dates, and then a single yes/no question a database can answer - 'Was this site included in the removal that was applied for me on those five sites?' Explicitly does NOT ask anyone to confirm corporate structure, which is the thing a support agent cannot answer and which invites escalation to someone who says less. Three exits offered, all of which close the matter: yes (recorded complete), no (apply it now), or an unqualified we-hold-nothing. Plus the suppression-vs-one-time question framed so that 'one-time, we do not suppress' counts as a good answer rather than a refusal, the relatives/associates cross-listing question, and - specific to the inmate/sealed-record/mugshot brands in this group - a request for the SOURCE of any criminal entry whether or not it is removed, since an entry hidden rather than corrected returns on the next ingest.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://personsearchers.com/optout
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `support@personsearchers.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
