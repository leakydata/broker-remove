# List Service Direct

- **Email:** dataremoval@listservicedirect.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** listservicedirect.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-09-07)
- Reference: `gmail:1a079d7033ae9cb0 -- dataremoval@ 452 mailbox full, other two delivered`
- Note: RESENT 2026-09-06 TO THREE ADDRESSES; TWO DELIVERED, THE DESIGNATED ONE BOUNCED AGAIN. dataremoval@listservicedirect.com returned 'The recipient's mailbox is full and can't accept messages now' within seven seconds -- the same soft bounce as before, so the mailbox has stayed full across the whole interval. micah@ and info@ did NOT bounce. So the company is reachable and it is specifically THE ADDRESS PUBLISHED FOR DATA REMOVAL that is broken. THE SHAPE OF THE FAILURE: their mail server accepts the connection and then discards the message for want of space. A consumer writing to the address the company itself nominates for removals gets a bounce that reads like their own mistake. Nobody at the company learns that the request existed. Not a refusal, not a dark pattern -- an unattended mailbox doing the work of one. The letter says this to them plainly and asks whoever receives it to forward it and to tell the mailbox owner it is full. WHAT WAS SENT: access with RENTALS named explicitly, because in a list business a rental leaves a copy with the renter that a deletion at the source never reaches; deletion with the 1798.105(c) direction and a count; and SUPPRESSION ASKED FOR IN PREFERENCE TO DELETION, with the reason -- in a compiled-list business a deletion is undone by the next refresh from the supplying source, and a suppression entry keyed to name and address survives it, so an accurate suppression is worth more than a deletion that lapses within the month. Also opt-out, and sources named. CA register 2020-2023, 2024. Watch micah@ and info@ for a reply.

## Steps

1. Email `dataremoval@listservicedirect.com` -- a dedicated removal address, and
   the only route they publish.
2. If it bounces "mailbox full", wait and resend rather than looking elsewhere.
   See below.

## Gotchas

The removal mailbox fills up. That is the whole gotcha, and it is covered below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Mailbox full is not a dead address

`dataremoval@listservicedirect.com` bounced with:

> *"The recipient's mailbox is full and can't accept messages now. Please try
> resending your message later."*

This is a **soft** bounce and it means something quite specific: the address is
real, it was provisioned deliberately for data removal, and it has filled up
because nobody is emptying it. That is different from `Address not found`, which
means the mailbox was never there or has been torn down.

Do not go looking for another route yet, and do not mark the broker unreachable.
Retry in a later pass -- a full mailbox is often drained within a day or two.

**Worth noticing what a full removal mailbox implies.** It is not evidence of
malice, but it is evidence that requests are arriving faster than anyone is reading
them, and that at least some senders have had their requests bounce without ever
being told what to do next.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** List Service Direct Inc.
- **Registered address:** 1983 Marcus Avenue Suite 220, New Hyde Park, NY
- **Filed contact email:** [named individual]@listservicedirect.com
- **Website:** http://www.listservicedirect.com

*Source: `data/registries/registry2024.csv`.*

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
