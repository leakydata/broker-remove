# Anexinet Corp.

- **Email:** privacy@anexinet.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** anexinet.com
- **Priority: 2.**

## Status

- Current: `covered_by_sibling` (updated 2026-09-03) — see `verinext.md`
- Note: 2026-08-30 Sent the standard data-broker letter (full identifier set) to privacy@anexinet.com. Anexinet is an IT/managed-services firm on the CA data broker registry; no public opt-out page found, email is the only known route.
- Note (2026-08-31): Hard-bounced same day — 550 5.4.1 "Recipient address rejected: Access denied" (Exchange Online). The registry-sourced address was never actually live; `email_verified` corrected from `ca_data_broker_registry` to `bounced`. **anexinet.com is a duplicate/legacy registration of `verinext`** (the domain redirects to verinext.com) — that canonical entry is already submitted, at a different address (dpo@verinext.com). No resend needed here: this was a dead legacy mailbox, not a live second channel, so the request is covered by the verinext thread.
- **Correction (2026-09-03): this playbook's own advice was not followed.** A bounce-cleanup pass this session found the same bounce independently — confirmed Anexinet rebranded to Verinext (dpo@verinext.com found on verinext.com's privacy policy) — and resent there without first checking whether a `verinext` row already existed and had already been actioned. It had: submitted 2026-08-20, to the identical address. The duplicate letter is harmless (a second copy of the same request reads as a follow-up, not a new intake), but it is exactly the failure mode this note already warned about. **Lesson: before resending a bounce to a "rebrand" address, grep the registry for the successor's own id first** — the playbook may already contain the answer.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

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
