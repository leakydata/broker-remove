# Narvar, Inc

- **Email:** legal@narvar.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** corp.narvar.com
- **Priority: 2.**

## Status

- Current: `acknowledged` (updated 2026-09-16)
- Note: legal@narvar.com autoresponder 2026-09-15 23:33: 'THIS EMAIL WAS RECEIVED. Thank you for contacting the Narvar Legal email. This email is to answer general questions regarding how Narvar handles requests from consumers to exercise their privacy rights.' Template, not a human. Note it CC'd legal@narvar.com back to itself, so watch for a loop (the SF 56 pattern).

## Steps

Emailed legal@narvar.com. Narvar is a shipping-notification/post-purchase SaaS platform used by retailers -- framed as the client-uploaded-SaaS variant: no direct account, asked which retailer's use of the platform produced a record, and asked for a platform-level do-not-contact suppression regardless.

Route in practice: the email above gets an **automated bounce-equivalent**, not a human reply — see Gotchas. Use the DSAR web form or the phone line instead:
- Form: `https://narvar.my.onetrust.com/webform/04b3731f-2a9a-42ce-bd6b-106d4b4ec3bf/a7c944bf-3cec-4f00-9dc5-dea5bf2b6f4f`
- Phone: 866-528-0244
Queued in `handoff.py` (no browser available to this agent).

## Gotchas

**`legal@narvar.com` is a dead letter box by design**, despite being the address named in their own privacy policy correspondence patterns. Auto-reply received 2026-09-15, eighteen days after sending: *"CONSUMERS TRYING TO MANAGE THEIR PERSONAL DATA MAINTAINED BY NARVAR CANNOT DO SO BY EMAIL... ANY REQUESTS SENT TO THIS EMAIL WILL NOT BE PROCESSED AND WILL BE DELETED."* Two routes offered instead: their OneTrust DSAR tool, or a phone line. Do not resend to this address — go straight to the form or the call.

## Verification

Not yet reachable — needs the human handoff step above before there is anything to verify.
