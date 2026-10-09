# Corporationwiki

- **Opt-out:** https://www.corporationwiki.com/profiles/public (dead, see Status)
- **Method:** email — moot; there is no operator left to email. See Gotchas.
- **Domain:** corporationwiki.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-10-09)
- **2026-10-09: the 2026-09-02 guess was right — this is a rename, not a closure, and the renamed owner is a court-appointed custodian with nothing to search.**
  corporationwiki.com now serves a static "Domain Update" notice: *Atlas Data
  Privacy Corporation, et al. v. Sagewire Research, LLC, et al.*, Superior
  Court of New Jersey, Bergen County, Docket No. BER-L-000869-24 — a Daniel's
  Law suit brought by Atlas on behalf of roughly 19,078 assigned "covered
  persons" (law enforcement, prosecutors and similar). The domain is now
  controlled by Atlas Data Privacy Corporation, the same court-appointed
  custodian already encountered at `brokers/g/golookup.md`. `verify_emails.py`
  proposed `support@atlas.net` as an off-domain contact (flagged
  `offdomain_needs_confirmation`, correctly held from auto-send) — this is
  that same custodian mailbox, confirmed by fetching the live site rather than
  guessed. No letter was sent: GoLookUp's 2026-10-04 statutory letter to this
  identical mailbox already produced Atlas's standing answer — *"no personal
  information held by any data broker was transferred to Atlas... we
  therefore have no ability to... remove or delete your personal
  information"* — and there is nothing left on corporationwiki.com to search
  or display. Recorded as `not_found` on the same reasoning as GoLookUp: the
  listing is already gone, but through litigation this project had no part
  in, so `confirmed` would overstate this project's role and `unreachable`
  would understate that the domain is live, just inert.
- Prior (2026-09-02): `unreachable` — 410 GONE on every path, live MX behind a
  withdrawn site, flagged as possibly a rename rather than a closure.
  Confirmed above.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.corporationwiki.com/profiles/public
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**An automated off-domain discovery can be right for a reason the scraper
doesn't know.** `verify_emails.py` flags any contact address found off the
broker's own domain as `offdomain_needs_confirmation` and correctly withholds
it from auto-send, because most of the time an off-domain address is a wrong
guess. Here it wasn't a guess at all — `support@atlas.net` is the real
current owner, a litigation custodian, not a stray scrape. Worth fetching the
live site by hand before assuming "off-domain" means "unrelated"; a seized
data-broker domain is exactly the case where the real contact is never on
the original domain.

**Same custodian, same answer, no need to ask twice.** Atlas's position (see
`brokers/g/golookup.md`) is that it holds none of the underlying personal
data and has no operational ability to act on a deletion request for any
domain it has taken over this way. There's no reason to expect a
domain-specific answer from the same mailbox.

## Verification

Confirmed 2026-10-09 by fetching corporationwiki.com directly: static court
notice, no search tool, no listing, no form. Re-check only if Atlas's
custodianship of this specific docket changes.

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
