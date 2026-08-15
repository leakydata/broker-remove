# broker-remove

Tooling to submit and track data-removal requests across data broker and
people-search sites, and to keep a durable record of what was sent where.

Built around a simple idea: the hard part of opting out isn't any single form,
it's that there are hundreds of them, each slightly different, each needing to be
re-checked later because brokers re-ingest public records and your listing comes
back. So the valuable artifact isn't a submission — it's the **registry of how
each broker works** plus a **status log** you can act on months from now.

## Status

Early. The registry tracks **966 brokers** (55 hand-verified with working opt-out
endpoints, the rest imported as stubs from Optery's public directory). The
submission flow is driven by an agent with browser control rather than by a
headless scraper — see [Design notes](#design-notes).

## Layout

| Path | Purpose |
|---|---|
| `data/curated_brokers.json` | Hand-verified opt-out endpoints. **Edit this one.** |
| `data/brokers.json` | Generated registry. Do not hand-edit. |
| `data/profile.json` | Your identity. **Gitignored.** Copy from `profile.example.json`. |
| `data/removal_status.json` | Per-broker status + attempt history. **Gitignored.** |
| `brokers/<id>.md` | Per-broker playbook: steps, selectors, gotchas. |
| `scripts/` | CLI tooling (below). |
| `.claude/skills/data-broker-removal/` | Agent skill driving the workflow. |

## Quick start

```bash
cp data/profile.example.json data/profile.json   # then fill it in
python3 scripts/build_registry.py                # generate data/brokers.json
python3 scripts/tracker.py next 10               # what to work on
```

## Scripts

| Script | Does |
|---|---|
| `build_registry.py` | Merges curated entries + Optery directory into `brokers.json`. |
| `tracker.py` | `list` / `show` / `set` / `next` / `stats` / `report`. |
| `generate_checklist.py` | Emits `docs/MANUAL_CHECKLIST.md` — everything needing a human. |
| `make_optout_email.py` | Renders statutory deletion-request emails per broker. |

Record every attempt as you go:

```bash
python3 scripts/tracker.py set spokeo submitted --note "confirmation #12345"
python3 scripts/tracker.py report
```

### Status vocabulary

`pending` `not_found` `submitted` `email_pending` `captcha_blocked`
`manual_required` `confirmed` `failed` `unreachable`

`not_found` is a real result, not a failure — it means a search genuinely returned
no record. `confirmed` means the broker affirmatively confirmed removal; a
submitted form is only `submitted`.

## Design notes

**Why JSON files and not a database.** The registry is meant to be reviewed and
extended by people. JSON diffs cleanly in review, so a new broker definition is a
readable pull request. There's no query load and no similarity search here that
would justify the opacity of a binary store.

**On CAPTCHAs.** This project does not automate CAPTCHA solving and won't take a
patch that adds it. That's partly a terms-of-service question and partly that it
backfires: brokers reject requests they flag as automated, so a defeated CAPTCHA
can get a request thrown out rather than honored. The supported path for a gated
site is `make_optout_email.py` — brokers are obliged under state privacy law to
honor a written request sent to their privacy address, and email has no CAPTCHA,
leaves a timestamped record, and starts a statutory response clock.

**On identity disambiguation.** Common names collide. Picking the wrong record
both leaves your data up and suppresses a stranger's listing. Match on
corroborating signals — prior cities, phone area code, relatives — rather than on
name alone, and when it's genuinely ambiguous, ask rather than guess.

**On data minimization.** Fill only what a form requires. Every optional field
you complete is additional personal data handed to a data broker, which is the
opposite of the point.

**Verification matters.** A submission is not a removal. Re-check after 7–14 days;
reappearance is common and is worth tracking, because it tells you which brokers
need a recurring sweep rather than a one-time request.

## Contributing a broker

Append to `data/curated_brokers.json` and re-run `build_registry.py`. Required:
`id`, `name`, `domain`, `priority` (1–5), `method`, `optout_url`. Find the opt-out
URL via the site's privacy policy, `/optout`, `/removal`, or the "Do Not Sell My
Personal Information" link in the footer. A `brokers/<id>.md` playbook alongside it
is worth more than the registry entry on its own.

## Caveats

- Opting out does not remove the data from its original public-record source.
- Most brokers require an emailed confirmation link; unconfirmed requests are void.
- Some "opt-out" pages funnel into a paid removal service. The free statutory path
  always exists — find it rather than paying.
- Nothing here is legal advice.

## License

MIT

## Data sources for finding more brokers

Four US states require data brokers to register and publish contact details. These
are authoritative — far better than guessing `privacy@<domain>`:

| State | Registry | Automation notes |
|---|---|---|
| California | <https://oag.ca.gov/data-brokers> | Hard-blocks automated access (Akamai). Individual registrations readable at `/data-broker/registration/<id>`. |
| Vermont | <https://bizfilings.vermont.gov/online/DatabrokerInquire/> | JS single-page app; needs a real browser. |
| Oregon | <https://justice.oregon.gov/consumer/DataBroker/> | Returns 401 to plain requests. |
| Texas | <https://www.sos.state.tx.us/> | Registry moved; path needs rediscovery. |

Ingesting these is open work — see CONTRIBUTING.md.
