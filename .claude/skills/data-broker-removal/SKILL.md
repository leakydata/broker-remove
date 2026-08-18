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

## Running the scripts

Use `uv run scripts/<name>.py` — never bare `python3`. uv resolves the interpreter
from each script's inline PEP 723 metadata, so it works on a machine with no
Python set up. Keep every command in reports and docs in that form so a user can
copy it verbatim.

## Workflow

1. **Pick work.** `uv run scripts/tracker.py next 10` lists the highest-priority
   brokers not yet in a terminal state.
2. **Read the playbook** at `brokers/<id>.md` if one exists. If not, write one as
   you go — that file is the durable output, more valuable than the single submission.
3. **Submit** the opt-out using the browser tools. Most flows are: search for the
   record → select the matching profile → enter email → confirm.
4. **Record immediately**, before moving on:
   ```
   uv run scripts/tracker.py set <id> <status> --note "what happened" --ref "<confirmation id>"
   ```
5. **Report** with `uv run scripts/tracker.py report`.

## Two operating modes

Pick one at the start of a session and say which you're using.

### Assisted mode (default when the user is at the keyboard)

The user stays in the loop only for the seconds a CAPTCHA takes. Everything else
runs unattended.

1. Work the queue normally: search, identify the record, fill every field.
2. When you hit a CAPTCHA, **stop and hand off immediately** — do not batch it.
   State the tab and what to click, in one short line: "Spokeo tab — tick the
   reCAPTCHA and I'll submit."
3. **Wait for the user to say it's done, then submit within the same minute.**
4. Confirm the result, record status, move to the next broker without being asked.

The just-in-time handoff is not a stylistic choice. A reCAPTCHA token expires
roughly two minutes after it's solved, so a solved checkbox sitting in a queued
tab goes stale and the user has to redo it. Solve-then-submit must be adjacent.

Keep exactly one CAPTCHA pending at a time. While waiting, it's fine to stage the
*next* broker's form in another tab — just don't ask for a second solve until the
first is submitted.

### Batch mode (user is away)

Stage as much as possible, mark blockers `captcha_blocked`, and keep going. At the
end run `generate_checklist.py` so every human step sits in one document. Warn the
user that pre-filled forms may need re-filling if a session has expired by the time
they get to them.

## Status vocabulary

`pending` `not_found` `submitted` `email_pending` `captcha_blocked`
`manual_required` `confirmed` `failed` `unreachable`

Use `not_found` when a search genuinely returns no matching record — that is a
real, useful result, not a failure. Use `submitted` only when the site actually
acknowledged the request. Never mark `confirmed` on the strength of a form
submission alone; that status means the broker affirmatively confirmed removal.

## Handoff mode — batch the human steps

Some routes need exactly one human action: a CAPTCHA, a confirm click, a phone
call. Everything either side of it automates cleanly — finding the route, filling
the form, clicking the emailed verification link, reading the reply, recording
the result.

**Do not stop and ask each time.** One interruption per CAPTCHA is the most
expensive possible way to spend the only genuinely scarce resource in this work,
and it makes long unattended runs pointless. Queue them and clear a batch.

```bash
uv run scripts/handoff.py add <broker> --action captcha --minutes 1 \
    --url "https://..." --steps "Solve the CAPTCHA, then press Submit"
uv run scripts/handoff.py list           # what's waiting, with time estimate
uv run scripts/handoff.py list --brief   # one line, for a notification
uv run scripts/handoff.py done <broker>
uv run scripts/handoff.py done <broker> --failed "form errored again"
```

Actions: `captcha`, `click`, `phone`, `postal`, `id`, `decision`.

**How to run a pass in this mode:**

1. Work everything that does not need a person. Where a route needs one action,
   stage the form as far as it will go, then queue the item and move on to the
   next broker.
2. **Write each entry so it stands alone.** Broker, URL, and the exact steps.
   Never rely on a browser tab still being open — tabs do not survive the wait,
   and an entry that says "the tab I left open" is worthless an hour later.
3. Give a realistic `--minutes`. Knowing the queue is six minutes rather than an
   hour is what decides whether someone clears it now or never.
4. **Notify once per batch, not once per item**, and only when a batch is worth
   coming back for — three or four items, or one that is time-critical (an
   expiring link). Lead with the count and the cost: *"4 CAPTCHAs waiting, ~5
   min"* beats *"need your help"*.
5. When the batch is cleared, do the follow-through: click the verification
   links, read the confirmations, record the outcomes.

**Time-critical items go first in the queue and are called out in the
notification.** Some confirmation links expire in 24 hours; a CAPTCHA solved
after that is wasted.

**If an item fails twice, stop queueing it.** Close it with `--failed`, record
the reason in the playbook, and switch to another channel. Repeatedly asking
someone to re-solve a CAPTCHA for a form that is broken server-side spends their
attention on nothing.

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

