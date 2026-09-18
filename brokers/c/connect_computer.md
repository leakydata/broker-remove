# Connect Computer LLC

- **Email:** support@calltruth.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** calltruth.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-28)
- Note: PERMANENT FAILURE CONFIRMED 2026-08-28, third and final bounce (26th, 27th, 28th Aug). 'DNS Error: DNS type mx lookup of calltruth.com responded with code SERVFAIL', status 4.4.3 -- a TEMPORARY code that simply never resolved, which is why it took three days to become final. Verified by hand: calltruth.com SERVFAILs on NS, SOA, MX and A, from two independent resolvers. The domain is still REGISTERED (eNom, clientTransferProhibited) and still delegated to DNS1-4.NAME-SERVICES.COM, but those nameservers do not answer. So this is a third distinct shape alongside the ones already in dead_addresses.json: NXDOMAIN means the name does not exist, no-MX-no-A means the name exists with no mail route, and SERVFAIL means the name is delegated to nameservers that are broken or gone. Practically undeliverable and slow to prove, because a resolver cannot tell a broken nameserver from a briefly unreachable one -- which is also why check_email_domains.py cannot pre-empt this class the way it pre-empts the other two. Retry only if the delegation is ever seen to answer.

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

> **Correction (2026-08-25):** That same day's run sent another request to `support@calltruth.com`, which this playbook already recorded as `unreachable` earlier the same day. Same root cause as the note above (registry email_to didn't reflect this playbook's own status) — no new information, no status change.

> **Correction (2026-08-29):** the same thing happened again, later. A letter reached `support@calltruth.com` around 2026-08-26, sat as a "delivery incomplete, will retry" notice for two days — exactly the pattern this playbook already warned about for a SERVFAIL domain — and hard-failed on 2026-08-28. The registry's `email_verified` flag was still `true` (`ca_data_broker_registry`) at the time, which is presumably why it went out; corrected the flag to `false`/`bounced` here so the queue itself carries the finding, not only this file's prose.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Connect Computer LLC
- **Registered address:** 2470 Windy Hill Road, Suite 226, Marietta, GA
  30067, United States
- **Filed contact email:** support@calltruth.com
- **Website:** http://calltruth.com
- **Opt-out route they filed:** A consumer may opt out of sale under the
  CCPA by visiting https://www.calltruth.com/opt_out.php (which can be
  accessed directly at the provided URL or by clicking the 'Do Not Sell
  My Info'Â hyperlink on the CallTruth homepage). Customers can submit
  other requests and also opt out by emailing CallTruth customer support
  at support@calltruth.com.
- **Route for protected individuals:** A consumer may opt out of having
  their listing displayed by going online to
  https://www.calltruth.com/opt_out.php and submitting a request. A
  consumer may also contact Customer Care at support@calltruth.com or
  mail in their request at the business address. (Cal. Gov. Code
  6208.1(b) / 6254.21(c)(1) — for survivors of domestic violence,
  stalking and similar, a stronger and faster route than the ordinary
  consumer request)
- **What they say they collect:** Additional information can be found in
  our Privacy Policy located at https://www.calltruth.com/privacy.php.

*Source: `data/registries/complete-reg-data-brokers.csv`.*

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
