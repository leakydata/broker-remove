# Tailoring requests by broker category

A generic people-search letter under-asks at companies that aren't people-search.
What "delete my data" means depends on the business model, and naming the right
artifacts makes the request harder to sidestep.

## People search / background reports
Standard letter. Add: cover the *full record set* (criminal, court, property,
relatives), not just the directory listing. Ask that suppression apply to phone,
address and email lookups — **not only name search**, which is how PeopleConnect
scopes theirs.

**Scope the suppression to the person, not to the identifier** (§154). Ask them to
*search* on prior addresses and disconnected numbers, and to suppress the records
that are about you — never to suppress an address or a number in itself. Those
addresses have new residents and those numbers have been reassigned, and a company
that does what is literally asked will remove strangers from its file. Saying this
explicitly also pre-empts a refusal from the companies that have thought about it.

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

**The industry-wide levers come first.** Before writing to individual mailers, two
registrations do more than any single letter, and a broker volunteered both:

- **DMAchoice** (ANA/DMA mail preference service) — one registration most US direct
  mailers subscribe to, lasting ten years. It is the postal analogue of California's
  DROP, and **unlike DROP it is not state-restricted**, so it works for a consumer
  in a state with no privacy statute (§151). A company cannot register on the
  consumer's behalf; the individual must do it.
- **optoutprescreen.com** — prescreened credit and insurance offers, free, and can
  be made permanent by posting a signed form.

Neither replaces the letters — a mailer that ignores DMAchoice is unaffected, and
neither touches the compiled file itself — but they suppress the *output* across the
industry while the letters work one company at a time.

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

## Skip tracing  (e.g. Kind Skiptracing)

The customers are debt collectors, process servers, repossession agents, bail
bondsmen, investigators and increasingly landlords. The product is locating a
person who has not been findable by ordinary means. That makes four things worth
asking that the standard letter does not reach.

**1. Stored file, or compiled at query time?** This decides whether a deletion
means anything. If the file is assembled on demand from credit header data,
utility and telecom connections, public records and other brokers' APIs, there may
be nothing stored to delete — and a deletion confirmation would be *true and
worthless at the same time*, with the next search returning the person exactly as
before. Ask which architecture it is, say plainly that "we compile at query time"
is a complete answer, and name the substitute you want if it is: **suppression
applied at query time**, plus the upstream source names so you can go to them
directly.

**2. The access log — who has looked you up.** This is the ask specific to the
category and probably the most valuable thing in the letter. For a skip tracing
service the search log is not incidental: it records *who has been trying to find
this person, when, and on what stated basis*. Request, under the right of access,
the date of each search, the customer or **category** of customer, the permissible
purpose claimed, and what was returned. Offer the fallback yourself — categories
and dates without customer names is still substantive — and say that a **nil
result against the named identifiers is a real answer**, because by §138 it is
something only this request could have produced.

**3. Which framework, asked neutrally.** Either they treat output as a consumer
report under the FCRA, in which case also request the **§ 609 file disclosure and
the list of everyone who has obtained it**; or they take the non-FCRA position, in
which case the state consumer privacy statutes apply *without* the FCRA exemption
and the request stands in full. The positions are exclusive. Raise both so
whichever applies does not cost a round trip. Ask separately whether any data
derives from **credit header** records and from which agency, so the source can be
approached too.

**4. Whether a consumer suppression list exists at all.** Ask it as a yes/no, and
ask whether it is honored across every product and every customer or only some.
The reason to ask bluntly: a service whose function is defeating someone's efforts
not to be located is one where **the ability to be excluded is the only protection
the searched-for person has**, and the person who most needs it is the least
likely to know it exists. "We have no such mechanism" is a more useful answer than
a confirmation implying a protection that is not offered.

**On the identifiers.** Prior addresses and disconnected numbers matter more here
than anywhere: a skip trace is built precisely out of that trail, so a search
scoped to current details misses the part of the file that makes it a skip trace.
But note the §144 tension is sharpest in this category — writing to a
people-locating company hands it a fuller identifier set than most of its searches
start with. Send the list, and ask them explicitly to be particular about the
retention clause.

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

**Cite the BDEX result when asking them to search prior identifiers.** The
instruction "search every address, not only the current ones" reads as boilerplate
and is easy to skim past. One concrete result makes it an argument:

> Another identity-data company ran my full twelve-address list this week and
> reported that four matched — and all four were addresses at providers that no
> longer exist. Not one currently-used address matched. Records keep whatever
> identifiers were current when the data was acquired, so the abandoned ones are
> the live keys.

That converts a request into a reason, and it pre-empts the search that would
otherwise return a truthful nothing. See `_SILENT_FAILURES.md` §87.

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

### Two asks that only work on scraped-data companies

**"Generated or observed?"** Ask whether any work email, phone number or role
attributed to you was **constructed from a pattern** rather than collected. Kaspr
volunteered exactly this distinction — their record's email was *"generated by our
own internal tool based on your work experience"* — and once one company has said
it, the question is answerable rather than accusatory.

It matters beyond curiosity: a constructed identifier is one the subject never
used, cannot confirm, and **may simply be wrong**, attributing them to a company
or role that is not theirs. That is a correction issue as much as a deletion one,
and correction rights survive in places deletion rights do not.

**Suppression matters more here than anywhere.** A record built by scraping public
sources is rebuilt by scraping them again. A deletion without a standing
suppression entry is undone by the company's own next collection cycle — not by a
supplier, not by a client, by them — and the confirmation email reads identically
either way. Say that plainly; it is the most obviously true version of the
suppression argument and the hardest to wave off.

### The stale-affiliation point

Scraped professional records persist long after the affiliation ends. If the file
shows a current employer or institution that the subject has left, **it is not
merely out of date — it is being sold as a present fact about them.**

Ask three things: what affiliation the record asserts, whether it is marked
current, and deletion either way. This is often the most concrete harm in the
category and the easiest for a company to check.


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


## Real-estate investor lead platforms  (e.g. BatchLeads, PropStream, PropertyReach, Leadsherpa)

A subtype of the property-data category above, and the asks differ enough to be
worth separating. These products exist so investors and wholesalers can pull a
list of owners and start dialling.

**Concede the deed immediately** — same as the property variant. Deeds,
assessments and mortgages are county records and no consumer can claw them back.
A letter that ignores that invites a true and useless reply.

**Then go for the append, which is the whole point.** The county published a
property and an owner name. It did **not** publish the owner's mobile number.
That number was skip-traced from somewhere else and bolted on, and it is what
produces the calls and texts:

> The deed is a county record I cannot claw back, but the phone number bolted
> onto it is not a public record and is what produces the calls and texts. Please
> tell me which of my telephone numbers and email addresses are attached to any
> property record, and delete them.

