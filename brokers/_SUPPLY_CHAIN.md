# Who names whom

A deletion at a reseller stops that reseller. It does nothing about the source,
which keeps supplying the same record to that company and to everyone else who
buys from it. So the single most valuable disclosure any company can make is
NOT what it holds — it is WHERE IT GOT IT.

That disclosure is provided for. §1798.110(a)(2) requires the categories of
sources on request, and GDPR Article 15(1)(g) requires the source itself, not a
category. Almost nobody volunteers it.

MEASURED 2026-09-07 across the whole ledger: 326 rows have notes that discuss
sources, suppliers or upstreams. THIRTEEN contain a source that was actually
NAMED. Roughly four per cent of the conversations that touched the question got
an answer to it.

Those thirteen are worth more than the other three hundred, because each one is
a place where the record can be stopped at origin instead of one reseller at a
time. This file is the map.

---

## The chain, as companies themselves described it

    KASPR              -> CORESIGNAL
    named Coresignal as the source of the subject's profile. Coresignal sells
    scraped professional-profile data as a bulk feed.
        Kaspr: confirmed        Coresignal: covered_by_sibling

    LUSHA              -> MIXRANK / ONLINE MEDIA GROUP, INC.
    "All other details (Name, Employer, Job Title) were sourced from Mixrank —
    Online Media Group, Inc."
    Lusha's disclosure was organised BY SUPPLIER, field by field, which is the
    format every other company should be asked for.
        Lusha: replied          Mixrank: submitted   Online Media: submitted

    LEIDOS DIGITAL SOLUTIONS  -> L2, INC.
    "Leidos Digital Solutions is a reseller of voter data and does not itself
    retain this data which is provided directly to our customers from L2,
    Inc... we repurchase voter data from L2 each time our customers purchase
    this data from us."
    A STRUCTURAL NIL: they hold nothing because they buy fresh each time. The
    suppression has to be at L2 or it does not exist.
        Leidos: replied         L2: submitted        Intranet Quorum: replied

    AD DIRECT          -> ACXIOM
    "Ad Direct Inc. does not compile or maintain data on consumers... we obtain
    consumer mailing lists on behalf of our clients from a third party,
    Acxiom." They also added a Do Not Mail entry of their own accord.
        Ad Direct: submitted    Acxiom: submitted

    CRISIL IREVNA US LLC  -> DUN & BRADSTREET
    Licenses the dataset it resells. Because they named it, a sharper ask
    became available: give me the D-U-N-S number or whatever key the licence
    delivers, since the record is still in the D&B file and returns on the next
    refresh.
        CRISIL: submitted       D&B: acknowledged

    USADATA, FULLENRICH — named their suppliers UNPROMPTED, alongside a nil.
        USADATA: replied        FullEnrich: confirmed

---

## Why the named ones are the useful ones

A nil from a reseller and a nil from a source mean opposite things.

  - A RESELLER's nil is a fact about today's inventory. Leidos holds nothing
    because it repurchases on demand — and will hold the subject's record again
    the moment a customer asks for it. Nothing was suppressed by that nil.
  - A SOURCE's nil, or a source's suppression, is the thing that persists.

So whenever a company says "we do not own this data", "we license it", "we are
a reseller", or "we obtain lists on behalf of clients", the correct follow-up
is not about their copy. It is: NAME THE SUPPLIER. Categories if names are
commercially impossible, but names are what make the next letter possible.

Searchbug said exactly this on 2026-09-07 — "Searchbug is a data broker and
does not own any of this data" — and has been asked accordingly.

## The ask that works

Three sentences, added to any letter to a company that resells or licenses:

    You have said you do not own this data. A suppression applied at your end
    stops you reselling me; it does nothing about the source, which will keep
    supplying the same record to you and to everyone else who buys from them.

    Which suppliers provide the data in which I appear? Names are far more
    useful than categories, because they are the only thing that lets me stop
    this at origin rather than one reseller at a time.

    And when you suppress me, does that suppression survive your next refresh
    from those suppliers? If nothing persists to exclude me, the removal lasts
    until the next load — which is worth knowing either way.

## What this file is for

Every entry above is a company that can be written to BECAUSE another company
named it. Six of the seven upstreams already have rows in this project. When a
new source is named, add it here and check whether it has a row; if it does
not, it is the highest-value new letter available, because it arrives with
provenance rather than from a register list.
