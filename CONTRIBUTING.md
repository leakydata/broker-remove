# Contributing

The most valuable thing you can contribute is a **broker playbook** — a
`brokers/<id>.md` describing how one broker's opt-out actually works, including
the parts that waste people's time. Registry entries are easy; playbooks are where
the real knowledge lives, and they're what makes the next person's removal fast.

You do not need to be a programmer to contribute one. If you opted out of a site
manually and took notes, that's a contribution.

## Adding a broker

1. Add an entry to `data/curated_brokers.json`:

   ```json
   {
     "id": "examplebroker",
     "name": "Example Broker",
     "domain": "examplebroker.com",
     "priority": 3,
     "method": "web_form",
     "optout_url": "https://examplebroker.com/opt-out",
     "needs_email_confirm": true,
     "email_to": "privacy@examplebroker.com",
     "notes": "One line on anything surprising."
   }
   ```

2. Run `uv run scripts/build_registry.py` then `uv run scripts/validate.py`.
3. Write `brokers/<id>.md` using `brokers/_TEMPLATE.md`.
4. Open a pull request.

### Fields

| Field | Meaning |
|---|---|
| `id` | lowercase, underscores, stable — it's the key everything joins on |
| `priority` | 1–5. **5** = upstream aggregator or very widely scraped; **1** = niche |
| `method` | `web_form`, `web_form_captcha`, `email`, `account_required`, `postal`, `phone` |
| `needs_email_confirm` | `true` if the request is void until a link is clicked |
| `email_to` | **Verify this address.** See below. |

## Verify email addresses — do not guess

`privacy@<domain>` is a coin flip. We shipped a request to
`privacy@peoplefinders.com` and it hard-bounced with a 550; the real contact was
`customercare@peoplefinders.com`.

This matters more than it sounds: **a bounced request looks exactly like a pending
one.** Someone can believe they opted out for months while nothing happened.

Find the real address in the broker's privacy policy, or in a state data broker
registry — California, Vermont, Oregon and Texas all require registration and
publish contact details. If you send one, check for a bounce and record the result.

## Writing a good playbook

The template has the structure. What makes one genuinely useful:

- **Name the step that silently eats data.** LexisNexis and Acxiom both discard
  typed values that weren't committed with "Add Person" / "+", and only complain at
  the very end. That single sentence saves someone twenty minutes.
- **Say where the CAPTCHA is** — page load or submit. Page-load gates (Cloudflare on
  PeopleFinders) block automation entirely; submit gates don't.
- **Record scope limits honestly.** LexisNexis suppression doesn't touch
  FCRA-regulated products. PeopleConnect only covers name searches, not phone or
  address lookups. "Removed" is rarely total, and pretending otherwise is worse
  than useless.
- **Note the fallbacks** — phone number, postal address, privacy email.
- **Flag upsells.** Some "opt-out" pages funnel into a paid removal service. The
  free statutory path always exists.

## What this project won't take

- **CAPTCHA-solving integrations**, whether a paid service or a local model. Partly
  terms-of-service, mostly that it backfires: brokers reject requests they flag as
  automated, so a defeated CAPTCHA can get a request thrown out rather than
  honored. The supported route for a gated site is
  `scripts/make_optout_email.py` — brokers must honor written requests under state
  privacy law, and email has no CAPTCHA.
- **False or inflated status claims.** The protected-person path
  (`make_protected_person_request.py`) is for people who genuinely hold or held
  those roles. Filing a present-tense claim for an ended role, or citing a statute
  as compelling when it isn't, gets requests declined and poisons the well for
  people who legitimately qualify.
- **Anything that submits more personal data than a form requires.** Every optional
  field filled is extra data handed to a data broker.
- **Scraping brokers for personal data.** This project removes data; it does not
  collect it.

## Running anything in this repo

All scripts run through [uv](https://docs.astral.sh/uv/) — no virtualenv, no
`pip install`, no Python setup:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh    # macOS/Linux, one time
uv run scripts/validate.py                          # then just run things
```

Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Each script carries inline PEP 723 metadata declaring its Python requirement, so
uv fetches an interpreter automatically. Dependencies are deliberately empty —
everything is standard library, so this keeps working without a lockfile going
stale.

## Testing

```bash
uv run scripts/validate.py          # schema, duplicates, missing playbooks
uv run scripts/build_registry.py    # regenerate data/brokers.json
```

`validate.py` exits non-zero on errors, so it works as a pre-commit check.

Never commit `data/profile.json`, `data/removal_status.json`, or `outbox/` —
they hold personal data and are gitignored. Check with `git status` before pushing.

## This repository is public — never commit personal data

The registry and playbooks are meant to be shared. The *person* using them is not.

`data/profile.json`, `data/removal_status.json` and `outbox/` are gitignored, but
gitignoring the source is not sufficient on its own. The failure mode that actually
bites is **tooling that copies text from a protected file into a tracked one** —
a status note containing an email address, scaffolded into `brokers/<id>.md`, is
laundered straight into public git history. That happened in this repo and is why
`scripts/redact.py` exists.

Two guards, both automatic:

- `scaffold_playbook.py` redacts profile values as it writes, replacing them with
  `[EMAIL]`, `[PHONE]`, `[PERSONAL]`, `[YEAR]`.
- `validate.py` **fails with an error** if any tracked file contains a value drawn
  from `profile.json`. Run it before every push:

  ```bash
  uv run scripts/validate.py     # exits non-zero on a leak
  uv run scripts/redact.py       # lists leaks on their own
  ```

When writing a playbook by hand, describe the *pattern*, never the person. "A
broker displayed a masked phone number the profile did not have" teaches the same
lesson as naming the number, and costs the author nothing.

Note that git history is permanent: a leak that is committed and later deleted is
still in the history and still public. Catch it before the commit.
