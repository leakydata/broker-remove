# Trestle

- **Opt-out:** https://portal.trestleiq.com/do-not-sell
- **Email:** privacy@trestleiq.com (verified)
- **Method:** email — statutory request by email. No web form needed.
- **Domain:** trestleiq.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: Trestle/Superset sent four completion emails 2026-08-20 13:37Z from noreply@trustsuperset.com: two 'right to opt out has been completed' and two 'right to deletion has been completed'. Both rights, both confirmed separately.

## Steps

1. **Use `privacy@trestleiq.com`.** A registry entry of `[named individual]@trestleiq.com`
   appears nowhere on their site; the published address is `privacy@`.
2. Send the request by email. No form, no account, no ID document.
3. Confirmations arrive from `noreply@trustsuperset.com` — a different domain
   from the one written to, which is worth expecting so it is not filtered as
   unrelated.

## Gotchas

**They confirm each right separately, and that is a feature.** Four messages
arrived at 13:37 UTC, two saying:

> "We are writing to confirm that your request to exercise your right to opt out
> has been completed."

and two saying:

> "We are writing to confirm that your request to exercise your right to
> deletion has been completed."

Most brokers collapse deletion and opt-out into one sentence, which leaves it
ambiguous whether the opt-out is a standing state or just a side effect of the
delete. Separate confirmations remove that ambiguity. Record both.

**Lead with numbers and addresses, not the name.** Their own product description
names phone verification, phone validation, CNAM lookup, reverse phone lookup
and reverse address lookup. In a reverse-lookup business the identifier is the
key and the name is the value, so a request framed around the name asks them to
search the wrong column.

**Three asks that are specific to this product shape**, all worth reusing for
phone-validation brokers:

- Remove the mapping in **both directions**. A record unreachable from one
  direction but intact from the other is harder to query, not removed.
- Search the **disconnected** numbers specifically. A disconnected number
  persists *more* readily in a validation dataset than a live one, because
  nothing generates fresh evidence to contradict the stale mapping.
- Confirm **CNAM / caller-name separately** rather than folding it into a general
  deletion. Caller-name data lives in different systems and fails independently.

**On their do-not-sell portal.** `portal.trestleiq.com/do-not-sell` exists; the
email asked them to treat the letter as also constituting that request, while
explaining why the reverse-direction and CNAM answers were wanted in writing
rather than through a form. They completed the opt-out without requiring the
portal, so the form is not mandatory.

## Verification

Both rights are confirmed in writing. Re-check on the standard cadence rather
than immediately. Their outbound domain is `trustsuperset.com`, so any future
correspondence will come from there rather than from trestleiq.com.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Trestle Solutions, Inc.
- **Registered address:** 12819 SE 38th St, Unit 263, Bellevue, WA, 98006
- **Filed contact email:** privacy@trestleiq.com
- **Filed phone:** 4802082749
- **Website:** trestleiq.com

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
