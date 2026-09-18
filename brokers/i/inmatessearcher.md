# Inmatessearcher

- **Opt-out:** https://www.inmatessearcher.com/api/helper/optOutLight/search
- **Email:** support@inmatessearcher.com (verified — replies from a named agent)
- **Method:** web_form — Web form.
- **Domain:** inmatessearcher.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: 2026-08-20 13:04Z, signed by a named agent: 'From the information you provided, we have removed your information from our database at https://www.inmatessearcher.com'. Sixth optOutLight sibling to confirm. Answered only for its own hostname; the platform-wide yes/no and the suppression-vs-one-time question went unacknowledged rather than refused (see _DEFLECTIONS.md 40).

## Steps

1. Email `support@inmatessearcher.com` with the people-search variant request. This site indexes criminal/inmate records specifically, so the full-record-set language (criminal, court records) is directly on point rather than boilerplate here.
2. No dedicated privacy address found — support inbox is the only published contact.

## Gotchas

- Public-facing criminal-record listings are the most consequential category to get removed — if this one bounces or goes unanswered, prioritize a re-check over lower-stakes ad-tech entries in the same batch.

## Verification

Re-search inmatessearcher.com directly for the profile once a reply arrives. Awaiting reply as of 2026-08-18.

## The CAPTCHA is on the search, not on the removal

Most opt-out flows put the anti-bot check at submission. This one puts it on the
**search**, so you cannot find out whether a listing exists without clearing it.

That changes how the work queues. The usual pattern is "stage everything, hand off
one click at the end". Here the hand-off comes *before anything is known*, and
whoever clears the CAPTCHA then has to carry the rest of the flow themselves --
read the results, pick the listing, submit an address, and reply to the
acknowledgement. Worth saying so in the hand-off note rather than implying it is one
click.

City is required even though the page instructs *"Enter the name and state in the
form below"*. Leaving it blank returns focus to the field and reports nothing.

## Their confirmation is a REPLY, not a click

Their own wording, and unusually explicit:

> *"When you locate your listing, submit your email address to validate your
> ownership of the information. An acknowledgement email will be sent to you
> immediately. Respond to the acknowledgement email to authorize removal of your
> listing. If you do not respond to the email, your listing will NOT be removed."*

Almost every other broker here confirms by clicking a link. A reply is much easier
to leave undone, and someone habituated to the click pattern will open the
acknowledgement, scan for a link, find none, and close it -- having done exactly the
thing that voids the request. Their capitalisation of "NOT" is doing real work.

## Their own definition of a negative

> *"If you are unable to locate your listing then it means your information was
> never collected, or has already been removed."*

Useful, because it is a broker stating **in advance** what an empty result means.
That converts an empty search from an inference into their own stated position, and
it can be recorded as `not_found` on their authority -- with the caveat that it is
scoped to the name, city and state searched, so a listing filed under a former city
would not appear.

## Outcome

Confirmed 2026-08-20 13:04 UTC, signed by a named support agent:

> "From the information you provided, we have removed your information from our
> database at https://www.inmatessearcher.com"

Same template, down to the punctuation, as privaterecords, backgroundcheckers,
mugshotlook, weinform and checksecrets — differing only in brand name and URL.
Six confirmations, one wording, which is the strongest evidence yet that the
sixteen brands run one removal process behind one queue.

**What they did not answer**, and this is the pattern rather than an oversight
(`_DEFLECTIONS.md` §40):

- the yes/no on whether the removal covered the other ten sites on the platform
- whether it is a suppression that survives the next ingest, or a one-time removal
- whether it reaches entries where the subject appears on *another* person's
  profile as a relative or associate
- which source any criminal, inmate or sealed-record entry came from

The reply also pre-blames the requester's browser cache:

> "If your name still appears in our listings, it is possible we were unable to
> distinguish your listing across multiple similar listings ... or your browser
> cache contains stale data."

That sentence does real work for them — it converts a failed removal into a
user-side problem in advance. Verify with a **cold fetch** rather than a browser
session, so the cache explanation cannot apply.

**Citing siblings remains the single most effective technique here.** The letter
that produced this quoted five prior confirmations verbatim with dates, asked one
yes/no question a database can answer, and explicitly declined to ask anyone to
confirm corporate structure. Keep all three of those properties when reusing it.

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
