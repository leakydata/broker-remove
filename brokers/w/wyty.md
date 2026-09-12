# Wyty

- **Opt-out:** —
- **Email:** support@wyty.com (CONFIRMED — published and matched exactly)
- **Method:** email
- **Domain:** wyty.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-09-07)
- Reference: `gmail:1a07b66a370b7419`
- Note: THE MATCHING RULE DISCLOSED, AND IT CREATES A RISK WORTH MORE THAN THE REMOVAL. Follow-up reply 2026-09-02, unread until 2026-09-07; the removal itself remains confirmed and this is activity on a settled row, not a reversal. Two answers: (1) addresses and phone numbers CAN go on the same suppression entry, but 'some of the addresses don't have a city or state. Please correct and re-send'; (2) 'It is exact match but not case sensitive. Also, we join on first name, last name, city, and state.' NO OTHER COMPANY IN THIS PROJECT HAS DESCRIBED ITS MATCHING RULE, and that honesty is what made the problem visible: a suppression keyed to name plus city plus state matches ANY person of that name in that town. The subject lived at seven addresses in one small borough and the name is common, so the entry plausibly removes a different person of the same name -- a stranger who never asked, will never know, and cannot undo it. See SILENT_FAILURES 400. This is 193 reaching further than expected: there the lesson was suppress the association not the value; here the suppression KEY ITSELF is coarser than a person, so even a correctly scoped association suppression over-reaches. SENT 2026-09-07: the corrected address list, every line carrying city and state -- current plus sixteen prior -- and ten prior phone numbers. THEN THREE OPTIONS WITH THE CHOICE LEFT TO THEM, because they can see the data and I cannot: (a) add a distinguishing field, date of birth or a phone number, so the join is name plus city plus state plus something actually the subject's -- DOB offered explicitly TO NARROW THE MATCH, not to widen the search; (b) if no distinguishing field is possible, apply the suppression only where collision is least likely and SAY WHICH ENTRIES WERE KEPT AND WHICH DROPPED, since a partial suppression that is understood beats a complete one that quietly covers other people; (c) if the risk is overstated, say so and it will be accepted. Also asked, hedged deliberately: does exact matching require a separate entry per name variant -- and if so add them ONLY if genuinely required, since each extra entry carries the same collision risk. More suppression is not automatically better. And whether the suppression survives a CHANGE OF DATA SUPPLIER, not merely the next rebuild.

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
