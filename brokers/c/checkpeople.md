# CheckPeople

- **Email:** support@checkpeople.com  (verified — they reply and act)
- **Phone:** 1-800-267-2122
- **Method:** email, with a follow-up information request
- **Priority: 3.**
- Current: `confirmed` (updated 2026-08-19) — record removed; 48h propagation window; email-search scope still unanswered

## They will ask for a profile link

The first reply is a templated request for:

    First and Last Name / City and State / Street Address / Link to the profile

**One profile per email** — they explicitly refuse combined requests. Find the
profile URL by searching:

    https://checkpeople.com/name/<first>-<last>/in-<ST>/<city>

then take the `VIEW DETAILS` href, which carries a UUID:
`checkpeople.com/name/First-Last/in-ST/City/<uuid>`

## Gotchas
- **Check their stated birth year.** Theirs was off by a year for this record
  (1978 vs an actual [YEAR]). Flag the discrepancy proactively in your reply — left
  unmentioned, an inaccurate field is an easy reason to say the record could not
  be matched.
- The listing is broad: multiple phone numbers, prior addresses in other states,
  named relatives, linked social profiles, an **income estimate** and a
  **relationship-status inference**. Say the request covers the entire record, or
  they may remove only the name and address.
- Ask them to search all your email addresses and report any additional profiles,
  since their one-per-email rule means you need to know how many exist.

## Verification
Re-run the city search URL above after ~7 days and confirm the UUID no longer
resolves.

## Confirmed, and the scope the confirmation quietly narrowed (updated 2026-08-19)

Four days, three exchanges, one removal:

> "We have ensured that your opt-out request has been completed and approved. The
> record listed for `<NAME>` has been successfully removed from our website.
> Please allow 48 hours for the data to be officially removed. We recommend
> clearing your cache and cookies and/or browser history."

Recorded `confirmed`. Two things about how it got there are worth carrying.

### The one-profile-per-email rule does the narrowing

The middle message was not a refusal, it was a form:

> "We need to gather a few extra details to locate the record you are requesting
> to remove. ... First and Last Name / City and State / Street Address / Link to
> the profile. **Please include only one profile per email request.**"

That last sentence is the whole thing. The original letter asked them to search
four email addresses. The reply asked for one profile URL. The confirmation then
came back for **"the record listed for"** that one name — and said nothing about
whether the four addresses surfaced anything else.

> **A confirmation that echoes back the identifier you supplied has confirmed
> exactly that identifier and nothing else.** Read the noun in the confirmation
> sentence: "the record listed for X" is narrower than "your records", which is
> narrower than "any record matching the identifiers you gave us."

So the follow-up is still open: did the four email addresses match anything, and
under variant spellings? That question survives the confirmation.

### The birth-year discrepancy, and why to raise it before they do

The listing carried a birth year one off from the true one. That was flagged
*proactively* in the reply supplying the profile link, with the note that the
record is still the right one.

> **Volunteer known inaccuracies in the broker's own record before asking for
> removal.** An off-by-one date is a ready-made reason to say "we could not match
> your request", and it is much weaker as an objection once you have already named
> it yourself and asserted the record is yours anyway.

### And on "allow 48 hours"

Re-verify after the stated window rather than immediately, and clear cache first —
their own instruction is sound, and a cached page is the commonest cause of a
false `still_listed`.

See [[freepeoplesearch]] for the near-identical flow, and [[_DEFLECTIONS]] on
per-record submission caps.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** CHECKPEOPLE, LLC
- **Registered address:** 111 N Orange Ave STE 800, Orlando, Florida,
  32801
- **Filed contact email:** compliance@checkpeople.com
- **Filed phone:** (561) 461-8439
- **Website:** checkpeople.com

*Source: `data/registries/registry.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://checkpeople.com/opt-out
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `compliance@checkpeople.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
