# Fastpeoplesearch Io

- **Opt-out:** https://fastpeoplesearch.io/remove-my-info
- **Email:** support@fastpeoplesearch.io (verified)
- **Method:** web_form — Web form.
- **Domain:** fastpeoplesearch.io
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: People-search. Foregrounded the two asks that usually go missing: search every FORMER address and disconnected number, not just current ones; and confirm whether relatives/associates listings are removed too, since a profile can be deleted while the subject's name persists as a 'related person' on someone else's. Pre-empted the profile-URL demand.

## Steps

1. Email `support@fastpeoplesearch.io`.
2. Insist that **every former address and disconnected number** is searched, not
   just current details.
3. Ask whether **relatives and associates** listings are removed too.
4. Ask whether the removal is a suppression against re-listing or one-time.
5. Pre-empt the profile-URL demand.

## Gotchas

Two asks that routinely go missing from people-search requests, and both leave the
record substantially intact when they do.

**Former identifiers.** The most common way one of these requests comes back
incomplete: a search of current details finds one profile, that profile is removed,
and records held under a former address or a disconnected number stay live. The
index is built from exactly those. List them and say "search each".

**Relatives and associates.** These listings name family members and known
associates reciprocally. Deleting your profile while leaving your name on a
relative's listing as a "related person" leaves the association searchable — and
the association is often the thing that makes a person findable in the first
place. Ask for it by name; a profile-scoped deletion will not touch it.

Expect the profile-URL demand (*"send us a link to the page where you appear"*).
Answer it once and move on: they are better placed to search their own index than
you are, and if the profile is not there then the request is satisfied anyway. See
`beenverified.md`, where that catch-22 is worked through.

## Verification

Re-run the public search on **each** former address and each old number
separately, not just the name. And search a relative's listing for your own name
in the related-persons block — that is where a profile-scoped removal leaves
residue.

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
