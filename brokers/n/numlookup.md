# NumLookup

- **Email:** `hello@numlookup.com` — replies within minutes, substantively
- **Method:** email
- **Domain:** numlookup.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Best-behaved reply in the project so far: they echoed back the exact query they will act on, which is what makes an audit possible at all. Auditing it found a real defect. They split the identifiers into two blocks - 'State: PA' carrying ONE phone number, and 'State: MD' carrying the other eleven - which is a parsing artifact, not anything the letter said. Nearly all twelve numbers are 814 and 717, both Pennsylvania area codes; only one is a Maryland number. If redaction is applied per block, eleven numbers would go unremoved from any PA-associated record. Replied asking them to drop the state qualifier and act on the numbers themselves, and noting that no address or email from the letter appears in their summary at all. Also queried 'redacted from our website', which is display-layer language - deleted from the index, or hidden from the page while still held and still supplied. They ask the consumer to verify after 5 days.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** NumLookup LLC.
- **Registered address:** 869 Somerset Drive Northwest,, Atlanta, GA,
  30327
- **Filed contact email:** hello@numlookup.com
- **Filed phone:** 4088632316
- **Website:** https://www.numlookup.com

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
