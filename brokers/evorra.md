# Evorra

- **Opt-out:** https://evorra.com/opt-out/
- **Email:** privacy@evorra.com (verified)
- **Method:** web_form — Web form.
- **Domain:** evorra.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Audience-platform variant. Stated plainly that the plaintext identifiers are probably not the key: asked for hashed email digests, cookie/MAID/CTV identifiers, IP-derived household associations and the identity-graph linkages joining them. Asked whether deletion removes the underlying observations or only the mapping, and which DSPs/SSPs the segments were activated to.

## Steps

1. Email `privacy@evorra.com`.
2. State plainly that the plaintext identifiers are probably **not** the key, and
   list what is: hashed digests, cookie IDs, MAIDs, CTV identifiers, IP-derived
   household associations, and the graph linkages joining them.
3. Ask whether deletion removes the underlying **observations** or only the
   **mapping** to an identifier.
4. Ask which DSPs, SSPs and clients the segments were activated to.

## Gotchas

Writing to an audience platform with a people-search letter produces a truthful,
useless answer. They will not find the person by name, because that is not how the
data is organised, and they will say so.

Saying so yourself, in the letter, changes the exchange. It signals that a
name-search "no record" will not be accepted as a complete answer, and it tells
the person reading which of their systems to actually look in.

**The mapping-versus-observation question is the sharp one.** An audience platform
can delete the row joining a device identifier to a segment while keeping every
location, page-view and purchase observation that produced the segment. That is a
defensible reading of "delete my data" and it leaves the substance intact. Ask
which was done, in those words.

**Activation is the other half.** Segments containing you were pushed to
downstream platforms. A deletion binding only Evorra leaves live copies wherever
the audience was activated, and the activation list is something only they have.

**Search hashed forms, and say so in the letter.** This industry exchanges
identity as MD5 and SHA-256 digests of email addresses, not as addresses. So
*"we hold no record of that email"* can be entirely true while the digest of that
same address sits in the file — the same record under a different key, and the
key the business actually trades on.

This is not a trick question to catch them out; most of the time nobody at the
company has thought about it, because to them the hash simply *is* the identifier.
Asking in plain terms — "please search hashed forms of each address as well as
plaintext" — usually gets a straight answer.

## Verification

Nothing public to search — you cannot look yourself up in an audience platform,
which is why the written answer carries the entire weight.

Ask the confirmation to name the identifier types deleted, state whether
observations or only mappings were removed, and list the downstream platforms
notified.
