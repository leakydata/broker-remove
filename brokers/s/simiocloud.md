# Simiocloud

- **Email:** Privacy@simiocloud.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** simiocloud.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-10-09)
- Note: OPT-OUT SUBMITTED 2026-10-09, confirmed on screen: 'Thanks for contacting SimioCloud! We will remove your information within two to three weeks.' Both boxes ticked -- opt out of promotional communications AND opt out of SimioCloud PRODUCTS, the second being the one that matters, since it covers inclusion in what they sell rather than just what they mail. THE reCAPTCHA WAS INVISIBLE, which settles the question left open earlier today. I had flagged this row as unclassifiable because the accessibility tree showed only a reCAPTCHA container and screenshots of the page froze the renderer. Clicking Submit answered in one step what inspection could not: it went straight through. That is 457's lesson applied -- press the button and let the form say whether the CAPTCHA is required, instead of inferring from the widget's presence that it is. THREE SEPARATE FORMS HERE, and the choice matters for a Pennsylvania resident. simiocloud.com/optout (this one) is framed as removal from products and marketing lists and asks nothing about state of residence. The ACCESS form (/access-form/) and DELETION form (/deletion-form) are both framed as being for residents whose state has a consumer privacy law, so they are the likelier to be refused on residency -- the opt-out was the right target and is the one that does not depend on a statute the subject does not have. Worth trying the deletion form separately to see whether it refuses, but the substantive removal is already requested.

## Steps

1. Email `privacy@simiocloud.com` if you like, but it will not process the request —
   the autoreply says the request "was not submitted in the manner required by our
   Product & Services Privacy Policy". It is still worth sending, because the
   autoreply itself carries the routing below.
2. **Use `simiocloud.com/optout`.** This is the broad route and it is open to
   everyone — see Gotchas.
3. Select **Myself**, then first / middle / last / email / confirm email / phone /
   address / city / state / zip.
4. **Tick BOTH boxes**: "Opt-out of promotional communications" *and* "Opt-out of
   SimioCloud products". They are separate rights on one form.
5. Solve the reCAPTCHA and submit.
6. Only if you live in a covered state, the narrower statutory routes are
   `simiocloud.com/deletion-form` and `simiocloud.com/access-form`.

## Gotchas

- **There is a honeypot.** The form carries a hidden `wpforms[hp]` field *labelled
  "Email"* near the bottom. It must be left blank — filling it silently marks the
  submission as spam, with no error shown. Anything auto-filling every field by
  label will trip it.
- **Both tick-boxes, not one.** Promotional communications and product inclusion are
  separate, and only ticking the first leaves the data in the products.
- The state-gated `/deletion-form` looks like the "real" statutory route and is
  therefore tempting, but for a resident of a state without a comprehensive privacy
  law it is the *worse* option — see below.

## Verification

No public lookup — a donor and customer marketing data business, so nothing to
search yourself in. The written statement is the evidence.

**The opt-out route here is unusually broad, and their own wording is why it is
worth using in preference to the statutory form:**

> "Consumers, **regardless of their state of residence**, may opt-out of
> SimioCloud's database at any time and at no cost via our website... Exercising
> this opt-out right will prevent SimioCloud from selling your personal
> information, processing your personal information for targeted advertising or
> profiling, and will result in the **removal of your personal information from
> SimioCloud's database**."

That is sale, targeted advertising, profiling *and* database removal — offered to
everyone, not only residents of covered states.

> **When a broker offers both a statutory route and a voluntary one, read the
> voluntary one before assuming it is weaker.** Statutory forms are gated on
> residency and scoped to the statute; a company-wide opt-out can be broader and
> available to people the statute does not cover. For a Pennsylvania resident this
> one is strictly better.

Keep the autoreply — it is where that commitment is recorded.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Simio Cloud, LLC
- **Registered address:** 10155 Westmoor Drive, Bldg. 3, Suite 165,
  Westminster, CO, 80021
- **Filed contact email:** privacy@simiocloud.com
- **Filed phone:** 866-600-3430
- **Website:** www.simiocloud.com

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
