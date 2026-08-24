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

## Arrest and booking publishers: split the ask in two

A site that republishes arrest and booking records is not a data broker in the usual
sense, and the usual letter goes badly there. Deletion runs straight into a
First Amendment and public-record argument that is, on the merits, often a strong
one -- and once that argument is joined the whole request is lost with it.

**Concede the unwinnable point first, explicitly.** Say that you are not asking them
to alter the public record at its source, and that you are not disputing accuracy.
That removes the reflex and costs nothing, because it was never available anyway.

**Then split the request.** A publication of this kind does two separable things:

  1. it **hosts a page**; and
  2. it makes that page **findable by name**.

The second is what does the lasting damage. A name search returning a booking record
indefinitely, regardless of outcome, attaches a permanent consequence to something
that may never have produced a charge. **De-indexing is a different question from
deletion, and it is frequently granted where deletion is refused** -- it does not
require the publisher to concede anything about their right to publish.

**Invite the refusal to be stated.** "If you decline on First Amendment or
public-record grounds, please say so plainly" gets you a recordable answer instead of
silence, and it makes the separate de-indexing question harder to leave unanswered.

## Lookup-by-identifier products: name the reverse lookups

Where the product is a lookup keyed to a phone number, address or email, ask for the
suppression to cover **reverse lookups** explicitly, not only search by name.

This is the PeopleConnect failure mode written in advance: a suppression that is
keyed to the name query leaves the record reachable by every other path, and the
confirmation will say the removal is complete because, on the query they blocked, it
is. Naming the reverse lookups in the original letter makes a name-only answer
visibly a partial one.

## Sell-side and identity platforms: ask which hat they are wearing

Ad-tech intermediaries typically hold some data as a **controller** and some as a
**processor** on behalf of publishers or buyers. A deletion request answered from
the processor side is answered honestly and achieves nothing.

Ask directly which parts they hold in which capacity, so requests can be directed at
the right party rather than assumed. Pair it with the other question that bounds any
answer they give: **which identifier types did you match on?** A deletion is only as
broad as the key it was run against, and that is invisible from outside.

## On a continuously-fed publisher, an opt-out is a point in time, not a state

The most useful sentence any broker has volunteered in this project came from an
arrest-record publisher, answering directly when asked whether their opt-out was
prospective:

> *"An opt out is not a standing suppression, it is a removal of current information
> that matches criteria. Should information be received in the future you will have to
> request for an additional opt out in the future."*

**That is a different kind of answer from a refusal, and it changes what "done"
means.** Most brokers leave this ambiguous, and the ambiguity always resolves in their
favour: a confirmation saying "your information has been removed" is true on the day
it is sent and says nothing about the next data load.

For a publisher fed continuously from an external source — arrest and booking feeds,
court dockets, licence registries, property transfers — the practical consequence is
that a removal is **not** terminal:

- the record can return without anyone doing anything wrong;
- nothing will notify you when it does;
- the confirmation you hold remains accurate and useless.

**So this category cannot be marked closed.** It has to be **re-checked on a cycle**,
and the tracker note should say why, so that a future reader does not see a
`not_found` and assume the matter is settled.

**Ask the question explicitly, in these words**, because the honest answer and the
evasive one look identical otherwise: *is the opt-out a standing suppression applied
to future data, or a removal of what matches today?*

## Their removal mechanism is worth knowing too

> *"Our opt out process is the same as our unpublish process. This will include us
> removing the web page and replacing it with a 404 page... This will also request
> that search engines update their information when they recrawl our pages. We can not
> confirm when that will be as we do not own or control 3rd party sites or search
> engines and can not force them to remove."*

Three things follow. The page becomes a **404**, which is a real removal rather than a
de-listing. The **recrawl is requested, not performed** — so the search-engine result
outlives the page, by an interval nobody controls. And they say plainly that they
cannot compel third parties, which is both true and the reason a search-engine hit is
never evidence that a removal failed.

## MAID-only brokers: decide once, and reset afterwards

Three companies have now answered the same way: they cannot look a person up by name,
email, address or telephone number, because the only identifier they hold is a
**mobile advertising ID**.

