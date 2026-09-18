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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** 4Eyes.ai Inc.
- **Trading as:** 4Eyes.ai, 4-Eyes.ai
- **Registered address:** 600 Cleveland St suite 227, Clearwater, FL
- **Filed contact email:** [named individual]@4-eyes.ai
- **Website:** https://www.4-eyes.ai/

*Source: `data/registries/registry2024.csv`.*

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
