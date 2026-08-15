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
python3 scripts/scaffold_playbook.py --missing   # fills registry/status facts
```

then write the part that was actually learned. `scripts/validate.py` **errors** if
an acted-on broker has no playbook, so this cannot drift silently.

When a reply arrives, update the broker's playbook, not just the tracker note.
The tracker records *what happened*; the playbook records *what to do next time*.
