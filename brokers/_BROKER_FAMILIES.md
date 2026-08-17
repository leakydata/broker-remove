# Broker families — one letter can cover dozens of sites

Many "different" data brokers are one company running a template across every US
state. They share a single privacy contact, so **one well-scoped letter naming
every property covers all of them** — and is far more likely to be actioned than
fifty near-identical emails landing in the same inbox on the same morning.

## Families found so far

| Contact | Sites | What they are |
|---|---|---|
| `privacy@courtrecords.us` | **51** | `<state>courtrecords.us` for every state |
| `privacy@infotracer.com` | **48** | InfoTracer + `<state>arrests` for every state |
| `contact@licensedata.org` | **10** | California professional-licence sites (nursing, contractors, firearms, notaries…) |
| `support@mailer.intelius.com` | 5 | PeopleConnect: criminalrecords.com, publicrecords.com, reversephonelookup, snoopstation, peoplefinder |
| `support@verifyrecords.com` | 4 | verifyrecords, verifypublicrecords, arrestwarrant.org, texaswarrantroundup.org |
| `privacy@eab.com` | 2 | EAB, Appily |
| `notice@tunnldata.com` | 2 | Tunnl, Deep Root |

**120 brokers reachable through 7 addresses.**

## Finding them

Group pending brokers by `email_to` in `data/brokers.json` — any address with more
than one broker attached is a family. Worth re-running as the registry grows.

## Writing the letter

- **Name every property explicitly.** "All properties you operate" invites a
  narrow reading; an enumerated list does not.
- **Ask which properties held a record.** The answer maps the family for you and
  surfaces sites the registry may have missed.
- For arrest, warrant and court-record families, also ask them to **disclose any
  entry attributed to you and its source** — not only to remove it. A common name
  attracts misattribution, and you cannot correct a record you have never seen.
- Send **one** letter per family. Fifty separate emails to one privacy team reads
  as a mail flood and gets triaged accordingly.

## Remaining families (as of the latest sweep)

| Contact | Sites | Notes |
|---|---|---|
| `support@mailer.intelius.com` | 5 | criminalrecords.com, publicrecords.com, reversephonelookup, snoopstation, peoplefinder — PeopleConnect properties **not** covered by the main suppression portal |
| `privacy@eab.com` | 2 | EAB, Appily (education/student data) |
| `notice@tunnldata.com` | 2 | Tunnl, Deep Root (political audience data) |

**The long tail is genuinely long: 374 brokers now have a unique contact each.**
Family consolidation was worth roughly 120 brokers for 7 letters; beyond that,
there is no shortcut and it becomes a paced sending exercise.

## Hosted rights portals — a different shape of contact

A growing number of larger firms use a third-party privacy platform rather than
their own form:

- **OneTrust** — `<company>-privacy.my.onetrust.com/webform/<uuid>/<uuid>`
  (Affinity Solutions). Usually one right selectable per submission; email
  verification follows.
- **TrustArc** — `submit-irm.trustarc.eu/services/validation/<uuid>`
  (Dun & Bradstreet). **The bare host returns 400** — the full validation path
  with the company's UUID is required.
- **Transcend / Ketch / Osano** appear similarly.

These UUIDs are not discoverable by guessing. Find them in the company's **privacy
policy**, not on its homepage or in its support replies — the same lesson as
`_DEFLECTIONS.md` §7: the policy page is written for regulators and carries the
real route.

## Spotting a family from the ticket number

Brands that look independent often share one privacy queue, and the **support
ticket reference is the tell**. Three brands in this registry — a background-check
site, a court-records aggregator, and a court-case search site — all issued
Zendesk references in the same numeric range on the same day:

| Brand | Reference |
|---|---|
| court-records aggregator | 5381**35** |
| background-check site | 5381**36** |
| court-case search | 5386**31** |

Consecutive and near-consecutive numbers from one Zendesk instance. A fourth,
unrelated site issued `127xxx` — a different instance, therefore a different
operator.

That single observation collapses **52 separate registry entries** into one
contact, because the family includes a `<state>courtrecords.us` domain for nearly
every US state. One letter naming all of them, sent to the shared queue, does the
work of fifty.

**How to use this:**

- Record the reference number for every ticket, not just the fact that one was
  issued. It is free, and it is what makes the pattern visible later.
- When two brands return references in the same range, write one letter that
  **names every domain in the family explicitly**, so there is no ambiguity about
  scope and no chance of a partial removal being reported as complete.
- Sequential numbers also tell you roughly how much volume the queue handles,
  which is a decent proxy for whether a slow reply means backlog or neglect.

## Rebrands surface as an address on a different domain

A bulk check of published privacy contacts turned up two entries whose site
publishes a privacy address on a **completely different domain**:

| Registry says | Site publishes | What it means |
|---|---|---|
| `privacy@intentgine.com` | `privacy@pharosiq.com` | Intentgine now operates as PharosIQ |
| `privacy@iwave.com` | `privacy@kindsight.io` | iWave now operates as Kindsight (`iwave.com` redirects to `kindsight.io/iwave/`) |

Neither is an address correction — both are **companies that changed name**, which
is the same class as the acquisition redirect in `_DEFLECTIONS.md` §11 but found
without needing the broker to tell you.

This is worth doing deliberately, because the failure is silent in both
directions: writing to the old domain may bounce, or may reach an abandoned
mailbox that no longer has anyone behind it. A cross-domain privacy address on a
broker's own site is the cheapest rebrand detector available — no research
required, it falls out of the verification sweep for free.

**Check the redirect too.** `iwave.com` resolving to `kindsight.io/iwave/`
confirms the relationship rather than leaving it as an inference from a shared
contact address.

