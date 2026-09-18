# LexisNexis

- **Opt-out:** https://optout.lexisnexis.com/
- **Method:** multi-step wizard, **no CAPTCHA**, fully automatable
- **Privacy hotline:** 1-800-831-2578
- **Priority: 5.** Major risk-data aggregator.

## Steps
1. Welcome → **Next**
2. Instructions → **Next**
3. **Opt-Out Reason** (select). Use *"I do not want my information shared"*.
   The other options — law enforcement officer, judicial officer, identity theft
   victim, at risk of physical harm — are status claims that are false for most
   people and trigger a documentation upload. Do not select one to skip a step.
4. **Person to Opt Out**: First / Middle (optional) / Last / **SSN (optional)**.
   Leave the SSN blank. Click **Add Person** — the name must appear under
   "Entered" before Next, or it is dropped.
5. **Addresses to Opt Out**: Address 1 / 2 / City / State / Zip → **Add Address**
   (same commit-then-continue pattern) → **Next**.
6. **Communications**: email is enough. Postal defaults to
   "Do not send postal mail" — leave it. → **Confirm**.
7. Success page shows a numeric **Confirmation ID**. Record it.

## Gotchas
- Both "Add Person" and "Add Address" must be clicked before **Next**; values
  typed but not added are silently discarded.
- SSN is offered as "the most precise way to identify persons". It is optional and
  not worth handing to a data broker to slightly improve a match.
- **Scope limit worth knowing:** suppression does not remove data from restricted
  public-records products sold to commercial/government users, anything regulated
  by the FCRA, real-time gateways, news, or legal documents. This is a
  public-facing suppression, not a deletion.
- LexisNexis warns opting out may make instant identity/insurance verification
  harder for you in future.
- The suppression does not expire, but records can be reintroduced from new source
  data — re-check periodically.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** RELX Inc.
- **Trading as:** LexisNexis
- **Registered address:** 1801 Varsity Dr., Raleigh, NC, 27606
- **Filed contact email:** privacy.inquiries@lexisnexis.com
- **Filed phone:** 8008973259
- **Website:** www.lexisnexis.com

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
