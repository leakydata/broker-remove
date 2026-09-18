# X Mode Social

- **Email:** privacy@xmodesocial.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** xmodesocial.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Outlogic answered the geographic query on 2026-08-20 16:39Z: 'We do not collect personal addresses, nor do we have access to them. We need a valid MAID to look up the precise lat/long associated with it. The MAID is the only information we collect.' That is a claim about INDEX DIRECTION - the lookup is MAID->lat/long and they say they cannot go place->device. Sent one short final reply noting that place-first querying is ordinarily the commercial function of location data, offering 'the request tooling only supports one direction' as a closing answer, and committing to stop either way. Two clear answers already given; do not push a third time (see the ViewDNS lesson).

## Steps

**The company now trades as Outlogic.** Write to `privacy@outlogic.io`, which is
published on `outlogic.io/privacy`. The old `privacy@xmodesocial.com`
hard-bounces `550 5.2.1` — while `xmodesocial.com` still has live Google MX, so
the registry entry looks perfectly healthy and the bounce is mailbox-level.

They also publish `[named individual]@outlogic.io`, plus `eurep@` and `ukrep@` for the
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

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