**Distress scoring is the ask with the sharpest edge.** Likelihood-to-sell,
motivated-seller, absentee-owner, equity position, pre-foreclosure, financial
distress. Worth naming plainly why it matters rather than listing it neutrally:
**a distress score is a signal to contact someone precisely when they are least
able to deal with being contacted.** That sentence lands, and it is true.

**Exported lists are the operative copies.** The platform's purpose is bulk
export. Ask how many times a record was supplied and to whom — a deletion at
source leaves every downloaded CSV intact.

**Do-not-call held independently of the property record**, and specifically
**do-not-skip-trace**: these platforms re-run enrichment on demand, so a number
deleted today is re-appended the next time somebody pulls that address.

**Search every prior address.** A property record follows the address and an
owner record follows the person, so the two diverge — a search limited to the
current address finds the least interesting record and misses the rest.


## Ad-serving and bidding infrastructure  (e.g. Beeswax, Adprime, AdsWizz, adtech DSPs)

Distinct from the audience-data companies above: these run the **pipes** rather
than owning the audience. That changes the opening move.

**Lead with the controller/processor split, and make naming the price of the
deflection.** Data may sit with them for their own account — an identity graph
entry, a segment they build — or be processed for a customer running campaigns on
their platform. Both are plausible, and the second is a legitimate answer:

> I am not trying to make you answer for something that is not yours. But "we are
> only infrastructure" without naming the controller leaves me with a right and
> nobody to exercise it against — which in practice is no right at all.

That framing concedes the point and still extracts something usable. See
`_DEFLECTIONS.md` §50 and §52 for the same move against a processor claim.

**The ask that matters is the bid stream.** Impression and bid records attach a
device to the sites and apps where it was seen. That is **a browsing history by
another name**, and it is the single most revealing thing in the category — it
can indicate health conditions, finances, religion, politics and sexuality
without any of them being declared. It is also exactly what a contact-shaped
deletion misses, because there is no name on it.

Ask for it explicitly, including the site and app list, not just "any data
associated with me".

**Then the standard identity-graph asks:** hashed match keys with the
suppression-versus-inventory split, cookie/device/CTV identifiers, any persistent
pseudonymous ID the platform assigned, **the edges** between those and real-world
identifiers, IP-derived household association, and segment memberships as
inferences rather than facts.

**Pre-empt the browser opt-out.** It will be offered. Device-scoped, dies when
storage is cleared or the device is replaced, and does nothing about server-side
records keyed to a hashed email. Say so before they say it, so the reply has to
engage rather than redirect.


## Health-adjacent brokers: ask what they are before writing

A broker whose name suggests health, life sciences or biotech should get a
**categorisation question first**, not a health-data letter. The name may mean
patient data, prescriber data, clinical trial records, or nothing medical at all
— and each needs a different request.

  1. Health, condition, treatment, medication or diagnosis data, or anything
     **inferred** about health from other signals.
  2. Healthcare **professional** data — prescribers, practitioners, affiliations.
  3. Clinical trial, patient registry or research participation records.
  4. Consumer contact or marketing records with no health dimension.
  5. Something else.

**Why the branches matter.**

**On (1), ask specifically whether any health attribute is inferred rather than
reported.** This is the sharpest question in the category. An inference is neither
verifiable nor correctable by the person it describes, it can simply be wrong, and
it is acted on by insurers, employers and advertisers who never see the
uncertainty. Say why it matters rather than listing it neutrally:

> Health information is the category where a general assurance tells a person
> least and where being wrong costs most — an inferred condition attached to a
> name is acted on by others, and the person it describes never sees it.

**On (2), a hit is a misattribution, not a privacy problem.** If the subject is
not a healthcare professional, a prescriber record bearing their name is a wrong
record about someone — and **correction matters as much as deletion**, because a
wrong record can be acted on by a third party. Say so explicitly; it changes what
you are asking for.

### Pre-empt the HIPAA deflection

Expect "this is health data, HIPAA governs it, your state request does not
apply". Answer it before it arrives, and concede the legitimate part:

> If you consider any of this data to be covered by HIPAA rather than state
> consumer privacy law, please say so and identify which elements. That is a
> legitimate distinction and I will not argue it — but I would note that data
> held by a broker outside a covered entity or business associate relationship is
> generally not HIPAA-protected, which is precisely why a consumer request is the
> only route available to me.

That is accurate, it is not adversarial, and it closes the escape route without
accusing anyone of trying to use it.

**Also invoke the sensitive-data right.** Several state statutes treat health
information as sensitive personal information with a separate right to **limit
its use and disclosure**, which survives independently of a deletion right. Ask
for both.


## Nonprofit and donor platforms  (e.g. Blackbaud, DonorSearch, iWave, Kindsight)

These sit in **two positions at once**, and conflating them wastes the request.

**Position one: service provider.** Most individual records are hosted for
nonprofit, educational and healthcare customers running their fundraising or CRM
systems on the platform. A deletion request for that data properly goes to the
organisation. **Concede this immediately** — it is true, and a letter that ignores
it invites a reply scoped entirely to it.

**Position two: data broker.** These companies are *registered* as data brokers,
which is a determination that they sell or share personal information about
people **with whom they have no direct relationship**. That is a different
dataset and it is what the letter should target.

### The ask that matters: wealth screening

Capacity-to-give ratings, estimated net worth, real-estate value, philanthropic
propensity, major-gift likelihood. Name them, and say plainly why:

> These are inferences you generated rather than facts I supplied, they are shown
> to fundraising organisations who then decide how to approach me, and the person
> they describe never sees them. **An estimate of what someone can afford to give
> is a financial assessment made without their knowledge.**

That framing does more work than a list, because it identifies the harm rather
than the category.

### Ask which customer organisations hold you

If the answer is "go to the controller", the controllers must be named or the
right is unexercisable. Offer the alternative that a service provider is
generally required to assist with:

> If that is commercially or contractually restricted, please say so plainly, and
> please pass this request to them on my behalf instead.

### Where a breach is in the picture

Ask directly and without accusation, and connect it to the same gap:

> A person who cannot find out which organisations hold their data through your
> platform also cannot find out whether they were affected by a breach of it, and
> those two gaps are the same gap.

That reframes a breach question as a scope question, which is answerable, rather
than as a grievance, which is not.

### Search the institutional address

Donor and alumni records are decades old and keep whatever address was current
when the gift or enrolment was recorded. A `.edu` address and the postal
addresses contemporaneous with the affiliation are the highest-value keys here —
flag which prior addresses map to that period, since it narrows the search for
them.

## Political data / voter file enrichment

**Example:** Catalist.

**What they hold.** A national voter file — registration status, party where the
state records it, and vote history — joined to purchased commercial data and then
scored: partisanship, ideology, turnout likelihood, issue support,
persuadability.

