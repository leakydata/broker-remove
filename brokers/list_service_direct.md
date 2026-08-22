# List Service Direct

- **Email:** dataremoval@listservicedirect.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** listservicedirect.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-22)
- Note: dataremoval@listservicedirect.com bounced: 'The recipient's mailbox is full and can't accept messages now.' That is a soft bounce, not a dead address - the mailbox exists and someone stopped reading it. Rather than waiting for it to drain, resent 2026-08-22 to micah@listservicedirect.com (a named contact, not the generic removal box) with a list-rental-category letter (downstream purchaser deletion, permanent suppression). Delivered without bouncing.

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

