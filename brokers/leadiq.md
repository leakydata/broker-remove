# Leadiq

- **Opt-out:** https://leadiq.com/request-removal
- **Email:** privacy@leadiq.com (verified)
- **Method:** web_form — Web form.
- **Domain:** leadiq.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: B2B sales prospecting. Professional identifiers and hashed forms; direct-dial and personal mobile numbers called out as the part with the most immediate effect; which customers captured the record into a CRM or sequencer, since that copy is beyond their deletion and is what produces the calls; re-verification cycle vs persistent suppression; do-not-contact entries outliving the record.

## Steps

1. Email `privacy@leadiq.com`.
2. Search professional identifiers and hashed forms, not consumer ones.
3. Name the **direct-dial and personal mobile numbers** specifically.
4. Ask which customers captured the record into a CRM or sequencer.
5. Ask about re-verification cycles and independent suppression entries.

## Gotchas

Same shape as `hireez.md` and `growbots.md` — a B2B contact database that exists to
be exported, where deleting the source removes the least consequential copy.

**The addition worth making here is the phone numbers.** These products compete on
supplying a **direct dial or a personal mobile**, which is the element with the
most immediate effect on somebody's day: an email can be filtered, a mobile number
rings. Name the numbers explicitly and ask for confirmation of which were held,
rather than trusting "your record has been deleted" to have covered them.

**Re-verification is the suppression question in this category.** Contact databases
periodically re-check and re-enrich records against upstream sources. A deletion
with no persistent suppression entry means the record is rebuilt at the next cycle
— and it will have been deleted exactly as asked.

## Verification

No public listing. Ask the confirmation to name which telephone numbers and email
addresses were held and deleted, whether the suppression survives re-verification,
and which customers hold exported copies.

## What happened (2026-08-20)

Zendesk ticket #275388. Two days after the letter, from "Kelly C":

> *"We're unable to locate any data connected to this email/s. Can you verify if
> it would be under a different email address or format? We can also search
> under your LinkedIn profile URL."*

Followed by a standing paragraph about the business: business contact information
only, "typically found on public professional profiles, business cards, or email
signatures", no sensitive categories.

**The negative is probably honest and almost certainly beside the point.** Eight
personal email addresses were searched. None of them is a work address, and a
prospecting database is indexed on work addresses — a large share of which it
*constructs* from name-and-domain patterns rather than observing. Searching
consumer emails in a B2B index is a real search on the wrong keys, and it returns
a true nothing.

That is the trap in the follow-up question. "Which format is it under" asks the
consumer to reproduce an identifier LeadIQ generated. See `_DEFLECTIONS.md` §44 —
the same structural shape as being asked for a mobile advertising ID.

**The LinkedIn offer was declined, and the reason is worth keeping.** §38 covers
a LinkedIn URL demanded as *verification*. Here it was offered as a *search
convenience*, which is softer and therefore easier to accept without thinking. A
profile URL is a stable, unique, employer-linked key; handing one to a contact
database supplies an identifier it may not hold plus a link between it and every
other identifier in the letter. If no record exists, that search does not test
for a match, it assembles one.

**What was sent back instead:**

1. The structural point about constructed work addresses, stated as a limitation
   rather than a complaint.
2. The proportionality objection to the profile URL, with the reason given.
3. A redirect to the keys already supplied — **telephone numbers first**, since a
   direct dial is keyed to the person and not the employer, and name variants.
4. **The ask that survives a null result:** add name, numbers and addresses to a
   permanent do-not-add suppression entry even if nothing is held today, citing
   SourceIT, which holds SHA-1/SHA-256 hashes purely to prevent re-adding while
   holding no record. A prospecting database is continuously rebuilt from
   suppliers, so "no record today" has a short shelf life.
5. Which upstream suppliers feed the contact database — the SourceIT technique
   (`_SILENT_FAILURES.md` §74), which surfaced a broker no list contained.

**Status stays `submitted`, not `not_found`.** The search was real, it was run on
the wrong keys, and the suppression request is unanswered.
