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

## Detecting a family from the privacy address alone

The cheapest signal in this whole project: **a broker whose published privacy
contact lives on another broker's domain**. No WHOIS, no corporate filings, no
reading of terms — the site has told you, in its own privacy policy, which desk
handles it.

`scripts/family_scan.py` groups the registry by contact address and marks each
member's status. Across 1,002 tracked brokers it found **115 whose privacy
address belongs to a different broker in the registry**, in these shapes:

| Shape | Example | What it means |
|---|---|---|
| One mailbox, dozens of state-named sites | 51 `*courtrecords.us` sites → `privacy@courtrecords.us` | A network, not fifty-one companies |
| A brand's address on unrelated-looking sites | `sheriffsdepartment.net`, `recordsquarry.com`, `instantcheckspy.com` → `truthfinder.com` | Affiliate fronts, or quietly-owned brands |
| A shared support mailbox on a mailer subdomain | five sites → `support@mailer.intelius.com` | One operator behind several products |
| A rebrand giving itself away | `intentgine` → `privacy@pharosiq.com` | The new name, before anyone announced it |

### The half that saves work

One letter naming every sibling is **one ticket** with an unambiguous scope,
instead of one ticket per brand — each re-verifying identity, each restarting a
clock, each an opportunity to be refused. With a daily send cap that is the
difference between a week and an afternoon. Fifty-one court-record sites went out
as a single message.

### The half that creates silent gaps

**A sibling your letter did not name is a sibling nobody removed** — and in the
tracker it is indistinguishable from one that was, because the request did go to
the right address. Sharing a contact is evidence of a shared **desk**; it is not
proof of a shared **database**, and no broker will volunteer that your request
was narrower than you assumed.

So `family_scan.py --actionable` reports the case that matters: a group where
some members have been written to and others are still pending. That is a prompt
to reply on the existing ticket naming the rest, not to open a new one.

### Ask the question that has no bad answer

Where a site merely *publishes* another company's address, it may be a front
rather than a subsidiary. So ask both halves at once:

> *"Please confirm whether these sites are handled by you. If they are, extend my
> request to cover them explicitly. If they are not, please tell me who does
> operate them."*

Confirmation extends the request. Denial names the real operator. Both outcomes
are progress; only silence is not.

### A caution from the same scan

A near-miss check for addresses one character away from a common role name turned
up `dprivacy@forddirect.com` — which looks exactly like a typo for `privacy@` and
is the **genuine published address**, confirmed against their own site. It also
turned up `optout@` on four sites, flagged only because `opt-out@` exists too.

Never auto-correct an address that looks wrong. Flag it, then verify it against
what the broker publishes. The one address in that batch that really was a typo —
`rivacy@truthfinder.com`, missing its leading `p` — would have bounced silently at
a domain that does exist, which is the worst kind of wrong address to hold.

## Ticket numbers give away a shared helpdesk

A helpdesk hands out ticket references from one sequence per tenant. So two brands
that look unrelated — different names, different domains, different reply addresses
— will issue numbers a few hundred apart if one company is behind both, and a few
million apart if not.

Three brands in this project number from a single sequence:

    537420   InfoTracer          (and its 46 state arrest-record sites)
    538631   CourtCaseFinder
    538837   IDStrong

**Why this is better evidence than it looks.** The number is assigned by the vendor
rather than chosen by the broker, and nobody involved thinks of it as identifying —
there is no incentive to obscure it and no reason to notice it leaks. It is the
kind of signal that survives precisely because it is beneath attention.

**Why it is still only a question.** A shared Zendesk instance is not a shared
database. Two companies can use one support vendor, or one agency can run the desks
of several clients. So the finding is a *question to put to the operator*, never a
fact to record — and the question is worth putting because every answer helps:

- *Same operation?* → one request covers all of them; name the properties.
- *Same vendor only?* → pursue them independently, nothing lost.
- *Some other relationship?* → they name the entity that actually holds the
  records.

`scripts/family_scan.py --tickets` clusters recorded ticket references and reports
where more than one brand shares a window. It is deliberately conservative:

- **Six digits minimum.** An earlier version matched five-digit numbers and
  cheerfully grouped two unrelated brokers because one note mentioned a **ZIP
  code**. Five-digit "references" are postcodes far more often than tickets.
- **The window is adjustable** (`--window`, default 5000). Wide enough to catch a
  busy desk's numbering over days; narrow enough that unrelated instances do not
  collide.

Compare the strength of the signals available from outside:

| Signal | Strength | Why |
|---|---|---|
| Shared privacy address on another broker's domain | Strong | The broker published it themselves |
| Word-for-word identical support template, same day | Strong | One desk, one macro |
| Ticket numbers in one sequence | **Moderate** | One vendor tenant; may be an agency |
| Similar domain name | Weak | Proves nothing; cheap to ask about |

