# GoLookUp

- **Email:** support@atlas.net (verified — the only contact golookup.com
  publishes, but see Status: it belongs to the court-appointed custodian of
  the seized domain, not to any operating business)
- **Opt-out (fallback):** https://golookup.com/optout (now also dead — see below)
- **Method:** email — moot now; there is no operator left to email. See Gotchas.
- **Domain:** golookup.com
- **Priority: 3.**

## Status

- Current: `not_found` (updated 2026-10-08)
- **2026-10-08: golookup.com is dead — seized by court order, not just unresponsive.**
  support@atlas.net replied to the 2026-10-04 statutory letter: *"Atlas Data
  Privacy Corporation did not acquire any part of these businesses... Only the
  domain names... are now controlled by Atlas. We use those domains only to
  display a notice for public awareness, not to operate any people-search or
  similar business... no personal information held by any data broker was
  transferred to Atlas. We, therefore, have no ability to... remove or delete
  your personal information."* Direct fetch of golookup.com (2026-10-08)
  confirms it: the homepage now reads "This Domain Has Been Transferred by
  Court Order," citing a 2025-06-25 default judgment against Lucky2Media, LLC
  in NJ Superior Court, Mercer County (Docket MER-L-000286-24) under **Daniel's
  Law**, enjoining Lucky2Media from disclosing covered persons' home addresses
  and phone numbers via golookup.com. No search tool remains on the domain —
  it is a static notice page, nothing else. `/optout` (the page this project's
  2026-10-04 submission used) is gone with the rest of the site.
  **Recorded as `not_found` rather than `confirmed` or `unreachable`**: there
  is no listing left to display (so the practical harm this project exists to
  stop is already gone), but that happened through litigation this project had
  no part in, not through the request that was sent — `confirmed` would
  overstate what this project did, and `unreachable` would understate that the
  site is actually up, just inert.
- Prior (2026-10-04): `submitted` — statutory letter sent to support@atlas.net
  as a faster alternative to the (then still-live) web form, which needed an
  email-confirmation click this project cannot complete headless. Superseded
  by the above.

## Steps

**None — there is nothing left to action.** If this entry is ever revisited
(e.g. the brand resurfaces under a new operator, which is common after a
Daniel's Law takedown — see Gotchas), start over as a new discovery rather
than reusing support@atlas.net; that address is a litigation custodian's
contact, not a business one, and will give the same answer every time.

## Gotchas

- **Daniel's Law takedowns kill the site, not necessarily the underlying
  business.** Lucky2Media LLC (the former operator, per the court filing) may
  still run other people-search brands under other domains — this was not
  checked, because Daniel's Law is a New Jersey covered-persons statute and
  this project does not invoke it on a PA resident's behalf (see CONTRIBUTING).
  If a near-identical site turns up later under a new domain with the same
  page structure, it's worth fingerprinting (per `_FAMILIES.md`'s
  shared-infrastructure method) before assuming it's unrelated.
- **A court-seized domain's custodian (here, Atlas) is a dead end for removal
  requests even though it answers mail.** It is reachable and honest, but it
  holds no data and has no authority over the former operator's other
  properties. Don't mistake a prompt, substantive reply for progress on the
  actual request — read what it says, not just whether it came.
- **The old finding — that support@atlas.net was published off golookup.com's
  own domain — turned out to mean exactly what it looked like: a third party,
  not the broker itself.** It just wasn't a *support vendor* as guessed; it
  was the receiver appointed over the seized domain.

## Verification

Re-fetching https://golookup.com should keep showing the court-order notice.
If it ever shows a working search tool again, the domain has changed hands
again and this entry needs to be reopened as a fresh discovery.

## If they ignore you

Not applicable — there is no live operator to escalate against. A Daniel's
Law judgment is already the escalation.