> *"Matchbook Data and its products only work with advertising identifiers for mobile
> devices and not with personal identifiers such as names, email addresses, telephone
> numbers, etc. Therefore, in order to fulfill your request, you must submit the mobile
> advertising identifiers of your device(s) to us."*

**The offers differ, and the difference is the whole decision:**

  - **Check-then-tell** — supply the MAID, they hash it, check it, and *tell you
    whether there was a match*. You learn something either way.
  - **Blind ingest** — supply the MAID and they act, but you never learn whether they
    held anything. *"Without the advertising identifiers, we will not be able to process
    your request to determine if we hold any relevant data."*

The second is a worse trade on its face: you hand over a live identifier to a company
that may not have had it, and get nothing back that you did not already know.

**But the MAID is resettable, and that changes everything.** On both major mobile
platforms the advertising identifier can be reset or deleted outright, which mints a
new one and orphans the old. So the sequence is:

  1. supply the current MAID to **all** such brokers at once;
  2. let them delete or suppress against it;
  3. **reset the advertising ID on the device.**

What each of them retains is then a dead identifier that matches nothing. The
disclosure is real but time-boxed, and it buys deletion across every broker in the
category for one exposure rather than one per company.

**A fourth company has now said the same thing, and it produced the most useful side
effect of the pattern.** Mogean answered:

> *"Mogean does not have any of the information that you provided. We deal exclusively
> in mobile advertising identifiers, so if you reply back with your valid advertising
> identifier GUID we will check our systems."*

The first sentence is an **unqualified negative for every identifier supplied** — name,
addresses, telephone numbers, email addresses. That is worth recording on its own: a
MAID-only broker cannot match you by name, so asking it to try produces the cleanest
`not_found` available anywhere, for everything except the identifier space it actually
uses. **Send the letter even when you expect the MAID gate**, because the refusal comes
with a negative attached.

Watch for the closing move, too: *"we are unable to process your request and are
considering this request closed."* A closed ticket means a later reply starts from the
top. Ask them to hold it open — it costs a sentence.

**Two questions worth asking regardless of what you decide**, because neither depends on
supplying anything:

  - **If I supply an identifier and you find no match, will you tell me?** A confirmed
    no-match is a real result.
  - **Does deletion cover the derived records** — location, visit and dwell histories,
    audience segments, inferred attributes keyed to that identifier — **or only the
    identifier row?** Deleting the key while keeping the history keyed to it is not a
    deletion in any useful sense.

**Two practical notes.** If tracking is already disabled, the iOS identifier is all
zeros — there is nothing to disclose and nothing to gain, so check before deciding.
And decide **once for the whole category**: handling these one at a time multiplies
the disclosure without multiplying the benefit, since they are all asking for the same
value.

## When a privacy alias is a distribution list

A bounce worth recognising: a request to `privacy@` returns **four separate
non-delivery reports**, each naming a different individual employee, each saying the
mailbox is full.

That reveals the alias is not a queue or a ticketing address but a **forwarding list of
named people**. Which means there is no privacy *process* — only individuals — and when
those individuals leave, the address keeps accepting mail while delivering to nobody.

**Read it as a signal about the company, not just a delivery failure.** Four
simultaneously over-quota mailboxes is what a privacy function looks like after the
staff have gone, and it is a strong hint that the entity is defunct, insolvent or
absorbed. Check the corporate status before spending more effort on the address, and
look for the acquirer instead.

## Single-dataset republishers: check the source, not the broker

Some sites republish exactly one public dataset and nothing else, and say so:

> *"The provider information displayed on this site comes entirely from the
> official NPPES public data release published by the Centers for Medicare &
> Medicaid Services (CMS) under the Freedom of Information Act."*

That sentence is a gift, because it makes the question **checkable without them**.
If the upstream dataset holds no record matching the subject, the republisher
cannot hold one either — and many of these datasets are public with a free API:

- **NPPES / NPI registry** — `npiregistry.cms.hhs.gov/api/?version=2.1&...`
- **FEC individual contributions**, **SEC EDGAR**, state professional licensing
  registers, **FAA airmen**, and most county assessor systems all have equivalent
  direct-lookup routes.

Querying the source first is better than writing to the broker, and not only
because it is faster:

