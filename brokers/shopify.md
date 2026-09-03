# Shopify

- **Opt-out:** https://privacy.shopify.com/en/erasure_requests/shopify_buyer/new
- **Email:** support@shopify.com — **unmonitored, creates no ticket.** Use the portal.
- **Method:** web_form (self-service privacy portal; CAPTCHA + email verification)
- **Domain:** shopify.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- **2026-09-03 (§296):** SUBMITTED AND VERIFIED 2026-08-20. Human solved the CAPTCHA and pressed Submit; email verification link clicked at 16:36Z with ~10 min left on a 30-minute expiry. Portal now shows: 'Your erasure request has been received. Your data will be erased within 30 days.' Reference ID f7e04aba-0821-41d6-aaa4-4b5decb44754. Covers the cross-merchant controller layer for [primary address] only - one email per submission.

## Gotchas

**This is not a broker letter, and sending one gets a correct refusal.** For most
of the data involved, Shopify is a **processor acting for merchants**, not a
controller. Asking them to delete a merchant's customer records on the
requester's say-so is asking for something they should refuse, and it burns the
exchange.

Split the request explicitly into what they can act on themselves and what they
cannot. Say so in the letter — conceding the point first is what makes the rest
credible.

**What they can act on as controller** — and this is the part worth having:

- any **cross-merchant profile**, purchase graph, risk or fraud scoring, or
  identity linkage built by aggregating activity across multiple stores. This is
  genuinely theirs rather than any single merchant's, and it is the part a
  merchant-by-merchant campaign can never reach.
- opt-out of sale/sharing and targeted advertising, including Shop Pay and any
  audience products using cross-merchant activity
- suppression of the **linkage** between emails, phone numbers and payment
  identifiers where that linkage exists to recognise the person across unrelated
  merchants. Deleting the endpoint rows while keeping the join means the profile
  reassembles at the next checkout.

**What to ask for rather than demand:** the list of merchant stores holding
records matching the identifiers. Frame it precisely:

> I am not asking you to delete those, I am asking to be told where to write.
> Without that list I cannot exercise a right I plainly have, because I have no
> way to enumerate the stores.

That is the load-bearing sentence. "Contact the merchants" is not actionable
advice when the merchants are unknown, and saying so converts a brush-off into a
question they have to answer or decline in writing.

**Accept "we hold nothing outside individual merchant stores" as complete.** Say
in the letter that it will be recorded and not pursued. A platform is far more
likely to answer a question whose safe answer is available.

## Verification

No public search page. Verification is the written answer. The useful outcome is
either a cross-merchant deletion confirmation or a merchant list; a reply that
only says "contact the merchants" should be pushed once on the enumeration point.

## Outcome: the email route is a dead end, and the portal is better anyway

`support@shopify.com` auto-replies:

> "Quick heads-up: this email address isn't monitored and a support ticket
> hasn't been created."

An honest dead end — it says so plainly rather than swallowing the message —
but a dead end. Do not re-send.

**The real route: `privacy.shopify.com`.** A self-service portal, no account, no
ID document. Path: *Erase my data* → subject type → email address.

Five subject types are offered, and picking correctly is the whole game:

| type | what it reaches |
|---|---|
| Shopify merchant or partner | merchant account holders |
| **User of Shopify Services (incl. Shop / Shop Pay)** | data Shopify collected **directly** |
| **Merchant customer** | data **merchants shared with Shopify** for Shopify's own use |
| Making a request on behalf of someone else | authorized agents |
| Shopify Employee or Candidate | staff and applicants |

**"Merchant customer" is the one that reaches the cross-merchant layer**, and the
portal says so in terms that match the argument the letter made:

> "we will erase personal data associated with this email address that is shared
> by merchants with Shopify for Shopify's use as a data controller or business,
> such as for buyer recommendations or ads"

That is Shopify acting as controller rather than processor — the layer that no
merchant-by-merchant campaign can ever reach, because it exists precisely in the
gaps between merchants. It is the part worth having.

The page also states the processor boundary up front, which is worth quoting
back at anyone who claims a platform can wave through merchant data:

> "To erase personal data from a merchant's store, contact them directly."

**Two paths, not one.** "Merchant customer" covers data merchants shared *with*
Shopify. Data Shopify collected *directly* via Shop and Shop Pay is a separate
subject type and a separate submission. If both apply, both are needed.

## Gotchas

**One email address per submission**, and both reCAPTCHA and hCaptcha are loaded
on the page. Full coverage of a twelve-address identity set is twelve runs, each
with a CAPTCHA and an emailed verification link. In practice do the two or three
addresses most likely to have been used at checkout and treat the rest as
optional — the cost is entirely in human clicks, not in the request.

**Verification is by email link**, so each submission can only use an address
whose inbox is reachable.

**Keep the merchant-enumeration ask for the letter, not the portal.** The portal
has one field. The question worth asking — *which merchant stores hold records
matching these identifiers* — has no field to put it in, and "contact the
merchants" is not actionable advice when the merchants are unknown. That ask
belongs in correspondence if a channel ever opens.

## Submitted 2026-08-20

CAPTCHA solved and submitted by a human, verification link clicked the same hour.
Portal confirms:

> "Your erasure request has been received. Your data will be erased within 30
> days."
>
> Reference ID: `f7e04aba-0821-41d6-aaa4-4b5decb44754`

**The verification link expires in 30 minutes**, and that is short enough to
matter. A staged form submitted at the end of a work session, with the link
clicked "later", will simply have to be redone — CAPTCHA and all. Check the inbox
within the half hour or do not submit yet.

Covers the primary contact address only. One email address per submission, so the
remaining addresses are separate runs, each with its own CAPTCHA and its own
30-minute link.
