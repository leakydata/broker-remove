# Onemata

- **Email:** privacy@onemata.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** onemata.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Mobile/location data broker - handled under the MAID-only pattern. Explicitly declined to supply an advertising identifier and said why: if they hold one linked to the subject they can find it from the other identifiers, and if they do not, supplying one would create the very association being asked about, trading a new identifier for the deletion of nothing. Asked the two identifier-independent questions that work regardless: will they report a no-match plainly, and does deletion cover the DERIVED records (visit, dwell, home-and-work inference, movement history, segments) or only the identifier row. Deleting the key while keeping the history keyed to it is not a deletion.

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

That is not the residue of a wound-up business. That is four email service
providers wired up and a marketing stack in current use.

> **A dead website is not evidence that a data broker has stopped holding data.**
> The site is the only part of the operation a consumer can see, and it is the
> cheapest part to switch off. Check MX and SPF before concluding anything: a
> domain that still routes mail through Microsoft and sends through four ESPs is
> being operated by somebody.

This shape deserves its own status. `unreachable` records that the published
route is genuinely gone, without implying the company is — and without implying
the data is.

Wrote to `info@` with `legal@` copied, framing the outage as a fault report,
asking whether the business or its datasets have been sold, transferred or merged
and to whom, and carrying the full MAID-only framing (see
`_CATEGORY_VARIANTS.md`): no advertising identifier supplied, a request for a
plain no-match answer, and the question of whether deletion reaches derived
location, visit and dwell records or only the identifier row.
