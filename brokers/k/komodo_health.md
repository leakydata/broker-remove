# Komodo Health

- **Opt-out:** https://komodohealth-privacy.my.onetrust.com/webform/5c3cf8b1-3cf1-422d-84d5-618844b7316f/267fe393-726e-4ba9-87ad-c470e0e554ae
- **Email:** trust-and-safety@komodohealth.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** komodohealth.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Auto-reply asks for the individual's state of residence before responding - the residency gate again, this time as a precondition to any answer.

## Steps

1. Email `[named individual]@komodohealth.com`.
2. Do **not** open with an argument about de-identification. Ask the narrower
   question instead — see below.
3. Ask separately for professional-side records, using professional identifiers.
4. Ask for the source **categories** (clearinghouse, pharmacy, laboratory,
   provider, payer) and the client recipients.

## Gotchas

**The de-identification answer is coming, so ask a question it does not answer.**

A health-data company will say patient-level data is de-identified and therefore
not personal information. Arguing that in the abstract produces a policy exchange
and no facts. Ask this instead:

> *"Is there a token or persistent identifier in your systems that corresponds to
> me? What is it derived from, and can you locate it given the identifiers below?"*

That is answerable, and it goes to the substance. A token that reliably links
claims **across providers and over time** is functionally an identifier for one
person — that linkage is exactly what makes a longitudinal map longitudinal. The
question does not accuse anyone of breaching a de-identification framework; it asks
what the framework actually produces.

**Say explicitly that a negative is acceptable.** *"We cannot locate a token from
these identifiers"* is a real answer and worth having — it tells you the linkage
runs only one way, which is itself the thing you wanted to know. Offering to accept
it makes the question much easier to answer honestly.

**Two records, not one.** These companies hold patient-side data *and*
professional-side data about clinicians and researchers. The second is keyed to
professional identifiers — a `.edu` address, employer, title, licence number — and
a consumer-shaped search will not reach it. Ask for both.

**Ask for the source categories rather than named suppliers.** A company that will
not name its clearinghouse may still say "clearinghouse", and that is enough to
know where to write next.

## Verification

Nothing public to search. Ask the reply to state, separately: whether a token
exists, whether a professional record exists, which source categories fed either,
and which clients received data. A single "we hold no personal information about
you" answers none of those and should not be treated as though it did.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Komodo Health, Inc.
- **Registered address:** 257 Park Ave South, 2nd Floor, New York, NY,
  10010
- **Filed contact email:** [named individual]@komodohealth.com
- **Filed phone:** 4154691787
- **Website:** https://www.komodohealth.com

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
