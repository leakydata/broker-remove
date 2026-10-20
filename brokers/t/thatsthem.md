# ThatsThem

- **Opt-out:** https://thatsthem.com/optout
- **Method:** web_form, no CAPTCHA. Fully automatable.

## Status

- Current: `confirmed` (updated 2026-10-20)
- Note: Spokeo's own registration discloses a carve-out — its self-service
  opt-out and (per the filing) its Customer Care route both exclude
  Thatsthem.com, which requires its own separate request. A letter to
  `legal@spokeo.com` naming the carve-out and asking for Thatsthem coverage
  got forwarded internally: ThatsThem support (`support@thatsthem.zendesk.com`,
  agent Nik, ticket visible via Zendesk) replied on the same thread 2026-10-19:
  *"I was able to successfully remove the listings associated with the
  specific information provided. Please allow 24-72 hours to see this reflect
  on our site."* That is a broker-issued removal confirmation, so `confirmed`
  is earned — but note it came through Spokeo's internal routing, not through
  ThatsThem's own `/optout` form or `optout@thatsthem.com` address. If working
  this broker fresh (not via a Spokeo escalation), use the form below first;
  only fall back to Spokeo's legal address if ThatsThem's own channel goes
  unanswered.

## Steps
Single page form, all fields required:
Full Name / Street Address / City / State (select, 2-letter) / ZIP / Email / Phone
→ "Submit Opt-Out Request". Success renders inline: "Request Submitted!"

## Gotchas
- No search step and no CAPTCHA — one of the easiest. Good first target.
- State field is a `<select>` keyed on the 2-letter code.
- Confirmation email within 72h; processing stated at 72h.

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
