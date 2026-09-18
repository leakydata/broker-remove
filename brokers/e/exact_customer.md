# Exact Customer

- **Email:** privacy@exactcustomer.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** exactcustomer.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Identity-resolution / visitor-identification variant. Asked specifically about website-visitor de-anonymisation: any record connecting the subject to a browsing event on a client's site, including records held on behalf of a client rather than for their own account, and which clients received it. Plus the identity-graph edges rather than just the named row.

## Steps

1. Email `privacy@exactcustomer.com`.
2. Ask specifically about **website-visitor identification**: any record
   connecting you to a browsing event on a client's site.
3. Ask for records held **on behalf of a client** as well as for their own
   account, and which clients received them.
4. Ask for the identity-graph edges, not just the named row.

## Gotchas

The distinguishing question for a visitor-identification business is not "what do
you know about me" but **"what did you tell your clients about me, and when"**.

These services match a device, IP address or cookie against an identity graph to
tell a website operator the name and contact details of an otherwise anonymous
visitor. If such a match happened, there are two records: the identity record, and
the *event* record joining you to a particular site at a particular time. The
second is often the more sensitive and is easy to leave out of a deletion.

**Data held on behalf of a client is the standard exit.** The processor framing —
"we only process this for our customers, please contact them" — is technically
often true and practically a dead end, since you do not know who the clients are.
So ask for the client list in the same breath as the deletion. If they will not
delete, they should at least name who can. See `_DEFLECTIONS.md` on the
processor/controller deflection.

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

Nothing public to check. Ask for the confirmation to state whether any visitor-
identification event involving you was recorded, and which clients it was
disclosed to.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Exact Opco, LLC
- **Trading as:** Exact Customer
- **Registered address:** 552 7th Ave, Suite 401, New York, NY, 10018
- **Filed contact email:** info@exactcustomer.com
- **Filed phone:** 516-253-6644
- **Website:** www.exactcustomer.com

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
