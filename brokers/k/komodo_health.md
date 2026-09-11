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

1. Email `trust-and-safety@komodohealth.com`.
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
