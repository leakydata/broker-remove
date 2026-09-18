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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** ID5 Technology Ltd
- **Trading as:** ID5
- **Registered address:** 8 Devonshire Square, 6th Floor, London, UK,
  EC2M 4YJ
- **Filed contact email:** privacy@id5.io
- **Filed phone:** 6785496936
- **Website:** https://id5.io

*Source: `data/registries/registry.csv`.*

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
