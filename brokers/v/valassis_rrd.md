# Valassis Rrd

- **Opt-out:** https://privacyportal.onetrust.com/webform/45e4be25-919b-483f-9f95-12809576a2b3/6e633594-9a81-48bb-97ab-6fb29bf46019
- **Email:** DataPrivacy@rrd.com (verified)
- **Method:** unknown — Route not yet established.
- **Priority: 1.**

## Status

- Current: `manual_required` (updated 2026-09-19)
- Note: Letter to DataPrivacy@rrd.com 2026-09-12, covering Valassis and the RRD group's direct-mail and marketing data businesses. Two asks beyond the standard letter: (1) deletion-vs-suppression stated as the whole request, because a shared-mail business ingests continuously and a deletion without a persistent entry is a gap that closes at the next ingest; (2) the controller/processor split (444), asking them to name the client for anything held on a client's behalf so it can be redirected rather than answered honestly from the wrong side. Also asked which of several systems was searched -- marketing database, shared-mail household file, client services are three different searches.
- 2026-09-18: two separate OneTrust portal notifications arrived, both "Your
  Privacy Request Needs Attention": Request ID `WKZ2LXPF3V` from
  privacy.requests@privacy.rrd.com, and a second, apparently distinct ticket
  `TE95J69KDE` from valassisprivacy.request@privacy.rrd.com. **RRD's
  notification email never includes the comment text itself** -- only a
  login-gated link into their OneTrust privacy portal. Queued to
  `scripts/handoff.py` for a human to open both and read what was actually
  asked. This is a genuine gap in an email-only workflow: a broker can put a
  substantive question behind a portal login and the requester has no way to
  see it without a browser and an account-free login flow.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://privacyportal.onetrust.com/webform/45e4be25-919b-483f-9f95-12809576a2b3/6e633594-9a81-48bb-97ab-6fb29bf46019
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `DataPrivacy@rrd.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

- **Their portal notifications carry no content.** "Your Privacy Request
  Needs Attention" emails from `*.privacy.rrd.com` addresses only link into a
  OneTrust portal behind a login; the comment itself never appears in the
  email. An email-only workflow cannot answer whatever they asked without a
  human opening that link, which is why this sits at `manual_required`
  rather than `submitted`.
- Two tickets appeared for what was one letter: `WKZ2LXPF3V` from
  privacy.requests@privacy.rrd.com and `TE95J69KDE` from
  valassisprivacy.request@privacy.rrd.com, both dated 2026-09-18. Worth
  checking whether these are the same request split by RRD's intake (Valassis
  vs. the broader RRD group) or genuinely two separate matters.

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
