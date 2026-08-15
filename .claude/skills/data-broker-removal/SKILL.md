---
name: data-broker-removal
description: Submit and track opt-out / data-deletion requests to data broker and people-search sites on behalf of the profile in data/profile.json. Use when the user asks to remove their personal information from data brokers, opt out of people-search sites, check removal progress, or add a new broker to the registry.
---

# Data Broker Removal

Works through the broker registry submitting opt-out requests, recording the
outcome of every attempt so nothing is done twice and nothing is silently
skipped.

## Layout

| Path | Purpose |
|---|---|
| `data/profile.json` | The identity submitted on forms. Never commit real values. |
| `data/curated_brokers.json` | Hand-verified opt-out endpoints. **Edit this one.** |
| `data/brokers.json` | Generated registry (curated + Optery directory). |
| `data/removal_status.json` | Per-broker status + full attempt history. |
| `brokers/<id>.md` | Per-broker playbook: exact steps, selectors, gotchas. |
| `scripts/tracker.py` | Status CLI. |
| `scripts/build_registry.py` | Regenerates `brokers.json`. |
| `docs/REMOVAL_REPORT.md` | Generated progress report. |

## Workflow

1. **Pick work.** `python3 scripts/tracker.py next 10` lists the highest-priority
   brokers not yet in a terminal state.
2. **Read the playbook** at `brokers/<id>.md` if one exists. If not, write one as
   you go — that file is the durable output, more valuable than the single submission.
3. **Submit** the opt-out using the browser tools. Most flows are: search for the
   record → select the matching profile → enter email → confirm.
4. **Record immediately**, before moving on:
   ```
   python3 scripts/tracker.py set <id> <status> --note "what happened" --ref "<confirmation id>"
   ```
5. **Report** with `python3 scripts/tracker.py report`.

## Status vocabulary

`pending` `not_found` `submitted` `email_pending` `captcha_blocked`
`manual_required` `confirmed` `failed` `unreachable`

Use `not_found` when a search genuinely returns no matching record — that is a
real, useful result, not a failure. Use `submitted` only when the site actually
acknowledged the request. Never mark `confirmed` on the strength of a form
submission alone; that status means the broker affirmatively confirmed removal.

## Hard rules

These exist because getting them wrong causes real harm to the user:

- **Never solve a CAPTCHA.** Mark `captcha_blocked`, note the exact URL and how
  far the flow got, and hand it to the user.
- **Never create an account or enter a password.** Mark `manual_required`.
- **Never upload a government ID, SSN, or a photo of a document.** Several brokers
  (LexisNexis, some credit bureaus) request these. Stop and ask the user.
- **Never submit more identity than the form requires.** If a form asks only for
  a name and email, do not volunteer the street address or phone. Every field
  filled is data handed to a broker.
- **Confirm before final submission** on any flow that posts personal data, and
  before sending any opt-out email from the user's account.
- **Watch for the upsell trap.** Some "opt-out" pages funnel into a paid removal
  service. The free statutory path always exists; find it or mark `manual_required`.

## Verification

A submission is not a removal. Re-check roughly 7–14 days later by searching the
site for the profile again. If the record is gone, set `confirmed`. If it is back,
set `pending` and note the recurrence — reappearance is common and worth tracking,
since it tells you which brokers need a recurring sweep.

## Adding a broker

Append to `data/curated_brokers.json`, then run `python3 scripts/build_registry.py`.
Required fields: `id`, `name`, `domain`, `priority` (1–5), `method`, `optout_url`.
Find the opt-out URL via the site's privacy policy, `/optout`, `/opt-out`,
`/removal`, or the CCPA / "Do Not Sell My Personal Information" link in the footer.