- **It produces a stronger negative.** "The authoritative source contains no
  matching record" beats "a broker searched and says they found nothing", which
  depends entirely on how they searched and which fields they used.
- **It costs the subject nothing.** No identifiers are handed to anyone, no
  ticket is opened, no mailbox learns that this person is looking.
- **It settles the sibling question too**, because every other republisher of the
  same dataset is answered by the same query.

### How to run it

Search **every state the subject has lived in**, not just the current one, and use
a wildcard on the given name (`Rob*` catches both `Rob` and `Robert`) so that a
formal name is not missed behind the one somebody actually goes by.

### Where it stops

Two limits, both worth writing into the record rather than glossing:

**The claim is theirs.** "We republish only X" is an assertion. Record the
`not_found` as conditional on it, so that if the site is later seen carrying data
that is not in X, the conclusion reopens rather than standing as settled fact.

**A near-match is not a match, and this is where the temptation bites.** These
searches routinely surface someone with the same first and last name in a city
the subject has genuinely lived in. That is a coincidence, and coincidences are
common with common names. The opt-out tools for this category are keyed to the
record's own identifier — an NPI, a licence number, a filing ID — so acting on a
near-match does not merely fail; **it removes a stranger's record.** Middle name,
date of birth and exact address are what separate two people. Absent those, do
nothing.

## Benefit-location services: the opt-out that can cost the subject money

Most brokers lose nothing worth having when a record is removed. A small category
is different, and it needs flagging rather than processing.

Firms that locate individuals **on behalf of pension plans, insurers and benefit
administrators** exist because people move and lose touch with money they are
owed — an old employer's defined-benefit pension, a lapsed 401(k), an unclaimed
life-insurance payout, a union benefit. Their consumer request forms say so
plainly:

> *"If [we are] trying to reach you for one of these purposes, by submitting this
> form, you may make it more difficult for your former employers, pensions, and
> unions, to locate your contact information and communicate with you regarding
> your benefits."*

Read that as **true rather than as a dark pattern**. It is the same sentence a
retention team would write, but here the underlying claim holds up: removing
yourself from a locate database can sever the only route by which money reaches
you.

### What to do

**Do not submit these on someone's behalf.** Surface the trade-off and let the
subject decide. The relevant question is simply whether they have any old
employer pension, 401(k), union benefit or lapsed policy that has not been
consolidated — and most people do not know, which is itself an argument for
caution.

**Ask for disclosure and correction instead**, which carries none of the same
cost and is often the more valuable answer:

- Am I recorded in any **deceased or death-match file** — including a partial,
  probabilistic, or later-resolved match? False Death Master File matches suspend
  benefits and freeze accounts, usually with no notice and no visible cause. A
  deletion would remove the evidence while leaving the flag propagating through
  every client already holding it.
- **Which clients received my record**, and will you direct them to correct it?
- What are the **sources**?

**Expect a processor defence, and expect it to be right.** These firms usually
hold the data for client organisations, so even a granted request reaches only
what they hold in their own right. The plan or insurer is the controller.

**Expect an SSN demand.** The Social Security number is the matching key for
death-audit work, so their forms ask for at least the last four digits, plus full
date of birth. Sending it hands over a more sensitive identifier than any being
deleted. Refuse, and say why.

Related: "Where deletion is the wrong ask", above — identity-verification data and
persistent suppression lists are the other two members of that family.

## Contact centres and BPOs: three artefacts nobody asks for

An outsourced contact-centre operator holds almost everything about the public on
behalf of clients, so the first ask is **name the client**, not *delete it* — a
truthful "we are only a service provider" is unactionable when the consumer
cannot know whose contact-centre work touched them.

But there are three artefacts that a general deletion request never reaches, and
they are the real reason to write to this category at all.

**Recordings and transcripts are two different things.** A transcript is usually
generated into a separate system for quality scoring or analytics, and is
frequently retained *longer* than the audio it came from. "Delete my call
recording" leaves the transcript sitting in the analytics platform. Name both.

