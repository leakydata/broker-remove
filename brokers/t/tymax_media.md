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
