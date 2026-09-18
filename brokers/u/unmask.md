# Unmask

- **Opt-out:** —
- **Email:** contact@unmask.com — unverified. Their privacy policy returns
  **403** to a scripted fetch, so no dedicated privacy address could be read.
- **Method:** email
- **Domain:** unmask.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-26)
- Reference: `gmail:1a01f8b25904557d`
- Note: 2026-08-26 (reply received 2026-08-25, recorded late): UnMask confirmed 'the record listed for [PERSONAL] has been successfully removed'. Route note worth keeping: their first reply asked for the details in a specific format, and the answer was to restate what the original letter already contained rather than supply anything new - 'happy to give this in the cleaner format you asked for, note it is unchanged from my original message, I am restating it, not adding anything new.' That framing gets a re-formatted request accepted without conceding that the first one was incomplete. Re-verify the listing.

## Gotchas

**A 403 is not a NO_EMAIL.** `verify_emails.py` reports NO_EMAIL for this
domain, but the cause is a bot block on the privacy policy, not an absent
address. Those two states are worth distinguishing before concluding anything —
the same lesson as `_SILENT_FAILURES.md` §65's note on failed fetches. Send to
the address on record and say in the letter why:

> Your privacy policy returns 403 to an ordinary request from a Linux desktop
> browser, so I have not been able to read it to find the address you would
> prefer I use. If there is a dedicated privacy mailbox, please forward this
> rather than reply asking me to resend, and please tell me what it is.

Asking them to forward-and-name is cheap for them and turns a blocked scrape
into a verified registry entry.

**It is a people search *and* a reverse lookup.** Ask for the identifier
direction as well as the name direction: a search on any phone number or email
must not return the name, address, or a "possible owner" suggestion. A profile
page can be gone while the lookup still resolves.

**The four standard people-search asks apply**: `noindex` on any URL that carried
the name; removal of appearances on *other people's* profiles as relative,
associate or household member; a statement of whether this is suppression or a
one-time removal; and whether the removal covers sibling sites.

**Protect reassigned numbers.** Ask them to suppress the historical association
with the subject's name rather than remove whatever record currently exists for
an old number.

**Common-name caution.** Ask them to match on date of birth and not to remove
other people's records.

## Verification

Search the site directly for the name, then run a reverse lookup on the current
number and two prior numbers. A name search alone will not detect a surviving
reverse mapping.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** UNMASK, LLC
- **Registered address:** 6900 Tavistock Lakes Blvd STE 400, Orlando,
  Florida, 32827
- **Filed contact email:** compliance@unmask.com
- **Filed phone:** 3213766933
- **Website:** unmask.com

*Source: `data/registries/registry.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://unmask.com/opt-out/
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `compliance@unmask.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