Append to `data/curated_brokers.json`, then run `uv run scripts/build_registry.py`.
Required fields: `id`, `name`, `domain`, `priority` (1–5), `method`, `optout_url`.
Find the opt-out URL via the site's privacy policy, `/optout`, `/opt-out`,
`/removal`, or the CCPA / "Do Not Sell My Personal Information" link in the footer.

## Filling forms reliably

`form_input` sets a DOM value directly. On React/Vue-controlled inputs — common on
modern opt-out pages — that reports success and then re-renders back to empty. Click
the field and use `type` instead, so real key events fire.

**Always screenshot to verify fields hold their values before handing off for a
CAPTCHA.** A false success wastes the one thing you're asking the user to do, and
CAPTCHA tokens expire in about two minutes, so there is no second try for free.

Forms inside cross-origin iframes (Acxiom) return nothing from `read_page` /
`form_input` at all — drive those by coordinates.

Watch for **commit-then-continue** patterns: LexisNexis ("Add Person"/"Add Address")
and Acxiom (blue "+" per field group) both discard typed values that were never
committed to a list, and only complain at final submit.

## Multiple email addresses

Brokers index records by email, so each address a person uses is a separate
searchable identity. A removal keyed on one address routinely leaves records tied
to the others in place.

`profile.json` carries `all_emails` (every address the person uses) alongside
`confirmation_email` (where verification links should go). On any form or letter
that accepts more than one address, submit all of them. Use `confirmation_email`
only for the verification field.

When a form accepts exactly one, prefer the address most likely to be *in the
broker's record* — usually the oldest or most public one — rather than the one
that's most convenient to check.

## Protected-person removals

Judges, law enforcement officers, and public officials — **including retired and
former** — get a separate, broader removal track at several brokers
(`scripts/make_protected_person_request.py`). It is usually offered as company
policy rather than compelled by statute.

Rules for using it honestly:

- **Never file a present-tense status claim for a role that has ended.** State the
  role, the jurisdiction, and the year service ended. Most programs explicitly
  cover retired personnel, so accuracy costs nothing and overstating gets the
  request declined outright — leaving the record in place.
- **Never cite a statute as compelling removal when it does not.** Many states
  (Pennsylvania among them) protect officer home addresses in their public-records
  law while having no data-broker removal statute at all. Those exemptions bind
  government agencies, not private brokers. Offer them as *supporting evidence*
  for a policy-based request and say so plainly.
- New Jersey's Daniel's Law is the main statute that genuinely compels broker
  removal, and it applies to NJ-covered persons — do not invoke it for other states.
- These requests typically require a **date of birth**. Ask; do not infer one from
  a listed age.
- Ask the broker to apply the alternative ordinary consumer deletion if it declines
  the protected basis, so a rejection doesn't waste the request.

## Email has two distinct roles — don't conflate them

Opt-out forms use email for two different purposes, and treating them as one thing
loses either coverage or automation:

1. **Identity data** — the addresses whose records the broker should find and purge.
   Assert *every* address the person uses (`all_emails`). Missing one leaves those
   records in place.
2. **Confirmation / contact field** — merely where the verification link is sent.
   Point this at a mailbox the agent can actually read (`confirmation_email`), so
   verification can be completed unattended.

Record-matching does not depend on the confirmation address, so these can differ
freely. Setting `confirmation_email` to a readable mailbox converts the single most
common blocker — "click the link in your email" — from a manual step into an
automated one, without weakening the request at all.

Keep the sending account and `confirmation_email` the same where possible; a letter
that arrives from one address and asks for replies at another invites a
verification query.

## Unattended loop mode

Each iteration, work in this order and stop when the useful work runs out. Do not
wait for the user between steps — queue anything blocked and keep moving.

**1. Handle the inbox first.** New replies are worth more than new sends.
   - Check for bounces (`from:mailer-daemon OR from:postmaster`). A bounce means
     the contact is wrong: find the real address, fix `curated_brokers.json`, resend,
     and set `email_verified`. A bounced request looks identical to a pending one,
     so this is the highest-value check in the loop.
   - Check for broker replies. Record ticket numbers via `tracker.py --ref`.
   - **Answer deflections rather than accepting them.** The recurring ones:
     - *"Your state has no privacy law."* Check whether the same message states a
       company policy to remove on request — invoke that instead. Also check
       whether their own form's state dropdown includes your state; it often does.
     - *"We don't process privacy requests by email."* Look for a second, ungated
       privacy route (`/privacy-rights`, `/do-not-sell`, `/ccpa`).
     - *"We don't store data, we fetch it from third parties."* The listing still
       displays; ask for suppression of the display.
     - *"Publicly available data is exempt."* Ask them to honor it as policy, and
       to confirm in writing which basis they applied.

