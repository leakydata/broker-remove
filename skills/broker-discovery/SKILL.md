---
name: broker-discovery
description: Find data brokers that hold someone's information but appear on no public list. Use when the user asks which brokers have their data, wants to expand the broker registry, asks who else is selling their information, or wants to find brokers beyond the obvious people-search sites.
---

# Finding the brokers nobody lists

Commercial removal services work from a list of a few hundred well-known
people-search sites. That list is the visible surface. Most of the industry is
not on it, and the four methods below reach past it.

Order them by yield: the state registries first, because they are authoritative
and bulk; supplier disclosure last, because it is one broker at a time but finds
things nothing else can.

## 1. State registration filings — the biggest single source

Several states require data brokers to register annually and publish a contact
address. This is a legal filing, not a scrape, and it is the strongest provenance
available:

    state_registry  >  scraped privacy policy  >  guessed from a slug

**California** is the largest. `${CLAUDE_PLUGIN_ROOT}/scripts/import_state_registries.py`
fetches and imports all four files:

```bash
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/import_state_registries.py" --fetch
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/import_state_registries.py"           # propose
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/import_state_registries.py" --apply
```

942 registrants, each with the contact address the company itself nominated to
receive exactly this kind of letter.

**Still unmined: Vermont, Texas and Oregon** run their own registries. The
overlap with California is partial — a broker with no California nexus can appear
in Vermont and nowhere else. Same importer, different column names; add a
`SOURCES` entry.

Two cautions:

- **Absence proves nothing.** A broker that never had a California nexus never
  filed. The registry is a floor.
- **Deregistration is a signal, not a deletion.** Present in 2024, absent in
  2026 means acquired, wound up, or simply did not file — and the obligation did
  not lapse with the paperwork. Keep them, record the years.

## 2. Corporate families — one letter can cover five brands

**A corporate family registers under one contact address.** Grouping registrants
by the domain of that address recovers the family structure directly, from a
sworn filing rather than an inference.

```bash
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/import_state_registries.py" --families
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/build_families_doc.py"
```

Read the result in `${CLAUDE_PLUGIN_ROOT}/brokers/_FAMILIES.md`. It found
BeenVerified registering under a completely unrelated-looking brand's privacy
address — nothing on either website connects them.

Why this matters before you write, not after: a confirmation naming one hostname
from a company that runs four is not a confirmation, and you cannot tell unless
you already knew about the other three.

**The name field is also a brand list.** Registrants put their whole portfolio in
it. Splitting those yields brand names in no broker list; they go to
`data/broker_leads.json` as leads and are not promoted to brokers until each has
a real domain and a contact route.

**State the family as a question, not an accusation.** A shared contact proves a
shared filer, not a shared database. *"If these share an index, please confirm
the removal covers all of them; if they are separate, say so and I will file
separately."* Both answers are useful; only silence is not.

## 3. Infrastructure tells — for families with no filing

When there is no registration to read, siblings still leak. In rough order of
strength:

| Tell | Strength |
|---|---|
| Sequential support-ticket IDs across different brands' help desks | Near-conclusive — ticket counters are per account |
| Byte-identical opt-out email template | Strong, but vendors sell templates |
| Identical canned support reply, word for word | Strong |
| Shared nameserver pair | Suggestive only — shared hosting is common |

`family_scan.py` automates part of this. The ticket-ID tell is the best one and
costs nothing: **record every ticket number you are given**, even when nothing
seems wrong. A number alone means nothing; the fourth one turns three into a
sequence.

## 4. Supplier disclosure — ask where the data came from

Add one sentence to every letter:

> If you licensed my information from a supplier, please tell me which one.

A reseller knows its upstream and no public list does. This is how a 250-million
record broker entered this registry — named by a small email-marketing firm that
answered honestly. It costs a sentence and it reaches the part of the industry
that has no consumer-facing website at all.

Ask the same question of anyone who says *"we hold nothing"* — a company with no
record of you may still know who would.

## Turning a lead into a broker

Never import a name with no route. That is how a registry ends up with hundreds
of entries the queue cannot use, while reporting nothing left to do.

```bash
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/resolve_optery_domains.py"   # name -> verified domain
uv run "${CLAUDE_PLUGIN_ROOT}/scripts/verify_emails.py" --no-email --apply   # domain -> contact address
```

`verify_emails.py` reads the broker's own privacy pages and grades what it finds:

- `DISCOVERED` — a rights-shaped address on the broker's own domain.
- `DISCOVERED_WEAK` — only a general mailbox, usually `sales@`. Usable, not verified.
- `DISCOVERED_REGIONAL` — every published address is scoped to a region and none
  to the requester's. Say so in the letter and ask to be routed.
- `DISCOVERED_OFFDOMAIN` — the address is on some other company's domain. Either
  an acquisition or a wrong domain, and **these are held out of the send queue**
  until a human confirms which. A letter carries a full identifier set, so a
  wrong route is not a wasted send, it is a disclosure caused by the removal
  effort itself.

**Verify the domain before trusting an address scraped off it.** One registry
entry pointed at a background-screening firm's name but a real-estate brokerage's
website; the sweep duly proposed a real-estate software vendor's support desk as
the privacy contact. Two honest derivations, one confident wrong answer. Follow
the redirect and read the company name.
