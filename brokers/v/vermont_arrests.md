# Vermont Arrests (vtarrests.org)

- **Opt-out:** https://www.infotracer.com/optout/
- **Email:** privacy@infotracer.com (published on the InfoTracer opt-out page)
- **Method:** email
- **Domain:** vtarrests.org — operated by InfoTracer
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)
- Note: Sent 2026-08-20 to privacy@infotracer.com. Missed from the 48-site InfoTracer batch because the registry held support@ for this one site; corrected.

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

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://members.infotracer.com/removeMyData
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@infotracer.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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