**Voiceprints are biometric data, and nobody is told they exist.** Speaker
identification and voice authentication create a template from a caller's voice.
The person it was taken from is not informed, it is not visible in any account
page, and it is essentially never covered by a request phrased as "delete my
data" or "close my account". Ask for it by name — voiceprint, speaker-ID
template, voice-authentication enrolment — and cite the applicable state
biometric statute, because that is the framework under which it is most clearly
actionable.

**Quality, training and model-evaluation sets.** Recordings and transcripts feed
agent scoring and, increasingly, speech and language model development. Ask
whether any material involving the subject has been used that way, and ask for an
honest description of the limits rather than a promise. A model already trained
is a different problem from a row in a table; saying so invites a truthful answer
instead of a reassuring one.

**Search every prior telephone number.** A contact-centre record is keyed to the
number that was dialled or that called in — for any older engagement, a number
the person has long since given up.

## Reverse-lookup sites with user comments

A comment board bolted onto a directory needs **three separate asks**, and the
second is usually the one that matters:

1. **The directory entry**, in both directions.
2. **The user comments.** Any post naming the person or their number. These sit
   in a different table from the directory data, they are separately indexed, and
   they are frequently the part that actually surfaces someone by name. A removal
   scoped to the listing leaves every comment in place.
3. **Suppression against re-creation.** On a user-generated site a number can be
   given a brand-new page the day after the old one is deleted. Ask that the
   numbers cannot be re-added or re-commented — otherwise the removal has a
   shelf life of one visitor.

Ask for a `noindex` directive as well as content removal: comment pages accumulate
search authority, and a removed page that stays indexed keeps the person findable
for months.

**Watch what address they publish.** One of these sites lists a **ProtonMail
address** as its privacy contact. That is worth recording rather than merely
noting: it says there is no company mail domain behind the site and that whoever
runs it prefers not to be identifiable. Expect no ticket number, no letterhead
and no escalation path — and set expectations accordingly rather than reading
silence as refusal.

**If the site is not in English, write in both languages.** It costs one extra
paragraph and materially raises the chance that whoever reads it acts.

## Domain intelligence / registrant lookup  (e.g. DomainTools, ViewDNS, Whoxy)

Holds **who you were when you registered a domain**, which is often an address
and a telephone number that appear in no other dataset — so these records
survive every removal keyed to your current details and are invisible to any
verification that searches them.

Lead with the fact that you cannot enumerate what they hold: WHOIS history is
not searchable by person without a paid account, so **"tell me what you hold, in
categories" is a substantive ask here**, not a formality. It is the only way the
subject learns which registrations and which old contact details are in
circulation.

Ask for suppression explicitly. These indexes are rebuilt in bulk from archived
snapshots, so deleting a row from the live index without a suppression entry is
undone the next time an older snapshot is re-imported.

Expect "it was lawfully public at the time" and answer it twice: the publication
was a condition of registering a domain rather than a choice about publicity,
and the industry itself reversed the practice — registrars now redact by
default. Then move to the stronger ground: **the republication and commercial
supply today is a separate act**, done by them, now.

See `_SILENT_FAILURES.md` §67.

**Check the product line before you write.** "Firms that plausibly hold
pre-redaction WHOIS" is a hypothesis, not a finding, and a letter written from
it must say so — one sentence, "I found this republished elsewhere and I am
writing to firms that may hold the underlying records; do you?" ViewDNS replied
within half an hour to say they offer no historical-WHOIS tool at all, and they
were right. See the §67 correction in `_SILENT_FAILURES.md`.

**The surface that is usually there even when historical WHOIS is not** is a
**reverse WHOIS lookup**: name or email in, domains out. It is person-keyed by
construction, so it implies an index of registrant identities, and it is the
better thing to ask about. The narrow question — *does that index retain
registrant details from records now redacted at the registrar, or only reflect
currently-published WHOIS?* — is answerable from a database and closes the
matter either way.

**Watch for the login wall.** Where the reverse lookup requires an account, the
data subject is the only party who must identify themselves to learn what is
published about them. Worth naming to them as feedback; it is not a violation,
but it is an asymmetry most companies have not thought about.


## B2B contact & sales prospecting databases  (e.g. Apollo, ZoomInfo, RocketReach, Hunter, ContactOut, SignalHire, Wiza, Snov, Prospeo, LeadIQ)

