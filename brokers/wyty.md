# Wyty

- **Opt-out:** —
- **Email:** support@wyty.com (CONFIRMED — published and matched exactly)
- **Method:** email
- **Domain:** wyty.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-07)
- **Note (2026-09-02):** followed up on the completed removal with three questions (listing URL, what the suppression is keyed to, whether it survives a rebuild). Wyty answered directly and usefully: addresses and phone numbers CAN share one suppression entry; the name match is exact-string but case-insensitive, and **joins on first name + last name + city + state together** — so an address entry with no city/state attached is not weakly matched, it is unmatchable against their join key. They flagged that some of the addresses I'd sent lacked a city/state and asked me to resend. **Worth generalizing: when a broker states its join key explicitly, re-check your own letter's formatting against it** — a suppression list is only as good as whether the entries can actually be looked up.
- Note (2026-09-07): resent the full address and phone list with every entry spelled out individually (no shared trailing "City, State" relying on a prior line), plus the name variants, so nothing depends on inferred grouping. Awaiting confirmation the corrected entries were added.

## Gotchas

Standard people-search variant. Four asks, because the general version of the
request tends to be satisfied while leaving the parts that matter:

1. **`noindex` as well as removal.** A page whose content is gone but whose URL
   stays indexed remains findable through cached results for months, and that is
   where most removals actually end up.
2. **Appearances on other people's profiles** — as relative, associate or
   possible household member. Those entries are indexed independently of the
   subject's own page and are frequently the route by which a person is found
   after a profile-scoped deletion.
3. **Suppression or one-time removal?** Ask directly, and pre-accept the
   unflattering answer: "one-time removal, we do not suppress" is useful
   information and will not be treated as a refusal. Brokers answer questions
   that have a safe answer.
4. **Does it cover sibling sites?** A removal scoped to one hostname is
   indistinguishable from a complete removal right up until somebody finds the
   subject on a sibling (`_DEFLECTIONS.md` §40).

**Common name, criminal-record caution.** Ask them to match on date of birth,
not to remove other people's records, and — if any criminal, arrest or court
entry is attributed to the subject — to say what it is and which source it came
from *whether or not they remove it*. An entry that is hidden rather than
corrected returns the next time the source is ingested, and it cannot be fixed at
source without knowing the source.

**Search historical identifiers.** A people-search index is built largely from
details a person has stopped using, so a search of current details finds the
least interesting record and misses the rest.

## Verification

Search the site directly against the current address and the two longest-held
prior localities.

## Outcome

Two messages. An autoresponder on arrival promising a reply "within 1 - 4"
days, then 45 minutes later:

> "Hi, Your information has been opted out as requested."

**Note the verb.** The request asked for deletion *and* opt-out; the answer says
opted out. That may be exact language or may be loose, and the difference matters
— an opt-out is a flag on a record that still exists, a deletion is not. Recorded
as confirmed because it is an unambiguous written statement of action taken, with
the scope caveat noted here.

None of the four asks was addressed: no word on `noindex`, on associate entries
appearing on other people's profiles, on whether this is suppression or a
one-time removal, or on sibling-site coverage. That is the norm rather than a
snub (`_DEFLECTIONS.md` §40) — brokers answer the question with a safe answer and
skip the rest.

Beating a 1-4 day SLA by three days is worth noticing for a different reason: it
suggests the opt-out is a self-service database operation rather than a queue a
person works. Sites that behave this way tend to honour the request quickly and
re-acquire the record just as quickly, which is why the suppression question was
asked and why re-verification matters more here than the confirmation does.
