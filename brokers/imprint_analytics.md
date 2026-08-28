# Imprint Analytics LLC

- **Email:** privacy@imprintanalytics.io (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** imprintanalytics.io
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Note: HARD BOUNCE 2026-08-28: privacy@imprintanalytics.io -> 550 5.1.1 'the email account that you tried to reach does not exist'. That address is the one Imprint Analytics LLC FILED ON THE CALIFORNIA DATA BROKER REGISTRY, and it is the only contact the company publishes anywhere: imprintanalytics.io has live Google Workspace MX but serves no website (TLS handshake fails outright; plain HTTP returns Cloudflare error 1001), so discover_contacts found nothing and there is no privacy policy page to read a second address off. A registered broker with a mailbox that does not exist and no site is unreachable by every route the statute creates. Handoff: CA AG complaint is the remaining lever.

## Steps

There is no route. Recorded so nobody spends a send rediscovering that.

    dig +short MX imprintanalytics.io   -> aspmx.l.google.com. and friends (live)
    dig +short A  imprintanalytics.io   -> 160.153.0.60 (GoDaddy parking range)
    curl -I https://imprintanalytics.io -> exit 35, TLS handshake fails
    curl -I http://imprintanalytics.io  -> HTTP 409, body "error code: 1001"

Both DNS checks pass. The mail check passes. The domain resolves and answers on
port 80. Every cheap signal this project uses to decide a broker is alive says
yes, and there is still no company on the other end -- no page, no privacy
policy, no second address. See `_SILENT_FAILURES.md` §145.

## Gotchas

**Do not stop at DNS-health checks.** MX resolves, the A record resolves, port
80 answers — every check this project normally runs to decide a domain is
alive says yes, and there is still no reachable company behind any of them.
See `_SILENT_FAILURES.md` §145.

## Verification

Nothing to verify — no route exists (see Status/Steps above). Re-check
periodically whether imprintanalytics.io starts serving a real site.
