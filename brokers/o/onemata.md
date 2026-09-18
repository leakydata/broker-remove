# Onemata

- **Email:** privacy@onemata.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** onemata.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-19)
- Note: CORRECTION to the earlier note. info@ and legal@ were tried after privacy@; all three hard-bounced 'address not found'. So the earlier reading - dead storefront, live machinery, inferred from Microsoft 365 MX and an SPF record authorising four ESPs - was wrong in its conclusion. SPF records say who WOULD be permitted to send and nobody removes them when they stop; MX proves delivery was once arranged, not that a mailbox exists. Three hard bounces outrank all of it. There is no reachable route of any kind: no website, no privacy policy, no form, no working mailbox. Whether they still hold data is unknowable from outside, which is precisely what unreachable should mean.

## Steps

1. Write to `privacy@onemata.com`.
2. Treat it as a **MAID-only broker** — see `_CATEGORY_VARIANTS.md`.

## Gotchas

**Do not supply an advertising identifier to prove one is not held.** The
standard move from this category is to say they deal only in mobile identifiers
and ask for yours. Refusing is the right answer and it has a reason worth stating
in the letter: if they already hold an identifier linked to the subject they can
find it from the other identifiers, and if they do not, supplying one *creates*
the association being complained about. A request that can only be honoured by
first enlarging the record is not a workable request.

**Two questions work regardless of whether an identifier is supplied**, which is
what makes them worth asking first:
- Will they state plainly that they hold no match?
- Does deletion reach the **derived** records — visit, dwell, home-and-work
  inference, movement history, segments — or only the identifier row? Deleting
  the key while retaining the history keyed to it is not a deletion in any useful
  sense.

**Prior addresses are load-bearing here** in a way they are not elsewhere. A
location dataset infers a home from where a device rests overnight, so every
address the subject has lived at is a probe against that inference.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->


## Outcome: the storefront is gone, the machinery is running

`privacy@onemata.com` hard-bounced with "address not found", and there is no
website on which to find an alternative. `onemata.com` and `www.onemata.com`
return a Wix **"ConnectYourDomain Error"** page for every path tried, including
`/privacy` and `/privacy-policy`. So: no privacy policy to read, no opt-out form,
no contact page, and the one published address dead.

The obvious conclusion is that the company folded. The DNS says otherwise:

- MX pointing at Microsoft 365
- an SPF record authorising **Outlook, SendGrid, HubSpot, Oracle Email Delivery
  and Google** to send on the domain's behalf, plus several static IP ranges
- a Brevo verification token and two Google site-verification tokens

That reads like a business still running. **It is not, and the correction
matters more than the original observation.**

`info@` and `legal@` were both tried after `privacy@`. All three hard-bounced
with "address not found". So the Microsoft 365 MX resolves, and nothing exists
behind it — no mailbox at any of the three addresses a company would normally
keep. The elaborate SPF record authorising four ESPs is **stale configuration,
not evidence of use**: SPF says who *would be permitted* to send, and nobody ever
removes it when they stop.

> **DNS is a record of intent, and it long outlives the thing it described.**
> An MX record proves someone once arranged for mail to be delivered. An SPF
> record proves someone once integrated a marketing stack. Neither proves a
> mailbox exists today. Three hard bounces outrank all of it — this is §30 and
> §35 again: only a delivered message proves an address works.

The honest reading of Onemata is therefore narrower than "dead storefront, live
machinery": there is **no reachable route of any kind**. Whether the company
still holds data is genuinely unknown, and unknowable from outside — which is its
own finding, and the reason `unreachable` exists as a status separate from
`failed`.

This shape deserves its own status. `unreachable` records that the published
route is genuinely gone, without implying the company is — and without implying
the data is.

Wrote to `info@` with `legal@` copied, framing the outage as a fault report,
asking whether the business or its datasets have been sold, transferred or merged
and to whom, and carrying the full MAID-only framing (see
`_CATEGORY_VARIANTS.md`): no advertising identifier supplied, a request for a
plain no-match answer, and the question of whether deletion reaches derived
location, visit and dwell records or only the identifier row.

## Unverified last-resort channel from the state registry

Onemata's CA data broker registration (oag.ca.gov/data-broker/registration/546702)
lists a phone line, (833) 663-6282, and a "do not sell my personal info" form at
`onemata.com/do-not-sell-my-personal-info`, in addition to the dead `privacy@`
address. Neither is verified working — the live site would not load at all when
checked (bare domain 404s, www returns the Wix error page above) — so treat the
phone number as the only channel worth a human trying next, not a confirmed
route.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Onemata Corporation
- **Registered address:** 2420 W 26th Ave, Suite 500D, Denver, CO 80211,
  United States
- **Filed contact email:** privacy@onemata.com
- **Website:** http://onemata.com
- **Opt-out route they filed:** Consumers may opt out of the sale of
  their personal information by clicking on the "Do Not Sell My Personal
  Information" link at the bottom of our website and completing the
  online form. Consumers may also submit requests under the CCPA by
  completing the online form provided on our website
  (https://www.onemata.com/do-not-sell-my-personal-info), by calling us
  at our toll-free telephone number (833) 663-6282, or by emailing
  privacy@onemata.com
- **Route for protected individuals:** Onemata does not post personal
  information online. A consumer can request Onemata delete the personal
  information we have collected on that consumer by completing the online
  form provided on our website
  (https://www.onemata.com/do-not-sell-my-personal-info), by calling us
  at our toll-free telephone number (833) 663-6282, or by emailing
  privacy@onemata.com (Cal. Gov. Code 6208.1(b) / 6254.21(c)(1) — for
  survivors of domestic violence, stalking and similar, a stronger and
  faster route than the ordinary consumer request)

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
