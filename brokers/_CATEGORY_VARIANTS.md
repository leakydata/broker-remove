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

## Transaction / purchase data  (e.g. Affinity Solutions)
Sourced from financial institution partners. Ask for transaction records,
merchant-level purchase history, spend categories, **and derived segments**. Also
ask **which financial institutions supplied the data** — that names the upstream
relationship you may not know exists.

## Identity / wealth graphs  (e.g. Aidentified)
Sold to financial services. The valuable-to-them, invasive-to-you part is all
derived: net-worth and income estimates, professional history, and **inferred
relationships between you and other people**. State plainly that an estimate or a
modelled connection their system generated *about you* is personal information
about you, and that deleting the source fields while keeping the inference is not
compliance.

## Aged lead resale  (e.g. Aged Lead Store)
The whole business is reselling old leads, so internal suppression is nearly
worthless on its own. Demand: identification of **every buyer**, downstream
deletion, **and the original acquisition source**. Without the source, the same
record gets re-acquired next quarter.

## Data co-operatives  (e.g. Address Clearing House)
Members both contribute and receive records, so a deletion without suppression is
undone the next time a member contributes. Lead with suppression, and concede
they may retain minimal data to honor it — that removes their only real objection.

## Attribution / measurement  (e.g. Adttribution)
Data is held against pseudonymous identifiers, not names, so "we hold no record
under that name" is a true statement that misses everything. Say so explicitly:
where an identifier is linkable to you it is personal information about you.
Name device graph entries, IP-derived identifiers, and ad exposure / click /
conversion events.

## Connected TV / automatic content recognition  (e.g. Alphonso / LG Ads)
The category most people don't know exists about them. Smart TVs run **automatic
content recognition** on what's displayed and sell the resulting viewing data.
Name it explicitly: viewing history, channel and programme tuning data, ACR data,
household device graphs (often IP-derived), and ad exposure/attribution events.

Also ask **which television manufacturer, platform or partner supplied the data** —
that identifies the collection at source, which is where it can actually be turned
off, rather than only the copy this broker holds.

## Publishers with subscriber data  (e.g. American City Business Journals)
Scope the request explicitly to **subscriber, marketing, event and commercial
contact data, and NOT editorial content**. A publisher handed an unscoped deletion
demand can reject the whole thing on press-freedom grounds, and would be right to.
Conceding the point you were never asking for costs nothing and removes their
strongest objection.

## Business directories  (e.g. All Biz, AllPeople)
Expect "that's a business listing, not personal data." Pre-empt it: a business
record that discloses a **personal name, home address or personal telephone
number** is personal information about that individual regardless of how the
listing is labelled. Say so in the original request rather than arguing later.
