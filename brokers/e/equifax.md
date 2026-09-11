# Equifax

- **Opt-out:** https://myprivacy.equifax.com/opt-in-opt-out/personal-info
- **Email:** usprivacy@equifax.com (verified)
- **Method:** web_form — Web form.
- **Domain:** myprivacy.equifax.com
- **Priority: 5.**

## Status

- Current: `submitted` (updated 2026-08-21)
- Note: 2026-08-21: first contact via the address nominated in the California data broker registration. Scoped explicitly to non-FCRA data (marketing, identity graph, skip-trace) with the credit file excluded up front, plus prescreen opt-out and, for Equifax, a Work Number Employment Data Report and freeze.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Scope the letter before they scope it for you

A request to a credit bureau that does not say what it is *not* about gets
answered as though it were about the credit file, and that answer is correct,
unhelpful, and closes the ticket.

So the letter opens by conceding the exemption: the consumer credit file is a
regulated consumer report under the FCRA, state deletion rights do not reach it,
disputes run elsewhere, **and I am not asking you to delete it.** Everything
after that is about the businesses sitting alongside the bureau — which are not
consumer reporting and are squarely in scope.

Conceding the strong point first is what makes the rest answerable. It also
removes the easiest way to dispose of the letter.

## What is actually being asked for

- **Marketing and audience attributes** — income, wealth, spending, life-stage,
  propensity. Inferences Equifax generated, not facts anyone supplied.
- **IXI Services** measures, and any household wealth or investable-asset band.
- **Identity and device data** — hashed email match keys, persistent identifiers,
  and **the edges** between those and name, address and phone. Endpoints without
  edges rebuilds at the next match.
- **The Work Number** — treated as FCRA-regulated, so the letter asks for what
  the FCRA *gives* rather than arguing about what it withholds: the **Employment
  Data Report**, the list of employers reporting into it, and a **freeze** on the
  file so it cannot be disclosed without authorisation. This is the single most
  useful thing in the letter and it is not a deletion request at all.
- **Prescreen opt-out** as a permanent election.

## The registration named the family

Equifax's California data broker registration uses `usprivacy@equifax.com`, and
so do six other filings — **Equifax Workforce Solutions** (The Work Number),
**PayNet** (twice, under two hostnames), **Ansonia Credit Data**, and **Austin
Consolidated Holdings**. See `_SILENT_FAILURES.md` §78.

That is why the letter asks which entities hold a record and directs the request
to each of them. Without the registry there would have been no reason to think
Ansonia Credit Data had anything to do with Equifax.

## Expect a partial answer, and make partial acceptable

The letter asks them to identify which category each element falls into and says
plainly that "this part is exempt and here is the basis" is an answer that will
be accepted without argument. A desk that expects a fight has a reason to send
the safe non-answer; a desk offered an easy honest out often takes it. The
failure mode to guard against is not refusal — it is a reply scoped to the credit
file that leaves the marketing side unmentioned, which reads as complete.
