# Pbi Research

- **Email:** CCPARequests@pbinfo.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** pbinfo.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-19)
- Note: Death-audit and beneficiary-location services for insurers and pension plans - a category that needs a different letter from a marketing broker, so it got one. Led with DISCLOSURE rather than deletion: whether the subject appears in any deceased or death-match file, including a partial, probabilistic or later-resolved match. False positives in Death Master File matching are a known and serious harm - benefits suspended, accounts frozen, credit files flagged, usually with no notice and no visible cause - and a clean deletion would remove the evidence while leaving a bad flag propagating downstream. So correction was asked for ahead of deletion, plus categories of client recipient with a direction to correct their copies too. Also pre-empted the GLBA angle alongside FCRA, since that is the exemption this category actually reaches for, and explicitly refused to send an SSN.

## Steps

1. Write to `CCPARequests@pbinfo.com`. Their MX is Mimecast
   and delivers.
2. **Lead with disclosure and correction, not deletion** — see below.

## Gotchas

**This is a category where deletion can be the wrong first ask.** Death-audit
and beneficiary-location services match individuals against the Social Security
Death Master File, obituary data and similar sources. False positives are a known
and serious harm: a living person wrongly matched can find benefits suspended,
accounts frozen and credit files flagged, usually with no notice and no visible
cause.

If such a flag exists, a clean deletion removes the evidence and leaves the flag
propagating through every client who already received it. So ask, in this order:

1. **Am I in any deceased or death-match file** — including a partial,
   probabilistic, or later-resolved match?
2. **Which clients received it**, and will you direct them to correct their
   copies?
3. Only then, delete and suppress.

**Search the locate files, not just a marketing list.** Records held for locate
purposes are assembled from credit header data, change-of-address feeds and
prior-address chains — sources a marketing suppression never touches. The prior
addresses are the point of the request here.

**Pre-empt GLBA as well as FCRA.** Vendors serving insurers and pension plans
reach for the Gramm-Leach-Bliley exemption more often than the FCRA one, and a
letter that only anticipates FCRA invites a partial answer.

**Refuse the SSN.** This category will ask, because SSN is their matching key.
Sending one to get data deleted creates a more sensitive record than the one
being removed.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->


## Outcome: not submitted, because opting out here has a real cost

PBI is **Pension Benefit Information, LLC** (Minneapolis). Their consumer request
form carries this, and it is not a dark pattern:

> *"If PBI is trying to reach you for one of these purposes, by submitting this
> form, you may make it more difficult for your former employers, pensions, and
> unions, to locate your contact information and communicate with you regarding
> your benefits."*

That is true. Locate services of this kind are how people are reunited with
unclaimed pensions and life-insurance proceeds. **This is one of the few places
where a successful opt-out can leave the subject materially worse off**, and the
trade-off belongs to the subject, not to whoever is running the removals.

See `_CATEGORY_VARIANTS.md` — "Where deletion is the wrong ask" — and treat this
as the clearest instance of it.

## Three further blockers, even if the answer is yes

**The form demands the last four digits of the SSN, plus full date of birth.**
Handing over a more sensitive identifier than any being deleted, in order to
delete them. The letter had already refused an SSN for exactly this reason.

**It requires certifying California residency.** *"I certify that I am a resident
of: California"*, with the CCPA framing throughout — *"Consumer requests under the
California Consumer Privacy Act are only available to California residents."*
There is a dropdown for other states, but the request is built around a statute
that does not reach a Pennsylvania resident.

**There is no email route at all.** `CCPARequests@pbinfo.com` auto-replies:
*"this email address cannot accept consumer privacy rights requests."* An address
named for CCPA requests that refuses CCPA requests. Phone: 1-800-327-2720.

## Gotchas

**The processor claim is made up front**, and it is probably right: *"Where
personal information is provided to PBI by client organizations, PBI is a service
provider or contractor... your pension plan, insurance company, or other business
is the proper entity to address any questions."* So even a successful request
here reaches only what PBI holds in its own right.

**Anti-bot arithmetic gates submit** — *"What is 50 - 40 + .5?"* — the same shape
as the DTN form where the Submit button does not render until it is answered.

**Their California privacy policy link points at `pbinfo.mystagingwebsite.com`** —
a staging host leaking into production. Worth noting only because it suggests the
privacy pages are not closely maintained.
