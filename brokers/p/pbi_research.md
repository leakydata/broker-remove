# Pbi Research

- **Email:** CCPARequests@pbinfo.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** pbinfo.com
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-19)
- Note: NOT SUBMITTED - this one needs the subject to decide, and the reason is unusual enough to record carefully. PBI is Pension Benefit Information, LLC. Their form carries a warning that is legitimate rather than a dark pattern: 'by submitting this form, you may make it more difficult for your former employers, pensions, and unions, to locate your contact information and communicate with you regarding your benefits.' PBI's locate business is how people get reunited with unclaimed pensions and life-insurance proceeds. So opting out has a real cost that most broker opt-outs do not, and it is not a cost an agent should absorb on someone's behalf. Three further blockers even if the answer is yes: (1) the form REQUIRES last 4 of SSN plus full DOB - handing over a more sensitive identifier than the ones being deleted, which the letter explicitly refused; (2) it requires certifying California residency, which would be false; (3) CCPARequests@pbinfo.com is auto-reply only and states plainly that it cannot accept privacy requests, so there is no email route. Anti-bot arithmetic question gates submit. Their CA privacy policy link also points at pbinfo.mystagingwebsite.com - a staging host leaking into production.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Pension Benefit Information, LLC
- **Registered address:** 333 South Seventh St., Suite 2400, Minneapolis,
  MN 55402, United States
- **Filed contact email:** CCPARequests@pbinfo.com
- **Website:** http://www.pbinfo.com
- **Opt-out route they filed:** California consumers may opt out or
  submit requests under the CCPA at: https://www.pbinfo.com/crf/ or
  https://www.pbinfo.com/dnsmpi/. California consumers may also submit a
  request by phone at 1-800-327-2720 or by mail to: Pension Benefit
  Information, LLC, Attn: Director of Data, CCPA Consumer Request, 333
  South Seventh Street, Suite 2400, Minneapolis, MN 55402.
- **Route for protected individuals:** Not applicable. (Cal. Gov. Code
  6208.1(b) / 6254.21(c)(1) — for survivors of domestic violence,
  stalking and similar, a stronger and faster route than the ordinary
  consumer request)
- **What they say they collect:** Additional information is available at:
  https://www.pbinfo.com/ca-privacy-policy/.

*Source: `data/registries/complete-reg-data-brokers.csv`.*

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
