# USATrace

- **Opt-out:** https://www.usatrace.com/your-privacy/
- **Email:** research@usatrace.com (verified)
- **Method:** web_form — Web form.
- **Domain:** usatrace.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Front end for PeopleFinders - the search form says 'Powered by PeopleFinders' and their privacy page states plainly 'USA Trace is not a data broker - we do not store any information, nor do we have access to the information contained in the public record profiles'. Sibling of quickpeopletrace.com; one letter covers both. Their /your-privacy/ page is the most candid writing any broker has produced in this project, and it is worth reading rather than skimming: it explains what data brokers are, concedes it cannot remove anything at source, and offers only to block the preview. Two things asked back that only they can answer: their page says partners are contractually barred from sharing 'social security numbers, ethnicity information, and sexual orientation (among others)' - so what IS in the 'among others'? And do they forward block requests upstream to PeopleFinders, since a block request is a signal that a named person wants suppression even if they cannot act on it themselves. The block tool itself is per-profile and capped at ONE name/profile combination, which is _DEFLECTIONS 30 again, and it must not be used on a profile that has not been positively verified as the subject's.

## Steps

1. Write to `research@usatrace.com` (confirmed — QuickPeopleTrace
   gave it out).
2. Self-service: `/your-privacy/` has a search-and-block tool. Find the profile,
   click block. **48 hours to propagate**, and it covers quickpeopletrace.com too.

## Gotchas

**Their privacy page is the most candid writing any broker has produced in this
project.** It is worth reading rather than skimming — it explains what data
brokers are, states plainly *"USA Trace is not a data broker – we do not store
any information, nor do we have access to the information contained in the public
record profiles"*, and concedes the limit of what it can do: *"this does not
remove the information from the source – it only blocks it from appearing on
USATrace.com"*.

The search form carries **"Powered by PeopleFinders"** at its foot, so the
upstream is stated on the page as well as in correspondence.

**Two things worth asking them, because they are unusually likely to answer.**
Their page says partners are contractually barred from sharing *"social security
numbers, ethnicity information, and sexual orientation (among others)"* — **what
is in the "among others"?** No one else in this sector publishes such a list.
And: **do they pass block requests upstream?** They cannot remove at source, but
a block request is a signal that a named person wants suppression; forwarding it
costs them nothing and they are the sort of operator who might.

**The block is capped at one profile.** *"We will only accommodate one
name/profile combination per person."* `_DEFLECTIONS.md` §30 again — and it bites
hardest on the person with the longest address history, who generates the most
distinct profiles at the source.

**Do not click a profile you have not verified.** The tool is keyed to a search
result, so on a common name the wrong click blocks a stranger's preview and
leaves the subject's in place. Hand this to someone who can recognise their own
record; do not guess from a list.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
