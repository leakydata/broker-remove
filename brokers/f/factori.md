# Factori

- **Email:** privacy@factori.ai (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** factori.ai
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Auto-acknowledged; they state a deletion request has been noted.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Factori Technologies LLC
- **Registered address:** 8th Green STE A, Dover, DE
- **Filed contact email:** privacy@factori.ai
- **Website:** https://www.factori.ai

*Source: `data/registries/registry2024.csv`.*

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
