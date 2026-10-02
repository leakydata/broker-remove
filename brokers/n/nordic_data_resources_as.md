# Nordic Data Resources AS

- **Email:** privacy@nordicdataresources.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** nordicdataresources.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-10-01)
- Reference: `gmail:1a0f8a285f571243`
- **2026-10-01: CONFIRMED.** Final reply states the pseudonymous profile and personal data tied to the *verified* identifier (the sending address) have been **deleted from active systems**, the direct-marketing objection and sale/sharing opt-out have been **registered**, and a minimal technical suppression record is retained solely to give effect to the opt-out (not for enrichment). Explicitly confirms the request is handled under the GDPR as an EEA-established controller and is **not** being declined on the basis of Pennsylvania residence. No active or archived audience segments, including none of the named special-category segments (health, political opinion, religion, sexual orientation, ethnicity, trade union). They declined to attribute the profile to a specific upstream source, saying their own records don't reliably establish that provenance — a believable limitation rather than a stonewall, since the rest of the reply was unusually forthcoming. The other eleven email identifiers remain pending the evidentiary-verification offer (archived correspondence, account/service records) — not pursued, same reasoning as onaudience.md. Closing at `confirmed` for the verified identifier.
- Note: 2026-09-05 (§339): A VERIFICATION RULE THAT IS RIGHT IN GENERAL AND IMPOSSIBLE HERE. NDR will process only the SENDING address: 'we are unable to process a request relating to an email address solely on the basis of a message sent from a different address... please submit a separate request from each relevant address.' Sound in principle, and I said so. BUT FOUR OF THE TWELVE ADDRESSES CANNOT SEND MAIL AND NEVER WILL: [EMAIL] (WebTV shut 2013), [EMAIL] (ISP gone), [EMAIL] (folded into Ask.com), [EMAIL] (closed university mailbox). Not reluctance -- the providers do not exist. AND THOSE FOUR ARE THE LIKELIEST TO BE IN THE FILE, since a record compiled years ago is keyed to whatever address was current then. So the rule as applied means THE RECORDS MOST LIKELY TO EXIST ARE THE ONES NOBODY ON EARTH CAN EVER REQUEST REMOVAL OF -- the HealthLink Dimensions shape, arriving from a European controller with a better-reasoned policy. PROPOSED THE EXCLUDE-ONLY ROUTE: treat the four as search keys for suppression rather than verified deletion requests -- do not say what matched, do not confirm anything, simply suppress. If an impostor did it the worst case is a stranger's dead address stops being targeted; the risk of acting is nil and the cost of not acting is that the data is permanent. Offered to send separate messages from the addresses that still work. PRESSED THE HASH POINT, which their own reply sharpens: they say they process 'data relating to internet users' but not names, addresses or phone numbers, so the key is an identifier, and in this industry that is usually a HASHED EMAIL. Asked them to hash the addresses themselves (lowercased, trimmed, SHA-256 plus MD5/SHA-1) and search the results -- costs nothing, discloses nothing, needs no verification since I am not asking to see what comes back. Three questions still open: which framework (Norwegian AS -- GDPR follows establishment, not data-subject location), lawful basis and provenance of the segments, and whether any segment touches special category data.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `privacy@nordicdataresources.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

- **They will only process the sending address without extra proof** — a
  verification-by-sender-address rule, applied consistently even though it
  structurally excludes the oldest, most-likely-to-match addresses (closed
  mailboxes can never send the confirming email). They accept archived
  correspondence or account/service records as alternative evidence for a
  dead address, instead of refusing outright — worth citing to other
  advertising-identity brokers who refuse unverified addresses with no
  alternative path at all.
- **Explicitly GDPR-governed, not state-law-gated**: an EEA-established
  controller handles a Pennsylvania resident's request under GDPR and says
  so in writing — "not declining on the basis of your residence." A useful
  model reply to quote back at a US broker that tries a residence deflection.
- **They distinguish "received or observed" data from "inferred or modeled"
  characteristics** in their own disclosures — ask for that split explicitly
  with any identity-graph/ad-tech broker, since it changes what a deletion
  actually removes.

## Verification

Re-email `privacy@nordicdataresources.com` after some months asking whether a
fresh search against the verified identifier still returns nothing, and
whether any of the eleven suppressed-but-unverified addresses has since
turned up a record.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Nordic Data Resources AS
- **Registered address:** Hvervenmoveien 49, Hønefoss, Oslo, 3511
- **Filed contact email:** privacy@nordicdataresources.com
- **Filed phone:** 708679178
- **Website:** www.nordicdataresources.com

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
