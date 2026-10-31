# All Global Resources, LLC

- **Email:** info@agrgroupinc.com — the only address on either known domain that has never bounced
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** agrgroupinc.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-10-18)
- 2026-10-31: The 2026-10-18 resend to `info@agrgroupinc.com` has now gone 13
  days with no bounce and no reply. No bounce is mild positive evidence the
  mailbox is live (better than the three confirmed dead ends), but it is not
  a reply, and the CCPA 45-day clock runs from 2026-10-18 — due ~2026-12-02.
  Nothing to chase yet; re-check after the deadline passes.
- 2026-10-18: THE THIRD ADDRESS BOUNCED TOO. `drieke@executiveenergy.com` (found via the Vermont Act 171 filing, see below) hard-bounced within a minute — NXDOMAIN, `executiveenergy.com` does not resolve at all, so the whole domain is dead, not just the mailbox. That makes four dead ends across two domains: `lzepeda@agrgroupinc.com` (mailbox unavailable), `privacy@agrgroupinc.com` (Microsoft 365 access-denied), the `agrgroupinc.com` website itself (no HTTP route), and now `drieke@executiveenergy.com` (domain doesn't exist). **The one constant across every attempt: `info@agrgroupinc.com` has never bounced**, including when cc'd on both the August administrative note and the October full request. Promoted it from cc to primary recipient and resent the full consumer request there directly rather than only copying it. Not yet verified as delivered or as a working privacy intake — a mailbox that accepts mail is not evidence it is read or actioned, only better odds than three confirmed dead ends. `email_verified` stays `false` until there's a reply or a non-bounce confirmation beyond "it didn't come back."
- 2026-10-17: Found a THIRD address by checking a registry this entry had not previously checked. All prior notes here only covered the California filing (`lzepeda@`, then `privacy@`, both bounced). All Global Resources is **also** registered in Vermont under Act 171 of 2018, and that filing names a different contact entirely: `drieke@executiveenergy.com` — a different domain, suggesting the same person operates more than one entity. Sent the full consumer request there, cc `info@agrgroupinc.com`. Worth noting: `info@agrgroupinc.com` was cc'd on the August admin note too and has never bounced, unlike `privacy@` and `lzepeda@` at the same domain — it may be the one live mailbox on that tenant. **Lesson for other lapsed-looking brokers: check every state registry the company is listed in, not just the one that happened to be checked first.** A company can let one state's contact rot while another stays current.
- Note: THE LETTER BOUNCED IN TWO SECONDS, SO 502 WAS WRONG TOO. The MX record is live but THE MAILBOX IS NOT. Exact response from their own server: '550 5.4.1 Recipient address rejected: Access denied' from agrgroupinc-com.mail.protection.outlook.com. On Exchange Online a 5.4.1 recipient rejection means the address is not in the directory -- a live Microsoft 365 tenant with that mailbox gone, which usually means the named person has left. So the chain of my own errors today runs: 501 said no DNS therefore dead; 502 said MX is live therefore reachable; this says MX LIVE DOES NOT MEAN DELIVERABLE. Each step was a real improvement and each was still wrong, and the only thing that settled it was sending something and reading the bounce. SECOND ATTEMPT SENT, deliberately different in kind: a SHORT ADMINISTRATIVE NOTE WITH NO PERSONAL DATA IN IT, to privacy@agrgroupinc.com copying info@, asking only where a consumer request should be sent. Guessing addresses is reasonable; guessing addresses while attaching four email addresses, sixteen postal addresses, eleven phone numbers and a date of birth is not. Quoted the SMTP error to them and made the point that a bouncing registered contact leaves every consumer who follows the official route with a bounce and no next step -- and that the registration is now the ONLY published route, since the website is gone. Status manual_required rather than unreachable: there is a live tenant and a plausible path, it just needs a human to find the right mailbox.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `info@agrgroupinc.com`** with a written request — `privacy@agrgroupinc.com`, `lzepeda@agrgroupinc.com`, and `drieke@executiveenergy.com` have all bounced; this is the only address that hasn't. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

**Re-confirmed (2026-09-03):** agrgroupinc.com is now unreachable from every angle (DNS/connect failures on all attempts, not just HTTP), and the company is absent from the CPPA's current (2025) data broker registry entirely — the 2024 filing that named the already-dead `lzepeda@` address appears to have lapsed rather than been renewed. Consistent with the company having wound down since the original registration. No further route found; the postal fallback noted above remains the only option if this is ever pursued further.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** All Global Resources, LLC
- **Registered address:** 2925 N. Green Valley Parkway, Suite C,
  Henderson, NV
- **Filed contact email:** [named individual]@agrgroupinc.com
- **Website:** https://www.agrgroupinc.com

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
