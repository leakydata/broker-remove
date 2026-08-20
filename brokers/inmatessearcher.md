# Inmatessearcher

- **Opt-out:** https://www.inmatessearcher.com/api/helper/optOutLight/search
- **Email:** support@inmatessearcher.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** inmatessearcher.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: SENT 2026-08-20 00:10 UTC as part of ONE consolidated letter to nine addresses covering all sixteen brands on the /api/helper/optOutLight/search platform. The letter names every site, gives the shared URL path as the reason for treating them as one operator, explicitly does NOT ask anyone to confirm corporate structure (only which sites they actioned), and leads with the precedent that privaterecords granted this identical request for this identical person from an email thread on 2026-08-19 without any form. Also carries the five questions none of the family has answered across three exchanges, with the criminal/inmate/sealed-record/mugshot question expanded because three members are branded specifically around that content.

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