The largest single category by count, and the one where the standard consumer
letter fails most quietly. These products sell a work email address and a
telephone number for a named person at a named company, usually to someone who
will then cold-contact them.

**Why a consumer-shaped request returns a true nothing.** The index key is a
*work* address, and a large share of those were never chosen by the person they
belong to — they are generated from name-and-domain patterns observed at other
employees, or captured from a signature block by a customer's browser extension.
So a search over personal webmail addresses is a real search on keys the index
does not use. The negative is honest and means almost nothing.

Say so in the letter, without accusing anyone of dodging:

> A search over the personal email addresses above will very likely return
> nothing even if you hold a record, because those are not the keys a B2B contact
> database is built on. Please search the **telephone numbers** and the **name
> variants** instead. For your product the phone number is the most person-shaped
> field you hold: a direct dial or personal mobile follows someone between jobs,
> and it is the element that actually produces the calls.

**Do not answer "which email format is it under."** That asks you to reproduce an
identifier the broker manufactured. Listing plausible permutations invites a hit
on a different person with the same name, which is worse than a miss. Instead ask
them to state whether their records are keyed to observed addresses or to
pattern-generated ones — the answer tells you whether a null result on your real
addresses could ever have been informative. See `_DEFLECTIONS.md` §44.

**Never supply a LinkedIn or other profile URL to one of these.** Offered as
verification (`_DEFLECTIONS.md` §38) or as a search convenience (§44), the effect
is the same: a stable, unique, employer-linked key handed to a database whose
business is joining keys. If no record exists, that search does not test for a
match, it assembles one. The single exception is a broker that has already
demonstrated it holds the profile — one that has sent you the scraped record. It
cannot re-learn what it has already shown you.

**Four asks specific to this category:**

1. **Exported copies.** The platform exists so customers can push contacts into a
   CRM or a sequencer. Every export is a copy the broker's deletion cannot reach,
   and it is the copy that generates the calls and the emails. Ask which
   customers received the record and ask them to be directed to delete it.
   Without that list there is no route to the copies at all.

2. **Capture-by-extension.** Many of these products acquire records when a
   customer's browser extension is pointed at a page. That means the record may
   originate from a *customer* rather than a supplier, and it can be recreated by
   any customer repeating the action. Ask which mechanism produced yours, because
   supplier suppression does not stop the other one.

3. **Re-verification.** Records are periodically re-checked and re-enriched
   against upstream sources. A deletion with no persistent suppression entry is
   rebuilt at the next cycle, having been deleted exactly as asked. Ask which was
   applied — deletion, or deletion plus standing suppression.

4. **The ask that survives a null result.** This is the one to keep whatever the
   search returns:

   > If you hold nothing today, please still add my name, telephone numbers and
   > email addresses to a permanent do-not-add suppression entry, so a future
   > ingest from a supplier cannot create a record I would have to find all over
   > again.

   Cite a company that already does it. SourceIT retains SHA-1/SHA-256 hashes of
   addresses purely to prevent re-adding — holding the suppression while holding
   no record. Naming another firm's practice moves the request from "will you do
   me a favour" to "this is normal", which is the most reliable lever available.

**Ask who supplies them.** A reseller knows its upstream and no public list does.
This is how L2 Data — 250 million consumer records — entered the registry at all.
See `_SILENT_FAILURES.md` §74.

**Status handling.** A null result here is not `not_found`. It is a search run on
the wrong keys with the suppression request outstanding. Leave it `submitted`.

## When you cannot tell what kind of broker it is

Most of the registry now comes from state registration filings, and **a
registration entry does not describe a business.** It gives a legal name, a
domain and a contact address. For a large share of the remaining queue there is
no way to tell from the outside whether the company holds contact records, an
identity graph, location traces, modelled scores, or transaction data.

The temptation is to guess and send the letter for the category the name
suggests. Resist it. A letter aimed at the wrong kind of company is worse than a
generic one: it advertises that the sender does not know who they are writing to,
and it invites a reply correcting the premise instead of answering the request.

**Ask, and make the answer do work.** Put the question early, framed as saving
them effort rather than as ignorance:

