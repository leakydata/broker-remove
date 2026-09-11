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
