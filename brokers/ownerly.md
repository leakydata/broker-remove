# Ownerly

- **Opt-out:** https://www.ownerly.com/optout
- **Email:** privacy@ownerly.com (verified)
- **Method:** web_form — Web form.
- **Domain:** ownerly.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Reference: `gmail:1a0064bacdeb8691`
- Note: Agent-authorization demand WITHDRAWN after a first-party reply - they reclassified and processed the same day, without any document being supplied. They then opted out 4 emails and 8 phone numbers, but the four opted out are exactly the four that were NEW in the second message; the original four are unlisted. Asked them to confirm all eight. Also pressed the point that no ADDRESS was searched, which for a property service is the index that matters, and asked for a plain written 'we hold no record' if that is the position.

## Steps

1. Email `privacy@ownerly.com`. Supply the **full address history** — Ownerly is
   property-keyed, so an address you no longer live at is exactly the key their
   record hangs on.
2. Open the letter with a first-party declaration: you are the consumer, not an
   agent, and every address and email listed is yours. See below for why.
3. If they demand authorization anyway, reply refusing the reclassification rather
   than supplying a power of attorney.

## Gotchas

They came back demanding a **signed authorization or power of attorney** proving
the sender may act "on the consumer's behalf" — for a request the consumer sent
about their own data.

The likely trigger is worth knowing, because it is self-inflicted and avoidable.
A letter that lists eight email addresses and then nominates one for
correspondence reads, to a triage clerk working from a template, like an agent
writing for a client. Nothing in it says otherwise. The fix was to open every
letter with an explicit first-party declaration — *"I am the consumer, writing
about my own data. I am not an authorized agent acting for anyone else, and every
email address, address and telephone number listed below is mine"* — which is now
baked into the template in `make_optout_email.py`.

**Do not comply with the demand.** Supplying a power of attorney to prove you are
yourself concedes the misclassification and adds a notarised document to a data
broker's file. Reply, state that this is a first-party request, explain that
multiple addresses are listed so that each can be searched, and ask them to
reclassify the ticket. That was done here.

Listing many identifiers is right — records are frequently held against details a
person no longer uses — but it needs the declaration in front of it. See
`_DEFLECTIONS.md` on the agent-authorization deflection generally.

## Verification

Re-run a property search on the former addresses, not just the current one. This
is a property-keyed index: clearing the current address proves the least.

Ask them to confirm the reclassification explicitly. A silent reclassification and
a silently dropped ticket look identical from outside.

## The authorization demand folded when it was answered

Worth recording as an outcome, not just as an obstacle. The demand for a signed
authorization or power of attorney was **withdrawn the same day**, after one
reply explaining that this is a first-party request and that every listed address
belongs to the consumer. No document was supplied. The ticket was reclassified
and processed.

So the deflection is not a wall, it is a triage default — and it costs one email
to clear. Do not supply a power of attorney to prove you are yourself; explain,
and ask for reclassification. See `_DEFLECTIONS.md`.

## The opt-out list matched the last message, not the ticket

They then confirmed opting out four email addresses and eight phone numbers. The
four are exactly the four that were **new** in the second message; the four from
the original request do not appear.

That may mean the originals were handled earlier and simply not re-listed. It may
also mean the reply was generated against the most recent message rather than
against the ticket as a whole. **From outside, those two look identical**, which
is the whole problem — and it is a pattern to watch for wherever a request is
amended mid-thread:

> A partial confirmation that happens to match your most recent message is not
> evidence that the earlier identifiers were processed.

Ask for the full list back, explicitly. A confirmation you cannot check is not
much better than none.

## A property service that reported only on emails and phones

Their search matched on "first name, last name, age, and/or address" and returned
nothing — but the reply reports on email addresses and telephone numbers only.
Ownerly's product is property and home-value data, which is keyed to an address.
Ten addresses were supplied and none is mentioned.

Ask for each address to be searched **as an address**, including any record that
does not carry the subject's name at all but which the site would surface to
somebody searching that address. That association is the thing worth deleting
here, and a name-keyed search will never find it.
