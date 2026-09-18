# CyberBackgroundChecks

- **Opt-out:** https://www.cyberbackgroundchecks.com/removal
- **Status: page-load gated.** Cloudflare "Performing security verification"
  blocks the page before any form is reachable.
- **Priority: 4.**

## Blocked at the door
Automation cannot reach the form at all — this is a page-load gate, not a submit
gate. See `_CLOUDFLARE_GATED.md` for the distinction and why it matters.

**Before writing it off**, try the alternate-route pattern that unblocked three
other brokers here:

    /privacy-rights   /do-not-sell   /ccpa   /request-my-info
    /notice-at-collection   + the footer "Do Not Sell or Share My Personal Information"

If none is reachable, use the statutory email route
(`scripts/make_optout_email.py`) and say in the letter that the self-service form
is inaccessible — that is a fact worth putting on the record, and several brokers
have responded to exactly that framing by processing the request directly.


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

1. **Open the opt-out page:** https://www.cyberbackgroundchecks.com/removal
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
