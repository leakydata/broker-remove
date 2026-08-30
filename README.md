# broker-remove

Tooling to submit and track data-removal requests across data broker and
people-search sites, and to keep a durable record of what was sent where.

Built around a simple idea: the hard part of opting out isn't any single form,
it's that there are hundreds of them, each slightly different, each needing to be
re-checked later because brokers re-ingest public records and your listing comes
back. So the valuable artifact isn't a submission — it's the **registry of how
each broker works** plus a **status log** you can act on months from now.

## Status

The registry tracks **1,248 curated brokers** (1,530 rows after merging the
imported directories), of which **1,180 have a working contact route on file**.
1,062 have been acted on: 851 requests submitted, 58 confirmed removed, 44
searched-and-found-nothing, 47 needing a human step, 37 unreachable.

Roughly a thousand per-broker playbooks have accumulated alongside those, and —
more usefully — three files of accumulated findings about *how removal requests
actually fail*. Those are the part worth reading if you are here for anything
other than this particular person's data:

| File | What is in it |
|---|---|
| `brokers/_SILENT_FAILURES.md` | ~200 numbered findings on requests that appear to succeed and do not. The core artifact. |
| `brokers/_CATEGORY_VARIANTS.md` | How the letter has to change by broker type — adtech, credit triggers, voter files, skip-trace, list managers, content licensing. |
| `brokers/_FAMILIES.md` | Multi-brand operators, and the fingerprints that expose the ones that do not declare themselves. |
| `data/dead_addresses.json` | 65 contact addresses that are dead, and *how* each is dead — the failure mode determines what to do next. |

### The recurring finding

Most removal requests do not fail loudly. They fail by landing somewhere adjacent
to where they needed to land, and reporting success:

- a record **recomputed on demand** rather than stored, so deletion clears an
  output that is rebuilt on the next request;
- a **sibling site** on the same platform still serving the record the deleted
  brand no longer shows;
- a **suppression that is a leaf, not a branch** — it stops at the company and
  never reaches the co-op members or list owners who supplied the data;
- an alias that **accepts mail and then fails delivery to everyone on it**, so the
  sender sees success and the company sees nothing;
- a `privacy@` group configured to **accept mail only from inside the company**,
  which works for every internal test and rejects every consumer.

None of those produce a bounce, a refusal, or an error. Several produce a warm
written confirmation that is entirely honest and accomplishes nothing.

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

## Install

This project uses [**uv**](https://docs.astral.sh/uv/) to run its scripts. uv
handles Python for you — you do **not** need to install Python, create a
virtualenv, or `pip install` anything.

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Or via a package manager** if you prefer:

```bash
brew install uv          # macOS (Homebrew)
pipx install uv          # any platform, if you already have pipx
winget install astral-sh.uv   # Windows
```

Then restart your terminal and check it worked:

```bash
uv --version
```

## Quick start

```bash
git clone https://github.com/leakydata/broker-remove.git
cd broker-remove

cp data/profile.example.json data/profile.json   # then fill in your details
uv run scripts/build_registry.py                 # generate data/brokers.json
uv run scripts/tracker.py next 10                # what to work on
```

Every script runs the same way — `uv run scripts/<name>.py`. The first run may
take a few seconds while uv fetches a Python interpreter; after that it is
instant. There is no install step and no dependencies to manage: the scripts use
only the Python standard library, and each one declares the Python version it
needs inline (PEP 723), so uv sorts the rest out.

<details>
<summary>Prefer not to use uv?</summary>

Every script is plain stdlib Python, so `python3 scripts/tracker.py stats` works
identically provided you have Python 3.9 or newer. uv is recommended because it
removes the "which Python / which venv" problem entirely.
</details>

## Scripts

| Script | Does |
|---|---|
| `build_registry.py` | Merges curated entries + Optery directory into `brokers.json`. |
| `tracker.py` | `list` / `show` / `set` / `next` / `stats` / `report`. |
| `generate_checklist.py` | Emits `docs/MANUAL_CHECKLIST.md` — everything needing a human. |
| `make_optout_email.py` | Renders statutory deletion-request emails per broker. |
| `make_protected_person_request.py` | Removal request for current/former law enforcement, judges, public officials. |
| `queue_batch.py` | Next batch of emails to send, respecting a daily cap. |
| `scaffold_playbook.py` | Creates `brokers/<id>.md` from registry + status data. |
| `validate.py` | Schema, duplicate, dead-address and missing-playbook checks. |
| `gate.sh` | Pre-commit gate: runs redact + validate and **exits non-zero** on failure. Run it before every commit. |
| `redact.py` | Refuses to let personal data reach a public commit. |
| `verify_removals.py` | Builds the re-check worklist. A submission is not a removal. |
| `handoff.py` | Queue of steps only a human can do — CAPTCHAs, portals, phone calls. |
| `fingerprint_scan.py` | Clusters brokers by shared LiveChat / analytics / GTM IDs to expose white-label families. |
| `discover_contacts.py` | Finds contact addresses in policies, PDFs and JS bundles. |
| `lapsed_scan.py` | Checks brokers whose registry filings have lapsed, before writing to a domain someone else may now own. |

Record every attempt as you go:

```bash
uv run scripts/tracker.py set spokeo submitted --note "confirmation #12345"
uv run scripts/tracker.py report
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

Append to `data/curated_brokers.json`, then run `uv run scripts/build_registry.py`
and `uv run scripts/validate.py`. Required:
`id`, `name`, `domain`, `priority` (1–5), `method`, `optout_url`. Find the opt-out
URL via the site's privacy policy, `/optout`, `/removal`, or the "Do Not Sell My
Personal Information" link in the footer. A `brokers/<id>.md` playbook alongside it
is worth more than the registry entry on its own.

## Caveats

- Opting out does not remove the data from its original public-record source.
- Most brokers require an emailed confirmation link; unconfirmed requests are void.
- Some "opt-out" pages funnel into a paid removal service. The free statutory path
  always exists — find it rather than paying.
- **A confirmation is not evidence.** "We have deleted your data" is the claim, not
  proof of it. Ask for something only a real search could have produced — the
  categories held, the source, whether anything was found at all. "We searched and
  found nothing" and "we deleted your record" are different facts, and a reply that
  does not distinguish them tells you nothing.
- **Deletion and suppression are opposites, not degrees.** A deletion leaves nothing
  to recognise you by, so the next file the company acquires puts you straight back.
  A suppression keeps just enough to keep you out. Ask which one you got, and ask
  that it be *exclude-only* — used to keep you out of outgoing files, never as a
  match key against incoming ones.
- **Do not hand over an identifier to find yourself.** A device ID, a mobile
  advertising ID, or a list of your pseudonymous handles will create a link between
  your name and a history that is currently unlinked. If the request fails you gave
  it away for nothing; if it succeeds you built the link in order to delete part of
  it. Offer email addresses and ask them to hash those instead.
- **Match on the full identifier set, never on a name.** Former addresses have
  current residents and old phone numbers get reassigned. On a people-search or
  court-records site, a name-only match removes a stranger's record instead of
  yours. "No match found" is a better outcome than a mistaken edit.
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
