# USATrace

- **Opt-out:** https://www.usatrace.com/your-privacy/
- **Email:** research@usatrace.com (verified)
- **Method:** web_form — Web form.
- **Domain:** usatrace.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-08-19)
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


## Outcome: nothing to block

Their preview index was searched twice. Neither search returned the subject.

- **Name + city + state:** the only entry for that city is a person of the same
  first and last name, a **different middle initial, and 33 years older**, whose
  other locations are three states the subject has never lived in.
- **Name + state, no city:** returns **nobody in that state at all**. The closest
  result by age has an address history entirely in two other states.

So `not_found` on the evidence, and the handoff item was cleared rather than left
open: there is no profile for a human to verify, and verification was the entire
purpose of handing it over. **The risk this flow carries — clicking *Block
Profile* on a stranger's listing — is the only thing that was ever at stake.**

> A search that returns nothing is a result worth recording. It converts
> "pending, someone should look" into "checked, nothing there", and it removes an
> item from the human queue rather than adding one.

## Two defects found while searching

**The state filter is not applied.** A search filtered to one state returns
results in three others. The filter is decorative; the result set is effectively
a national list. Anyone using this tool to find "their" profile is choosing from
a nationwide roster of people who share a name — which makes the
one-profile-per-person cap considerably worse than it first appears, and makes a
wrong click more likely, not less.

**The operating entity appears only in the footer.** `QuickLocate LLC`,
Mechanicsville VA, with a telephone number — a real corporate identity for the
USATrace / QuickPeopleTrace family that the privacy page itself never names.
Worth harvesting: a footer address is often the only place a shell-branded site
admits who runs it.

## The operator who changed the page (updated 2026-08-19)

The fullest reply in this project, from a named person, answering every question
asked rather than the easy subset. Worth reading closely because almost nothing in
it is boilerplate.

### The part that matters beyond one request

The letter had asked them to state the per-request block limit plainly — *"or tell
me plainly that you will not, so I know where I stand"* — because their page said
they accommodate *"one name/profile combination per person"*.

> "There is no limitation on blocks and **I have taken the opportunity to update
> the information on the page to reflect that multiple profiles may be blocked.**"

> **Asking a company to state a limit sometimes removes the limit.** A published
> restriction is often not a policy at all — it is stale wording nobody has
> revisited. Naming it as ambiguous gives them a cheap way to fix it, and the fix
> lands for everyone who reads that page afterwards, not just for you.

This is the only instance so far where raising a documentation problem produced a
documentation change. It cost one paragraph.

### Three plain answers, including two "no"s

- **Enquiry logs:** *"No, we do not."* — they retain no record that a given name
  was searched.
- **Upstream forwarding:** *"No, we do not forward the signal."* A block here tells
  them a named person wants suppression, and that signal stops at their door.
- **"Among others":** the excluded categories are not a secret list — it means
  anything outside the PeopleFinders report scope, bounded by not misleading buyers
  about FCRA-permissible purposes.

> **A plainly-stated "no" is more useful than a hedged "yes".** Two of the three
> answers above are refusals, and all three are now facts that can be relied on and
> quoted. Ask questions whose "no" you would still want in writing.

### Why the identifiers cannot drive the block

This is the structural finding, and it changes how the entry should be worked:

> "The blocking tool (both what we use manually and the consumer facing tool) uses
> **a specific identifying number generated in the profile** (i.e. from
> PeopleFinders.com) ... we would require either a screenshot, a direct link to the
> results page on USATrace.com, or the PeopleFinders link(s)."

They hold no underlying data — *"we can only use this information to make our best
guess(es) by trying to match it with the preview results"* — so a list of addresses
and phone numbers has nothing on their side to match against. The block is a
pointer to somebody else's record.

> **Where a site displays a partner's results, the suppression is keyed to the
> partner's record ID, not to you.** Sending identifiers is the right move at a
> broker that stores data and the wrong move here. This one needs a results-page
> URL or nothing.

**The open question that follows from it** — put to them and still unanswered: if
the upstream profile ID is regenerated, or two records are merged, does an existing
block silently stop matching and the listing reappear under a new ID? If so, a
block here needs periodic re-checking rather than being permanent.

### Declining the "best guess"

They offered to attempt a match from the identifiers. That offer was declined, and
the reasoning is the general rule:

> **Never let a broker guess which record is yours on a common name.** A guessed
> block removes an uninvolved stranger's listing and leaves yours in place. It does
> real harm to someone who never asked for anything, while giving the requester a
> false belief that they are covered — and neither of them ever finds out.

A search of their index returned no positively identifiable result; the closest
same-name match is a different person born decades apart. Recorded `not_found`
with nothing blocked, which is the honest state.

See [[quickpeopletrace]] — same operator, and the sibling that named this one.
