# Factori

- **Email:** privacy@factori.ai (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** factori.ai
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Mobile location/device data. Asked for MAIDs, device IDs and hashed emails; for the location OBSERVATIONS themselves (lat/long, dwell points, visits, derived home/work) rather than just the mapping; and for derived segments. Declined to volunteer a device identifier until they answer whether any non-device key could re-link a record - would rather not hand a new identifier to a company that may not hold one.

## Steps

1. Email `privacy@factori.ai`.
2. Ask for MAIDs (IDFA/AAID), device identifiers and hashed emails to be searched
   — the plaintext identifiers are almost certainly not the key.
3. Ask for the **location observations themselves** to be deleted, not the
   mapping to an identifier.
4. Ask what identifier they can search on **before** volunteering one.

## Gotchas

**Do not hand over a device identifier in the opening letter.** The instinct is to
supply the key that will find the record, and for a location-data business that
key is a mobile advertising ID. But if they do not currently hold one for you,
supplying it creates a new identifier in their system in order to ask them to
delete a record that may not exist.

Ask first: *what identifier can you search on, and do you hold any other key —
hashed email, IP-derived household, or an identifier derived from location
patterns — under which a record could be located or re-linked after a device
identifier is deleted?* Then decide. That ordering costs one round trip and is the
right way round.

**The observation/mapping distinction is the substance here.** A location dataset
can delete the row joining a device ID to a person while keeping every
latitude/longitude ping that produced the derived home location — and the derived
home location *is* the address. Ask explicitly which was deleted.

Location history is the category where "reasonably linkable" does most work: a
sequence of overnight dwell points identifies a dwelling, and a dwelling
identifies a household, with no name required at any stage. See
`_CATEGORY_VARIANTS.md`.

## Verification

Nothing public to search. Ask the confirmation to name the identifier types
deleted, state whether observations or only mappings were removed, and list the
clients notified.
