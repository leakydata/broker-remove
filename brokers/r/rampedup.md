# RampedUp

- **Email:** contact@rampedup.io (site-published — unverified until a reply arrives)
- **Email fallback (dead):** privacy@rampedup.io — the address on their CA data broker registration, but it is a restricted Google Workspace group that rejects outside mail
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** rampedup.io
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-29)
- Note: THREE ADDRESSES, NONE OF THEM A ROUTE. privacy@rampedup.io -- the address on the CURRENT (2025) CA filing -- is a restricted Google Workspace group that rejects outside senders and bounced 26 Aug. contact@rampedup.io -- the address on the 2024 filing and on their own site -- auto-replies 'this is *not* a monitored inbox' (reply came from contacts@, plural). So THE REGISTER EMAIL GOT WORSE BETWEEN FILINGS: the 2024 address is live-but-unmonitored, the 2025 address is dead. Designated method per both the autoresponder and the 2025 filing's rights URL is a portal at basic.rampedup.io/app/donotsell -- 'All inquiries must be completed via the online portal to AUTHENTICATE YOUR IDENTITY and comply with privacy guidelines.' It is a JS app shell inside their client application (the sibling path is /clientsignin) so it cannot be read without a browser; whether it demands a login is unknown. Also a phone line, (404) 682-9570 press 2. NOTE THE 7004/242 PROBLEM IN THEIR OWN WORDING: they require identity authentication for a DO NOT SELL request. An opt-out is not a verifiable consumer request and verification may not be required as a condition of honouring one. THE CONTRADICTION WORTH THE WHOLE FILE. Their 2024 filing describes the business as helping organisations 'keep their "OPTED-IN" professional contact data updated'. But Lusha's access response names RampedUp as the source of an email address that Lusha records as 'GUESSED emails based on full name and company email structures'. A GUESSED ADDRESS CANNOT BE OPTED-IN -- nobody opts in with an address that was invented for them by a pattern-matcher. Either the construction happened at Lusha's end and RampedUp supplied only the observed identifiers, or 'opted-in' is doing work the data cannot support. That is the single question to put to them, and it is answerable in one line. Metrics: 9,937 deletions and 9,937 opt-outs, all complied, mean 1 day -- but whole=part=9,937, the same-figure-in-every-box pattern from SF 239, so treat the numbers as decorative.

## Steps

1. Do not email at all. `contact@rampedup.io` is an unmonitored inbox that
   auto-replies to everything; `privacy@rampedup.io` is a restricted Google
   Group that bounces regardless of message content.
2. Use `https://basic.rampedup.io/app/donotsell` directly.

## Gotchas

- **The CA registration address is a Google Group, not a mailbox.** This is the recurring "internal-only distribution group" bounce class: it looks like any other 550 but Gmail's own delivery-failure text names it explicitly ("group you tried to contact ... may not exist, or you may not have permission to post"). The fix is the same every time — find a second address on the broker's own site, not a variant guess.
- **Neither published email address is actually monitored.** One is a dead
  Google Group, the other auto-replies "not a monitored inbox" to everything
  including a properly formatted opt-out letter. The portal is not a
  fallback here — it's the only route.

## Verification

No confirmation yet — pending the do-not-sell portal submission. No stated
timeframe found; ask when submitting.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** RampedUp
- **Registered address:** 1551 Dunwoody Village Parkway,, Dunwoody, GA,
  30338
- **Filed contact email:** privacy@rampedup.io
- **Filed phone:** 8882783433
- **Website:** rampedup.io

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
