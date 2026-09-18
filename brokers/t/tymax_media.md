# Tymax Media

- **Email:** privacyofficer@datacomplianceportal.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** datacomplianceportal.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-20)
- Note: NO ROUTE - the company appears to be gone. privacyofficer@datacomplianceportal.com hard-bounces. datacomplianceportal.com returns Cloudflare 522 (origin down) to both curl and a real browser. tymaxmedia.com itself: HTTPS fails with a certificate that does not match the hostname, and plain HTTP returns a 62-byte page reading 'This website is for lease. Offers can be sent to [phone].' The SOA serial is from 2017. So both the broker and the third-party compliance vendor it delegated privacy requests to are off the air, while the domain still resolves and still has live Outlook MX - which is exactly the shape that makes a dead broker look alive to a registry. SECOND INSTANCE of the outsourced-compliance-vendor failure: ROC Advertising's dataprivacy_rocadvertising@simpleoptoutcompliance.com bounced the same way earlier today. See _SILENT_FAILURES.md 68.

## Steps

**No route exists.** Recorded `unreachable`, not `pending`, so a later pass does
not spend three sends rediscovering it.

| check | result |
|---|---|
| `privacyofficer@datacomplianceportal.com` | bounce |
| `https://datacomplianceportal.com/` | Cloudflare **522**, origin down (browser and curl) |
| `dig A tymaxmedia.com` | resolves |
| `dig MX tymaxmedia.com` | live Outlook MX |
| `https://tymaxmedia.com/` | TLS certificate does not match the hostname |
| `http://tymaxmedia.com/` | 200 — 62 bytes, "This website is for lease." |
| `dig SOA tymaxmedia.com` | serial dated 2017 |

## Gotchas

- **The first three checks all say "healthy".** A resolving domain with live MX
  is a company that has stopped existing without telling its DNS. Do not stop at
  the registry-health checks.
- **The dead hop is somebody else's domain.** Their privacy contact lived at a
  third-party compliance vendor, so every check against `tymaxmedia.com` passes
  while the request goes nowhere. See `_SILENT_FAILURES.md` §68.
- **Try plain HTTP when HTTPS fails on certificate mismatch.** The parking page
  — the thing that actually tells you the company is gone — is only served over
  `http://`.
- **Do not hunt for another local part at the vendor.** When a compliance-vendor
  address bounces, go back to the broker's own domain and start again.

## Verification

Nothing to verify. Reopen only if the business resurfaces under a new domain —
the phone number on the parking page is the only remaining thread, and it is a
domain-sales line, not the company.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Tymax Media
- **Registered address:** 3755 Avocado Blvd, 305, La Mesa, CA 91941,
  United States
- **Filed contact email:** privacyofficer@datacomplianceportal.com
- **Website:** http://tymaxmedia.com
- **Opt-out route they filed:** Consumers can visit
  http://tymaxmedia.com/ccpa.php and click on the link to visit our data
  compliance portal.
- **Route for protected individuals:** Consumers can visit
  http://tymaxmedia.com/ccpa.php and click on the link to visit our data
  compliance portal. (Cal. Gov. Code 6208.1(b) / 6254.21(c)(1) — for
  survivors of domestic violence, stalking and similar, a stronger and
  faster route than the ordinary consumer request)
- **What they say they collect:** Additional information is available at
  http://tymaxmedia.com/privacy.php

*Source: `data/registries/complete-reg-data-brokers.csv`.*

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
