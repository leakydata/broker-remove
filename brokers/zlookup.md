# ZLookup

- **Opt-out:** —
- **Email:** hello@zlookup.com (CONFIRMED — note the registry had it capitalised;
  the published form is lowercase)
- **Method:** email
- **Domain:** zlookup.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-20)

## Steps

1. Email `hello@zlookup.com`.
2. Use the reverse-lookup variant. The product is a reverse phone lookup, so the
   request is not primarily about a profile page.

## Gotchas

**A profile deletion and a lookup suppression are different things, and they
look identical from outside.** The page can be gone while the number still
resolves to the name. Ask for four separate things and ask which were done:

1. delete the record held
2. suppress the **identifier direction** — a search on any number must not return
   the name, address, email, or a "possible owner" / "likely associated with"
   suggestion
3. apply the same to the **name direction**
4. `noindex` any URL that carried the name, in addition to removing content

**Protect the current holder of a reassigned number.** Several of the prior
numbers have very likely been reassigned by now. Ask them to suppress the
*historical association with the subject's name*, not to remove whatever record
currently exists for the number — otherwise the request damages a stranger. This
is the same principle as `_SILENT_FAILURES.md` §69: a privacy request that
quietly harms third parties has stopped being a privacy request.

**Ask which supplier the number data came from.** For carrier-derived and
marketing-derived phone data the useful fix is upstream.

## Verification

Re-run a reverse lookup on the current number and two or three prior numbers
directly on the site. A name search alone will not detect a surviving reverse
mapping.
