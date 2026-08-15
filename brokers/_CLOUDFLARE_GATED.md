# Brokers gated by bot detection on page load

A growing set of brokers put Cloudflare Turnstile (or similar) in front of the
**opt-out page itself**, not just the submit button. This is a meaningful
distinction:

- **Submit-gated** (Spokeo, Acxiom): automation can find the record, fill every
  field, and hand a human a single checkbox at the end. Cheap for the user.
- **Page-load gated** (PeopleFinders, FamilyTreeNow): automation never reaches the
  form at all. A human must open the page before anything can happen.

Confirmed page-load gated:

| Broker | Opt-out URL | Notes |
|---|---|---|
| PeopleFinders | peoplefinders.com/opt-out | "Please complete the security challenge" |
| FamilyTreeNow | familytreenow.com/optout | Turnstile hangs at "Verifying..." |

## Why this is worth documenting rather than defeating

These sites are legally obliged to provide a route to exercise privacy rights.
When the only self-service route is unreachable, that is worth recording — and it
is a reasonable thing to say in a written request. The email path
(`scripts/make_optout_email.py`) explicitly frames it that way: *your form is
inaccessible, so I am submitting in writing.*

Note that PeopleFinders' own policy says opt-outs are not accepted by email while
simultaneously gating the form behind a challenge that blocks legitimate users.
Documenting that contradiction is more useful than trying to route around it.
