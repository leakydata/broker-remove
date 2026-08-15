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

## Pattern: check for a second, ungated privacy route

Before writing a broker off as unreachable, look for a *different* privacy page.
TruePeopleSearch and FamilyTreeNow both gate `/removal` and `/optout` behind
Cloudflare while leaving `/privacy-rights` open — the Turnstile widget there
auto-passes. Same site, same company, one door locked and one open.

Worth trying on any gated broker:

    /privacy-rights   /do-not-sell   /privacy-request   /ccpa
    /notice-at-collection   footer "Do Not Sell or Share My Personal Information"

Also check whether **request type changes the outcome**. On both sites,
"Right to Delete" renders no form at all, while "Right to Know" reveals the full
form and submits. A broker can be simultaneously refusing deletion and accepting
disclosure requests — and a Right to Know still compels disclosure, creates a
dated record, and unlocks their appeal process.

## When every route fails, say so in writing

Two brokers now have no working self-service path at all:

- **PeopleFinders** — opt-out bot-gated, rights form returns a server error, email refused
- **Radaris** — wizard completes but never sends the promised verification email,
  terminating on a third-party upsell instead

The useful move is not to keep retrying. It is to **document the failure precisely
in a written request** — which page, which step, what the error said, how many
attempts — and ask them to process directly or name a route that works. That
converts a dead end into a dated record of the company failing to provide a
mechanism, which is worth having if the matter ever goes further.

Keep the tone measured and avoid asserting intent. "Your form returns this error
on two attempts, please process from this ticket" is harder to dismiss than an
accusation, and it gives them an easy way to fix it.
