# Forddirect

- **Email:** dprivacy@forddirect.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** forddirect.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Automotive. Named the three systems separately - FordDirect's own, records held on behalf of a dealer, and data shared with or from the OEM - since a deletion scoped to one while the others keep a copy is the default outcome unless the request names them. Also asked about VIN/plate/service-history keyed records, connected-vehicle telematics and whether any of it went to an insurer, and lead/enquiry history from third-party providers.

## Steps

1. Email `dprivacy@forddirect.com` — genuinely their published address, despite
   looking like a typo for `privacy@`.
2. Name the **three systems** separately: FordDirect's own records, records held
   on behalf of a dealer, and data shared with or received from the OEM.
3. Ask about VIN, plate and service-history keyed records.
4. Ask about connected-vehicle telematics and whether any went to an insurer.
5. Ask about lead and enquiry history from third-party providers.

## Gotchas

**`dprivacy@forddirect.com` is not a typo.** A near-miss check flagged it as one
character from `privacy@`, and verification against their own site confirmed it is
the address they publish. Worth remembering as the reason never to auto-correct an
odd-looking address — see `_BROKER_FAMILIES.md`.

**Automotive data lives in at least three places and a request usually reaches
one.** The manufacturer, the dealer, and the marketing intermediary each hold a
copy, with data flowing between them. A deletion scoped to whichever system the
responder owns is the default outcome unless the letter names the others, and the
confirmation will not mention the ones that were not searched.

**Search on former addresses.** Automotive marketing records are keyed to the
address a vehicle was registered or serviced at, so anything older than the
current move is filed under a previous address.

**Two categories worth naming explicitly**, because "personal information" will
not obviously reach them:

- **Vehicle-linked records** — VIN, plate, service history, lease or finance
  agreement. Personal information about the person whatever table it sits in.
- **Connected-vehicle telematics** — driving, location, mileage and diagnostic
  data. Ask separately whether it was shared with an **insurer** or an analytics
  partner; that onward flow is the part with real consequences and it is not
  addressed by deleting a marketing record.

## Verification

No public listing. Ask which of the three systems held a record, what the source
was, and which parties it was disclosed to — the disclosure list is the next set
of requests to file.

## Opt-out: free. Deletion: a utility bill.

They processed the **opt-out** straight from the email, with no verification at all:

> *"your request to opt-out of the sale and sharing of your data has been
> processed."*

The **deletion** went to a Mine-hosted webform at
`forddirect.privacy.saymine.io/forddirect`, introduced this way:

> *"Our deletion process requires a verification step. This is an important
> security measure designed to protect your privacy..."*

The verification step turns out to be a **required upload of a copy of your utility
bill**. The form will not submit without it.

**Do not upload it**, and say why rather than simply declining — see
`_DEFLECTIONS.md` §26, which this case produced. The short version:

- The document discloses more than the request removes: name, home address, account
  number, billing history, supplier — into a third-party ticketing system.
- **Their own handling shows it is unnecessary.** The opt-out was processed on the
  strength of an email, for the same person and the same records.
- A utility bill is weak verification anyway: not an identity credential, trivially
  forged, and it proves an *address* rather than a *person*.

Offer proportionate alternatives instead — a code to a listed address, confirming
details they already hold, answering questions about the record — each of which
verifies you against **their** data rather than against a document.

## Their state list is complete, which is worth noting

The form opens with a required **State / Province** selector, and unlike EAB's it
lists **all** states: Pennsylvania is present and accepted. Same control, opposite
design.

Worth recording because it settles what the EAB case only suggested — a restricted
state list is a **choice**, not a technical constraint of the platform or a
necessity of privacy compliance. Two companies, the same field, one of which will
serve a Pennsylvania resident and one of which cannot. See `eab.md`.

## The three systems, still unanswered

The reply addresses FordDirect's own processing and nothing else. The original
letter named three estates — FordDirect, records held on behalf of a **dealer**,
and data shared with or received from **Ford Motor Company** — and asked which held
a record. Re-put on the thread, along with the connected-vehicle question: whether
any telematics or driving data was shared with an insurer or analytics partner.