> I know you are a registered data broker in California, and I know essentially
> nothing else about what you hold, because a registration entry does not
> describe a business. Rather than guess and send you a letter aimed at the wrong
> kind of company, I would rather ask — and the answer also tells me what to ask
> for.
>
> **Which of these describes what you hold about people?** More than one may
> apply, and a one-line answer is enough:
>
> 1. Contact records — names, addresses, phone numbers, email addresses.
> 2. Identifier or identity-graph data — hashed emails, device or advertising
>    identifiers, cookie IDs, and the links between them.
> 3. Location or movement data.
> 4. Modelled or inferred attributes — scores, segments, propensities, estimated
>    income, life stage.
> 5. Transaction, purchase or financial records.
> 6. Public-record data — court, property, voter, licensing.
> 7. Something else, in which case please say what.

Then the asks that hold **whatever the answer is**:

- **Search every identifier, current and prior.** And: *"if your index is keyed
  to something I have not supplied and cannot supply, please tell me what it is
  keyed to."* That single sentence is the most valuable line in the letter — it
  converts a dead-end null result into a description of the index, which is what
  a follow-up needs. It is also how the MAID-only brokers were identified.
- **The links, not only the rows.**
- **Inferences as well as facts**, since anything modelled is personal
  information under the same statutes and is the part a person cannot discover
  any other way.
- **Standing suppression, and a do-not-add entry even on a null result.**
- **Sources and recipients.**
- **The processor escape hatch**, offered as acceptable: if you act only for
  clients, say so, name them, pass it on.

**Cite a precedent for the suppression ask.** The do-not-add-on-null-result
request is the one most often refused on the reasoning that there is nothing to
suppress. Naming a company that did it anyway converts the ask from a favour into
a norm:

> another registered broker replied to me this week having found no record, and
> added a permanent suppression entry itemising every address and email anyway.

That is IDM (`_DEFLECTIONS.md` and `idm.md`), and it is the strongest single
lever in this whole file — see the SourceIT hash precedent for the same move.

**Why this works better than a guess.** Every branch of the answer is useful.
"We only hold X" scopes the follow-up. "We hold nothing" closes it. "We are a
processor" redirects it. And a company that answers the categorisation question
has already engaged with the substance — which is most of the difficulty.

**Do not use this variant when the category is genuinely knowable.** A
people-search site, a credit bureau or a prospecting database should get the
specific letter, because specificity is what makes those land. This is for the
long tail where the honest position is that you do not know.

## Property and real-estate data  (e.g. ATTOM, PropStream, CoreLogic/Cotality, PropertyReach)

The public-record core is real: deeds, assessments, mortgages and liens are
county records, the broker aggregates them, and no consumer can claw that back.
A letter that ignores this invites a one-line reply — *"this is public record"* —
which is true and answers nothing.

**So concede it in the first paragraph**, and say the exemption is acceptable
where it genuinely applies. Then ask for the layer built on top, which is the
actual product and is not a public record:

- **Automated valuation and equity estimates.** An AVM figure, an estimated
  equity position or remaining mortgage balance is a model output no county
  recorded. It is a financial inference about a named person and their home.
- **Propensity and life-event scores** — likelihood to sell, to refinance, to
  move; distress or default indicators; "life event" flags. These are
  predictions about what someone is about to do with their home, sold to people
  who want to contact them about it. They are why the mail arrives.
- **The person-to-property linkage, and the append.** A deed names an owner; the
  product resolves that into a contact record with telephone numbers and email
  addresses appended from elsewhere. **The append is not a public record and
  neither is the linkage graph.** This is the single most important ask in the
  category and it is the one most easily lost inside a public-record answer.
- **Occupancy and household inference** — owner-occupied versus absentee, length
  of residence, household composition, inferred demographics.

**Two things specific to address history.** Ask **how many records matched**: a
person with a long address history routinely appears as several unreconciled
records in a property database, and a removal applied to one is not a removal.
And list every prior property, in every county — see §47, where a prior
out-of-state address was what got a request honoured at all.

**Licensees are the operative copies.** Property data is licensed in bulk to
lenders, insurers, investors, marketers and other data companies. Ask who
received it and ask them to be directed to delete.

