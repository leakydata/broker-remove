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

## Telematics / driving & mobility data  (e.g. Arity)

Collected through mobile apps and connected vehicles, so the record is keyed to a
**device or vehicle**, not to a name. A name-and-address search may honestly
return nothing while a substantial trip history remains.

Ask for: driving, telematics, trip, location and mobility records tied to you or
to any device or vehicle of yours; plus any **risk score** derived from them —
these feed insurance pricing, so the derived score matters as much as the raw
data. Ask them to search on mobile advertising identifiers, hashed emails and
device identifiers linked to your details, **and to say which identifier types
they matched on**. That last part converts "no records found" from a dead end
into a usable answer.

## Email-keyed identity resolution  (e.g. AtData)

The email address *is* the product: validation, activity scoring, and linking an
address to a postal address, phone and demographic profile.

The trap is **hashing**. These businesses routinely hold MD5 / SHA-1 / SHA-256
digests of addresses rather than the plaintext, and a request that only names
plaintext addresses can be answered truthfully and narrowly. A hash still resolves
to you and still joins records together.

Ask explicitly whether they hold hashed forms of each address, state that hashed
identifiers are in scope, and require that the **linkage** be deleted — not just
the plaintext row. Give every address you have ever used; each is a separate key.

## Social listening / consumer intelligence  (e.g. Brandwatch)

Archives publicly posted social content and builds author profiles, sentiment and
demographic inferences from it. The data is keyed to **social handles**, so a
search on name and email can return nothing while a large archive exists.

Ask for: archived posts, comments and profile information attributed to your
accounts; any handle-to-person linkage or identity resolution; and any sentiment,
interest, influence or demographic attribute inferred from that content.

Head off the standard objection directly: *that a post was publicly visible when
collected does not exempt the resulting archive, profile, or inference* — it is
still personal information about an identifiable person. Offer to supply the
relevant account handles if they say they need them to search; that removes the
"we couldn't locate you" exit without volunteering handles they may not hold.

## Client-uploaded SaaS platforms  (e.g. Birdeye)

Reputation, review-solicitation, messaging and CRM platforms hold your details
because *a business you dealt with uploaded them* — you have no relationship with
the platform and usually cannot name which client is responsible.

Expect the **processor deflection**: "we act only on behalf of our clients; please
contact them." Don't accept it flatly, because you cannot act on it — you don't
know who uploaded you and they do. Ask them to either forward the request to the
client(s) whose records contain your details **and tell you who they are**, or
confirm the request was actioned across those instances.

Also ask for your phone and email to be added to any platform-level
do-not-contact list, so client campaigns running through the platform stop
re-soliciting you even where a record legitimately remains.

## Vehicle history / ownership lookup  (e.g. Bumper)

Keyed to a **VIN or plate**, not to a person, so a name-and-address search can
return nothing while records that resolve to you remain.

Ask for: ownership and title history, registration and lien records, VIN-linked
records, sales and listing history, and any report naming you or linked to your
address. The thing to name explicitly is the **name-to-vehicle linkage** — ask for
the linkage deleted, not merely your name detached from a record that still
describes the vehicle. Registrations are indexed against the address held at the
time, so prior addresses matter more here than usual.

## Reverse phone lookup / caller ID  (e.g. CallerSmart)

Keyed to **phone numbers**. Lead with the numbers, not the name, and include
disconnected ones — those are the most likely to still be indexed and the least
likely to be found by a name search.

The extra ask: **user-submitted comments, reports and ratings** attached to a
number are personal information about whoever holds it. A number stripped of your
name but still carrying commentary about you is not a completed removal.

## Recruitment / résumé databases  (e.g. CareerBuilder)

Two failure modes worth naming in the letter:

- **Closing the account leaves the résumé.** Deactivating a profile frequently
  leaves the searchable résumé record live and visible to employer subscribers —
  which is the part that matters. Ask for the database entry, not the account.
- **The record may not be yours to remember.** Résumés get re-uploaded by staffing
  agencies and sourced from partner sites, so a profile can exist under a former
  email address years after you last used the service. Historic identifiers do the
  work here.

## Talent intelligence / candidate scoring  (e.g. Censia)

Assembles candidate profiles from public and licensed sources *without the
subject's knowledge*, then scores them for employers. Nobody involved has an
account to close.

Ask for the profile **and the generated attributes**: skills and seniority
inferences, compensation estimates, predicted job-change or "likelihood to move"
scores, ranking and match scores. These are personal information the company
created about you, and they survive deletion of the source record if you don't
name them. Pair the deletion request with an explicit **objection to profiling and
automated decision-making**, and ask whether any has been applied — this is one of
the few categories where that right straightforwardly bites.

