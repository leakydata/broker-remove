# Moneybot5000

- **Opt-out:** https://www.moneybot5000.com/svc/optout/search/optouts
- **Email:** support@moneybot5000.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** moneybot5000.com
- **Priority: 2.**

## Status

- Current: `not_found` (updated 2026-10-16)
- **2026-10-16:** Closed the two items left open from the August exchange. Confirmed (b) no data from the search was shared with any data partner, and (c) no financial inference/attribute was held or modeled. Combined with the 2026-10-11 finding below, this broker's handling of this request is now fully closed except for the already-disclosed unclaimed-money carve-out and the Daniel's-Law flag, both noted below.
- Note: DEMONSTRATED NIL ON THEIR PEOPLE SEARCH, 2026-10-11 -- the 518a method, and the site says it in its own words. Drove the opt-out record search at /svc/optout/search/optouts: Cloudflare interstitial self-resolved in about six seconds, then a Turnstile widget had to reach 'Success!' before the Search button would fire -- MY FIRST CLICK DID NOTHING BECAUSE TURNSTILE HAD NOT FINISHED, and the page simply did not move, which is the 484 shape again. Second click after Turnstile succeeded returned results. SEARCHED [PERSONAL] + [PERSONAL] + state PA. THEIR OWN BANNER AT THE TOP OF THE RESULTS READS 'No exact match for [PERSONAL]'. Roughly one hundred namesake records returned, and NONE IS HIM: no record carries the January [YEAR] date of birth, the middle name [PERSONAL], or the [PERSONAL] plus Waynesboro plus State College address history together. This is an OBSERVED absence rather than a company's assertion, which 518a identifies as the strongest evidence class available -- the index is public, so there is no question of a broken query returning zero. ONE AMBIGUOUS RECORD WORTH THE SUBJECT'S EYES: a bare entry reading only '[PERSONAL], State College, PA' with NO age, NO date of birth and no relatives. He lived at three State College addresses. It is not identifiable as him or as anyone else from what is displayed, and I did not click through -- see the third-party note below. THREE FAQ FINDINGS WORTH MORE THAN THE SEARCH. (1) A ONE-RECORD CAP: 'we only permit you to remove ONE record from our People Search Results through our online Do Not Sell My Info/Opt-Out process' -- and the same FAQ admits multiple records about one person are likely because unmatched new records create separate entries. So the self-service route is structurally incapable of clearing a person who has more than one record, and the overflow goes to privacy@moneybot5000.com. (2) A CARVE-OUT IN THEIR OWN WORDS: 'it is possible that your name might appear in search results for the OTHER SEARCH SERVICES available through MoneyBot5000 even after you opt-out of People Search' -- the Spokeo/Thatsthem shape of 508, disclosed but easy to miss. Property Search is a separate opt-out at /svc/optout/search/optouts/property. (3) A DANIEL'S LAW ROUTE at privacy@moneybot5000.com for covered persons, defined by them as judges, prosecutors, law enforcement and immediate household family. FLAGGED SEPARATELY FOR THE SUBJECT, because one of his addresses is [PERSONAL]@ and a Pennsylvania constable may qualify -- that is his call to make, not mine, and I have asserted nothing.

## Steps

1. Email `support@moneybot5000.com`. They reply within the minute, via a ticket desk.
2. Expect a partial answer: removal offered on two surfaces, refused on a third.
3. Run BOTH opt-out flows — resident and property — each is search, select, then
   click a verification link.
4. Push on the carve-out separately; the flows do not touch it.

## Gotchas

The refusal is one clause inside two pages of helpful instructions, which is exactly
how it gets missed. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Two routes offered, one product refused

> *"At this time, we are unable to remove data from the unclaimed money feature."*

Then two working opt-out routes, with clear instructions: **Property Search**
(`/svc/optout/search/optouts/property`) and **possible resident**
(`/svc/optout/search/optouts`).

The shape is the hazard. Most of the reply is cooperative and specific; the refusal is a
single clause near the top. Complete both flows, collect both confirmations, and it
feels finished — while the refused product carries on. See `_SILENT_FAILURES.md` §34.

**Ask which kind of "unable" it is.** A live external lookup with nowhere to store a
suppression is a different problem from a policy position that unclaimed-property data is
public record. The first invites asking for **display-level suppression** even where the
source cannot be changed; the second is a position to record and stop pressing. The word
covers both and only they know which they meant.

## Their scope wording is honest, and it is the right unit

> *"Information about the property may still be available, but details about your
> identity and any association to the property will be removed."*

The property record persists; **the person and the link between person and property**
are what go. That is precisely the correct thing to remove — the linkage is what turns a
public filing into a way to find someone — and saying so plainly is better than most
companies manage.

The resident flow also claims something prospective: they will *"instruct our data
partners not to return your record in future search results."* Worth getting confirmed,
and worth asking whether the property flow does the same.

## What the flows will not cover

Neither opt-out touches an **attribute**. If a financial inference is attached to the
record — income band, creditworthiness, debt, distress, likelihood to respond to an
offer — it is not a listing and will not be removed by opting a listing out. That has to
be asked for separately, and it is the part that actually gets sold.

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