**The deflection to expect, and it is half right.** Registration and vote history
are public records in most states. The company did not create them and cannot
unmake them at the county or state level. Conceding this immediately is what
makes the rest of the letter answerable.

**What the concession does not cover, and this is the whole ask.** The modelled
scores are not public records. No election authority holds a persuadability score.
They are inferences the company generates, they are personal information under
CCPA/CPRA, and they are the part of the file a person can neither see nor correct
anywhere. Neither is the commercial append — household composition, income or
wealth estimates, lifestyle segments, and phone numbers and email addresses that
came from no registration form. Nor is the identity linkage joining the voter
record to hashed emails and device IDs for advertising.

**Ask for three things separately** so the public-record answer cannot swallow
the letter:
1. modelled scores, by name;
2. commercial append **and its suppliers** — then write to those suppliers;
3. identity linkage to online identifiers, edges included.

**Search-key note.** A voter file is address-history-keyed by construction. It
will hold superseded registrations under prior addresses. Lead with the address
history and say explicitly that superseded registration records are in scope.

**Why it matters more than most.** A score about a person's politics, built
without their knowledge and sold on, is among the records people are most
surprised to learn exists.

## Search-intent data

**Example:** Captify (Verve).

**What they hold.** What people typed into search boxes across a publisher
network, turned into keyword and intent segments keyed to cookie and device IDs.

**The argument that distinguishes this category.** Search queries are **content,
not metadata**. A record of what someone searched for can disclose health
concerns, financial difficulty, legal trouble, relationships and beliefs — none
of which the person intended to publish, and all of which they would have
described as private had anyone asked. Say so, ask for stored query text,
query-derived keywords and intent segments by name, and ask specifically whether
any segment touches health or financial condition. A company that would quietly
delete a row may still tell you a sensitive segment existed if you ask about it
directly.

**Otherwise** it is a standard identity-graph letter: a name search returns
nothing, so ask for hashes, cookie/MAID/CTV IDs, household-IP linkage, and the
edges.

## Creator / influencer intelligence

**Example:** Captiv8.

**What they hold.** Profiles of people who post publicly, with audience
demographics, engagement metrics, estimated earnings, brand affinity and reach
scores.

**The deflection to expect:** "it came from a public profile."

**The answer.** A public post is a thing *you* published. A scored, ranked,
searchable dossier assembled from thousands of them and sold to brands is a thing
*they* created. The scores — audience composition, engagement quality, estimated
rates, brand fit — exist nowhere but in their database and were never published
by anyone. Ask for those by name, separately from the collected fields.

**Search-key note.** Records are keyed to **social handles**. Say so and ask them
to search handles, not only names and emails, or a truthful "no records found"
will come back while the profile sits untouched.

## Dealer management systems / automotive retail

**Example:** CDK Global.

**The deflection to expect, and it is largely right.** They supply software to
dealerships and process each dealer's data on that dealer's behalf. Concede it;
you are not asking them to alter a dealership's system of record.

**The question that survives the concession:** then why is the company a
*registered data broker*? Somewhere data leaves the processor role. Ask for:
cross-dealer consolidated profiles joining service and purchase history from
multiple dealerships into one consumer record; in-market-shopper and
equity-mining products built from it and licensed onward; identity linkage to
advertising identifiers; and VIN-linked ownership and service records.

**Why it is worth the letter.** Automotive data is a category people rarely
realise is traded, and it is unusually durable — a service visit from a decade
ago outlives the car, and the record is keyed to whatever address and phone
number were current at the time.

## Card-linked / purchase-history marketing

**Example:** Catalina Marketing; Bridg (Cardlytics).

**Concede first:** the underlying transactions belong to retailers, manufacturers
or banks, and those are their systems of record.

**Then ask for what the company itself builds:** the *linked shopper identity*
that ties purchases across visits and across retailers into one person. That
linkage exists in no single retailer's file. It is what turns transactions into a
profile, and it is theirs.

**The search-key problem is acute here.** Records are keyed to loyalty-card
numbers, frequent-shopper IDs, or retailer-issued household keys. The consumer
cannot supply any of them. Say that plainly and **ask what they can accept
instead** — putting the burden where the knowledge is, rather than letting an
unmeetable identifier requirement quietly end the request.

**Ask for the sensitive inferences by name:** dietary, health-adjacent,
household-composition, income and life-stage. Purchase data is unusually
revealing about exactly those.

**Verification note.** Payment-adjacent brokers tend to ask for a card number or
its last four digits. Rule that out in advance, in the first letter.

## Biometric / facial recognition

**Example:** Clearview AI.

This is the category where the usual letter is least adequate, because the thing
worth deleting is not the thing the company collected.

**The faceprint is the thing, not the photograph.** An image scraped from the open
web is a copy of something already visible. The **biometric vector** computed from
it is not — it is generated by the company, exists nowhere else, and is what turns
an unremarkable photograph into a searchable index entry tying a face to a name,
an employer, an address and every other image of the same person online.
Deleting a stored JPEG while retaining the vector, the hash or the cluster
identity fulfils nothing. **Ask for explicit confirmation that the biometric
templates are deleted, not only the images.**

**Suppression matters more here than almost anywhere.** These databases are built
by continuous crawling. A deletion without a durable do-not-re-enrol entry is
undone by the next crawl of the same public page, and the person has no way of
knowing. If maintaining that entry requires retaining a vector of the face solely
to recognise and exclude it, ask them to say so and confirm it is used only to
exclude, never to return a match — the same suppression-vs-inventory question as
hashed email, with higher stakes.

**Ask for the search history.** Has any client query ever returned a result
matching you, how many times, over what period? Clients include law enforcement
and government agencies. A person who has appeared in such a search has an
obvious interest in knowing, and no other way to find out. If they will not
disclose it, make them say so and say why rather than let the question go
unanswered.

**Ask for the source URLs.** Which pages were the images collected from? You can
then approach those sites. It is trivial for the company and impossible for you.

**Pre-empt "publicly available."** Publication makes an image viewable by people
who visit that page. It does not make the subject **searchable by face across the
whole internet by anyone holding a photograph of them**. The second capability
was created by the company, and it is the one the request is about. These are
different questions and the letter should say so before the reply conflates them.

**The verification trap, which is specific to this category.** The standard ID
demand is worse here than anywhere else: it asks a person to hand a facial
recognition company a **new, high-quality photograph of their face** plus a
document bearing their legal name, in order to be removed from a facial
recognition database. That is materially more identifying data than the removal
itself concerns. Refuse it with that reason stated, and ask for a clear answer as
to whether an alternative exists — a recorded refusal is more useful than an
unmeetable requirement left hanging.

## Collector / hobby data

**Example:** Collectors DataStore (Ludex).

