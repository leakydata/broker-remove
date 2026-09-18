# Roc Advertising

- **Email:** dataprivacy_rocadvertising@simpleoptoutcompliance.com — verified against their own published page
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** simpleoptoutcompliance.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Resent 2026-08-20 to first-party privacy@rocadvertising.com after the published vendor address at simpleoptoutcompliance.com hard-bounced 550 5.1.1. Subject line 'Data Removal Request' as their policy requires.

## Steps

1. **Do not use the address in the aggregator listings.**
   `dataprivacy_rocadvertising@simpleoptoutcompliance.com` hard-bounces
   `550 5.1.1`. The domain resolves and has an SES inbound MX, so the bounce is
   mailbox-level, not domain-level — it looks like a typo and is not one.
2. Fetch `https://www.rocadvertising.com/privacy-policy/` and **decode HTML
   entities before extracting addresses** (see `_SILENT_FAILURES.md` §64). The
   live address is `privacy@` their own domain, written entirely as character
   entities, twice, with different decimal/hex mixes each time.
3. Send with the exact subject line their policy requires:
   **`Data Removal Request`**.
4. Ask for suppression, not only deletion — their policy states they buy
   one-time mailing lists from a data broker, so the record is re-acquirable by
   construction.

## Gotchas

- **The corporate name is not the brand name.** The policy attributes the
  list-rental business to "Results Only Consulting", not to ROC Advertising.
  Address the letter to both; a mailbox that files by legal entity will not
  match a letter addressed only to the trading name.
- **They publish their own answer.** Their policy says consumers "may delete
  their record, opt-out or unsubscribe from having their data rented or sold"
  by writing with that subject line. Quote it rather than arguing statute — the
  ask is theirs, and there is nothing left to dispute.
- **A stated mailing lead time.** The policy warns that advertising prepared in
  advance may continue for "up to 10-days after unsubscribing, and 45-days after
  opting-out or deleting their record". Treat 45 days, not the confirmation
  date, as the point at which to judge whether it worked.

## Verification

No public profile to re-check — this is a mail-list business, so the observable
is mail volume, not a search result. Their own policy sets the window: judge at
**45 days after confirmation**, not before. If mail continues past that, quote
the 45-day figure back at them; it is their number.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Results Only Consulting and Advertising
- **Registered address:** 4251 Gateway Blvd, Suite B, Sacramento, CA
  95834, United States
- **Filed contact email:** dataprivacy_ROCAdvertising@SimpleOptOutCompliance.com
- **Website:** http://www.rocadvertising.com
- **Opt-out route they filed:** To complete your data privacy request,
  please submit an email to
  dataprivacy_rocadvertising@simpleoptoutcompliance.com with the subject
  line titled â€œData Removal Requestâ€ and we will promptly process
  your request.
- **Route for protected individuals:** To complete your demand for
  deletion request, please submit an email
  dataprivacy_rocadvertising@simpleoptoutcompliance.com with the subject
  line titled â€œData Deletion Requestâ€ and we will promptly process
  your request. (Cal. Gov. Code 6208.1(b) / 6254.21(c)(1) — for survivors
  of domestic violence, stalking and similar, a stronger and faster route
  than the ordinary consumer request)
- **What they say they collect:** Consumers may visit
  https://www.rocadvertising.com/privacy-policy/ to view our privacy
  policy which includes data collecting practices.

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
