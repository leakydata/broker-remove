# Peoplewhiz Com

- **Opt-out:** https://www.peoplewhiz.com/optout
- **Email:** support@peoplewhiz.com — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** peoplewhiz.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Consolidated letter covering BOTH peoplewhiz.com and peoplewhizr.com. family_scan does not pair them because their registry contacts are different addresses on different domains, but DNS does: peoplewhizr.com publishes no MX record at all while peoplewhiz.com carries Rackspace mail, which is the ordinary shape when one operator handles a second brand's correspondence. Rather than assert the relationship, the letter states the inference and its evidence and invites them to correct it - 'if that reading is wrong and they are unrelated, please say so plainly, I will take it at face value'. That costs nothing if wrong and saves a second exchange if right. Standard people-search asks otherwise.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## Scope: this letter covers PeopleWhizr too

`peoplewhiz.com` and `peoplewhizr.com` are almost certainly one operation, and
the evidence is in DNS rather than on either website:

- `peoplewhizr.com` publishes **no MX record at all** — so `support@peoplewhizr.com`,
  which the registry held, could never have received anything.
- `peoplewhiz.com` carries Rackspace mail.

One brand with no mail routing beside a near-identically-named brand that has it
is the ordinary shape of a second property whose correspondence is handled by the
first.

`family_scan.py` does not pair them, because it groups by **shared contact
address** and these two have different addresses on different domains. That is a
real blind spot worth knowing: the scan finds families that share a mailbox, not
families that share an operator. **A missing MX on one of two similarly-named
domains is the cheaper signal, and it costs one `dig`.**

The letter states the inference *and its evidence*, then invites correction:

> *"If that reading is wrong and they are unrelated, please say so plainly — I
> will take it at face value and write to the other one separately."*

That framing costs nothing if the guess is wrong and saves an entire exchange if
it is right. It also avoids the failure mode of asserting a relationship that
does not exist, which invites a correction on the relationship instead of an
answer on the data.

If they deny the connection, `peoplewhizr_com` reverts to pending — and will need
a web route, since its domain cannot take mail.