Worth writing to precisely because nobody thinks to. Ask for **collection
contents and valuations, purchase and sale history, marketplace activity, grading
or submission records, consignment and auction participation** — not merely
whether a contact record exists.

**The argument:** an inventory or valuation held against a named person is a
statement about their assets. What someone collects, what they paid and what they
own is financial and personal information, and a valuation is an inference the
company generated rather than a fact anyone supplied.

## Academic / researcher and prescriber data

**Example:** Clarivate (Web of Science, ProQuest; DRG on the life-sciences side).

Two sub-categories that a general search will not reach, so name both:

1. **Researcher and author profiles** assembled from publications, affiliations,
   co-authorship and citation records — **including automatically generated
   profiles the subject never created and may never have seen.**
2. **Healthcare-professional, prescriber, referral and key-opinion-leader
   datasets**, which are compiled *about* individuals rather than collected
   *from* them, and whose subjects are usually unaware they exist.

**The search-key point is the one that decides the outcome.** An academic record
is keyed to whatever **institutional affiliation** was current when it was
created. A search on present-day contact details misses it entirely. Supply the
old institutional email address explicitly as a search key — and if it is a closed
mailbox, say so in the same breath so nobody replies to it. (See
`_SILENT_FAILURES.md` §87: the identifiers that match are frequently the ones
nobody would think to send.)

Ask for **influence, impact, tier or ranking scores** as inferences. Pre-empt the
B2B, professional-information *and* publicly-available exemptions together — a
compiled and scored profile is not the same thing as the public sources it was
compiled from.

## HCP credentialing and licence verification

**Example:** MedPro Systems.

Adjacent to the prescriber datasets above but a different animal, and the
difference changes what you are allowed to ask for.

**What they hold.** Practitioner and organisation licence status pulled from state
boards, the NPPES registry and federal databases, sold to pharmaceutical companies
so that drug-sample eligibility, DSCSA obligations, PDMA rules and Sunshine Act
transparency reporting can be satisfied. The file is a compliance instrument.

**Open with a do-not-suppress warning, not with the request.** This is the one
category where a careless removal has a named victim. A suppression applied on
name alone can pull a real practitioner out of the file that governs whether they
can be engaged and whether their employer can report accurately. On a common name
that is not a hypothetical. So the first paragraph should say: match against the
**full** identifier set, and if the only candidates are licensed practitioners
whose details do not match, *"no match found" is the correct answer and the one I
would rather have.* (`_SILENT_FAILURES.md` §153, §154.)

**Concede the public-record half immediately.** Licensing-board and NPPES data is
public record, deletion rights do not reach it, and you are not asking anyone to
alter a licensing record. Say so. The concession is what earns the next paragraph.

**The wedge is everything that is not the licence.** These companies also sell
commercial data solutions, pre-commercial packages and HCP engagement platforms,
and describe "first- and third-party data collection and validation". Ask three
things:
  (a) any record in a dataset **other than** a publicly-sourced licence file;
  (b) whether any dataset contains **non-practitioners** — purchased contact data,
      or people appearing as staff, contacts or recipients;
  (c) engagement records, **transfer-of-value or spend records**, sample-request
      history, event and interaction data.

**Expect and ask for a nil result — in the right form.** Most subjects are not
HCPs. Say so in the letter, then ask for the nil result *against the named
identifiers* rather than a bare "your request has been processed", which is
compatible with no search having run at all (§138).

**Do not supply an NPI, DEA number or licence number** you do not have, and say
you have none — it forecloses a verification demand for a credential that does not
exist.

## Applicant tracking / HR software

**Example:** ClearCompany.

**Concede the processor role** for a client's own applicant tracking system. Two
things survive it:

1. **Sourced candidate and talent-pool data** assembled independently of any
   application — enriched contact details, passive-candidate profiles. That is
   the vendor's, not a client's. Include **derived work addresses**: ask them to
   construct `first.last@` patterns from your employment history and search those.
   You cannot list addresses you have never owned; they can generate them.
2. **Retention after the fact.** Applicant records outlive the role, the
   requisition and sometimes the employer, sitting searchable long after any
   relationship ended. Ask **which employer** each record relates to — naming the
   client is the part you cannot do for yourself.

Ask for **fit, match, ranking and screening scores**. A person who has been scored
by a hiring system has an interest in knowing it happened.

### A reusable line for any processor deflection

> *"If your answer is that you act only as a service provider and hold nothing in
> your own right, please say so explicitly, and say whether the opt-out will
> nonetheless be propagated. A processor that cannot delete can usually still
> suppress."*

That converts the processor answer from a dead end into a partial win, and it
costs nothing to include in the first letter.

## Location data

**Example:** Cuebiq.

The hardest category to make a request in, because the record is keyed to a
mobile advertising identifier and **nobody can supply their own**. A MAID is not
reliably surfaced to the person it describes, a resettable one may have changed
many times over the period the history covers, and any value readable off a phone
today will not match the historical rows. The identifiers that *would* match are
exactly the ones the subject has no way of knowing. If a MAID is the only accepted
key, the right is exercisable only by someone holding information the system is
designed not to give them.

**But location data has a property that makes verification possible anyway.** A
person's home is where their device dwells overnight, persistently, for months or
years. So offer this, concretely:

> *"Query your data for devices showing a persistent overnight dwell pattern at
> the residential addresses listed below, over the periods I lived at each. Then
> **confirm the match back to me before deleting anything** — tell me how many
> device identifiers matched and over what date ranges, and let me confirm the
> periods are right."*

Confirm-before-delete is what makes this safe to offer and hard to refuse: no
other person's records can be touched, because nothing is deleted until the
subject verifies. It preserves the entire protective purpose of verification while
using only information the subject can actually supply.

**Two details that make the offer read as good faith rather than a fishing
expedition.** First, list only *residential* addresses — **omit PO boxes and say
why**: a device does not dwell at a post office box overnight, so including them
would only add noise. Second, close with *"if this specific method does not fit
your systems, please tell me what would — I am asking you to name a route that
exists, not to waive the check."* Both signal that you understand their problem
and are trying to solve it with them.

**Ask about sensitive-location inferences by name** — places of worship, medical
facilities, legal offices, shelters, union halls, protest sites — and say you want
to be told **even where they conclude they may retain them**. Location history is
unusually revealing about exactly those, and being told one exists has value on
its own.

**Suppression must be forward-looking**, or the next feed from the same app
publisher restores everything. And **ask for the app publishers and SDK partners**
by name: that is the upstream, it is invisible from outside, and it is trivial for
them to state.

## Customer data platforms

**Example:** DataDojo.

A CDP's entire function is identity resolution — joining fragments from many
sources into one persistent profile. So say plainly: **the linkage is the thing.**
Deleting attribute rows while keeping the resolved profile ID, the match keys, or
the mappings between identifiers does not fulfil the request, because the profile
is rebuilt from the next inbound feed and the person never learns of it. Ask for
confirmation that the **edges** are deleted.

