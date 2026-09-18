# Pathway Ventures, LLC

- **Email:** ~~privacyofficer@indivizio.com~~ — **hard-bounces 550, do not use.** It
  is the address in their own California registry filing; the domain behind it
  does not exist.
- **Method:** email — no working route found.
- **Domain:** indivizio.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Note: Recovered from the committed playbook brokers/p/pathway_ventures.md, because the ledger carries no notes and this row's status had no evidence behind it: 2026-08-28: The 2026-08-27 first-contact letter looked like a normal submission and was logged `submitted` — it had in fact hard-bounced the same day (550, address not found). `indivizio.com` has **no A record at all**: the domain does not resolve, so there is no site to read for an alternative address and no route of any kind. Registry has no other notes on Pathway Ventures / Indivizio, so there is no clue what the business actually does either.

## Steps

No route exists. The registered contact domain does not resolve, so nothing was
ever, and can currently be, delivered. If the domain is ever reinstated, or a
successor entity files a later state registration under the same legal name,
re-run `scripts/check_email_domains.py` and the route reopens.

## Gotchas

**A bounced send can still get logged `submitted`.** This entry was marked
`submitted` on the same day the letter hard-bounced — the send succeeded, the
delivery didn't, and nobody checked the bounce folder before recording the
status. Check `check_email_domains.py` (or just resolve the domain) *before*
spending a send on an entry sourced only from a state registry filing — a
filing records an address at the time it was made, not that the domain still
exists.

## Verification

Nothing to verify. Re-check the domain periodically; a dead domain can mean a
lapsed registration, a wound-up company, or a rebrand that left the filing
behind, and only the last of those reopens.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Pathway Ventures, LLC
- **Registered address:** 4464 Lone Tree Way Unit #3135, Antioch, CA
- **Filed contact email:** privacyofficer@indivizio.com
- **Website:** https://www.indivizio.com

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
