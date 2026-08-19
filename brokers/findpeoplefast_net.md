# Findpeoplefast Net

- **Opt-out:** https://findpeoplefast.net/company/remove-my-info
- **Email:** support@findpeoplefast.net — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** findpeoplefast.net
- **Priority: 2.**

## Status

- Current: `manual_required` (updated 2026-08-19) — Google Form is live but requires a profile URL the site’s own search will not produce
- Note: People-search. Every former address and disconnected number; relatives-and-associates listings; suppression vs one-time; upstream sources. Pre-empted the profile-URL demand and the account/ID demands.

## Steps

1. Email `support@findpeoplefast.net`.
2. Insist every former address and disconnected number is searched.
3. Ask whether relatives-and-associates listings are removed too.
4. Ask suppression versus one-time, and for the upstream sources.

## Gotchas

Same shape as `fastpeoplesearch_io.md`, and the same two asks that routinely go
missing: **former identifiers**, because the index is built from them, and
**relatives and associates**, because a profile-scoped deletion leaves the subject
named on other people's listings as a "related person".

That second one is worth insisting on. Reciprocal listings mean a person can be
found through a relative's page after their own is gone, and no confirmation will
mention it because the request was read as being about a profile.

## Verification

Re-run the public search on each former address and each old number separately,
and search a relative's listing for the subject's name in the related-persons
block — that is where a profile-scoped removal leaves residue.

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

## The form that requires an artifact the site will not issue (updated 2026-08-19)

Better placed than its sibling — the Google Form behind `/company/remove-my-info`
is **live** (CocoFinder's was taken down by Google for a Terms of Service
violation). But it is unusable for a different reason.

The form's fields:

    First Name *          Last Name *          Your Email *
    URL (Please paste the URL you request to remove) *
    Leave a message
    Removal Confirmation *  "I acknowledge that my information will be removed
                             within two business days."

**The URL is required.** And the site will not produce one:

- the on-site people search accepts a name and then **does not navigate** on
  submit — the page simply stays where it is;
- guessed profile paths in the obvious shape (`/name/<first>-<last>/<state>/<city>`)
  return a 404, and the 404 page is monetised with competitor advertising.

> **A removal route that requires a profile URL is only as good as the site's own
> search.** When the search does not work, the requirement is not a verification
> step — it is a precondition the requester has no way to satisfy, and the broker
> never has to refuse anything.

That is worth distinguishing from the ordinary "send us the profile link"
deflection, which is at least satisfiable with effort. Here the door is locked and
the key is not issued.

**Two further notes on the form itself:**

- It is a Google Form that captures the **submitter's signed-in Google account
  address** alongside the answers. Check which account the browser is signed into
  before submitting, and treat that address as disclosed.
- The confirmation checkbox commits *them* to two business days, which is a
  useful thing to have agreed in writing — if the submission ever goes through.

`support@findpeoplefast.net` is the same autoresponder loop as the rest of the
family: it re-sent its "we need a Profile Page URL" template in reply to a message
that already contained every field it asked for. See [[cocofinder]].

Family: Cloudflare pair `coleman` + `paloma`, seven brands. See
[[_BROKER_FAMILIES]].
