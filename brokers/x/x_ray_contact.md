# X Ray Contact

- **Opt-out:** https://x-ray.contact/blog/x-ray-contact-privacy-policy-update-account-deletion/
- **Email:** support@x-ray.contact (verified)
- **Method:** unknown — Route not yet established.
- **Domain:** x-ray.contact
- **Priority: 1.**

## Status

- Current: `not_found` (updated 2026-09-22)
- Note: 2026-09-21 reply: "X-Ray Contact does not store, retain, or maintain databases of personal information, nor do we ingest, host, or store address books, user contact cards, or caller-ID records... Our platform functions strictly as an automated, real-time search engine that queries publicly available third-party sources only at the exact moment a user submits an active search request." This is the "we don't store data, we retrieve it from third parties" deflection (see `_DEFLECTIONS.md`) — the correct counter is to ask for suppression at the display layer, since a live query can still surface a result even with nothing stored locally. Replied 2026-09-22 asking (a) which underlying source(s) they query for phone/caller-ID data, so removal can be pursued at the source, and (b) whether an internal display-filter/exclusion list is possible even without a stored record. Recorded as `not_found` for their own systems (a real, well-explained answer) but the upstream-source question is still open — don't treat this as a full resolution of findability.
- Prior (2026-09-17): Emailed support@x-ray.contact 2026-09-17 (they also publish an
  account-deletion page — see below). Contact/caller-ID app; phone-first
  letter, and specifically asked them to check any contact-book/address-book
  ingestion path separately from the main index, since that store is
  populated by a different route (a customer's phone contacts) than a
  supplier feed and a query against the main index won't reach it.

## Steps

1. Email `support@x-ray.contact`, or see the account-deletion page:
   https://x-ray.contact/blog/x-ray-contact-privacy-policy-update-account-deletion/

## Gotchas

- If this product ingests a customer's phone contacts, the subject's data can
  arrive via any correspondent's install — a one-time deletion doesn't stop a
  future re-sync. Ask for a do-not-contribute rule at ingest if a reply
  confirms contact-book ingestion.
- **Claims to store nothing — a live, real-time query against third-party
  sources at search time.** If true, there is no local record to delete, but
  a search still surfaces a result sourced fresh from an upstream provider.
  Ask which upstream source(s) they query and pursue removal there, or ask
  for a display-layer exclusion filter keyed to the identifiers even without
  a stored record.

## Verification

Watch for their answer on the upstream-source question. No public search
surface confirmed.

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
