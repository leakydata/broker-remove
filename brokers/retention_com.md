# Retention Com

- **Opt-out:** https://app.retention.com/optout/
- **Email:** support@retention.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** retention.com
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-20)
- Note: CONFIRMED 2026-08-19 21:00 UTC. support@retention.com, Cc optouts@retention.com: 'We have processed your Opt-Out removal request. [one address] has been marked for removal in our vendor database.' Read the scope carefully: they name ONE email address, and the phrase is 'marked for removal in our vendor database', not deleted. Retention.com resolves anonymous site visitors to identities, so one address suppressed is one edge cut in a graph keyed on twelve. Scope question outstanding.

## Steps

Email to `optouts@retention.com`; the reply came from `support@retention.com`
with `optouts@` on Cc.

> "We have processed your Opt-Out removal request. \<one address\> has been
> marked for removal in our vendor database."

## Gotchas

- **Read the scope, not the verb.** The confirmation names **one** email address
  and says "marked for removal in our vendor database" — not deleted, and not
  scoped to the twelve addresses the request listed. For a business whose product
  is resolving anonymous site visitors to identities, one address suppressed is
  one edge cut in a graph keyed on many. The question of whether the other
  eleven were searched is open, and the confirmation is silent rather than
  negative on it.
- **"Marked for removal" is a suppression flag, not a deletion.** That is not
  necessarily worse — a suppression flag is what actually stops re-acquisition —
  but it means the record still exists in some form, and it is worth asking which
  they applied rather than assuming the better reading.

## Verification

No public profile to search. The observable is indirect: whether identity-resolved
mail keyed to these addresses continues. Follow up on scope first — a one-address
confirmation against a twelve-address request is the thing to resolve before
treating this as complete.
