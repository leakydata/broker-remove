# Driveniq

- **Email:** support@drivenIQ.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** driveniq.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Acknowledged: VisitIQ Case #01055286. support@driveniq.com routes into VisitIQ's support desk (visitiq.io), which is DrivenIQ's product - so the two names share a queue.

## Steps

1. Email `support@driveniq.com` with the identity-resolution framing below.
2. Ask for deletion of the **identifier graph**, not just the named record.
3. Ask them to search **hashed** forms of every email address.
4. Ask which clients and platforms the data was syndicated to.

## Gotchas

The product here is not a list of people; it is a set of **links between
identifiers** — this hashed email is that device is that household is that
address. Once you see that, the standard deletion request is obviously
insufficient: delete the name and the edges remain, ready to be re-attached to a
name the next time one arrives.

So the request has to name the graph explicitly: device identifiers, mobile
advertising IDs, cookie IDs, IP-derived household associations, hashed
identifiers, **and the linkage records joining them**. Ask for the linkages by
name, because a company answering literally will delete what you asked for.

**Hashed identifiers are the specific trap.** A truthful "we have no record of
that email address" is entirely compatible with holding its MD5 and SHA-256
digest — which is the same record under a different key, and is how these
businesses exchange identity in the first place. Ask for hashed forms to be
searched, in those words.

Also ask for **inferred attributes**: income and vehicle estimates, life-event
predictions, propensity scores, segment memberships. Nobody supplied those; the
system generated them about you, which makes them personal information about you.
Deleting the fields a person could have provided while keeping the model output
is not deletion. See `_CATEGORY_VARIANTS.md` on identity-keyed brokers.

## Verification

Nothing public to search — you cannot look yourself up in an identity graph,
which is exactly why the written answer carries the whole weight.

Ask for the confirmation to name the **identifier types** deleted and the
downstream recipients notified. "Your data has been deleted" from a company whose
product is linkage does not say whether the linkage went with it.
