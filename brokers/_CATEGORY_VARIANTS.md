# Tailoring requests by broker category

A generic people-search letter under-asks at companies that aren't people-search.
What "delete my data" means depends on the business model, and naming the right
artifacts makes the request harder to sidestep.

## People search / background reports
Standard letter. Add: cover the *full record set* (criminal, court, property,
relatives), not just the directory listing. Ask that suppression apply to phone,
address and email lookups — **not only name search**, which is how PeopleConnect
scopes theirs.

## Ad tech / audience data  (e.g. 33Across)
Directly identifying records are the small part. Also demand:
- cookie IDs, mobile advertising IDs (MAIDs), and **hashed email identifiers**
- inferred or modelled **audience segments** derived from you
- opt-out of **sharing for cross-context behavioural advertising** specifically
- propagation to downstream DSP / SSP / data partners

Ask them to search **hashed forms** of each address (SHA-256 / MD5 of the
lowercased string) — identifier matching in advertising is routinely done on
hashed email, so a plaintext-only search can miss everything.

## Direct mail / list rental  (e.g. 360 Media Direct)
Ask for deletion **and** permanent internal suppression, and say explicitly that
suppression is not a substitute for deletion. Acknowledge they may need to retain
minimal data to honor suppression — that concession costs nothing and removes
their easiest objection. Cover list partners, brokers, and clients who rented the
file.

## Lead generation  (e.g. 33 Mile Radius)
The sold copies are the problem. Deleting their record does nothing about leads
already delivered. Ask them to **identify the purchasers** and pass the deletion
request downstream.

## Credit / risk data  (e.g. LexisNexis, CoreLogic)
Expect a hard carve-out for FCRA-regulated products; that part genuinely is
exempt. Aim at the public-facing product, and file a separate security freeze
where offered. Don't claim a statute reaches the FCRA side — it invites a blanket
refusal of the whole request.
