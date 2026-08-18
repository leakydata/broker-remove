# Foursquare

- **Email:** privacy@foursquare.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** foursquare.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Zendesk request 332742 opened.

## Steps

1. Email `privacy@foursquare.com`.
2. Frame the request as covering **two separate systems**: any consumer app or
   account data, and the location/audience data held about people who never used a
   Foursquare app.
3. Ask for MAIDs, device IDs and hashed emails to be searched.
4. Ask for the location **observations** to be deleted, not the mapping.
5. Ask what identifier they can search on **before** volunteering one.

## Gotchas

**The two-systems framing is the important part of this letter.** Foursquare is
publicly a consumer app, and that is the reading a privacy request will get by
default: someone checks the app databases, finds no account, and answers
truthfully that no record exists.

The data that matters was collected through **partner SDKs embedded in other
companies' apps** and acquired from third parties — from people who never
installed anything of Foursquare's and have no reason to think of them at all. Say
so explicitly, and ask which system held a record. Otherwise the honest answer to
the question they think you asked closes the file.

**Do not open with a device identifier.** If they do not hold one for you,
supplying it creates a new identifier in their system in order to ask them to
delete a record that may not exist. Ask first what they can search on, and whether
any *other* key would re-link a record after a device ID is deleted.

**Observations, not mappings.** A location dataset can delete the row joining a
device ID to a person while keeping every ping that produced the derived home
location — and the derived home location is the address. This is the same
distinction as `factori.md` and `evorra.md`; it is the single most useful question
to ask a location broker.

## Verification

Nothing public to search. Ask the confirmation to name the identifier types
deleted, say whether observations or only mappings were removed, list the
downstream partners notified, and state whether the suppression persists across
ingests from partner SDKs.

## They confirmed the key is a device identifier — which is why not to send one yet

Their reply splits the two rights across two channels and is unusually clear about
the mechanics:

> *"To opt out of the sale or sharing of your personal data, please submit your
> request through our Opt-Out Page. You will need to enter your **Apple IDFA or
> Android Advertising ID** and select your opt-out preferences. **This identifier is
> used only to locate and process your request — not to verify your identity.**"*

Deletion goes through a separate Privacy Portal, which "may request additional
information to verify your identity".

**So the answer to "what can you search on" is: a mobile advertising ID.** That
confirms the shape but leaves the decision open, because the letter asked a second
question they did not answer: *do you hold any **other** key?*

That matters more than it sounds:

- **If they hold no record keyed to your device**, supplying an advertising ID
  hands Foursquare a new identifier for you in order to ask them to delete
  something that may not exist. The request creates the link it was meant to break.
- **If they do**, supply it immediately — there is no downside, since they already
  have it.

One round trip settles which. Ask before fetching the identifier, not after.

## Two questions that decide whether the opt-out is durable

An advertising identifier is **user-resettable**, and on iOS it is zeroed entirely
when app tracking is declined. So an opt-out bound to that string is a weaker thing
than it appears:

  a. **If the identifier is reset, does the opt-out follow?** Or does the reset
     produce a fresh identifier with no suppression attached — leaving the person
     opted in again through an action Apple and Google actively encourage?
  b. **If a device's IDFA is all zeros**, is there a record at all, and under what
     key? It cannot be that one.

Both are asked on the thread. Neither can be answered by a form field, which is the
general lesson: **the portal captures what its fields ask; the substance goes in
the email.**

## What the opt-out page cannot cover

Three asks from the original letter reach neither channel, and were re-put on the
thread:

- whether deletion removes the **location observations** or only the mapping to an
  identifier — a sequence of overnight dwell points identifies a dwelling with no
  name involved at any stage;
- which clients and platforms **received** the data, since an opt-out binding only
  Foursquare leaves live copies wherever an audience was activated;
- whether the suppression **persists across ingests** from partner SDKs.

## They closed the ticket without answering

Fourteen minutes after the follow-up:

> *"We've reviewed your case and can confirm that all available steps and guidance
> were provided based on the information at hand. At this time, there are no
> additional actions we can take on our end."*

Read what that actually says. It is about **steps** — routes for the consumer to
use — and on that narrow point it is true: they did supply the opt-out page and the
Privacy Portal.

But the outstanding items were never requests for steps. They were **questions of
fact about Foursquare's own systems**, which only Foursquare can answer:

- Is there any key other than a mobile advertising identifier?
- Does deletion remove the location observations or only the mapping?
- Does an opt-out survive an advertising-ID reset?
- Which partners received the data?

**This is a soft close, and it is worth recognising as a category.** Nothing was
refused, so there is nothing to appeal; the ticket simply reports completion
against a definition of the request that nobody agreed to. It is more comfortable
for everyone than a refusal and leaves the requester with less.

**The reply that fits:** separate the two explicitly — *these are not steps, they
are questions about your data model* — and then ask for the refusal instead:

> *"If the answer is that Foursquare will not say, I would rather have that in
> writing than have the ticket closed as resolved. A refusal I can read is useful
> to me; a closure that describes unanswered questions as 'guidance provided' is
> not."*

That converts a soft close into either an answer or a documented refusal, and both
are better than a resolved ticket with four open questions inside it.

