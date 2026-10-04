# GoLookUp

- **Email:** support@atlas.net (verified — found in the "Contact Us" line of the
  golookup.com/optout footer itself, even though the domain doesn't match)
- **Opt-out (fallback):** https://golookup.com/optout
- **Method:** email — tried first instead of the web form; see Gotchas.
- **Domain:** golookup.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-10-04)
- Note: 2026-10-04: the opt-out page requires a confirmation email per
  `needs_email_confirm`, and this project does not have a browser to work that
  form — but the same page's footer publishes "CONTACT US: support@atlas.net" in
  plain text, off golookup.com's own domain. Sent the statutory deletion/opt-out
  letter there instead of queuing the form for a human. No reply yet.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `support@atlas.net`** with a written statutory request — do not assume
   the mismatched domain is a wrong address; it is the address GoLookUp itself
   publishes for contact, just hosted off their own domain (a third-party support
   vendor is the likely explanation, though unconfirmed).
2. **If that bounces or goes unanswered**, fall back to the web form at
   https://golookup.com/optout. It needs an email-confirmation click, so it is a
   handoff item, not something this project can finish headless.
3. **Ask them to state which identifiers matched.** "We deleted your record" and
   "we searched and found nothing" are different outcomes.

## Gotchas

- **The published contact address is off-domain.** `support@atlas.net`, not
  anything `@golookup.com`. Worth flagging as a finding rather than discarding —
  `verify_emails.py` surfaces these as `DISCOVERED_OFFDOMAIN` and they are real
  evidence (the broker's own page said so), not a guess, but they deserve a
  reply to confirm before trusting them for anything beyond a first attempt.
- **The web form route needs a confirmation-email click**, which this project's
  email-only channel cannot complete — stays queued for a human unless the email
  route above lands.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
3. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
4. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.

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
