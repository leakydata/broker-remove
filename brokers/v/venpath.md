# VenPath

- **Opt-out:** —
- **Email:** privacy@venpath.net — **a Google Group closed to external posting.**
  Not a mailbox.
- **Method:** email
- **Domain:** venpath.net
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-20)
- Note: privacy@venpath.net is a GOOGLE GROUP, not a mailbox: bounce reads 'the group you tried to contact (privacy) may not exist, or you may not have permission to post messages to the group', signed 'venpath.net admins'. Not a 5.1.1. venpath.net has NO A record (site gone) but LIVE Google MX - the website is dead while the Workspace tenant is still paid for. Inverse of the Tymax case in 68.

## Gotchas

**Pre-empt the MAID wall instead of waiting for it.** Mobile-app and location
data businesses reply that they hold only advertising identifiers and that the
requester must supply theirs. Answering that in the first letter saves a full
round trip. The argument, in short:

> A consumer cannot look up their own advertising identifiers historically. Both
> mobile platforms show only the current value, and only while the setting is
> enabled. Resetting one mints a new identifier without retiring the old, so a
> phone used in 2019 has emitted several IDs that cannot be recovered — and those
> are precisely the ones attached to any data already held. A request that can
> only be made by supplying advertising identifiers is one the consumer is
> structurally unable to make.

Frame it as a description of the identifier, not as an accusation.

**Then give them a query they can actually run.** Substitute a **geographic
query**: search for any device showing a persistent overnight dwell pattern at
the current residence and each prior one; delete what matches; suppress so it is
not re-onboarded from a supply partner. Accept "no such device" as a complete
answer, in writing, and say so.

**The legal hinge:** a device appearing at the same dwelling every night for
months is not anonymous — the address is the identifier. Under CCPA as amended,
information reasonably capable of being associated with a particular consumer
*or household* is personal information.

**Three follow-ons for every location broker:** treat device-to-home-address
inference as identifying rather than derived analytics; name whether data touches
sensitive location categories (worship, medical and reproductive health,
addiction and mental health treatment, domestic violence shelters, union halls,
immigration services); and identify supply partners upstream and buyers
downstream.

**Never send a MAID to prove one is not held.** It hands a live identifier and an
email address to associate it with, in exchange for a search of the one ID least
likely to be in a historical file.

## Verification

Depends entirely on the written answer. A reply that repeats the MAID
requirement without addressing the dwell-pattern search has not answered it.

## Outcome: no route

The letter did not bounce as an unknown user. It bounced as a rejected mailing
list post:

> "We're writing to let you know that the group you tried to contact (privacy)
> may not exist, or you may not have permission to post messages to the group."
>
> — signed `venpath.net admins`

That is Google Workspace rejecting a post to a **Group**, which is a different
finding from "no such mailbox" and calls for a different response. There is
probably a `privacy` group; it is restricted to domain members. Every consumer
following the published privacy policy is rejected by configuration, and the
bounce text blames the sender for possibly misspelling the group name.

**Do not guess further local parts after this bounce.** Guessing is right after a
5.1.1 on a guessed address; it is pointless here, because the failure is not
about which name was used.

**The DNS finishes the story:**

```
dig +short A  venpath.net   →  (nothing)
dig +short MX venpath.net   →  aspmx.l.google.com. — live
```

No website, live mail. The site is gone and the Workspace tenant is still being
paid for — the exact inverse of Tymax in `_SILENT_FAILURES.md` §68, where live MX
fronted a for-lease parking page. Written up as §72.

Recorded `unreachable` rather than `failed` (nothing was refused) or `pending`
(nothing is left to try).

**The letter itself is still worth keeping** — the MAID pre-emption and the
geographic-query substitute below apply to every mobile-location broker, and this
one simply has nobody left to read it.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Venpath
- **Registered address:** 228 Park Ave S #37362, New York, NY
- **Filed contact email:** privacy@venpath.net
- **Website:** https://www.venpath.net

*Source: `data/registries/registry2024.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.venpath.net/legal/opt-out
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@venpath.net`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
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
