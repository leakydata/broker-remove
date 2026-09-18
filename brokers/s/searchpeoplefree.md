# SearchPeopleFREE

- **Opt-out:** https://www.searchpeoplefree.com/opt-out
- **Method:** two-stage — name+email → emailed link → full form
- **Gate:** Cloudflare Turnstile on the first stage, but it **auto-passes**
  (observed showing "Success!" without interaction). Page itself is not blocked.
- **Priority: 4.**

## Route
1. `/opt-out` → First / **Middle** / Last / Email + consent checkbox →
   **Begin removal process**
2. A link is emailed. **Expires in 24 hours** — after that, request a new one.
3. The linked form takes the full record details. Their guidance is explicit:
   *"Omitting information or providing inaccurate information on the opt-out form
   will only hinder the opt-out process."* Fill everything, including middle name.
4. Confirmation page + confirmation email. **3 days** to full removal.

Same two-stage shape as PeopleFinders — see `brokers/p/peoplefinders.md`, whose
pre-filled-name trap is worth re-reading before doing this one.

## Gotchas
- **Their matching is strict.** From their own FAQ: *"If our system cannot match
  the provided information to a record, the information will not be removed."* A
  near-miss silently fails rather than erroring — supply prior addresses and old
  phone numbers.
- To verify, they instruct you to **clear browser cache first**, then search again.
  A cached page will show a stale listing and look like failure.
- Heavy third-party ads on the page shift the layout as they load, which
  invalidates element references mid-form. Re-locate fields immediately before
  typing, and screenshot to confirm values landed.

## Lead worth following
Their own page advertises **EnformionGO** as the partner API behind their data
("Fast Developer API for Contact Enrichment, Sales, and Marketing Intelligence").
**Enformion is the upstream source** — removal here does not touch it. Worth
adding Enformion to the registry and filing separately; upstream removals reduce
re-population downstream.


## Part of the Mississippi Tornado Alley family

This site is one of **ten** named in a single 2026 California data broker
registration by **Mississippi Tornado Alley, LLC**, alongside
CyberBackgroundChecks, AdvancedBackgroundChecks, FastBackgroundCheck,
PeopleSearchNow, Phonebooks, SearchPeopleFree, SmartBackgroundChecks,
USA-People-Search, USPhoneBook and FastPeopleSearch.

Nothing on any of the sites connects them, and the legal entity's name appears on
none of them. See `mississippi_tornado_alley.md` for the consolidated letter sent
to `privacy@mtalley.zendesk.com` on 2026-08-23, and `_FAMILIES.md` for the
method.

**Read any confirmation from this site for scope.** One naming only this hostname
leaves nine siblings unaddressed, and that is indistinguishable from a complete
removal from the outside. The individual thread stays open until the family
answers for the estate.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.searchpeoplefree.com/opt-out
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `support@searchpeoplefree.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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
