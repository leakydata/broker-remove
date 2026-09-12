# Matchbook

- **Email:** privacy@matchbookdata.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** matchbookdata.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: SF 242 MAID-DENIAL COHORT. Their filing states the denial reason outright, so I wrote as one of the denied and said so. THE ARGUMENT THAT SURVIVES THEIR POSITION BEING TRUE: an opt-out under 1798.120 is A DIRECTION, NOT A LOOKUP, and is expressly not a verifiable consumer request -- the regulations bar requiring identity verification as a condition of honouring one. So when a person they cannot match directs them not to sell, the accurate outcomes are 'we hold no record we can match to you' (a nil result) or 'we have recorded your direction and will apply it if we ever can' (a prospective exclusion). 'DENIED' IS NEITHER, and it is the one that reads as a refusal to the person receiving it. CONCEDED THEIR POSITION IS HONEST AND REASONABLE, because it is: if a device ID is genuinely the only key, a name and address are not searchable against it and they cannot truthfully confirm a deletion they cannot perform. Both sides are telling the truth and the two truths do not meet -- that is the interesting part, and saying so is what makes the letter answerable. MY REFUSAL STATED WITH ITS REASONING rather than as obstinacy: the advertising identifier is the key that makes a person trackable across every app on their phone, so sending it to a location-data company means handing over the exact identifier that makes me findable, to the company I am asking to stop finding me. If they already hold it the disclosure told them nothing; if they do not, I have given them a live identifier they lacked in order to ask them to hold less. No branch favours me and no way to verify afterwards which occurred. THREE ROUTES ASKED FOR THAT REQUIRE NO NEW DISCLOSURE: (1) can they record a PROSPECTIVE exclusion at all -- with 'there is no mechanism by which a person who declines to disclose a device identifier can be excluded from our data' PRE-ACCEPTED as a complete and important answer describing a structural gap rather than a failing; (2) do they honour GLOBAL PRIVACY CONTROL, the only opt-out that carries the direction without carrying an identifier, and which the regulations treat as a valid opt-out request; (3) do they drop or suppress records carrying DEVICE-LEVEL opt-out flags -- platform limit-ad-tracking and DAA AppChoices work from the device outward and can be set without telling them anything. 1798.121 exercised on PRECISE GEOLOCATION where declared -- sensitive PI at 1798.140(ae)(1)(C), and like the opt-out a direction rather than a lookup. REFUSED SOMETHING TOO: not asking them to tell me my own device identifier and would decline it if offered -- a company that could answer that for a stranger supplying only a name and address would be demonstrating something considerably more alarming than the thing I am writing about. || SENT TO OUTLOGIC AND MATCHBOOK IN ONE MESSAGE, and the first question is why: their 2025 filings are IDENTICAL IN EVERY BOX -- delete 26/0/26, know 1/0/1, opt-out 526/171/171/355, mean 3 days, both declaring precise geolocation, same notes sentence. Two separately registered entities, one set of numbers. Asked plainly whether this is ONE DATASET OR TWO, because it matters to a requester: if a consumer writes to one and is denied, have they been denied by both, and if one suppresses an identifier does the other? 'The two share systems and the filings were made from the same report' pre-accepted as a good answer. This is the SF 216 succession-family shape appearing in the metrics rather than in the names.

## Steps

1. Email `privacy@matchbookdata.com` — answers within a minute via Zendesk.
2. Expect the MAID gate. It is not a deflection; it is what they actually hold.
3. Decide the advertising-ID question ONCE across every broker in this category —
   see `_CATEGORY_VARIANTS.md`.
4. Their opt-out form is at `/opt-out-form/`.

## Gotchas

They can only find you by mobile advertising ID, and unlike CityData.AI they will not
tell you whether there was a match. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## The MAID gate, in its weakest form

> *"Matchbook Data and its products only work with advertising identifiers for mobile
> devices and not with personal identifiers such as names, email addresses, telephone
> numbers, etc. Therefore, in order to fulfill your request, you must submit the mobile
> advertising identifiers of your device(s) to us. Without the advertising identifiers,
> we will not be able to process your request to determine if we hold any relevant
> data."*

Third company to say this, after Foursquare and CityData.AI. **This is not a
deflection** — it is a description of what the business actually holds, and it is
useful precisely because it says so plainly.

But it is the **weakest of the three offers**. CityData.AI offered check-then-tell:
hand over the identifier, they hash it, check it, and report whether there was a match.
Matchbook offers nothing back — the identifier is required even to learn whether
anything is held. So the exchange is: disclose a live identifier to a company that may
never have had it, and receive no information in return.

**The resettability of the MAID is what makes this tractable.** Supply once across all
three, let each delete against it, then reset the advertising ID on the device — what
they retain is a dead value. That converts a permanent disclosure into a time-boxed
one, and it argues for deciding the whole category in a single go rather than three
separate times. See `_CATEGORY_VARIANTS.md`.

Ticket reference #187177.