**Pre-accept the service-provider answer, then ask what defeats it.** Where a CDP
resolves identity inside a customer's own tenant on that customer's data, the
customer is the controller. Fine. But the company is a *registered data broker*,
so ask which of these exists:

1. a cross-customer, shared or reference identity graph;
2. enrichment or append data supplied *by* the CDP rather than received;
3. audience or segment products built from resolved profiles and licensed onward.

**Pre-commit to accepting "none of these exist" as a complete answer** — provided
they then name which customers hold matching records, and confirm suppression
applies regardless.

## Content syndication / intent data

**Example:** Contentgine.

**The argument that carries this category:** content engagement is behavioural
data about a person. A record that a named individual downloaded a particular
white paper, at a particular time, is a statement about their interests and their
employer's purchasing intentions. It is more revealing than a contact record, and
it is the part of the file the person has no way to see.

Ask for **which assets, which dates, and which clients received the resulting
lead**. The last is the one that matters — once a lead has been sold it is beyond
the seller's control, so knowing where it went is the only way to follow it.

Pair with the derived-address ask and the LinkedIn URL suppression
(`_SILENT_FAILURES.md` §90); this sector is where both bite hardest.

## Crawling businesses

**Example:** Crawlbee.

Say it outright in the letter: **suppression is the request, deletion alone
achieves very little.** A record deleted today is re-created by the next crawl of
the same page, and the person has no way of knowing it came back.

So invert the usual letter. Lead with the **source URL** as the thing to suppress
on — for a crawler, the source *is* the key — and make the deletion the rider
rather than the headline.

Then ask for the **source URLs they hold**: which pages the data about you was
collected from. Trivial for them, impossible for you, and it hands you the next
set of places to approach.

## Nonprofit fundraising / donor data

**Example:** RKD Group (registered as Data Management).

Two categories to name explicitly:

1. **Donor and giving records** — giving history, gift amounts, donor status,
   nonprofit affiliations. **Whom a person supports can reveal their religion,
   politics, health circumstances and family situation**, and it is among the most
   private information most people hold. Ask what the record says and which
   organisations it relates to.
2. **Capacity and propensity scores** — wealth estimates, capacity-to-give
   ratings, giving-likelihood and major-donor scores. An estimate of what someone
   can afford to give is a financial assessment made about them without their
   knowledge.

Ask both directions of the chain: which suppliers supplied the record, and which
client organisations received it. Donor files are address-keyed and often decades
deep, so lead with the address history.

### A rider for market-research firms

If the company conducts or supplies data for **surveys or market research**, ask
that panel membership, survey responses and call records be treated as in scope,
and that the do-not-call entry cover **research calls as well as marketing ones**.
Research calls are commonly treated as outside DNC rules, and almost nobody
expects that.

## Skip tracing

**Examples:** DataSkip; DealMachine (skip trace bundled with property leads).

Skip tracing is the business of locating a person who is *not readily locatable* —
assembling current address, telephone, employment, relatives and associates from
sources the subject never gave anything to. Three things need separate answers.

**1. The relatives-and-associates graph is the product.** A skip-trace record does
not merely describe you; it holds **edges** connecting you to household members,
relatives, former co-residents and known associates. Those edges are personal
information about you, and they are what makes the record useful. **Deleting your
row while retaining you as a linked associate on someone else's record does not
fulfil the request.** Ask for the links to go in *both* directions.

**2. Suppression is the entire request.** The product exists to reassemble a
person's whereabouts from continuously refreshed public and commercial sources. A
one-time deletion is undone by the next refresh, and the confirmation reads
identically either way. Insist on **forward-looking** suppression, and ask which
list any retained identifier sits on.

**3. Ask whether a report has been run.** Not *who* ran it — do not ask them to
identify a user, which they will refuse and which invites a refusal of the whole
question. Ask only whether a locate report on you exists in their logs, how many
times, over what period. **A person who has been the subject of a skip trace has
an obvious interest in knowing and no other way to find out.** If they decline,
make them decline explicitly.

Pair with the FCRA-in-the-alternative fallback: if some data is a consumer report,
ask for the §609 file and its sources, deletion of anything held *outside* the
regulated file, and non-FCRA suppression.

**Search-key note:** an address history is not incidental to a skip-trace record —
it *is* the record. Lead with it.

## Pre-date / social screening

**Example:** Date Detective.

The defining feature: **the subject of a report is never the customer.** Any record
was assembled so somebody else could read it, and the subject would never know it
existed.

**The ask that matters most is accuracy, not just deletion.** Reports of this kind
routinely mismatch on common names. Supply your **date of birth deliberately** as
the disambiguating field and ask directly: *has another person with my name had
their records attached to my identifiers?* A false criminal or court record in a
screening product does real and untraceable harm — the subject never learns why
someone stopped replying.

Also ask whether a report has been run (not by whom), and whether the service
claims **FCRA** status. If it does not, note that it therefore must not be used
for employment, tenancy or credit decisions — and ask which position they take.

## Consultancies and other non-obvious registrants

**Example:** Deloitte Consulting LLP.

Occasionally a firm appears in a state broker registry that does not look like a
data business at all. The letter almost writes itself, and the structure is
reusable:

**Concede every obvious deflection up front, so none of them can consume the
reply.** For a professional services firm that is: processing on behalf of clients
as a processor; HR and applicant records; privilege and audit-retention
obligations. Grant all three in the first paragraph.

**Then make the point they cannot answer with any of them:**

> *"None of that explains a data broker registration. Registration is required of
> an entity that sells or shares personal information about consumers with whom it
> has no direct relationship. So: what activity caused this entity to register,
> and does it involve personal information about me?"*

**Pre-commit to accepting a one-sentence answer.** If the registration reflects a
narrow activity that does not touch you, say you will take that and stop. It costs
nothing, it makes the reply cheap to write, and it must be honoured.

## Website-visitor identification

**Example:** Dealfront / Leadfeeder.

These products resolve website visitors from IP and related signals. Ask
**carefully**, because the honest answer may genuinely be *company-level only* —
and if it is, there is no personal information to delete.

Three questions, in this order:

1. Is any visitor record ever resolved to, or linked with, an **individual**
   rather than only an organisation — by joining an IP or cookie to a contact
   record, an email hash, or a device identifier?
2. Are **IP addresses** retained, and linked to any identifier of yours?
3. **If both answers are no, say so plainly — that is complete and will be
   accepted.**

The reason to ask this way: company-level and individual-level resolution are
described in *very similar marketing language*, and the difference is the whole
question of whether the product processes personal data at all. Asking accusingly
gets a defensive non-answer; asking precisely gets a usable one.