**2. Send the next email batch.** `queue_batch.py --size 10 --summary`, then send
   with the mail tool and record each with `tracker.py set <id> submitted --ref`.
   The script enforces a daily cap; when it reports the cap reached, stop sending
   for the day rather than raising the cap.

**3. Work browser forms** for brokers where email is refused or a form is required.
   Write `brokers/<id>.md` for anything new. If a page is bot-gated on load, try a
   second privacy route before marking it blocked.

**4. Record, validate, commit.** `validate.py`, then `generate_checklist.py`, then
   commit and push. Never commit `data/profile.json`, `removal_status.json`, or
   `outbox/`.

**5. Report briefly.** What was filed, what came back, what needs the user. Keep
   the standing list of user-blocked items short and specific.

Stop the loop when: the daily cap is reached *and* there are no unanswered replies
*and* no unblocked forms remain.

## Verify submissions actually landed

A page that appears after clicking submit is not proof of success. Two failure
modes seen in practice:

- **Upsell-as-confirmation.** Radaris routes a failed submission to a page selling
  a third-party removal service (OneRep), and passes the details just typed into
  that service's URL. It looks like an end state; nothing was submitted.
- **Silent wizard reset.** Multi-step forms can drop back to step 1 when a click
  lands slightly off, while stale element refs still resolve — so a chained batch
  of clicks reports success at every step and accomplishes nothing.

Rules that follow:

- Prefer a **positive, broker-issued artifact** as proof: a confirmation email, a
  ticket number, or a success URL. Record it with `--ref`.
- When a flow promises a verification email, **check the inbox before marking
  `submitted`.** No email means no request. Use `email_pending` at most.
- On multi-step wizards, screenshot after each step rather than chaining clicks.
- Never mark `submitted` on the strength of "the page changed".

## Playbooks are the deliverable — don't skip them on email batches

The per-broker `brokers/<id>.md` files are worth more than any single submission.
A submission helps one person once; a playbook helps everyone who tries that
broker afterwards, and it is what makes a reply interpretable weeks later.

The failure mode to guard against: playbooks get written diligently while working
browser forms (where something is learned each step) and skipped during email
batches (where it feels like nothing was learned). That is backwards — the email
brokers are the ones whose replies arrive later needing context.

Every broker moved to an acted-on status gets a playbook **in the same pass**:

```
uv run scripts/scaffold_playbook.py --missing   # fills registry/status facts
```

then write the part that was actually learned. `scripts/validate.py` **errors** if
an acted-on broker has no playbook, so this cannot drift silently.

When a reply arrives, update the broker's playbook, not just the tracker note.
The tracker records *what happened*; the playbook records *what to do next time*.

## Include prior addresses, old phone numbers, and name variants

Brokers **index records against former addresses and disconnected phone numbers**,
not just current ones. A request listing only present details lets a broker search,
find one record, remove it, and truthfully report the request complete while other
entries remain under an address from ten years ago.

`profile.json` carries `prior_addresses`, `prior_phones`, `middle_name` and
`variants.name_forms`. Every generated letter includes them, with a sentence saying
why — so the broker understands it is a deliberate widening of the search rather
than noise.

This does **not** conflict with data minimization. You are not disclosing anything
new: the broker already holds these details, which is the entire problem. You are
helping them locate what they have. Minimization applies to *optional form fields*
that give a broker data it lacks — a different situation entirely.

Name variants matter for the same reason. "[PERSONAL]" appears on Spokeo
and Radaris while the current record reads "[PERSONAL]"; a middle name or an
alias can be the only thing linking two records.

When a broker's own listing reveals a prior address or old number you did not know
about, add it to the profile — the listing is telling you how you are indexed.

## Broker listings tell you what identifiers you are missing

Work this loop in both directions. When a broker's listing shows a prior address,
an old phone number, or an alias the profile does not have, **that is the broker
telling you how it indexes you** — add it and every subsequent request gets
stronger.

Observed in practice:

- A broker displayed a masked phone number, e.g. `(555) 123-****`. The full number
  turned out to be a real prior number the profile did not have.
- A broker listed four cities as address history before any of those addresses
  were in the profile. The listing was describing history the profile lacked.
- Two brokers carried a middle-name alias while the current record showed only
  first and last. A middle name can be the only link between two records that
  otherwise look like different people.

Old and defunct identifiers are the most valuable, not the least. A dead
`@webtv.net` address or a disconnected landline is exactly what an aging record is
keyed on, and nobody else will think to supply it. Ask for university addresses,
old ISP or webmail accounts, PO boxes, and numbers from previous decades.

## Every reply is documentation — mine it before you file it

