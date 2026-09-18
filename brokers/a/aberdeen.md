# Aberdeen

- **Opt-out:** https://www.aberdeen.com/do-not-sell-my-personal-information/
- **Email:** privacy@spiceworks.com — **off-domain, corporate relationship unconfirmed**
- **Method:** web_form — Web form.
- **Domain:** aberdeen.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-11)
- Note: CONCERN RESOLVED 2026-09-11 -- THE OFF-DOMAIN ADDRESS IS CORRECT AND THE LETTER WAS PROPERLY SENT. This row had been held at email_pending because the registry flagged privacy@spiceworks.com as email_verified_by offdomain_needs_confirmation, with an explicit instruction to confirm the corporate relationship BEFORE sending -- the letter carries a full identifier set, so sending it to an unrelated party would be a disclosure rather than a request. That caution was right and the verification now passes. CHECKED TODAY ON ABERDEEN'S OWN SITE: aberdeen.com/privacy-policy/ names Spiceworks 23 times, identifies the group as 'Spiceworks Ziff Davis' (SWZD appears 8 times on the homepage), refers to 'Spiceworks and its affiliates' and 'Spiceworks businesses', and publishes privacy@spiceworks.com as the privacy contact. A negative control on the same host returns 403 for a nonsense path, so the policy page is real and not a catch-all. The address is therefore Aberdeen's own published privacy contact, not a guess from a shared registrant. SEND CONFIRMED from the mailbox: letter went 2026-08-29 10:15 UTC to privacy@spiceworks.com, subject 'Consumer Request to Delete and Opt Out of Sale of Personal Information - [PERSONAL] (Aberdeen)'. NO REPLY in 13 days. Moving to submitted, which is what it is: correctly sent, awaiting an answer. Due for a chase at the 45-day mark, 2026-10-13.

## Steps

1. **Before treating this as resolved, confirm the relationship.** Aberdeen
   and Spiceworks both plausibly sit under the same media/B2B-data parent
   (Foundry/Ziff Davis-adjacent), which would make this a legitimate shared
   privacy inbox — but that is a plausible story, not confirmed fact. If a
   reply comes back with no sign of actually knowing who Aberdeen is, that is
   itself the answer: this letter went to an unrelated company.
2. If a reply confirms the relationship, treat this as a normal submission.
   If not, do not repeat this mistake for other `offdomain_needs_confirmation`
   entries — check that flag before adding a broker to a send batch, not
   just whether `email_to` is populated.

## Gotchas

- **A registry hold flag is only useful if the send path actually reads it.**
  This project's `queue_batch.py` has a `HOLD` set specifically for this
  situation (see its comment on `DISCOVERED_OFFDOMAIN` /
  `firstadvantage.com`-style mistakes) — the failure here wasn't a missing
  safeguard, it was a batch built by hand from a copy of the registry that
  predated the flag being set, which bypassed it entirely.

## Verification

Sent 2026-08-29. When a reply arrives, read it specifically for evidence of
the corporate relationship before recording anything further.

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