**If the vendor is EU-established** (Dealfront Finland Oy is), frame it under GDPR
Articles 15, 17 and **21** — and if they rely on legitimate interests for B2B
prospecting, state explicitly that the letter **is an Article 21 objection** and
ask for the outcome. Offer CCPA or their own published policy in the alternative.

## Job boards and resume databases

**Example:** Dice.

The framing that matters: these companies do not only run a place to apply for
jobs. They sell **recruiter access to a searchable candidate database**, which
makes a profile a *product* rather than a service. Four asks:

1. **The resume itself** — one of the densest personal records a person ever
   creates: employment history, education, dates, skills, often an address and
   telephone number, all in one document.
2. **Records created without an application** — sourced, enriched or inferred
   profiles the person never made. Include **derived work addresses**
   (`first.last@employer`), which the subject cannot list because they have never
   owned them but the company can generate from a name and employment history.
3. **Search and view history** — has the profile been returned in recruiter
   searches, or viewed, how often, over what period. Ask **whether, not who**: the
   same principle that works in skip tracing (§ *Skip tracing*). Asking for the
   recruiter's identity invites a refusal that swallows the whole question.
4. **Inferred attributes** — skill inference, seniority and salary estimates, and
   especially **job-change-likelihood or "open to opportunities" scores.** A
   prediction that someone is likely to leave their job is a record they never
   agreed to, cannot see, and which could do real damage if it reached their
   current employer.

**Search-key note:** a job-board account may be a decade old and keyed to whatever
email address was current when it was created — frequently a university or former
work address. Supply those explicitly.

## Comment platforms and embedded widgets

**Example:** Disqus.

A comment platform that is also a **registered data broker** — and the two facts
together are the whole letter. Two scopes, and they need separating.

**1. Comment history is speech.** A record of what someone said, on which sites,
when, and in what order. The sensitivity is not in any individual comment; it is
in **the aggregate across years and sites**, which can disclose politics, religion,
health circumstances, employment grievances and family details. Unlike a purchase
record, it is in the person's own words. Ask for it explicitly, including comments
whose *visible* author name is a pseudonym but which are linked internally to an
account or email address.

**2. The part people do not expect.** A person who leaves a comment knows they
published a comment. They do not generally know that a widget embedded across
many thousands of sites can observe **which pages they visited, whether or not
they ever commented.** Ask separately for pageview and session records **on pages
where you never commented**, plus the usual hashes, device identifiers, segments
and edges.

**Make them state their role.** If the platform is a service provider to
publishers for the comments but the controller for the advertising data, that
distinction decides who you write to next — so ask for it plainly, and ask whether
the opt-out propagates regardless.

## Data marketplaces and pass-through platforms

**Example:** DemystData.

These connect customers to many third-party providers and return attributes about
a person **on demand**, often without storing a consumer record at all. So invert
the usual letter.

**Grant the null before they claim it.** If the platform genuinely queries
providers in real time and retains nothing, the honest answer to a deletion
request is largely *"there is nothing here"* — say you will accept that, record it,
and not press. It costs nothing and it makes the rest of the letter answerable.

**Then ask for what they uniquely know.** If they hold little themselves, the
valuable thing is **which providers were queried**:

1. Which data providers were queried for attributes about you — or, if
   per-individual logging is not kept, which providers sit in the relevant
   product's supply chain.
2. Whether any **query log, cache or audit record** containing your identifiers
   exists, and its retention. *A log of who asked about this person, and when, is
   personal information about that person* even where the attributes were never
   stored — and it is easy to overlook because it is not "a record about you" in
   the way a profile is.
3. Whether any **derived attribute, score or model output** was generated by the
   platform rather than passed through. An inference is created, not relayed.

**And if they cannot name providers, ask them to relay.** *"A pass-through that
cannot disclose can often still forward."* Contractual confidentiality usually
blocks disclosure, not transmission.

This is `_SILENT_FAILURES.md` §100 applied on purpose rather than discovered after
the fact: a marketplace sits at exactly the point in the supply chain where "who
holds data about me?" is answerable.

## Co-operatives, list swaps and pooled audiences

**Examples:** DojoMojo / Proxima; donor co-ops such as DonorBase and Donor Bureau.

A co-operative pools data from many members. That changes what a deletion *means*,
and one question matters more than everything else in the letter:

**Is the suppression registered with the pool, or only with this member?**

In a co-op, a suppression held locally is undone the moment the next member
uploads a list containing you — and nobody is notified, including the company that
suppressed you. A local-only entry is not a removal; it is a pause of unknown
length.

Two more:

- **Which member contributed me?** You gave your details to *one* organisation,
  for one purpose, and had no way of knowing they were pooled. This is the single
  fact you cannot discover for yourself and they can supply in one line.
- **Which members received the file onward?** Once shared it is beyond their
  control, which is exactly why you need to know where it went.

For **donor** co-ops specifically, add the sensitivity argument explicitly: whom a
person gives money to can reveal religion, politics, health circumstances, family
situation and bereavements. A gift to a disease charity, a religious body, a
shelter or a hospice was a statement made **to that organisation** — not to a
commercial file. Then ask for cause/interest coding, capacity-to-give and
**bequest-propensity** scores, and **bereavement inferences**, which this sector
uses for legacy and in-memoriam targeting.

## Workforce and talent intelligence

**Example:** Draup. (Related: Coresignal, Revelio.)

Built by crawling public professional profiles. Three arguments, in order:

1. **"It was public" is not an exemption.** A public profile is something you
   published, on one site. A structured, queryable, resold dataset of your
   employment history is something *they* created.
2. **The inferred layer is what you cannot see** — inferred skills, seniority and
   salary-band estimates, role-fit scores, and above all **attrition or flight-risk
   scores.** A prediction that a named person is likely to leave their employer is
   a record they never agreed to, cannot see, and which could do real damage if it
   reached that employer.
3. **Suppression against the source, not deletion.** Crawl-refreshed data comes
   back; only a forward-looking entry keyed to the profile URL lasts (§90).

**Ask directly about inferred demographics** — gender, ethnicity, age or
nationality derived from a name, a photograph, an institution or a location. These
are common in workforce analytics, are used in ways subjects would rarely
sanction, and are frequently wrong. Companies will not volunteer them; they will
often confirm or deny when asked plainly.

## Contextual and programmatic advertising networks

**Example:** Media.net; MaxMind on the geolocation side.

**Concede first, because the concession is what makes the answer usable.**
Contextual advertising works from the page, not the person. If the file is keyed
to cookie identifiers, mobile advertising IDs and IP-derived geography, a name
search returns nothing — *not because the search failed, but because the name was
never a key.* Say that in the letter and say that you will record such an answer
as a real result. Otherwise you get a defensive reply about a question you were
not asking.

