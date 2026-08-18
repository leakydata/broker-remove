# Id5

- **Email:** privacy@id5.io (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** id5.io
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Universal identity graph for advertising. Asked for hashed email digests, the minted ID5 identifier itself and everything it is joined to, and crucially the GRAPH EDGES rather than the node - deleting a name or a single identifier while keeping the linkages leaves the record re-nameable at the next match. Also asked whether deletion is permanent or only until the next partner sync, and which publishers and platforms hold the corresponding ID, since that distribution is the entire purpose of a shared ID.

## Steps

1. Email `privacy@id5.io`.
2. Ask for hashed email digests — the form identity is actually exchanged in.
3. Ask for the **minted ID5 identifier** and everything it is joined to.
4. Ask for the **graph edges**, not just the node.
5. Ask whether deletion survives the next partner sync, and which publishers hold
   the corresponding ID.

## Gotchas

A shared-ID provider is the purest case of the identity-graph problem, because the
identifier **is** the product and it exists by design in other people's systems.

**Ask for the edges, not the node.** Deleting a name, or even a single identifier,
while retaining the linkages preserves the record: the graph still knows that this
cookie, that device and that hashed email are one person, and the next match
re-attaches a name. The linkages are what a deletion has to reach.

**Ask whether deletion survives the sync.** An identity graph is continuously
rebuilt from partner contributions. A deletion without a persistent suppression
entry means the same edges are re-derived at the next ingest — deleted exactly as
requested, back within a cycle, and nothing in the confirmation would say so.

**And ask who else holds the ID.** A universal identifier is distributed to
publishers and platforms *on purpose*; that is the whole product. Deleting the
provider's copy while the same ID sits in fifty partner systems is the least
meaningful deletion available. The partner list is the only route to the rest, and
only they have it.

Expect the processor framing (`_DEFLECTIONS.md` §21) — ask for the party list in
the same breath.

## Verification

Nothing public to search. Ask the confirmation to name which identifier types were
deleted, whether the suppression persists across partner syncs, and which
publishers or platforms were notified.
