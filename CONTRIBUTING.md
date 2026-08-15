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

2. Run `python3 scripts/build_registry.py` then `python3 scripts/validate.py`.
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

## Testing

```bash
python3 scripts/validate.py          # schema + duplicate + sanity checks
python3 scripts/build_registry.py    # regenerate data/brokers.json
```

Never commit `data/profile.json`, `data/removal_status.json`, or `outbox/` —
they hold personal data and are gitignored. Check with `git status` before pushing.
