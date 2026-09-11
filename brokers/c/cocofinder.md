# CocoFinder

- **Opt-out:** https://cocofinder.com/optout
- **Email:** support@cocofinder.com (verified)
- **Method:** web_form — Web form.
- **Domain:** cocofinder.com
- **Priority: 3.**

## Status

- Current: `failed` (updated 2026-08-19)
- Reference: `gmail:1a0064b2dcdd7578`
- Note: NO WORKING REMOVAL ROUTE. Three routes, all dead: (1) the recorded optout URL cocofinder.com/optout returns 404, and the 404 page is monetised with affiliate ads for competing background-check services; (2) the real page /remove-my-info says 'please submit your request by filling out this form' and links to a Google Form which Google has TAKEN DOWN -- 'We're sorry. You can't access this item because it is in violation of our Terms of Service'; (3) support@cocofinder.com is an autoresponder that re-sends the same 'send us a Profile Page URL' template on every inbound message, including one that already contained every field it asked for. Nothing on any page signals the form is gone. Family: Cloudflare pair coleman+paloma.

## Steps

**There is currently no working route.** All three published paths fail — see
below. What was tried, in order:

1. `cocofinder.com/optout` (the URL carried in broker directories) — **404**.
2. `cocofinder.com/remove-my-info` — page loads, links to a Google Form.
3. The Google Form — **removed by Google for a Terms of Service violation**.
4. `support@cocofinder.com` — autoresponder loop; re-sends the same
   "send us a Profile Page URL" template on every inbound message.

If retrying later, check the Google Form destination first: it is the only step
that can silently come back to life, and the page linking to it will look identical
either way.

## Gotchas

- **The 404 page is monetised.** Following the stale opt-out URL lands on affiliate
  advertising for three competing background-check services, not on an error the
  site treats as a fault.
- **The `/remove-my-info` page still promises a working process** — including an
  FAQ stating removals take "between 24 to 48 hours" — while linking to a form that
  no longer exists. Nothing on the page signals the breakage.
- **Two identical autoresponder replies in one thread is the stop signal.** A third
  reply only re-triggers it.
- The form was a Google Form, so it also captured the submitter's signed-in Google
  account address. Worth knowing if it returns.

## Verification

Nothing has been submitted, so there is nothing to verify yet — the entry is
`failed` on route availability, not on a refusal.

Re-check by testing the Google Form link on `/remove-my-info` directly. If it
loads, the route is back; if it still returns the Terms of Service message, the
route is still dead regardless of what the page says.

The site's own FAQ describes the intended check: *"go back to CocoFinder's homepage
and search for your profile ... clear your cache and re-check after 48 hours."*
That remains the right verification once a submission is actually possible.

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

## Every route is dead, and none of them says so (updated 2026-08-19)

Three published routes. All three fail, and not one of them fails visibly.

**1. The recorded opt-out URL 404s.** `/optout` returns a 404 page — which is
itself monetised, carrying affiliate placements for three competing background-check
services. A consumer who followed a link from a broker directory lands on
advertising.

**2. The real page's form has been removed by Google.** `/remove-my-info` is live,
well-written, and says:

> "To remove your info, please submit your request by filling out this form."

The link goes to a Google Form. The Google Form returns:

> "We're sorry. **You can't access this item because it is in violation of our
> Terms of Service.**"

Read that carefully: this is not a broken link or an expired document. Google
assessed the form and took it down. And the page linking to it is unchanged —
still confident, still instructing people to use it, still carrying an FAQ
promising *"the average time of completing the request is between 24 to 48 hours."*

**3. `support@` is an autoresponder loop.** See below.

> **A removal route hosted on someone else's platform can be revoked without the
> broker noticing or caring.** The page keeps its instructions, the link keeps its
> shape, and the failure is two clicks away where nobody looks. Check the
> destination, not the page that points at it.

Recorded `failed`. There is currently no way for a consumer to exercise a removal
right here at all — which is worth stating plainly, because a broker with an
advertised process and no working route is materially different from one that
refuses.

## The autoresponder that answers its own answer

`support@cocofinder.com` replies to every inbound message with the same text:

> "To ensure we accurately locate your specific record and avoid inadvertently
> removing another individual's information, we need a few more details ...
> Profile Page URL(s) ... Full Name ... Associated Address ... Associated Phone
> Number ... Associated Email Address"

A detailed reply containing **every one of those fields** — name, aliases, date of
birth, current and prior addresses, current and prior phone numbers, twelve email
addresses — produced the identical message again, quoting the reply it was
answering.

> **A support address that re-sends the same template in response to a message
> containing everything it asked for is not a queue with a backlog. It is an
> autoresponder, and replying again only re-triggers it.** Two identical replies in
> one thread is the test; stop after the second and change channel.

Three of the four sites in this family did exactly that within an hour.

See [[_SILENT_FAILURES]] and [[findpeoplefast_net]] for the sibling whose form is
live but unusable.
