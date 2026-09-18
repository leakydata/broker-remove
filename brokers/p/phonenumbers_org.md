# Phonenumbers Org

- **Opt-out:** https://phonenumbers.org/optout/
- **Email:** privacy@privacy.phonenumbers.org — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** privacy.phonenumbers.org
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-09-07)
- Reference: `no acknowledgement; 45-day window open until ~2026-10-01`
- Note: RESTS ON A SEND AND NOTHING ELSE, flagged 2026-09-07. No acknowledgement, no reference number, no reply since the 17-19 August letter -- and the company's published opt-out URL now returns HTTP 404, so if the email did not land there is no second channel to fall back on. 'submitted' is doing more work for this row than the evidence supports; treat it as sent, not as received. See SILENT_FAILURES 393. NOT CHASED YET, DELIBERATELY: at 19-21 days this is well inside a 45-day response window and nothing is overdue. Telling a company it is late when it is not is both wrong and costs credibility on every later letter. DIARISED FOR THE FIRST WEEK OF OCTOBER 2026, when the ask is an acknowledgement rather than an accusation, and the dead route becomes a fact to report to them rather than a grievance -- your published opt-out URL returns 404, so if my email did not reach you there is now no route at all. A NOTE ON WHY THIS ROW IS NOT AN ERROR: a cross-reference of dead routes against submitted rows initially looked like fourteen requests filed through doors that no longer exist. All fourteen went by EMAIL; the dead URL is a stale field on the broker record, not the channel used. The route field describes the company, the via field describes the transaction, and joining on the wrong one manufactures an alarm.

## Steps

1. Write to **`privacy@privacy.phonenumbers.org`** — note
   the privacy *subdomain*, not the apex.
2. Standard reverse-lookup framing; see `numberguru.md` and `numlookup.md`.

## Gotchas

**The privacy subdomain has its own mail exchanger, separate from the apex.**
`phonenumbers.org` routes to Google; `privacy.phonenumbers.org` routes to
`aironmail.webair.com`. Those are different mail systems, so a plausible-looking
address guessed at the apex — `privacy@phonenumbers.org` — would land somewhere
else entirely, or nowhere.

> Where a broker publishes an address on a subdomain, use the subdomain exactly.
> The extra label is not decoration; it is a different destination.

Otherwise the standard reverse-lookup asks apply: search every prior number, not
the current one; remove the association in both directions; strip carrier,
line-type and location enrichment; suppression versus one-time removal; and
whether the lookup is answered from a stored index or resolved live against a
supplier at query time.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

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
