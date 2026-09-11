# Mississippi Tornado Alley, LLC — ten people-search sites, one filing

- **Contact:** `privacy@mtalley.zendesk.com` (the address named in their
  California data broker registration)
- **Registry id:** `cyberbackgroundchecks_com_advancedbackgroundchecks_com_fastb`
- **Method:** email
- **Priority: 4.** Ten consumer-facing people-search properties.

## Status

- Current: `submitted` (updated 2026-08-23) — one consolidated letter covering
  all ten.

## The properties

Named in a single registrant field in the 2026 California filing:

| Site | Individually tracked as |
|---|---|
| CyberBackgroundChecks.com | `cyberbackgroundchecks` |
| AdvancedBackgroundChecks.com | `advancedbackgroundchecks` |
| FastBackgroundCheck.com | — |
| PeopleSearchNow.com | `peoplesearchnow` |
| Phonebooks.com | — |
| SearchPeopleFree.com | `searchpeoplefree` |
| SmartBackgroundChecks.com | — |
| USA-People-Search.com | — |
| USPhoneBook.com | `usphonebook` |
| FastPeopleSearch.com | `fastpeoplesearch` |

## How this was found, and why it matters

**Nobody on the outside connects these ten.** Different brands, different
designs, no shared corporate footer. This project had already written to five of
them *separately, as unrelated brokers*, and would have kept doing so.

The California registration puts all ten in one registrant name — the brand-list
tell from `_SILENT_FAILURES.md` §78. The legal entity is "Mississippi Tornado
Alley, LLC", a name that appears nowhere on any of the sites and that no amount
of searching the brands would have surfaced.

It is the largest family in `_FAMILIES.md` by property count and the clearest
demonstration of why the registry beats inference: five separate letters, five
separate confirmations each naming one hostname, and the person would still have
been listed on five other sites with no way to know.

**The contact address is a Zendesk subdomain**, `mtalley.zendesk.com`, which is
also why the derived domain on the registry row is that rather than a real
website. The company has no consumer-facing presence of its own at all — only
the brands.

## The consolidated letter

Sent once, to the registration contact, naming all ten and asking for one answer
covering the estate. Beyond the standard asks it puts six questions:

1. **Which properties the removal was applied to** — named, not implied.
2. **One index or ten?** If they share a back end, one suppression covers
   everything. If not, ten confirmations are needed and the scope of every
   individual reply changes.
3. **Suppression or one-time removal.**
4. **Reverse lookups.** Phonebooks.com and USPhoneBook.com are reverse-lookup
   products by design — for those, the reverse direction *is* the record, and a
   name page disappearing proves nothing.
5. **Relatives and associates**, which are indexed separately and survive the
   deletion of the subject's own record.
6. **`noindex`**, not merely content removal.

**The escape hatch is deliberate and load-bearing:** *"If any of them is in fact a
separate company that merely shares this contact address, please say so plainly
and name which."* A shared statutory contact proves a shared filer, not a shared
database. Offering the deflating answer as acceptable is what keeps this a
question rather than an accusation — and it is the answer that would matter most.

## Individual threads

Left open rather than closed. If the family answers for the estate, close the
individual ones against it; if the family goes silent, the individual threads are
still live. Each individually tracked broker carries a note pointing here.

## Watch for

AdvancedBackgroundChecks replied to its individual letter with:

> *"This email address is dedicated to customer service inquiries and is not
> intended for privacy-related requests."*

Spydialer sent **word-for-word the same sentence** on the same day. Spydialer is
*not* in this registration. That is either an eleventh property filed elsewhere,
a shared support vendor, or coincidence of a very common template — recorded as
an open lead, not a conclusion. See `_FAMILIES.md` on the difference between a
shared template (weak evidence, vendors sell them) and a shared ticket counter
(strong).

The pattern is now confirmed a fourth time. FastPeopleSearch replied to the
follow-up letter with the same sentence, plus **the actual per-property route**
that the earlier replies only gestured at:

> *"If you are a resident of a state that has a consumer privacy law... please
> use our Opt-Out Form: https://www.fastpeoplesearch.com/removal"*

So the estate-wide letter to `privacy@mtalley.zendesk.com` gets deflected
per-property to a per-property web form — there is no single form that clears
all ten sites at once. Each of the ten needs its own form submission
(`<site>/removal` or the equivalent), which needs a human with a browser. This
is genuinely `manual_required`, not `unreachable` — the estate letter still
matters as the record of the request and the question about the three
unregistered siblings, but it will not by itself produce a removal on any one
property.

The reply also never answered the SpyDialer / TruePeopleSearch / FamilyTreeNow
question from the follow-up letter — it just repeated the generic per-property
deflection. Still open.
