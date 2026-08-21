# X Mode Social

- **Email:** privacy@xmodesocial.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** xmodesocial.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-21)
- Note: `privacy@xmodesocial.com` still hard-bounces (550 5.2.1) as of 2026-08-20/21.
  **Do not resend here.** The real request already ran to completion under the
  `outlogic.md` entry (same company, ticket #187713) — a full mobility-category
  letter, a back-and-forth on the MAID-only search constraint, and a final
  deflection ("we do not collect personal addresses... need a valid MAID").
  Resending under this id would duplicate that ticket rather than add coverage.
  Treat `x_mode_social` and `outlogic` as one company for status purposes; see
  `outlogic.md` for the actual exchange.

## Steps

**The company now trades as Outlogic.** Write to `privacy@outlogic.io`, which is
published on `outlogic.io/privacy`. The old `privacy@xmodesocial.com`
hard-bounces `550 5.2.1` — while `xmodesocial.com` still has live Google MX, so
the registry entry looks perfectly healthy and the bounce is mailbox-level.

They also publish `appeals@outlogic.io`, plus `eurep@` and `ukrep@` for the
EU/UK representatives.

## Gotchas

- **Their own privacy page has a broken link label.** The anchor's `href` is
  `appeals@outlogic.io` while the visible text reads `ppeals@outlogic.io` — the
  leading letter is outside the anchor. This is `_SILENT_FAILURES.md` §66 with
  the third polarity: the target is correct and the *text* is wrong, so a human
  who retypes what they see gets an invalid address while a click works. Copy
  the href, not the label.
- **You cannot supply the identifier they key on.** This is a MAID business.
  A consumer cannot look up their advertising IDs historically, and a reset
  mints a new one without retiring the old, so most people have had several and
  have a record of none. Say so plainly rather than pretending otherwise.
- **The argument that replaces it:** ask them to treat a device-to-home-address
  inference as identifying. Dwell pattern at a residential address is how a
  location dataset resolves to a person, which is the direct answer to "we hold
  no names".
- **Name the sensitive-location categories explicitly** — worship, medical and
  reproductive health, addiction and mental-health treatment, domestic-violence
  shelters, correctional facilities, union halls, military installations,
  political gatherings — and ask for a specific answer on them. A general "your
  data has been deleted" does not say whether that category was covered.
- **Ask for supply partners and downstream buyers.** Location data sold once
  persists in the buyer's systems, and an individual has no route to those
  buyers except through the seller.

## Verification

No public profile. The observables are whether they answer the sensitive-location
question specifically and whether they name supply partners — a reply that
addresses neither has not really answered.