**Then ask the three that are actually answerable.**

1. **Is there an identifier-keyed store, and can any of it reach a person?**
   Cookie IDs, IDFA/AAID, hashed email, household or ISP-level geography, segments
   attached to any of those — and is any of it linkable, by them or by a partner,
   to a name or an address. *"Keyed only to identifiers the consumer cannot
   produce"* is an answer, and a useful one.

2. **The hashed-email wedge — the one identifier a consumer can actually supply.**
   You cannot read your own cookie ID, and sending a device ID to an advertising
   company would create the very association you are ending. But the industry's
   identity layer is keyed to hashes of email addresses, and you have those. So
   ask them to **do the hashing themselves**: normalise as their systems normally
   do (lowercased, trimmed, SHA-256, plus MD5 and SHA-1 if held) and search on the
   results. It derives nothing they could not already derive and hands over
   nothing new. Same move works on fraud-scoring vendors — see MaxMind/minFraud.

3. **Where does the opt-out actually live?** This is the question worth the
   letter. If the mechanism is a cookie set in the browser that visits the opt-out
   page, it is scoped to one browser on one device, absent from the phone, and
   destroyed by a cache clear — *stored inside the thing it is meant to protect
   against.* Ask whether a **server-side** opt-out persists against an identifier,
   and say plainly that "we honour opt-outs" and "we set a cookie" are different
   claims, only one of which survives a browser reset. Ask about **GPC** in the
   same breath: honoured, and recorded persistently, or respected only in-session?

**Do not supply an IP address, and say why.** It would hand a company that derives
geography from network addresses a fresh dated association between an address and
a named person — the opposite of the request. Offer to reconsider if they say what
they would do with it afterwards.

## Media intelligence and social listening

**Example:** Meltwater.

Not one database. **Ask about three holdings separately**, or a single "no record
found" will be true of one and false of another and nobody will notice.

1. **The media and influencer contact database** — journalists, editors, bloggers,
   creators, compiled without a relationship and licensed to customers. Search on
   name, addresses, employment history and profile URL, including lapsed entries.

2. **The social listening archive, and specifically the author entity.** Monitoring
   stores public posts. It also builds a persistent **person-level author record**
   accumulated across posts: inferred audience demographics, reach and engagement
   metrics, topic affinities, influence scores, sentiment history. Deleting post
   copies while keeping the entity is a half-deletion and the standard way this
   request fails while appearing to succeed. Ask directly whether the entity
   exists, whether they hold one, and whether a deletion reaches it. The derived
   attributes are personal information they *created* rather than collected.

3. **The news and editorial archive — and state the limit.** Say explicitly that
   you are **not** asking them to remove, alter or suppress journalism: it is
   third-party editorial content they did not write, and it would be wrong to ask a
   monitoring company to make published reporting harder to find. What is in scope
   is the **index and what is derived from it** — if a customer can retrieve "every
   article mentioning [name]", or there is a mention-count, person-entity or
   alerting subscription keyed to the subject, that is a person-level record they
   hold. Drawing the line yourself is what stops the whole letter being refused on
   free-expression grounds.

Then the family question: which product line the registration covers, and which
acquired or sibling brands draw on the same underlying data, so a deletion is not
undone by a sibling holding its own copy.

## Political and nonprofit messaging platforms

**Example:** Message Digital.

Distinct from the voter-file enrichment section above: these are the **senders**,
not the compilers — texting, email and a client-facing data warehouse, run for
hundreds of campaigns and causes at once.

**The controller/processor split, with the forwarding ask.** Some of what they
hold is held *for* a client on instructions; some is theirs, in the warehouse and
reporting products. Ask which is which, apply the request in full to the second,
and for the first use the Outreach move: *forwarding is not altering.* Ask them to
pass the request through to the client programs holding the number and to say that
they have. An explicit refusal to name clients is workable; silence is not.

**Central or per client? — and why the answer is decisive here rather than
academic.** If suppression applies across every program on the platform, one
request does what a consumer expects. If it is per client, stopping one campaign
leaves hundreds untouched and a consumer told "done" is badly misled. What makes
this different from an ordinary list company: **political and nonprofit messaging
does not sit under the federal DNC registry the way commercial telemarketing
does.** For anything sent through the platform, their internal suppression is not
one mechanism among several — it is the only one that exists.

**Inferred affiliation is sensitive, and belongs in a separate ask.** Which
programs hold a person implies party and candidate support and issue positions.
Ask for deletion — or use-and-disclosure restriction where deletion is impossible
— of inferred political affiliation, party scores, candidate and issue-support
attributes and donor propensity scores, *separately* from any contact suppression,
so a "we have suppressed your number" reply cannot stand in for it.

**Sources.** Voter file, commercial cell-append vendor, list exchange, or a
client's own collection. A named vendor tells you where to write next.

**And the §154 limit, which bites hardest here.** Do **not** ask them to add
disconnected historic numbers to a permanent do-not-text file. Those numbers are
reassigned; the suppression would land on whoever holds them now.

## First-party businesses on the broker register

**Example:** Marriott International.

Occasionally the register turns up a company the subject has an actual account
with. A blanket deletion letter can then cost them something real, and the letter
has to be built around that.

**Open by saying what you are NOT asking for**, in the first paragraph, in
capitals if necessary: not to close or cancel an account, forfeit points, or erase
a booking or billing record — and if the request would do any of those, *stop and
ask first.*

**Then split the ask by whether it destroys anything.**
  - **Unconditional:** opt-out of sale and sharing, and marketing suppression.
    These touch no account and destroy nothing.
  - **Conditional:** deletion only of what is *not* required for an active
    account, a completed transaction, a legal obligation or fraud prevention —
    which in practice means marketing profiles, inferred preferences, segments,
    propensity scores, and anything **acquired from or shared with third parties**
    rather than generated by the subject's own dealings with them.

**Ask the question the registration itself raises.** A data broker sells personal
information about consumers it has *no direct relationship with*. So what is the
data that made this company a registrant, and which activity involves people who
are not its customers? A one-line answer changes what to ask for next.

**Name the category-specific sensitivity.** For a hotel chain, stay history: where
a person was, on what dates, sometimes with whom — which can reveal a medical
treatment, a religious observance, a legal proceeding or a relationship. Ask for
use-and-disclosure limitation on it *separately* from deletion, since the two are
frequently mutually exclusive.

**Never send an account number, card number, passport number or SSN**, and refuse
them in advance.

## Vehicle and automotive intelligence

**Example:** Mobility Global (formerly S&P Global Mobility).

