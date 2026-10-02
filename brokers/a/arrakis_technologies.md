# Arrakis Technologies Corp.

- **Email:** privacy@arrakis.ai (corrected 2026-10-01; sam@arrakis.ai bounced when the domain was dead)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** arrakis.ai
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-10-01)
- Reference: `gmail:1a0f6f940dfbb611`
- Note: 2026-08-25: bounced - 'the domain arrakis.ai couldn't be found'. NXDOMAIN: no MX, no A, no SOA. The domain is gone entirely, so the company is presumed defunct. Our checker correctly returns False for it; the row was queued anyway, which means the queue is not consulting the deliverability verdict before sending. Worth wiring up.
- 2026-10-01: domain is back. arrakis.ai now resolves (HTTP 503 on direct fetch, consistent with bot-protection rather than a dead site, not NXDOMAIN). Re-sent to `privacy@arrakis.ai` — the CA-registry-filed contact — rather than the originally-bounced `sam@arrakis.ai`.
- **2026-10-01: Reply — company shutting down.** `privacy+noreply@arrakis.ai` (from "Sam"): "We are closing down the business and have deleted our contact database. If you are an automated service, please remove Arrakis from your data broker list." Recording as `not_found` rather than `confirmed`: the statement is that the *whole* database is gone as part of winding down, not that our specific record was located and removed. Combined with the earlier dead-then-live DNS flip, this reads as a company genuinely in the process of shutting down rather than a bot wall or a rebrand. No ticket, no per-identifier confirmation — nothing to verify against going forward. If the domain goes fully dark again (NXDOMAIN) on a future check, that corroborates closure; if it instead starts resolving to a *different* company, that's a sold/rebranded domain and the request needs re-sending to whoever now controls it.

## Steps

No route exists. Both the registered contact domain and the company's
own domain publish no MX and no A record, so nothing was ever sent.

If the domain is ever reinstated, or a successor entity files a later state
registration under the same legal name, re-run
`scripts/check_email_domains.py` and the route reopens.

## Gotchas

**Do not "just try it".** A domain with no mail records produces a
*delayed delivery* notice and roughly 48 hours of retries before failing, so a
letter here would sit at `submitted` for two days and teach nobody anything. That
is the whole reason the deliverability check runs before the send rather than
after — see `_SILENT_FAILURES.md` §86.

## Verification

Nothing to verify. Re-check the domain periodically; a dead
domain can mean a lapsed registration, a wound-up company, or a rebrand that left
the filing behind, and only the last of those reopens.


## Unreachable: no mail route exists

Both the contact address published in their California data broker registration
**and** the company's own domain have no MX record and no A record. There is
nowhere to deliver a message, so no letter was ever sent.

Found by `check_email_domains.py`, which asks whether a contact domain can
receive mail at all before a send is spent on it. See `_SILENT_FAILURES.md` §86.

**Why this is `unreachable` rather than `failed`.** Nothing was attempted and
nothing was refused. A domain with no mail records produces a *delayed delivery*
notice and roughly 48 hours of retries before it finally fails, so writing here
would have shown `submitted` for two days and taught nobody anything.

**Re-check rather than treating this as final.** A dead domain can mean a lapsed
registration, a company that has wound up, or a rebrand that left the filing
behind. If the domain is ever reinstated, or a successor entity appears in a
later state registration under the same legal name, the route reopens.

> **Correction (2026-08-25):** That same day's run sent another request to `sam@arrakis.ai`, which this playbook already recorded as `unreachable` earlier the same day. Same root cause as the note above (registry email_to didn't reflect this playbook's own status) — no new information, no status change.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Arrakis Technologies Corp.
- **Registered address:** 548 Market St, PMB 61886, San Francisco, CA
- **Filed contact email:** [named individual]@arrakis.ai
- **Website:** https://www.arrakis.ai

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
