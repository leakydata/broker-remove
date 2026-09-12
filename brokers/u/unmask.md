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
