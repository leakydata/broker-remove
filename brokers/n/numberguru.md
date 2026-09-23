# NumberGuru

- **Email:** `privacy@numberguru.com` — published in their opt-out FAQ. Better
  than the `support@` the registry originally held.
- **Method:** email, plus a self-service opt-out that removes exactly one record
- **Domain:** numberguru.com
- **Operator:** The NumberGuru LLC
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-09-22)
- Note: 2026-09-22, a person (not the template loop) answered directly: "After searching, we hold no person search result (i.e. person report) corresponding to you. This is a confirmation that we have processed your opt-out request for each phone number, email, and username (public profile) provided. We will suppress the data and not return the requested record(s) in future results." They also confirmed **cross-brand scope explicitly**: "When we process an opt-out request on one brand, it applies to all of our brands. This applies to BeenVerified, MoneyBot5000, NeighborWho, NumberGuru, Ownerly, PeopleLooker, PeopleSmart, and ReversePhone." Treat this as a genuine nil plus forward suppression for all eight family brands — see `beenverified.md`, the sibling thread this reply actually landed on.
- Prior (2026-08-19): Closed the ticket with a customer-satisfaction survey - 'How would you rate our customer service?' - rather than answering any of it. The suppression question, the multiple-records question and the Property Search scope question all went unanswered, and the ticket is now shut. Worth recording as an artifact of the template loop in _DEFLECTIONS 31: the queue does not refuse, it processes, and processing ends in a CSAT request. That loop was eventually broken by a second escalation months later — see 2026-09-22 above. Persistence past the CSAT-close pattern can work.

## Steps

1. Writing to `support@` gets a template pointing at
   `/svc/optout/search/optouts`. That page is worth reading in full before using
   it, because its FAQ documents three limits that the opt-out itself does not
   mention.
2. Write to **`privacy@numberguru.com`** for anything the self-service flow
   cannot do — which, for anyone with more than one address, is most of it.
3. The self-service flow: search for the record, select it, receive a
   verification email, click through, receive a confirmation.

## Gotchas

**The online opt-out removes ONE record, by design.** Their words:

> *"Currently, in order to prevent fraud and protect the integrity of our Do Not
> Sell My Info/Opt-Out process, we only permit you to remove one record from our
> People Search Results through our online Do Not Sell My Info/Opt-Out process."*

And the same FAQ explains why one is rarely enough:

> *"there may be times when we receive a new record about you that is different
> enough from your existing record - for example, containing different spellings,
> initials, combinations of information, and/or addresses - that we cannot match
> this new record to your existing record. In these instances, a separate record
> may be created."*

So the cap bites hardest on exactly the people with the most exposure. A long
address history under several spellings of a name is not an edge case that
produces a second record; it is the ordinary case. **Anyone who uses the online
flow and stops has removed one of several and been told it succeeded.**

**People Search is not the only service.** The opt-out page carries a separate
link for Property Search, and the FAQ concedes the gap directly:

> *"it is possible that your name might appear in search results for the other
> search services available through NumberGuru even after you opt-out of People
> Search."*

Ask for every service by name and ask which ones they searched.

**There is no suppression, and they say so without saying so.** The FAQ invites
you to contact them again each time a new record appears. That is a one-time
removal with the burden of noticing recurrence transferred to the consumer,
permanently, and discharged only by re-checking forever. Ask explicitly for a
do-not-add list, and take a plain "we cannot do that" as a useful answer.

**The opt-out search may not run under automation.** The state selector is a
custom `DIV` widget rather than a real `<select>`, so setting it programmatically
fails and the search submits with nothing. Reported to them as a fault; hand the
flow to a human rather than fighting it.

**Cloudflare challenges the opt-out path but clears itself** in under ten
seconds. Do not read the interstitial as a block — wait and re-read before
concluding anything.

**They publish a Daniel's Law route** at the same `privacy@` address for covered
persons (judges, prosecutors, law enforcement and household family), which asks
for name, DOB, city/state and email rather than a screenshot.

## Verification

Re-run the opt-out search for the name after 24 hours. They warn that browser
caching can make a removed record look present; check in a clean profile.

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
