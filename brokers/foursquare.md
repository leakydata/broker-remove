# Foursquare

- **Email:** privacy@foursquare.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** foursquare.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Location/audience data. Framed as covering BOTH sides: any app/account data, and separately the location data held about people who never used a Foursquare app - collected via partner SDKs and acquired from third parties, which is the part a consumer has no way of knowing about. Asked for observations not just mappings, and declined to volunteer a MAID until they say whether any non-device key could re-link a record.

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
