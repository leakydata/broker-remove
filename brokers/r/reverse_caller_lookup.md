# Reverse Caller Lookup

- **Email:** support@reversecallerlookup.com (verified)
- **Method:** unknown — Route not yet established.
- **Priority: 1.**

## Status

- Current: `unreachable` (updated 2026-10-11)
- Note: RE-CHECKED 2026-10-10, RESULT INCONCLUSIVE, AND SAYING SO RATHER THAN PICKING A SIDE. reversecallerlookup.com has a DNS record (162.214.79.98), so the domain is registered and pointed somewhere, but curl returned no HTTP status at all on any of /, /privacy, /privacy-policy, /opt-out, /optout, /do-not-sell -- not a timeout code, not a refusal, an empty result. That is consistent with a connection that is dropped rather than refused, which can mean a firewall, a dead listener, or an aggressive bot defence. I cannot tell which from a script, and the three states call for three different responses. LEAVING THE STATUS AT unreachable because I have no evidence to move it, but the row should be treated as UNTESTED rather than confirmed: unlike all_global_resources, which has no DNS at all, this domain resolves, so something is there. Needs a browser session to settle.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `support@reversecallerlookup.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

- **Ask whether results are STORED or ASSEMBLED ON DEMAND.** It changes what a
  deletion can even mean: if the result is built at query time from upstream
  suppliers, there is no record to delete, and a suppression attaches only to the
  keys supplied -- everything outside that set is un-searched, not suppressed.
  That is the difference between a protection and the appearance of one.
- **The upstream names are worth more than the removal.** A removal here does
  nothing about the copy at the source.
- Reassignment: suppress the association keyed to name and DOB, never the bare
  number.

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
