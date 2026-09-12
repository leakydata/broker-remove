# 4Eyes.ai, 4-Eyes.ai

- **Email:** privacy@4-eyes.ai (bounced — see below)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** 4-eyes.ai
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-26)
- Note: 2026-08-26 DOWNGRADE, submitted -> unreachable. The letter of 2026-08-22 never landed: Gmail retried for 48 hours and gave up with 'the recipient server did not accept our requests to connect'. 4-eyes.ai publishes NO MX record; mail falls back to the A record under RFC 5321, and that host refuses SMTP outright. Our domain checker calls this 'weak' rather than False, which is the right default - A-record fallback genuinely works for some small domains, and condemning a broker on it is the expensive direction of the mistake - but the send path was not surfacing it, so the failure looked like silence for four days while the status read submitted. queue_batch now names weak-MX domains at send time so the bounce is anticipated rather than discovered later. Address added to data/dead_addresses.json.

## Steps

1. Email `privacy@4-eyes.ai` with the standard statutory deletion/opt-out letter,
   asking for hashed-email search and coverage of device/advertising IDs and
   modelled attributes in case matching is identifier-based.
2. Failed to deliver after 3 days of retries — see Status. Do not resend to the
   same address without checking for a live site first.

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
