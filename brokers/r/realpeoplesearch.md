# Realpeoplesearch

- **Opt-out:** https://realpeoplesearch.com/about/remove-my-info
- **Email:** support@realpeoplesearch.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** realpeoplesearch.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: FAMILY CONFIRMED (Cloudflare NS pair coleman+paloma): cocofinder.com, fastpeoplesearch.io, findpeoplefast.net, realpeoplesearch.com, searchpeoplefree.net, truepeoplesearch.net, usphonelookup.com -- seven brokers, one Cloudflare account. All four that have replied sent a BYTE-IDENTICAL template within 25 minutes: 'To ensure we accurately locate your specific record and avoid inadvertently removing another individual's information, we need a few more details to cross-reference our database' followed by the same five bullets (Profile Page URL(s) / Full Name / Associated Address / Associated Phone Number / Associated Email Address). Replied to all four with the full identifier set, declining to make a profile-URL hunt the precondition, and asking them to name the shared operator and treat the request as covering all seven.

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

## One Cloudflare account, seven front ends (updated 2026-08-19)

Four sites answered a consumer request within twenty-five minutes of each other
with a **byte-identical** message — same wording, same five bullets, same closing
sentence:

> "To ensure we accurately locate your specific record and **avoid inadvertently
> removing another individual's information**, we need a few more details to
> cross-reference our database.
>
> Profile Page URL(s) ... Full Name ... Associated Address ... Associated Phone
> Number ... Associated Email Address
>
> Once we receive these details, we will immediately locate the matching profile
> and proceed with your removal request."

DNS settled it. All four resolve to the **same Cloudflare nameserver pair**, and so
do three more sites in the tracker:

    coleman.ns.cloudflare.com + paloma.ns.cloudflare.com

    cocofinder.com          fastpeoplesearch.io     findpeoplefast.net
    realpeoplesearch.com    searchpeoplefree.net    truepeoplesearch.net
    usphonelookup.com

Cloudflare assigns a nameserver *pair* per account, so seven domains sharing the
identical pair is one account — the strongest structural family signal available
without insider knowledge. See [[_BROKER_FAMILIES]] for the ranked signal list and
the false-positive rule that matters here.

> **Write to the family, not the brand.** Four separate threads were doing the same
> work. Naming all seven in each reply and asking them to confirm the shared
> operator turns four conversations into one — and surfaces the three that had not
> been contacted at all.

## The request is reasonable; the framing is the problem

Unlike most "send us a profile URL" deflections, this one gives a real reason, and
it is the right reason: on a common name, removing a guessed profile takes down an
uninvolved stranger's listing. That concern deserves to be taken seriously rather
than argued with.

What to push back on is narrower — **the URL as a precondition**:

> **You can query your own index by any field. The requester can only query it by
> name, through a public search box, and read back whatever you choose to display.**
> A request scoped to the URLs a person happens to find is scoped to their search
> skill, not to what the broker actually holds.

The move that works: supply everything *except* the URL, point out that the
date-of-birth-plus-address-history combination is unique and therefore resolves
their accuracy concern completely, and offer the links only if that genuinely is
not enough. Then ask them to state any one-profile-per-request limit plainly rather
than letting it emerge later.

Still open across all four: standing suppression versus point-in-time deletion, and
whether they store the data or display an upstream partner's results.
