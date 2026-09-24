# Postpilot

- **Email:** privacy@postpilot.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** postpilot.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-23)
- Note: 2026-09-23, privacy@postpilot.com (a different address than the one on file — see below): "This confirms that PostPilot has completed the privacy request for [FIRST LAST]. The associated personal information has been deleted from our systems." Reference: signal. No detail on which identifiers matched, which systems were searched, or whether the identity-graph edges (browsing-session-to-postal-address resolution) were suppressed as well as the row — the three questions in the note below were not answered. Recorded `confirmed` because they affirmatively stated deletion, not merely receipt.
- Prior: Direct-mail RETARGETING for online retailers - postcards triggered by website visits. The valuable asset is not a mailing list but the resolution from a browsing session to a postal address, so that is what the letter targets: the cookie/device/hashed-email/IP to name-and-address mapping, the site-visitor and abandoned-cart matches, and the identity-graph edges underneath. Deleting a mailing record while leaving the ability to re-resolve from the next site visit is not a deletion, so the ask is a permanent do-not-mail AND do-not-resolve. Three questions: which merchant customers the record sits under (a consumer cannot know which shop's visit produced the postcard), which identity partner performs the online-to-postal match (that party holds the graph), and what they hold as controller in their own right.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `[named individual]@postpilot.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

**The registered filing address is not the one that answers.** The CA-registry
address (`[named individual]@postpilot.com`, redacted here) never replied
across two separate letters; `privacy@postpilot.com`, listed only as
`email_alt`, is the one that came back with a substantive deletion
confirmation. Lead with the alt address, not the registered one.

**The confirmation is thin on specifics.** "Completed... deleted from our
systems" with a bare reference code, no statement of which identifiers
matched, which systems were searched, or whether the postal-resolution
identity-graph edges (not just the mailing record) were suppressed. Treat the
outcome as confirmed deletion of *a* record, not necessarily confirmation
that the harder questions in the original letter (which merchant triggered
it, which identity partner performs the resolution) were ever answered.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** PostPilot, Inc.
- **Registered address:** 169 Madison Ave., Suite 11452, New York, NY,
  10016
- **Filed contact email:** [named individual]@postpilot.com (the deletion confirmation came from `privacy@postpilot.com`, the already-recorded `email_alt` — that address is now confirmed live and worth preferring over the registered one)
- **Filed phone:** (854) 205-5367
- **Website:** www.postpilot.com

*Source: `data/registries/registry.csv`.*

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