A broker's reply is the only place their real process is described. Reading it,
acting on it, and letting it evaporate wastes the most valuable output of the whole
exercise. **Before replying, write what it taught you into `brokers/<id>.md`.**

Classify the reply, then extract accordingly:

| Reply type | What to capture in the playbook |
|---|---|
| **Accepted / confirmed** | Exact wording, stated timeframe, ticket ref. Whether it needed anything beyond the letter — that tells the next person this one is easy. |
| **"We don't accept email"** | The route they name instead, verbatim URL. Whether that route is gated. This is how three brokers here got unblocked. |
| **Wants more information** | Precisely which fields, and any constraint ("one profile per email"). How to construct the identifier they want (search URL → record UUID). |
| **Deflection** | The exact claim, and the counter that answers it. Their own message often contains the counter — a company-policy sentence, or a form that contradicts the claim. |
| **Bounce** | The dead address, where the real one came from, and whether it is the address published in public directories. That last part matters: others are hitting the same wall. |
| **Partial / conditional** | What is *excluded*. "Name search only", "public-facing products only", FCRA carve-outs. Overstating what a removal achieved is worse than not doing it. |

Two rules that keep the folder honest:

- **Quote the broker.** Their sentence is evidence; a paraphrase is your opinion.
  A quoted company-policy line is what you invoke when they later deny it.
- **Write the pattern, not the person.** "A broker asked for a profile UUID" is as
  useful as naming the subject, and the repository is public. `validate.py` will
  reject the alternative anyway.

If a reply teaches something that generalizes past one broker — a gating pattern, a
deflection script, a family sharing one contact — it belongs in a `_TOPIC.md` file
as well, so it is findable by someone who never visits that broker's page.

## Verification is the step that makes any of this true

`uv run scripts/verify_removals.py` builds the worklist: which removals are due
for re-checking (default 7 days after submission) and the search URL to run.

Three outcomes, recorded with `--mark <id> gone|still_listed|not_found`:

- **`gone`** → status becomes `confirmed`. This is the only status that means the
  data is actually down.
- **`still_listed`** → they have not processed it, or the request did not match a
  record. If a *previous* check said `gone`, the tool flags **REAPPEARED** and
  resets the broker to `pending` — the suppression did not hold, which is
  escalation-worthy and means this broker needs a recurring sweep rather than a
  one-time request.
- **`not_found`** → no record. A real, useful result.

Two things the tool encodes that are easy to get wrong:

**Some brokers cannot be verified by search at all.** Aggregators like Acxiom,
Epsilon, LexisNexis, LiveRamp and the adtech firms publish no consumer-facing
listing. There is nothing to look up, so their *written confirmation is the only
evidence available* — which makes chasing a non-reply materially more important
for them than for a people-search site you can simply re-check. The tool lists
these separately rather than sending you hunting for a page that does not exist.

**Clear the browser cache before re-checking.** Several brokers (PeopleFinders,
SearchPeopleFREE, Radaris) warn that a cached page will show a stale listing.
Re-checking through a saved link is how you get a false negative — or worse, a
false positive that makes you re-file a removal that already worked.

## Wait before declaring a flow broken

A verification email can take several minutes. Checking the inbox immediately after
submitting, finding nothing, and concluding the broker never sent one is a mistake
this project has already made and published.

The Radaris case: the wizard ends on a third-party upsell page, which looks like a
dead end, and the real verification email arrives a few minutes later. It was
recorded as "never sends the email" on the strength of one immediate check. The
removal in fact went through and was later verified by search.

**Before recording a flow as broken:** wait at least 10–15 minutes, re-check, and
say in the note how long you waited. "No email after 15 minutes" is a finding;
"no email" checked within a minute is an artifact of impatience.

This cuts the other way too, and both errors are costly: never mark something
`submitted` on the strength of a page changing, and never mark it `failed` on the
strength of an inbox that has not had time to receive anything.

## Two agents are working this project — read the ledger first

A scheduled cloud session runs the same task as any local session, and they
cannot see each other's `data/removal_status.json`, which is gitignored because
its notes quote broker replies and carry personal identifiers.

So the shared state is **`data/removal_ledger.json`**, which is committed. It
holds broker id, status, date of last status change, and channel — and nothing
else. No notes, no quotes, no identifiers.

**At the start of every pass:**

    git pull --no-rebase origin main
    uv run scripts/sync_status.py --merge     # adopt what the other agent did

**At the end of every pass, before committing:**

    uv run scripts/sync_status.py             # publish what you did

Without this, both agents work from private copies of reality: a broker showing
`pending` may have been written to an hour ago, the daily send cap is counted
twice, and the same company receives two letters. That has already happened once.

A merge never downgrades a status. An outcome you obtained from a broker's own
reply outranks another agent's report that a letter went out, and the adopted
entry says plainly that no detail came with it.