**The DPPA fork is the whole letter.** Ask first whether any data held, received or
derived originated — directly or through an intermediary — in **state motor vehicle
records**: title, registration, lienholder or driver-licence records. If it did, the
Driver's Privacy Protection Act (18 U.S.C. 2721 et seq.) governs, and two things
follow that follow from nothing else:

  - disclosure and any resale are lawful only under an **enumerated permissible
    use** — ask which one they rely on;
  - **§2721(c) requires a reseller or rediscloser to keep, for five years, records
    identifying each recipient and the permitted purpose.** Ask for those records as
    they relate to the requester: who received it, when, for what purpose. This is
    an access-log request with a *federal statutory hook* rather than an appeal to
    goodwill, and it is the strongest version of the access-log ask this project
    has. Require a named exemption if they decline.

If it did *not* come from motor vehicle records, ask where instead — dealer
management systems, service and repair records, warranty registrations, telematics,
finance and lease records, purchased marketing files. Each has a different answer
and none is visible from outside.

**The vehicle is the key, not the name.** These files are indexed by VIN and by the
registrant's details *at the time of each transaction*, which means addresses the
person left years ago. Lead with the address history, and say explicitly that
records where the subject appears as registered owner, co-owner, lessee, service
customer, warranty registrant **or prior owner** are in scope. Apply the §154 limit:
other people live at those addresses now and other people have owned those vehicles
since.

**Do not supply a VIN or driver's licence number** unprompted; offer to reconsider
if one is genuinely needed to complete a search.

**Watch for a rename or divestiture.** This sector consolidates and spins out
constantly. Ask explicitly whether the request reaches records under a former name,
predecessor entities in the same lineage, and any copy retained by a former parent —
and say that if a copy sits with a company that is no longer theirs, naming it is
enough; you will write to them yourself.

## MAID-keyed opt-outs, and why to refuse them

**Examples:** ModFx Labs, Marketing Architects (IP variant), Fog Data Science.

A whole class of broker offers exactly one exclusion mechanism: send us the
identifier we track you by. Refuse it, and say why — the reasons are about the
mechanism, not about the requester, and stating them usually produces a better
answer than silence would.

**The three defects, in the order that lands best:**

1. **It fails the people most likely to use it.** A mobile advertising ID can be
   reset at any time, and resetting it is the commonest privacy advice given to
   phone owners — so anyone who follows that advice silently destroys the opt-out
   they submitted. On iOS after App Tracking Transparency, a user who declined
   tracking has **no advertising identifier at all**; instructions to "find your
   Advertising ID" send that person looking for something that is not there. The
   mechanism works for people who have taken no protective steps and fails for
   people who have. Say that plainly; it is not usually intentional and companies
   respond to it.
2. **It asks you to create the association you are asking them to end.** A named,
   dated message linking a device to an identity, often in a subject line, sent to a
   company that may hold nothing about you. If they hold nothing today, complying
   with their instructions is the act that creates the record.
3. **Nothing tells you whether it did anything.** "If your ID is in our records we
   will block it" is honest and unfalsifiable from outside — blocked-because-found
   and nothing-happened-because-absent produce identical silence.

The IP-address variant has the same shape plus one more: an IP identifies a
*network*, so the exclusion covers the household and its guests — people who never
asked to be excluded — and misses every device on any other network.

**Always counter-offer rather than just refusing.** Ask them to hash the email
addresses themselves (lowercased, trimmed, SHA-256, plus MD5/SHA-1) and search on
the results; ask whether anything is stored against a household, address, visit
record or identity graph rather than a raw identifier, since a device-ID opt-out
would never touch that; and ask for a **nil result stated against named
identifiers**, accepted in advance as a complete answer.

## EEA-established brokers selling US audiences

**Examples:** Nordic Data Resources (Norway), ONAUDIENCE (Poland), OAN (Poland),
Ocean.io (Denmark), Ogury (UK).

A recurring and easily-missed shape: a company incorporated in Europe, registered as
a data broker in California, selling audiences about Americans. The subject of this
project is a Pennsylvania resident, and Pennsylvania has no comprehensive consumer
privacy statute — so the default answer such a company can give is "no statute
applies to you."

**The argument that answers that, and it is worth making every time:**

> An EEA-established controller's obligations under the GDPR are not conditioned on
> the DATA SUBJECT being in Europe. They follow from where the controller is
> established and where processing takes place in the context of that establishment
> (Art. 3(1)). If the processing happens in the context of the European
> establishment, Articles 15, 17 and 21 appear to reach the data of an American just
> as they reach a European's.

Three things make this land rather than read as bluster:

1. **Frame it as a question and invite correction.** *"I may have that wrong, and I
   would genuinely rather be corrected than proceed on a mistaken premise."* The
   point is to get a reasoned answer, not to win an argument by assertion.
2. **Ask which framework they are answering under**, and ask them specifically *not*
   to decline solely because Pennsylvania has no statute — because that answer,
   standing alone, leaves a European-established company treating an American as
   having fewer rights than the law of its own establishment provides. Put that way
   it is a position most compliance functions will not want to adopt in writing.
3. **Add an Article 21 objection to direct-marketing processing as a separate item.**
   Unlike erasure it requires no balancing test — where it applies it is absolute —
   so it is the ask most likely to be honoured even if the rest is refused.

**Also fold in, since the same letter can carry it:** special category data under
Art. 9 (health, political opinion, religious belief, sexual orientation, ethnicity,
trade union membership) maps closely onto CCPA "sensitive personal information", so
ask for those segments reported *separately* and exercise both the Art. 9 concern
and the §1798.121 limit-use right in one paragraph.

For UK companies, name the **UK GDPR** alongside the GDPR — post-Brexit the
establishment argument runs the same way but under a different instrument.

## Gaming audience data

**Example:** OAN / Online Advertising Network ("over 600 gaming segments worldwide").

A distinct category, and one where the segments disclose considerably more than the
subject matter suggests. A file built on which games a person plays, how long, how
often, at what hours and how much they spend indicates:

  - **approximate age**, and in particular whether the player is a minor;
  - **daily routine and waking hours** — a proxy for employment status, shift
    pattern, and sometimes for insomnia or illness;
  - **disposable income and spending impulsivity**, from in-game purchase behaviour.
    This is the attribute most obviously capable of being used *against* the person
    it describes, and it is worth naming as such;
  - and from title selection, inferences touching religion, sexuality, political
    outlook and national origin.

**Say explicitly that you are not alleging they market those inferences** — only that
they are derivable from the signals, which is precisely why the question is *what is
stored*, not *what is sold*.

**Ask about children even when the subject is an adult.** Gaming audiences skew
young, so any provider in this field handles minors' records whether it intends to or
not. Ask what age assurance is applied before a record enters a segment, and what
happens when an inferred age falls below the threshold. Frame it honestly: *"This
does not concern me personally — I am not a child — but it bears directly on whether
the answers you give me about method can be trusted."* A company that cannot describe
its age handling cannot be relied on to describe its matching either.
