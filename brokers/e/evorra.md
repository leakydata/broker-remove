# Evorra

- **Opt-out:** https://evorra.com/opt-out/
- **Email:** privacy@evorra.com (verified)
- **Method:** web_form — Web form.
- **Domain:** evorra.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-24)
- Note: 2026-08-24: 'Your opt-out / deletion request has been processed for the email(s) provided.' Note the scope - email addresses only, not name/address/phone. Sent four identical copies of the same reply.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Evorra
- **Registered address:** 1412 Broadway, 21 FL, New York, NY
- **Filed contact email:** [named individual]@evorra.com
- **Website:** https://www.evorra.com

*Source: `data/registries/registry2024.csv`.*

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
