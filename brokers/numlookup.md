# NumLookup

- **Email:** `hello@numlookup.com` — replies within minutes, substantively
- **Method:** email
- **Domain:** numlookup.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- They committed to redacting within 5 days and asked the requester to verify
  afterwards.

## Steps

Write to `hello@numlookup.com`. No form, no account, no CAPTCHA, no jurisdiction
question. The reply arrives almost immediately and is not a template.

## Gotchas

**They echo back the exact query they will act on — read it, because it is where
the mistake shows up.** This is genuinely good practice and rare; most brokers
confirm in the abstract, which makes their scope unauditable. Here the echo made
a defect visible immediately.

The echo grouped the identifiers into two blocks: one headed `State: PA` carrying
a single phone number, and one headed `State: MD` carrying the other eleven.
Nothing in the letter said that. Eleven of the twelve numbers are 814 and 717 —
both Pennsylvania area codes — and exactly one is a Maryland number. It is a
parsing artifact: the first number landed in one block and the remainder fell
into the next.

If redaction is applied per block, eleven numbers would never be removed from any
Pennsylvania-associated record, and the confirmation would still say the request
was processed.

> **Where a broker tells you what they are about to do, check it against what you
> asked for.** The echo is not a courtesy to be thanked for and skimmed; it is the
> only audit opportunity in the entire exchange.

**Their parser only picked up names and phone numbers.** No address and no email
address from the letter appeared in the summary at all, though both were listed.
Restate them explicitly in the reply rather than assuming a silent success.

**"Redacted from our website" is display-layer language.** It does not say whether
the record is deleted from the index, or hidden from the page while still held,
still queryable through an API, and still supplied to anyone buying the feed. Ask
which.

**They put verification on the consumer:** *"Please confirm that your information
has been removed after 5 days."* Schedule it rather than trusting it.

## Verification

Re-run a lookup on each number after 5 days. Check both directions — the
number-to-name lookup and the name-to-number lookup return the same association
from opposite ends, and a removal can cover one without the other.
