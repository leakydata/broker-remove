# Findem

- **Email:** privacy@findem.ai — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** findem.ai
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-19)
- Note: CONFIRMED DELETION + BLOCKLIST: 'As requested, we have deleted all your public data in our database by permanently erasing it. Also, your details have been added to our blocklist which will ensure you will not be contacted in the future using our platform.' Notes the statutory retention of the request record itself: 'we are required to retain a record of your request for at least 24 months.' Sent to both [PERSONAL]@ and [PERSONAL]@ -- they matched across two of the supplied addresses. Reply-to is no-reply-privacy@findem.ai with privacy@findem.ai on Cc, so answer the Cc not the From.

## Steps

1. Email `privacy@findem.ai`.
2. Ask them to search **professional** identifiers — university and work email,
   public profile URLs, employment history — not only consumer ones.
3. Ask for the **enriched profile** to be deleted, not just the raw fields.
4. Ask which customers the profile was shown or disclosed to, and ask for the
   client list in the same breath as the deletion.

## Gotchas

A talent-intelligence profile is not keyed to a home address, so the standard
consumer identifier block can return a truthful "no record" while a full profile
exists. Give them the professional keys — a `.edu` address is often the strongest
one, since it survives every job change and is frequently the seed a profile was
built from.

**The assembled profile is the product.** Employment history, inferred skills,
seniority, tenure, predicted openness to a move: nobody supplied these, the system
inferred them, and they are personal information about the person all the same.
Deleting the source fields while retaining the derived profile is not deletion —
say so in the letter, because otherwise the fields are what gets deleted.

**Expect the processor deflection** (`_DEFLECTIONS.md` §21): *we hold this on
behalf of our customers*. Often true, and a dead end unless you also have the
customer list — which is why the letter asks for it in the same breath. A profile
assembled without the person's knowledge and shown to employers is the part that
outlives your deletion.

## Verification

Nothing public to search. Ask which identifiers they held you under, what the
sources were, and which customers saw the profile — that last list is the next set
of requests to file.

## Confirmed: deleted and blocklisted (updated 2026-08-19)

> "As requested, we have deleted all your public data in our database by
> permanently erasing it.
>
> Also, your details have been added to our **blocklist** which will ensure you
> will not be contacted in the future using our platform.
>
> Please note that we are required to retain a record of your request for at least
> 24 months."

Recorded `confirmed`. Three things in that make it a better confirmation than most.

**It says "permanently erasing", not "removed".** Erasure and de-listing are
different operations and most confirmations choose the vaguer word.

**It pairs deletion with a standing blocklist entry.** Deletion alone is a
point-in-time act at a company whose product is continuously sourced from public
profiles; the blocklist is what stops the next sourcing run rebuilding the record.
Both halves, volunteered.

**It discloses the retention it cannot avoid.** The request record itself is kept
for 24 months — which is a legal obligation, not a loophole.

> **A confirmation that names its own residual retention is more trustworthy than
> one that claims everything is gone.** Something always survives a deletion
> request: the record of the request. An operator that says so unprompted is
> describing their actual process rather than reciting a reassurance.

### Two operational details

**They matched across more than one supplied address.** The reply was addressed to
two of the email addresses in the letter, not just the correspondence one — good
evidence the search actually ran over the full identifier list rather than the
From: header.

**Reply to the Cc, not the From.** It arrives from `no-reply-privacy@findem.ai`
with `privacy@findem.ai` copied in, and the body names the latter as the contact.
See [[_SILENT_FAILURES]] §46 — a `no-reply` From: on privacy mail is a one-way
valve, and here the working address is sitting right there on the Cc line.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Findem Inc
- **Trading as:** Findem
- **Registered address:** 702 Marshall Street, Suite 520, Redwood City,
  CA
- **Filed contact email:** [named individual]@findem.ai
- **Website:** https://www.findem.ai

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
