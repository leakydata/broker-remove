# Civis

- **Opt-out:** https://docs.google.com/forms/d/e/1FAIpQLSfvUYww9wEK9Y4F6VY3nQtm0bBS8QTdcDthet6WAKDYqnnwHA/viewform
- **Email:** dataprotection@civisanalytics.com (verified)
- **Method:** web_form — Web form.
- **Domain:** civisanalytics.com
- **Priority: 2.**

## Status

- Current: `failed` (updated 2026-08-17)
- Note: Their Data Subject Request form (a Google Form) is restricted to 16 states and PENNSYLVANIA IS NOT AMONG THEM; selecting 'None of the above' does not advance past page one. Structural exclusion, not a bug — PA has no comprehensive consumer privacy statute. Original email request stands and already asks them to honor it as a matter of published policy. Awaiting reply.

## Steps

1. Email the published privacy address. Expect the request-form redirect.
2. Read the form's eligibility gate before filling it in — it is restricted by
   state of residence, and that restriction excludes a great deal of the country
   (*The request form excludes most of the country*).
3. Where the form refuses you, fall back to email and ask them to honour the
   request **as company policy**, stating in writing which basis they applied.
4. See *Other routes* below for what is left when both fail.

## Gotchas

Civis is a **self-declared data broker** with unusually broad collection, and its
own request form is the obstacle: it gates on state of residence, so a resident of
a state with no comprehensive privacy law cannot use it at all. The detail is in
*The request form excludes most of the country* below.

That gate is the general problem this project keeps running into, in its clearest
form. Where a broker's only self-service route checks residency, the absence of a
state statute is not merely "no legal leverage" — it is **no route at all**, even
for a request the broker would otherwise have honoured. Always ask for the request
to be honoured as company policy, and ask them to state which basis they used.
A written "we declined because you live in X" is worth having; silence is not.

## Verification

See *Other routes* below. There is no public index to search here — Civis sells to
organisations rather than publishing profiles — so verification is entirely a
matter of what they will put in writing.

## Self-declared data broker, unusually broad collection

Their privacy policy states plainly:

> *"The entity maintaining this website is a data broker under Texas law."*

Sources they name include *"Government entities that offer public records,
including census data, real property records, voter records, court records,
assessor information, tax rolls, and telephone and web directories"*, consumer
data providers, social networks, telecoms and advertising companies.

What they say they collect from those third parties is worth reading in full, and
quoting back:

> *"'Sensitive' personal information, such as racial or ethnic origin, citizenship
> or immigration status, sexual orientation, religious or philosophical beliefs or
> medical condition"*

> *"Inferences, including predictions relating to you and/or your household, and
> predictions about your preferences, characteristics, behaviors, attitudes,
> intelligence, abilities, and aptitudes"*

Predicted *intelligence* and *aptitudes*, assembled about people who have never
heard of the company. Ask for the inferences and scores explicitly — they are the
product, and they survive deletion of a source row.

## The request form excludes most of the country

Email is redirected to a Data Subject Request Form:

> *"We cannot process your request until we have received the completed form."*

The form is a **Google Form**, restricted to residents of sixteen states:
California, Colorado, Connecticut, Delaware, Indiana, Iowa, Kentucky, Maryland,
Montana, New Hampshire, New Jersey, Oregon, Rhode Island, Tennessee, Utah and
Virginia — plus "non-U.S. resident" and "None of the above".

**Selecting "None of the above" does not advance past the first page.** For a
resident of any other state the form is a dead end.

Unlike some exclusions this one is legally coherent rather than careless: those
sixteen states have comprehensive consumer privacy statutes and the others do not.
But the practical effect is that a resident of, say, Pennsylvania has no form route
at all, and the company will not process an emailed request without the form.

**What to do:** do not misstate your residency to get past the gate. Keep the
emailed request on file — it should already ask them to honor the request as a
matter of published policy where they believe no statute applies — and press that
point. Note also that they hold themselves out as a **registered Texas data
broker**, which is a separate regime worth citing.

## Other routes

- **Phone: 877-788-5865** — offered for California consumers specifically. They
  ask for full name, mailing address, email, telephone and the type of right being
  exercised.
- **Email: dataprotection@civisanalytics.com** (auto-acknowledges, then redirects
  to the form).
- Stated turnaround: *"within 45 days of successfully verifying your identity"*.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Civis Analytics, Inc.
- **Registered address:** 200 W. Monroe, Suite 2200, Chicago, IL, 60606
- **Filed contact email:** dataprotectionmail@civisanalytics.com
- **Filed phone:** (312) 985-0173
- **Website:** www.civisanalytics.com

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
