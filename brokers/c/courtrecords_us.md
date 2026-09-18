# Courtrecords Us

- **Opt-out:** https://courtrecords.us/optout/
- **Email:** privacy@courtrecords.us (verified)
- **Method:** web_form — Web form.
- **Domain:** courtrecords.us
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Reference: `gmail:1a00c8769c5bb484`
- Note: Zendesk ticket opened; reference issued. Same privacy queue serves the whole state-court-records family.

## Steps

1. One consolidated letter to `privacy@courtrecords.us`, naming **all 51 state
   properties explicitly** rather than the parent domain alone.
2. Include the full identifier set — every email address, every former address,
   every former phone. Court-record aggregators are address- and name-keyed, and
   a partial identifier set gets a partial match.
3. Ask which properties actually held a record. Their answer is the only way to
   know what the request covered.
4. Record the Zendesk ticket number they issue.

## Gotchas

Fifty-one state-named sites, one privacy queue. The family shares a Zendesk
instance — ticket numbers issued to this domain fall in the same range as those
from the sibling brands, which is how the shared operator is visible from outside
(see `_BROKER_FAMILIES.md`).

**Name the properties.** A letter addressed to the parent gets a reply about the
parent. Listing the state sites by name in the request is what makes "which
properties held a record?" a question they have to answer rather than one they
can read as rhetorical.

Court-record data carries a second problem beyond exposure: it is often simply
wrong, or attached to the wrong person of the same name. Ask them to **disclose
any entry attributed to the subject and its source**, not only to delete it. A
deleted inaccurate record leaves the source intact and the record reappears at
the next refresh; a disclosed one can be corrected upstream.

Expect the FCRA-exemption argument if they sell background reports as well as
search results — `_DEFLECTIONS.md` covers the response.

## Verification

The ticket reference is the lever. Reply on the ticket rather than filing again —
a second request restarts a clock and loses the scope already agreed.

Ask for two things specifically: **which properties held a record**, and **the
date the removal took effect**. "Your request has been completed" across a family
of dozens of sites, with no list, is not a verifiable answer.

Re-run the public search on the individual state properties, not just the parent
domain. A family index can be cleared centrally and still serve a cached profile
on one sub-site.

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
