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