**Insist on the refresh question.** These databases are rebuilt from county
records continuously, so a one-time deletion is refilled at the next ingest and
the confirmation reads identically either way. Ask them to confirm the
suppression survives the next county refresh, and that it is held independently
of the record so deleting one does not remove the other.


## MAID-only brokers: the geographic query is the way past the impasse

Five companies in this registry have now said, in substance, *"we can only find
you by mobile advertising ID; send us one."* Foursquare, CityData.AI, Matchbook
Data, Mogean and Outlogic (formerly X-Mode Social).

**The demand is structurally unanswerable, and worth saying so plainly.** A MAID
was generated about a person rather than by them, was never disclosed to them, is
resettable, and there is no lookup by which anyone can discover which values were
associated with their devices historically. So "submit such identifiers" asks the
consumer to produce something the industry created and never showed them.

And the disclosure runs the wrong way. If the broker holds nothing, sending a
live identifier **creates** a record rather than removing one. Since neither side
knows which case applies before the search, it is a one-way bet against the
requester.

### The substitute: ask them to search where the device sleeps

Location data has a natural key that is not an advertising ID. **Where a device
spends the night, repeatedly, over months** identifies a household member about
as reliably as a name field — and it is a query these systems exist to perform.

> Please identify any device showing a **persistent overnight dwell pattern** at
> [current address], and at [each prior address] for the period of residence, and
> delete the records for any such device together with any inferred home
> location, work location, visit history and identity-graph linkage attached to
> it.

This asks the same question in the only vocabulary the dataset speaks, and it
requires nothing from the requester that they do not already put in every letter.

**Pair it with confirm-before-delete.** The query may return devices belonging to
other people in the household, and deleting a family member's record on someone
else's say-so is the same harm as removing a stranger's listing. Offer it
explicitly:

> Because that query may return devices belonging to others in the household,
> tell me what you find and let me confirm before anything is deleted.

Offering this makes the request *easier* to grant, not harder — it removes the
broker's best reason to refuse.

### Three asks that do not depend on finding a record

1. **Does the opt-out form itself require a MAID?** Several of these brokers point
   at an opt-out page that has the identical problem. Ask before spending time on
   it.
2. **Can suppression be keyed to anything other than a MAID?** If not, say so
   plainly — it means **no consumer can hold a durable suppression with that
   company**, since the key resets. That is a significant admission and worth
   having in writing.
3. **Which SDK partners and app publishers feed the dataset?** That is the
   collection point the person never knowingly agreed to and cannot discover
   alone. Naming it is the only route to the source rather than the destination.

### When it fails: Outlogic refused, and refused clearly

The geographic query is worth asking, not guaranteed to work. Outlogic answered
in eleven minutes:

> *"We only collect MAIDS. We need a valid device ID to look up and provide the
> data we have, or to delete any data we may hold. Without that device ID, we
> can't search our systems."*

**Take that at face value and stop.** Two clear refusals is the limit — a third
attempt is not persistence, it is not listening, and it costs the goodwill that
makes the next exchange possible. Record `manual_required` and move the decision
to the human.

**Credit what deserves crediting.** The same message said:

> *"Please do not provide any personal data to us other than the MAID that we
> collect."*

That is a data broker actively refusing personal information it does not need,
having just been sent twelve email addresses, sixteen postal addresses and eleven
telephone numbers. Most companies in this file would have searched and kept all
of it. Saying so in the reply is not flattery — it is the difference between a
correspondent and a form letter, and it is what makes a later request land.

**Leave the structural observation on the record, and say no reply is needed.**
The combined effect of "we hold only MAIDs" and "we accept only a MAID" is that
consumer access is impossible in principle, not in practice: the only acceptable
key is one the industry issues, never discloses, and rotates. Someone whose 2023
movements are held cannot ask about them in 2026 even doing everything right.
Say it once, without demanding an answer, and stop.

### Close the loop honestly

Say that a null result from the geographic query will be accepted:

> If the geographic search returns nothing, I will accept that as a complete
> answer and say so. I would simply rather have a real negative from a query that
> could have found me than a null result from one that never could.

That sentence is the whole argument in miniature, and it is what distinguishes
this from refusing to cooperate.


