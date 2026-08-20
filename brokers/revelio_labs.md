# Revelio Labs

- **Email:** info@reveliolabs.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** reveliolabs.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Identity-verification deflection: 'Our records include many individuals with the same name... Please provide this person's LinkedIn URL. If this individual does not have the LinkedIn URL, please provide the names of this individuals' last 3 employers.' Reasonable in kind for a workforce dataset, but asks for NEW personal data. Replied: (a) search the 12 emails first, [EMAIL] is the natural join key and less intrusive per CPRA's necessity qualifier; (b) refused the LinkedIn URL as a live enrichable identifier rather than a verification token; (c) offered employer names conditional on written confirmation they are used only to locate-and-delete, deleted if no match, and not logged as a suppression key. Employer history is NOT in profile.json -- queued as a user decision.

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

## The verification request that asks for the thing you are trying to remove (updated 2026-08-19)

Revelio answered a workforce-data deletion request by declining to act until the
individual is disambiguated:

> "Our records include many individuals with the same name as the person
> referenced in your request. Under the CPRA, if there are reasonable doubts about
> the identity of the person making the request, additional information may be
> requested.
>
> Please provide this person's LinkedIn URL. If this individual does not have the
> LinkedIn URL, please provide the names of this individuals' last 3 employers."

**This one deserves credit before it deserves pushback.** It is reasonable in
kind. Common surname, employment-keyed dataset, and the CPRA genuinely does
contemplate requesting further information where identity is in doubt. Treating
it as a stalling tactic would be wrong.

But it asks for **new personal data from someone who has not yet been told the
company holds anything about them**, and that is the shape to be careful with.

### Three moves, in order

**1. Push the less intrusive route first — the statute is on your side.** The
CPRA's verification provision is qualified: the extra information must be
*necessary*, and a business should not collect more personal information than the
purpose requires. Where a cheaper identifier would do, it should be tried first.

Here it exists and had already been supplied: twelve email addresses. For a
workforce dataset the join key is almost never the current webmail —

> **A `.edu` address in an institutional format is the strongest disambiguator you
> already own.** It is tied to one person at one institution, it is the address a
> workforce dataset is most likely to have sourced, and unlike a name it does not
> collide.

**2. Decline the LinkedIn URL specifically, even if you concede the employers.**

> **A LinkedIn URL is not a verification token — it is a live, third-party,
> continuously-updated identifier.** Supplying it to a workforce-intelligence
> company lets them join the request to a public profile and enrich from it, which
> is adjacent to what the product does. The employer-name route achieves the same
> disambiguation without handing over a linkage you are asking them to delete.

**3. Concede the employers only against three written conditions.** The failure
mode is specific and worth naming to them:

> **A company that holds no record about you can end up holding one *because you
> identified yourself*.** The request becomes the data.

So before sending: (a) the names are used solely to locate and delete, never to
enrich; (b) if the search finds nothing the names are **deleted**, not retained as
a suppression key or a "requested but not found" log row; and (c) the request is
still processed as a deletion and opt-out, not silently converted into an
access-only request by the verification detour.

### What not to let the detour bury

Identity verification tends to reset a thread — the substantive questions from the
original letter quietly stop being answered. None of these depend on the
identification, so keep re-asking them: inferred attributes (estimated
compensation, inferred seniority, inferred gender or ethnicity,
likelihood-of-departure scores) and whether they are deleted rather than merely
detached from the name; the sources; whether existing licensees must delete
downstream; and whether a **standing do-not-source entry** is possible, since
continuous sourcing makes a one-time deletion a pause rather than a removal.

See [[_DEFLECTIONS]] and [[_CATEGORY_VARIANTS]].
