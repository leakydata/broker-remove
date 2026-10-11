# Contacts411

- **Email:** barrygold@contacts411.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** contacts411.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-10-11)
- Note: COVERED, IF AT ALL, ONLY THROUGH ALESCO -- AND THEIR OWN FILING SAYS SO. Contacts411's California registration practice description states: 'Contacts411 uses ALESCO CONSUMER DATA ONLY which is also CCPA compliant so sometimes we cannot find the individuals to opt out because they are already opted out by our data provider.' That is a named upstream in a statutory filing, and it is the only lever this row has, because the company itself is unreachable by any channel: contacts411.com publishes NO A RECORD AND NO MX, rechecked 2026-10-11, and its registered contact [named individual]@contacts411.com sits on that same dead domain. ACTION TAKEN 2026-10-11: rather than spend another send on a dead domain, put the dependency to ALESCO in the chase on that row, asking whether a suppression at Alesco propagates to customers and licensees, whether he can be added to a suppression file distributed to customers, and if neither, to say so plainly. If Alesco confirms propagation, this row is covered by that answer and should be recorded as covered_by_sibling with the Alesco reply quoted. If Alesco says the suppression stops at its edge, then this row is a genuine dead end -- a company holding and selling a record about him with no reachable address and no upstream willing to cut the supply -- and that is worth recording as such rather than left ambiguous. NOTE THEIR OWN SECOND CLAUSE, which cuts in his favour: they say they sometimes cannot find individuals to opt out BECAUSE THEY ARE ALREADY OPTED OUT BY THEIR DATA PROVIDER. That is Contacts411 asserting that upstream suppression does reach them.

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

> **Correction (2026-08-25):** That same day's run sent another request to `barrygold@contacts411.com (plus an unverified contact@contacts411.com added as a guess)`, which this playbook already recorded as `unreachable` earlier the same day. Same root cause as the note above (registry email_to didn't reflect this playbook's own status) — no new information, no status change.

> **Re-confirmed (2026-09-03):** re-checked rather than taking the 2026-08-25 finding on faith. Still dead: the agent egress proxy reports outright connection failures (CONNECT tunnel rejected) for both `contacts411.com` and `www.contacts411.com` — not just no mail, no reachable web server either. Both bounced addresses (`contact@` and `barrygold@`) now recorded in `dead_addresses.json` as `dead_domain`. No change to the `unreachable` status; this closes the gap where that status had never actually been logged against the address in the shared dead-address file.

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
