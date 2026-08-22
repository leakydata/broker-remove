# Leadiq

- **Opt-out:** https://leadiq.com/request-removal
- **Email:** privacy@leadiq.com (verified)
- **Method:** web_form — Web form.
- **Domain:** leadiq.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-08-22) — with two asks still open, see below
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

## Closed by them (2026-08-20)

Kelly followed up, confirming the phone numbers were searched too — the request
that actually mattered here — and got the same negative: *"we have also searched
the phone numbers you provided and have not located a matching record."* She also
clarified LeadIQ **does not hold personal email, DOB, or home address at all** —
not a search-scope limit, a categorical one: *"we do not maintain personal email
addresses from domains such as Gmail, Hotmail... nor do we maintain dates of
birth, home addresses, or other consumer information."*

She then declared the search complete unless a work email, professional phone,
or LinkedIn URL is supplied, and said the ticket would be closed without one.
**Declined the LinkedIn ask again, for the same proportionality reason as
before**, and let the ticket close rather than supply an identifier the database
doesn't currently hold just to manufacture a link.

**Recorded as `not_found`, with the qualifier attached — same shape as
`leadership_connect.md`.** The negative is now genuinely broader (name, phone
numbers, and a category statement that consumer identifiers aren't held at all),
but it is still not a search against a work email or LinkedIn profile, which is
the key this database actually uses. Someone who later has a professional
identifier tied to this person should re-open rather than trust this as final.


## 2026-08-22: they pushed back, and the pushback was correct

LeadIQ answered the follow-up within the hour and corrected my reading of their
first message:

> *"To clarify our previous request, we are not asking you to guess the specific
> email format that may exist in our database. We are asking whether you have any
> other professional/work email addresses associated with you."*

I had built a whole argument on the format half of "a different email address or
format". The address half was the real question. Corrected in
`_DEFLECTIONS.md` §44 rather than quietly edited, because the invented mechanism
was more interesting than the plain one — the §66 failure mode exactly.

What they did confirm, and it is useful:

> *"We do not maintain personal email addresses from domains such as Gmail,
> Hotmail, or similar consumer providers, nor do we maintain dates of birth, home
> addresses, or other consumer information."*

> *"We have also searched the phone numbers you provided and have not located a
> matching record."*

So the phone-first redirect was tried and came back empty, and the consumer
identifier block was genuinely unusable to them. That is a real search, honestly
reported, and the negative is credible.

**The one gap left is `.edu`.** Their sentence sweeps a `.edu` address of mine in with the
Gmail addresses under "consumer providers", which it plainly is not — a
university address is institutional and is exactly what a B2B index keys on.
Asked them to search that one specifically, with a commitment to accept an empty
result without further argument.

**On the LinkedIn URL, they made the honest case:**

> *"This is why we requested your LinkedIn profile—not to create or supplement a
> record, but to conclusively determine whether an existing record belongs to
> you."*

Still declined, and the reason recorded here matters for reuse: having argued in
writing that a profile URL is disproportionate, producing it the moment the
search came back empty would mean the argument was never sincere. The position
taken was conditional — if a candidate record surfaces that needs
disambiguating, that is a different situation. Say that explicitly rather than
simply refusing again.

**Two asks remain unanswered and neither depends on finding a record:** the
do-not-add suppression entry, and the list of upstream suppliers. Both were
restated with an offer to let them close the ticket at the same time.

**Status left at `not_found`** — the search was real and thorough. It flips only
if the `.edu` lookup returns something.
