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
