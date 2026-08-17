# Ownerly

- **Opt-out:** https://www.ownerly.com/optout
- **Email:** privacy@ownerly.com (verified)
- **Method:** web_form — Web form.
- **Domain:** ownerly.com
- **Priority: 3.**

## Status

- Current: `submitted` (updated 2026-08-17)
- Reference: `gmail:1a0064bacdeb8691`
- Note: Replied to an agent-authorization demand: they asked for a signed authorization or power of attorney proving I may act 'on the consumer's behalf', but this is a first-party request. Explained I am the consumer, that all listed email addresses are mine, and asked them to reclassify the ticket. Supplied full address history since Ownerly is property-keyed.

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
