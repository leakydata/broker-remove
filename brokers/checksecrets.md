# Checksecrets

- **Opt-out:** https://www.checksecrets.com/api/helper/optOutLight/search
- **Email:** support@checksecrets.com (verified)
- **Method:** web_form — Web form.
- **Domain:** checksecrets.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: CONFIRMED, 28-36 minutes after the consolidated 16-brand family letter went out: 'From the information you provided, we have removed your information from our database at <this site>.' Identical template to the privaterecords confirmation of 2026-08-19, which the letter had cited as precedent -- so citing a sibling's granted request appears to have worked. Same volunteered common-name hedge: 'it is possible we were unable to distinguish your listing across multiple similar listings, based on the information provided' -- so re-verify rather than closing. Phone support 8am-11pm EST if a listing survives. STILL UNANSWERED by every member: suppression vs one-time, multiple records, related-person entries, criminal/inmate/sealed-record/mugshot entries and their sources, FCRA scoping, and which of the sixteen sites were actioned.

## Steps

1. Email `support@checksecrets.com`. They answer, and helpfully.
2. Expect to be pointed at the self-service search at
   `https://www.checksecrets.com/api/helper/optOutLight/search`.
3. Search your current city. The **first** search of a session carries no CAPTCHA;
   every one after it does.
4. If a listing is found: submit an email address to prove ownership, then
   **reply to the acknowledgement email**. Without that reply nothing is removed.
5. If you have address history, do not run the search once per city — ask in the
   email thread for suppression at the record level, listing every locality at
   once. See `backgroundcheckers.md`, where that is worked through in full.

## Gotchas

**Same operator as BackgroundCheckers.** The two replied to separate requests with
a word-for-word identical support template on the same afternoon — same opening
line, same paragraphs, same closing — and publish the same
`/api/helper/optOutLight/search` endpoint. Two brands, one desk, one codebase.

The practical consequence is that everything learned at the sibling applies here
without re-learning it, and that is worth stating because the reverse is the
usual assumption: two domains, two investigations, two sets of CAPTCHAs. Read
`backgroundcheckers.md` first. The two findings that transfer:

- **Removal is authorised by replying to the acknowledgement email**, not by
  clicking a link. An acknowledgement that reads like a receipt is the thing you
  have to answer.
- **The search is city-scoped but its "no results" message is name-shaped.** An
  empty result answers for one locality while appearing to answer for the person.

Identical templates on the same day is a strong family signal in general — see
`_BROKER_FAMILIES.md`. Where you find one, check whether a request already filed
against the sibling can be extended by reply instead of filed again.

## Verification

Re-run the self-service search per locality, remembering the per-search CAPTCHA
cost, or ask the support thread directly for a written statement of what was
found and removed. The written answer is the better artifact: it is index-wide,
where each search is not.