## Recruiting and talent intelligence  (e.g. Atlas/Hunt Club, AdeptID, Censia, Findem, Revelio)

A talent database holds two layers and only the second one matters much.

**Layer one is scraped:** name, employer, title, dates, education, public profile
URL. Mostly reconstructible from a public profile, and mostly what a broker will
volunteer if asked.

**Layer two is generated:** a fit or match score, a seniority mapping, a skills
inference, a likelihood-to-move or openness-to-opportunity signal. **These are
shown to employers and invisible to the person they describe.** A deletion scoped
to the contact fields leaves them intact, and they are the part with
consequences — they decide whether someone is surfaced for a role at all.

So ask for them by name. "Delete my personal information" does not obviously
cover a propensity score, and a broker answering narrowly is not necessarily
being evasive.

**Ask about inferred demographics explicitly, including the benign framing.**
Inferred gender, ethnicity and age band appear in these systems, sometimes for
diversity measurement rather than targeting. That purpose may be entirely
legitimate and it does not change the fact that it is an inference about a person
attached to a hiring record. A general "we hold no sensitive data" will not reach
it, because the company may not classify it as sensitive.

**Search work identifiers, and say why.** These databases are keyed to work
addresses, employer names and titles, so a consumer-webmail search returns a true
nothing while a full record exists. Quote Kaspr, who stated it plainly when
disclosing their own record: the address was *"generated by our own internal tool
based on your work experience"*. A competitor describing the practice is far
harder to wave away than a consumer inferring it. See `_DEFLECTIONS.md` §44.

**Exported copies are the operative ones.** A profile pushed into an employer's
or agency's applicant tracking system is beyond the broker's deletion and is the
copy that gets acted on. Ask who received it and ask for them to be directed to
delete.

**Watch for the FCRA line.** Some talent products are treated as regulated
consumer reports and therefore outside state deletion rights; others are not. Ask
which, rather than assuming — and if the answer is that a product is
FCRA-regulated, pivot to what the FCRA *does* give: file disclosure from the
agency, and a dispute route for anything inaccurate.

**Do not supply a LinkedIn URL to one of these.** Same reasoning as the B2B
prospecting section: it is a stable, unique, employer-linked key, and if no record
exists the search assembles the match it claims to test. The exception is a broker
that has already sent you the scraped profile — it cannot re-learn what it has
shown you.


## Email engagement and deliverability data  (e.g. AudiencePoint, Validity, eDataSource)

A category that is easy to miss because there is no profile page and nothing to
search for. These companies hold **behavioural data generated by the act of
reading email** — open times, open frequency, click behaviour, device and client
type, engagement and deliverability scores — keyed to an email address, usually
hashed.

**The consent framing is the strongest part of the letter.** Nobody deliberately
discloses when they open their mail. Say so:

> It is information I never knowingly provided to anyone — it is generated by the
> act of reading mail, which is not a disclosure a person makes deliberately.

**Ask for the inferences, not just the events.** Predicted best-time-to-send,
inferred timezone, inferred waking or working hours, activity pattern. **A model
of when someone is awake and at their phone is a behavioural profile**, and it is
the part with the least visibility to the subject.

**Search hashed forms explicitly.** This data is routinely keyed to a hashed
address rather than plaintext, so a plaintext-only search returns a truthful
nothing. Draw the usual distinction: hashes kept for suppression are fine and
should not be deleted; hashes held as matchable inventory are the ask.

**The email addresses are the whole letter.** Postal addresses and phone numbers
are near-useless here — include them for completeness but lead with every email
address the person has ever used, including dead ones. **Engagement history
outlives the mailbox**: an address closed in 2015 can still carry years of
recorded behaviour.

**Expect a processor answer**, and pre-empt it. These businesses typically sit
between email service providers and senders, so "we process on behalf of our
clients" is likely true — and useless without names. Ask for the categories of
source at minimum.

**Watch the registered contact.** AudiencePoint's California registration
nominates a `security@` mailbox. That is not obviously a privacy channel, so open
by saying so and asking for a forward rather than assuming it will be routed.
See `_SILENT_FAILURES.md` §83 and §85 on registered contacts that are not
consumer channels.
