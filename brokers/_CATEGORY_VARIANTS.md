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

## Geodemographic segmentation  (e.g. Claritas)

Assigns **households** to lifestyle, income and life-stage clusters. The cluster
assignment is the product being licensed — not the name-and-address row.

Ask for the segment or cluster assignment explicitly, and ask whether it attaches
to the **address** rather than the name. If it does, deleting a name-keyed record
while leaving the address classified leaves the substance of the profile intact.
Prior addresses matter more than usual: the assignment is keyed to the address held
at the time.

## Predictive scoring / modelled audiences  (e.g. Civis Analytics)

Generates individual-level **scores** — propensity, likely views, turnout,
receptiveness — often from public records such as voter files.

Ask for the scores themselves to be deleted, not merely detached from your name,
and ask which categories of score were held. Where the source is a public record,
say plainly that you are asking them to delete their copy and the derived scoring,
not to alter the source — that removes the easiest deflection ("we can't change
public records") before it is offered. Pair with an objection to profiling and
automated decision-making.

## Media contact / PR databases  (e.g. Cision)

Journalist and influencer profiles assembled from bylines, public profiles and
social accounts. **There is no account to close** — the subject was never involved.

Ask for the contact record *and* the derived attributes: beat and topic
classifications, outlet affiliations, influence or reach scores. Add a request for
platform-level do-not-contact suppression, so subscriber outreach campaigns stop
even if some record legitimately remains.

## Research panels / survey exchanges  (e.g. Cint)

Panel **profiling answers** are the sensitive part: these questionnaires routinely
cover health, income, politics, religion and household composition — categories
treated as sensitive anywhere else. Ask whether profiling responses are retained
after a panellist record is closed.

Panel membership frequently sits with a partner rather than the exchange. Ask them
to forward the request and **name** the panel, rather than accepting a redirect you
cannot act on.

## Community sites with forums  (e.g. City-Data)

Two distinct record types in one place: directory-style entries tying a name to an
address or phone, and **forum accounts with post history**, usually registered
years ago under an email no longer in use.

List every historic email address. Ask for the underlying record removed rather
than the page de-indexed. Where material about you was posted by another user, ask
what exists and under what username rather than accepting a flat refusal — knowing
what is there is a prerequisite to doing anything about it.

## Predictive seller / life-event leads  (e.g. Catalyze AI)

Predicts which households are likely to sell property and sells the resulting
leads to agents. The signals underneath are often **probate, bereavement, divorce,
job change, or financial distress** — which makes this one of the more intrusive
categories in the whole registry.

Three asks the generic letter misses:

- **The inference is the personal information.** A likelihood-to-sell rating is
  something they generated about you and it is the product. Ask for the score
  deleted, not just the contact row.
- **Name the life-event signals.** Ask which categories were used and that they not
  be re-derived. If a prediction about you was built from a death in the family,
  that is worth knowing and worth objecting to specifically.
- **Leads already distributed keep working.** Ask which agents or brokerages
  received a lead and that they be directed to delete it. Deletion at source does
  nothing about copies sitting in agents' CRMs — and those are what generate the
  phone calls.

Pair with an explicit objection to profiling and automated decision-making.

## B2B SaaS holding your data via a business you dealt with  (e.g. Billtrust, Buildertrend)

Invoicing, payments, project management, CRM. You never signed up; a company you
dealt with entered your details. Expect the **processor deflection** ("contact our
clients"), which is unactionable because you cannot know which client uploaded you.

- Ask them to forward the request **and name the client(s)**, or confirm it was
  actioned across those instances.
- **Concede the retention point before they raise it.** Financial and tax records
  often carry a genuine legal retention obligation. Saying so — and asking which
  categories, on what basis, for how long, with everything outside that scope
  deleted and the remainder restricted to that purpose alone — converts a
  conversation-ending "we must keep records" into a narrow, answerable question.
- For property or project software, ask for **job-site addresses, photographs and
  uploaded documents**, not just the contact card. Those identify where you live
  and outlast the job by years.

## Yearbook / reunion sites  (e.g. Classmates)

Publishes **scanned yearbooks** alongside member profiles. Two things make this
category distinctive:

- The images are usually **photographs of minors**, digitised and published
  decades later without the subject's involvement or knowledge.
- Sites frequently hold **unclaimed "placeholder" profiles** generated from
  yearbook data for people who never registered.

So do not limit the request to registered-member data. Ask explicitly for the
scanned pages containing your name or photograph, for your name to be removed from
any index that makes them findable, and for any profile created about you that you
did not create. Any account will be very old, under an email and address long
abandoned — historic identifiers do all the work here.

## Healthcare list rental  (e.g. Complete Medical Lists)

List brokerage in the health sector. The question worth asking outright: **does any
record about me carry a health-related attribute** — condition, treatment,
medication, diagnosis category or "ailment selector"?

Consumers are routinely unaware their rental record carries one, and several state
statutes treat health-adjacent attributes as sensitive personal information. Asking
the question directly forces a specific answer instead of a generic confirmation,
and a "yes" changes the legal footing considerably.

List files refresh from external sources continuously, so ask for a standing
**suppression file** entry and make them say which they did.

## Automotive in-market intelligence  (e.g. Client Command)

Identifies consumers who look ready to buy a vehicle and sells that to dealerships.

Ask for the **in-market/propensity signal itself**, plus vehicle ownership and
service records, and any identity-graph or hashed identifier used to match you
across devices. As with all inference products, the score outlives the contact row
unless you name it.

The decisive ask: **which dealerships already received your details, and direct
them to delete.** A lead sitting in a dealer's CRM keeps generating calls and mail
indefinitely; deleting at source does nothing about it.

## Mobile location / mobility data  (e.g. Complementics, CityData.ai)

The most invasive category in the registry, and the one where a standard letter
achieves least. Data is keyed to **mobile advertising identifiers** (IDFA,
GAID/AAID) and device IDs; a name-and-address search returns nothing while a
detailed movement history remains.

Ask for, by name:

- the advertising and device identifiers themselves;
- **location and movement history** — visit and dwell records, place-visit
  history — not merely the advertising segments derived from them;
- **inferred home and work location**, which is the join between an anonymous
  device and a named person. If they hold an inferred home matching one of your
  addresses, that inference *is* a record about you;
- the identity-graph linkage joining device to name or household.

Two things to say explicitly:

- **Require them to name the identifier types they matched on.** Otherwise "no
  records found" is uninterpretable — it may only mean they searched a name field
  that was never populated.
- **Pre-empt the "it's aggregated" answer.** If the product is derived from
  individual device traces, those traces are personal information about
  identifiable people even where the published output is aggregate. Ask about the
  underlying records, not the aggregates.

Worth stating plainly why this matters: a movement history reveals home,
workplace, place of worship and medical visits without any of them being labelled.
Treat every prior address as a candidate home-location match.

## Court / criminal record republishers  (e.g. CourtCaseFinder)

Distinct from ordinary people-search, and the framing matters because the obvious
deflection — *"these are public records, we cannot alter them"* — is true and
irrelevant.

Concede it up front: **you are not asking them to change a court record.** You are
asking them to delete *their republished copy*, their index entry, and whatever
makes it findable by name. Say so explicitly and the deflection has nowhere to go.

The argument worth making: **aggregation is the harm.** A docket entry in a county
system is practically obscure; the same entry indexed by name and surfaced by a
search engine is not. That transformation is the product.

One more ask, specific to this category and worth making even if you expect
nothing: **if a record is indexed under your name but concerns someone else**, that
is a more serious problem than a privacy request. With a common name it is a real
possibility. Ask what they hold and on what basis they associated it with you —
a misattributed criminal record is worth finding out about.

Records refresh from bulk public-record feeds, so suppression matters more here
than almost anywhere: a one-time removal reappears at the next import.

## Real-estate investor lead platforms  (e.g. Connected Investors)

Identify property owners and sell owner contact details and "motivated seller"
leads to investors. Three things to name:

- **The classification is the personal information.** Labels like distressed,
  pre-foreclosure, probate, vacancy, high-equity or "motivated" are inferences
  about an identifiable person, and they are what is being sold. Ask which
  categories were applied to you.
- **Skip-traced contact details are not public record.** Where a phone number or
  email has been appended to a property record by a vendor, ask for the appended
  data and the linkage deleted — and **which vendor supplied it**, which gives you
  the next broker to write to.
- **Leads already distributed keep working.** Ask which subscribers received a
  lead and that they be directed to delete. The copy in an investor's list is what
  generates the calls and texts.

## Acquired research businesses  (e.g. Coalition Greenwich / CRISIL)

Where a research or data business has been acquired, records commonly survive
under the **predecessor's** data model rather than the acquirer's. Address the
letter to whichever entity holds the data and ask explicitly that records held
under any predecessor or affiliated name be searched — otherwise a truthful search
of current systems misses them entirely.

For panel and interview businesses, ask for the **responses**, not just the contact
record, and for a research-recruitment suppression entry so you are not
re-approached for future studies.

## Professional-services firms on broker lists  (e.g. BDO)

Some entries on public broker lists are accountancy, consulting or audit firms
rather than data brokers in any ordinary sense. They almost certainly hold nothing
about a random consumer.

Do not skip them — but write a **shorter, different letter**:

- Say plainly why you are writing (they appear on a published list) and that **a
  confirmation of "no records" is a complete answer**. This is courteous, it is
  true, and it makes the cheap reply the likely one.
- **Concede retention before they raise it.** Professional-services firms carry
  real regulatory retention duties. Asking which categories, on what basis, for
  how long — with everything outside deleted and the remainder restricted to that
  purpose — turns "we must keep records" from a conversation-ender into a narrow
  question.
- Ask for removal from **marketing, newsletter, publication and event lists**,
  which is the one thing such a firm plausibly does hold.

A "we hold nothing about you" in writing is a real outcome for a broker with no
public listing to re-check, and it is the most likely result here. Record it as
`not_found` on their confirmation, not on your assumption.

## Affiliate / lead-generation front sites  (e.g. Criminal.com, CriminalDataCheck)

A large share of "brokers" on public lists hold **no data at all**. They are
search-styled landing pages that funnel a query to a real background-check
provider and take a referral fee. One replied plainly:

> *"does not own, store, or publish any personal records, background reports, or
> criminal-history information. We are an informational website and keep no
> database of individuals, so there is nothing on our end to remove or delete.
> Searches started from our site are carried out by a third-party
> background-check provider..."*

**Do not skip them, and do not assume the claim is a brush-off.** It is usually
true, and the reply is valuable for two reasons:

1. **A written "we hold nothing" is a real outcome** for a broker with no public
   listing you could otherwise check. Record it as `not_found` on their
   confirmation — not on your assumption.
2. **They name the actual data holder.** That is the broker worth writing to, and
   it may not have been on your list. Follow the referral.

Tells that you are looking at a front rather than a holder: a contact page that is
mostly a search box; no privacy contact other than a generic `support@`; content
that reads as SEO copy about records in general rather than a searchable index.

**When the published address bounces there may be no route at all.** One of these
published exactly one address, it hard-bounced, and the site offered no
alternative. The domain and its MX resolve, so the domain is live and the mailbox
simply is not. Record `failed` with the reason rather than leaving it looking
pending — and note that if the front holds nothing, the request that matters is
the one to the provider behind it, which you can send regardless.

## Sensitive attributes need naming, because the general phrase does not reach them

A recurring failure across several categories, and it is nobody's bad faith: *"all
personal information you hold about me"* does not bring a modelled attribute to
mind, for the requester or the responder.

The pattern is always the same. The attribute was **assigned rather than
collected** — the person never gave it, has no idea it exists, and would not think
to ask for it. The responder searches the identity tables, finds and deletes the
record, and answers accurately. The segment tables are never opened.

Name the category. It costs a paragraph and it tells the responder which system to
look in.

| Category | Attributes worth naming |
|---|---|
| Consumer lists | health or medical interest, financial distress, ethnicity, religion, political affiliation |
| Location / visitation | segments derived from visits to medical facilities, places of worship, legal or financial offices, shelters, treatment centres, political events |
| Political / donor | partisanship, ideology, issue interests, giving capacity, wealth estimate, propensity to give |
| Healthcare professional | prescribing and referral inferences, trial involvement, influence and reach scores |
| Identity resolution | income and vehicle estimates, life-event predictions, propensity scores |

Two things to ask for in every case:

1. **Deletion, not suppression.** A do-not-contact flag stops the calls and leaves
   the attribute on a record that is still licensable. The attribute is the
   product; the contact was only ever the delivery mechanism.
2. **A written answer even when the answer is none.** If they hold nothing of the
   kind, saying so is easy for them and worth having from you. It is also the only
   way the question gets a durable answer rather than a silence.

**And ask about relationship edges where the product has them.** A network record
joining two named people is personal information about *both*, and deleting one
person's profile characteristically leaves the edge intact on the other's — still
naming you, still searchable, and never mentioned in a confirmation about "your
profile".

## Do not hand over a device identifier to establish that one is not held

A location broker's opt-out page needs your Apple IDFA or Android advertising ID.
The instinct is to fetch it and paste it in — it is the key, after all, and the
company says plainly it is used to locate the request rather than to verify you.

**Ask first whether they hold a record at all.**

If they do not, supplying an advertising identifier gives the company a fresh
identifier for you *in order to ask them to delete something that may not exist*.
The request creates the link it was meant to break, and the company now has a
device ID and an email address that arrived together — which is precisely the join
these businesses pay for.

If they do hold one, supply it immediately: they already have it, and nothing is
given away.

**One round trip settles it.** Ask what identifiers they hold you under, and
whether any key other than the advertising ID would locate or re-link a record
after that ID is deleted — a hashed email, an IP-derived household, a location
centroid, a persistent internal ID that survives an advertising-ID reset.

### Two follow-ups that decide whether the opt-out is worth anything

An advertising identifier is **user-resettable**, and on iOS it is zeroed when app
tracking is declined. So an opt-out bound to that one string may be undone by an
action the operating system actively encourages:

  a. **Does the opt-out survive a reset?** Or does a new identifier arrive with no
     suppression attached?
  b. **What about a device whose IDFA is all zeros?** If a record exists for such a
     device, it is not keyed to the advertising ID — so what is it keyed to?

Neither question fits in a form field. Ask them on the email thread, and treat the
portal as capturing only what its fields happen to ask.

## Where deletion is the wrong ask

Deletion is the default request, and at most brokers it is the right one. Three
categories where it is not, and asking for it first costs you something:

### 1. Identity-verification data — ask for disclosure, then correction

At a marketing broker the record is a nuisance. At an identity-verification
company it can decide whether somebody opens an account, passes a check, or is
believed about who they are.

So invert the order: **ask what exists before asking for it to go.** And where a
record is *wrong*, prefer correction — an inaccurate identity record deleted from
one file persists at whoever supplied it and returns at the next ingest, while a
corrected one is fixed at source. Deleting a wrong record also destroys the
evidence that it was wrong, which matters if it has already caused a decision.

**On legal-retention claims, split the two things.** These businesses often must
retain verification records. That is a reason to keep something; it is not a reason
to keep *selling* it. Ask them to confirm anything retained under an obligation is
used only to meet it — not for sale, sharing, marketing or model training.

### 2. Brokers that maintain a persistent suppression list

Where a company keeps your identifier specifically so it can go on ignoring you,
deletion removes the protection. One publishes this outright: *"if you would like
to request deleting all information... we may not be able to keep a record of your
opt-out preference and add information to the database again."* See
`_SILENT_FAILURES.md` §16 and §26.

### 3. De-identified health data — ask about the token, not the record

A health-data company will answer a deletion request by saying the data is
de-identified and therefore not personal information. Arguing that produces a
policy exchange and no facts.

Ask instead whether a **token or persistent identifier corresponding to you**
exists, what it is derived from, and whether they can locate it from your
identifiers. A token that links claims across providers and over time is
functionally an identifier for one person — that linkage is what makes a
longitudinal dataset longitudinal. And say explicitly that *"we cannot locate a
token from these identifiers"* is an acceptable answer: it tells you the linkage
runs one way, which is the thing you wanted to know, and it is far easier to
answer honestly than an accusation.

**The pattern across all three:** ask the question whose answer changes what you do
next, rather than the request that sounds strongest.

