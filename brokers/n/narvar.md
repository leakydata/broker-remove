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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Narvar, Inc
- **Registered address:** 3 East Third Avenue, San Matteo, CA, 94401
- **Filed contact email:** legal@narvar.com
- **Filed phone:** 6505859550
- **Website:** https://corp.narvar.com

*Source: `data/registries/registry.csv`.*

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
