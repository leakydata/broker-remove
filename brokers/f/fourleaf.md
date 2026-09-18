# Fourleaf

- **Email:** privacy@fourleafdata.com (verified)
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** fourleafdata.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-18)
- Note: CONFIRMED, BOTH RIGHTS, within one minute of sending. Two separate broker-issued emails from noreply@trustsuperset.com: 'your right to erasure request has been completed' and 'your right to opt-out of data sales request has been completed'. No verification hoop, no residency question, and they parsed the emailed letter into TWO request types unprompted - the opposite of a single-select form. Platform is Superset (trustsuperset.com).

## Steps

1. Email `privacy@fourleafdata.com`.
2. Ask for hashed identifier forms to be searched.
3. Ask for **permanent suppression**, not deletion.
4. Ask for derived and inferred attributes separately from source fields.
5. Ask for onward recipients and the acquisition source; invite a written
   negative.

## Gotchas

Standard data-provider shape, and the standard traps: hashed identifiers
(`email_industries.md`), suppression versus deletion (`dmdatabases_com.md`), and
inferred attributes (`aidentified.md`).

The one worth repeating because it is so easy to leave implicit: **"delete my
personal information" does not obviously reach a model output.** A scores-and-
segments file is not what most people picture when they say "my data", and a
responder acting in good faith may delete the identifying record while leaving the
propensity score that was derived from it — which is the part with commercial
value and the part that will be re-attached to a name at the next match.

Name the derived fields explicitly, and invite the written negative so that a
company holding nothing has a cheap way to say so.

## Verification

No public listing. Ask which suppression list the entry was added to, whether it is
checked at every build, and confirm separately that derived attributes were
deleted rather than merely disassociated.

## Confirmed, both rights, in under a minute

Two separate broker-issued emails arrived within a minute of the letter being
sent, from `noreply@trustsuperset.com`:

> *"We are writing to confirm that your right to erasure request has been
> completed."*

> *"We are writing to confirm that your right to opt-out of data sales request has
> been completed."*

No verification step, no residency question, no form to re-submit through. Worth
looking at closely, because two things went right that usually do not.

**They split one letter into two requests, unprompted.** The email asked for
deletion *and* opt-out of sale. Their system created both, actioned both, and
confirmed each separately. Compare `dataaxle.md`, where the same two rights are a
single-select dropdown and asking for both costs two submissions — and where a
consumer who picks one gets an accurate confirmation and no indication that the
other was never requested.

That is the whole difference between an intake designed to capture what was asked
and one designed to capture what fits the form.

**The platform is the thing to recognise, not the broker.** `trustsuperset.com` is
a privacy-request platform, as `privacy.tunnldata.com` is Ethyca. Where a broker
has outsourced intake to one of these, the request tends to reach a pipeline
rather than a person, and the outcome is fast and complete. Recognising the
platform predicts the experience better than recognising the company — see
`_BROKER_FAMILIES.md`.

**One caveat before treating this as finished.** "Completed" arriving in under a
minute means nobody read the letter. The specific asks in it — hashed identifier
forms, derived attributes as distinct from source fields, onward recipients, the
acquisition source — were almost certainly not considered. A follow-up on those is
still worth sending; the confirmations cover the statutory rights, not the
questions.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Fourleaf LLC
- **Registered address:** 30 N. Gould Street, Suite 5479, Sheridan, WY,
  82801
- **Filed contact email:** privacy@fourleafdata.com
- **Filed phone:** 8003606213
- **Website:** www.fourleafdata.com

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
