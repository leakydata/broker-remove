# Vermont Arrests (vtarrests.org)

- **Opt-out:** https://www.infotracer.com/optout/
- **Email:** privacy@infotracer.com (published on the InfoTracer opt-out page)
- **Method:** email
- **Domain:** vtarrests.org — operated by InfoTracer
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)

## Gotchas

**This one was missed by a stale registry value, not by a broker's behaviour.**
Forty-eight sibling state-arrest sites all carried `privacy@infotracer.com`;
`vtarrests.org` alone carried `support@infotracer.com`. The batch went out, this
site did not, and nothing flagged it — the entry looked complete because it had
*an* address. A single wrong field in a family of fifty is invisible unless the
family is checked for internal consistency.

**Check to add:** where many brokers share one contact address, assert that they
all share the *same* one, and treat any outlier as suspect rather than as a
special case. One-line check:

```
python3 -c "import json,collections;d=json.load(open('data/brokers.json'))['brokers'];
c=collections.Counter(b.get('email_to') for b in d if 'infotracer' in (b.get('domain') or '') or 'infotracer' in (b.get('email_to') or ''));print(c)"
```

An address with count 1 next to an address with count 48 is a typo, not a
variant.

**Send a short follow-up, not a forty-ninth full letter.** They have already
received forty-eight copies of the same request from the same person. Own the
error, name the one site, and reference the earlier identifiers:

> One site was left out of that batch by my own error: vtarrests.org. I had a
> stale contact address recorded for it, so it never reached you with the rest.

**Two questions still unanswered across the whole family** and worth repeating:
whether it is a suppression that survives the next ingest, and whether removal
reaches appearances on other people's records as relative or associate.

**Arrest-content ask.** If any arrest, booking or criminal entry is attributed to
the subject, ask what it is and which source it came from, whether or not they
remove it. A common name is very easily matched to the wrong person's record, and
an entry hidden rather than corrected returns at the next ingest.

## Verification

Search vtarrests.org directly. Because the other 48 sites were requested
earlier, a difference in outcome between Vermont and its siblings is itself
informative about whether the removal is per-site or platform-wide.
