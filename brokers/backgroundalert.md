# BackgroundAlert

- **Opt-out:** none — domain is dead
- **Email:** ~~info@backgroundalert.com~~ — **domain does not resolve (NXDOMAIN)**
- **Method:** none available
- **Domain:** backgroundalert.com
- **Priority: 2.** Background-check style listing, but the operator appears gone.

## Status

- Current: `unreachable` (2026-09-12)
- Note: A consumer request to `info@backgroundalert.com` hard-bounced
  (550 5.1.1). Direct DNS lookup confirms `backgroundalert.com` does not
  resolve at all — this is not a dead mailbox on a live domain, the domain
  registration itself appears to have lapsed or been withdrawn.

## Steps

No route exists. Nothing to do until/unless the domain comes back — and if
it does, check first whether a stranger has re-registered it (the standard
caution for any domain that goes fully dark; see `_SILENT_FAILURES.md`).

## Gotchas

- Distinguish this from a mailbox-only failure (a live domain that rejects
  one address, which is common and usually fixable by finding another
  contact). This is domain-level: nothing is listening at all.

## Verification

Nothing submitted; nothing to verify. Re-run a DNS lookup on a future pass
before assuming this is permanent.

**Re-checked 2026-09-15:** a direct `socket.gethostbyname` lookup still
returns NXDOMAIN, confirming the domain is dead — but `scripts/verify_emails.py`
(which fetches through this project's outbound proxy) returned `BLOCKED`
rather than `UNREACHABLE` for the same domain. That's worth flagging as a
possible discrepancy between direct DNS resolution and the proxy's view,
rather than assuming one tool is simply wrong — if this domain ever needs
re-checking, try both a plain DNS lookup and an actual page fetch before
concluding either way.
