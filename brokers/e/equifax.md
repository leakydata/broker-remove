# Equifax

- **Opt-out:** https://myprivacy.equifax.com/opt-in-opt-out/personal-info
- **Email:** usprivacy@equifax.com (verified)
- **Method:** web_form — Web form.
- **Domain:** myprivacy.equifax.com
- **Priority: 5.**

## Status

- Current: `submitted` (updated 2026-08-24)
- Note: 2026-08-24 second reply: claims Work Number is a processor and access/correction/deletion must go to the employer. Correct for deletion, incorrect for ACCESS - The Work Number is a CRA under the FCRA, s609 file disclosure comes from the CRA not the furnisher, and Equifax already runs an employee portal for the Employment Data Report and freeze. Pushed back on that specific point plus the four still unanswered.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://myprivacy.equifax.com/opt-in-opt-out/personal-info
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `usprivacy@equifax.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Austin Consolidated Holdings, Inc.
- **Registered address:** 11 E. 7th Street, Suite 620, Austin, TX 78701,
  United States
- **Filed contact email:** usprivacy@equifax.com
- **Website:** https://myprivacy.equifax.com/opt-in-opt-out/personal-info
- **Opt-out route they filed:** through a link on our website
- **Route for protected individuals:** We do not post personal
  information online so this is not applicable. (Cal. Gov. Code 6208.1(b)
  / 6254.21(c)(1) — for survivors of domestic violence, stalking and
  similar, a stronger and faster route than the ordinary consumer
  request)
- **What they say they collect:** Please visit
  https://www.equifax.com/privacy/privacy-statement/ to review our
  Privacy Statement for more information.

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
