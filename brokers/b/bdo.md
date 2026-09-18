# Bdo

- **Opt-out:** https://www.bdo.com/consumer-request-form
- **Email:** privacy@bdo.com (verified)
- **Method:** web_form — Web form.
- **Domain:** bdo.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Routed to BDO GCI, LLC with a 45-day clock and a working forward address privacy@bdo-gci.com. KEY FINDING: they state the address on their data-broker REGISTRATION (privacy@bdo.com) 'is no longer used for that purpose' -- a registered broker whose registered contact is retired but still published. Replied asking them to correct the registry entry, asking whether GCI scope covers BDO USA P.C. too, and pressing for categories/sources/recipients/suppression-vs-deletion.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://www.bdo.com/consumer-request-form
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@bdo-gci.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## The registered contact that the registrant has retired (updated 2026-08-19)

BDO answered a letter sent to the address published against its data-broker
registration. The reply was routed correctly and put a statutory clock on the
request — and then said this:

> "We understand that you are attempting to submit a privacy request related to
> our Global Corporate Intelligence services, for which BDO has previously
> registered as a data broker under certain state laws using the email address
> privacy@bdo.com. **Please note that this email address is no longer used for
> that purpose.** Your email has been shared with BDO GCI, LLC, which will
> process your request in accordance with applicable law. We expect to process
> your request within forty-five (45) days of receipt. ... Any further
> communications will come from privacy@bdo-gci.com."

Read that again with the consumer's eyes rather than the company's. The registry
is the *only* place a person can look up a broker they have never heard of. The
address in the registry entry is therefore the one address that is both findable
and authoritative. Here it still resolves, still accepts mail, and still gets a
human answer — so nothing bounces, nothing errors, and nothing in the world tells
a sender that they have written to a retired route.

> **A stale registered contact is invisible in a way a dead one is not.** A
> bounce is a signal; a courteous forward is a signal only if someone happens to
> send it. Every other consumer who used the same registry entry got whatever the
> default handling is, and none of them can tell.

This entry did not fail. It succeeded *because BDO chose to forward it*, which is
a property of BDO's goodwill rather than of the published route. The route itself
is wrong.

### The other thing this reply does well, and the gap it leaves

Two entities are named: **BDO GCI, LLC** (dba BDO Global Corporate Intelligence),
which is taking the request, and **BDO USA, P.C.**, pointed to separately via its
own privacy policy. The reply is explicit that these are "separate legal entities."

That is honest, and it is also the gap. A consumer now has to decide whether to
file the same request twice against two entities of one brand, without knowing
whether the second holds anything at all.

> **When a brand splits into entities, ask which entity holds the records before
> filing twice.** The answer is cheap for them and expensive to guess wrong: file
> once and you may miss half; file twice and you have doubled the work and the
> verification burden on yourself for no gain.

### What was asked in return

Beyond the deletion itself, four things, and the fourth is the one that decides
whether any of it lasts twelve months:

1. categories of personal information held at the time of deletion;
2. **sources** — provenance matters more for an intelligence service than for a
   consumer directory;
3. categories of recipient, and confirmation they were directed to delete; and
4. **point-in-time removal or standing suppression** — if the same source supplies
   the same details next quarter, does a suppression record stop the re-add?

See [[_DEFLECTIONS]] for the family of "we are a different entity" answers, and
[[_SILENT_FAILURES]] for the wider class of routes that fail without a signal.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** BDO GCI, LLC
- **Registered address:** 330 North Wabash Avenue, Suite 3200, Chicago,
  IL, 60611
- **Filed contact email:** privacy@bdo-gci.com
- **Filed phone:** 6165758785
- **Website:** https://www.bdo.com

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
