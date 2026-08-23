---
name: data-broker-removal
description: Remove someone's personal information from data brokers and people-search sites, and track it. Use when the user wants to opt out of data brokers, delete their personal data, get off people-search sites, stop being findable or doxxable, check removal progress, handle a broker's reply, or add a broker to the registry.
---

# Data broker removal

You are running a removal campaign on the user's behalf: writing to data brokers,
reading what comes back, and keeping a record that is still useful in six months
when the listings start coming back.

**The durable output is not any single submission.** It is the per-broker
playbook and the status log. A submission helps this person once; a playbook that
records what a broker actually did helps everyone who installs this next.

## Two directories, and never confuse them

| | Where | What |
|---|---|---|
| **Plugin** | `${CLAUDE_PLUGIN_ROOT}` | The registry, the playbooks, the knowledge files, the scripts. Shared, read-only, safe to publish. |
| **Workspace** | `$BROKER_REMOVE_WORKSPACE` | This person's profile, statuses, handoff queue, drafted letters. Private. Never commit it. |

Set the environment variable before running anything:

```bash
export BROKER_REMOVE_WORKSPACE="$HOME/.broker-remove"
```

If it is unset the scripts fall back to writing inside the plugin, which is wrong
for an installed copy — the identity would live inside the plugin and an update
would wipe the progress. **Check it is set before the first write of a session.**

## First run

If `$BROKER_REMOVE_WORKSPACE/data/profile.json` does not exist, do setup before
anything else:

1. `mkdir -p "$BROKER_REMOVE_WORKSPACE/data" "$BROKER_REMOVE_WORKSPACE/outbox"`
2. Copy `${CLAUDE_PLUGIN_ROOT}/data/profile.example.json` to
   `$BROKER_REMOVE_WORKSPACE/data/profile.json`.
3. Fill it in **with the user**, asking for each field. Explain as you go:
   - **Every email address they have ever used**, including dead ones. Brokers
     index on addresses people abandoned years ago; a dead address is a search
     key even when it is not a mailbox.
   - **Every prior home address and phone number.** This is the single biggest
     determinant of how much gets found. A people-search index is built largely
     out of details someone no longer uses.
   - **`confirmation_email`** must be a mailbox they can actually read today.
     This is a different field from the identity list and the distinction
     matters — see "the dead mailbox trap" below.
4. Tell them plainly that this file must never be committed anywhere.

## Running the scripts

Use `uv run "${CLAUDE_PLUGIN_ROOT}/scripts/<name>.py"` — not bare `python3`. uv
resolves the interpreter from each script's inline PEP 723 metadata, so it works
on a machine with no Python set up.

| Script | Purpose |
|---|---|
| `tracker.py` | Status: `set`, `show`, `next`, `stats`, `report` |
| `queue_batch.py` | The next batch of brokers to write to, letters rendered |
| `make_optout_email.py` | Render one letter |
| `handoff.py` | Queue the steps that need a human |
| `verify_removals.py` | Re-check submissions after 7 days |
| `validate.py` | Registry integrity **and a privacy-leak check** |
| `redact.py` | Standalone privacy-leak check |
| `playbook_audit.py` | Find missing, stale or scaffold-only playbooks |
| `import_state_registries.py` | Import official state broker registrations |
| `verify_emails.py` | Discover and verify broker contact addresses |

## The pass

Work in passes. One pass is:

1. **Inbox first.** Bounces before replies. A reply that answers a question you
   already superseded is answering the *quoted* message — check what it quotes.
2. **`verify_removals.py`** for anything submitted more than 7 days ago.
3. **Send the next batch** within the daily cap. Tailor per
   `${CLAUDE_PLUGIN_ROOT}/brokers/_CATEGORY_VARIANTS.md` — a people-search letter
   and a B2B prospecting letter should not be the same letter.
4. **Work browser forms.** Never solve a CAPTCHA (see below).
5. **Write `brokers/<id>.md`**, quoting the broker rather than paraphrasing.
   Then `playbook_audit.py`.
6. **`validate.py`, then commit.** Run the privacy check *before* the commit, not
   chained beside it — a guard whose failure does not block is not a guard.

## Hard rules

These are not preferences. Do not negotiate them away because a broker insists.

- **Never solve a CAPTCHA.** Stage the form completely, then hand off one click.
- **Never create an account with a broker.** An account is a new record.
- **Never upload a government ID.** Under the CPRA, verification information must
  be *necessary and proportionate*. A driver's licence to remove a phone number
  is neither. Say so and offer something lesser.
- **Never submit more personal data than the form requires.** Especially: do not
  hand a prospecting database a LinkedIn URL it does not already have. If no
  record exists, that search does not test for a match, it assembles one.
- **Never guess which record is the user's.** Removing a stranger's listing is a
  real harm. Ask.

## Status vocabulary

`pending` `not_found` `submitted` `email_pending` `captcha_blocked`
`manual_required` `confirmed` `failed` `unreachable`

- `not_found` is a real result, not a failure — but only when the search was run
  on keys the broker actually indexes.
- `submitted` requires a broker-issued artifact: a ticket number, a reference, an
  acknowledgement. A form that said "thank you" is not an artifact.
- `confirmed` means the broker affirmatively said the data is gone. A submission
  receipt is never `confirmed`.

## The failures that look like success

Read `${CLAUDE_PLUGIN_ROOT}/brokers/_SILENT_FAILURES.md`. It is long because the
ways a removal request quietly dies are many and none of them are visible from
the sender's side. The recurring ones:

- **The unconfirmed request.** A form said something reassuring; a verification
  email was never clicked; the request does not exist. Indistinguishable from
  success unless you check.
- **The dead mailbox trap.** A broker requires a work address as the record key,
  then emails the confirmation *to that address*. Anyone who has left the
  employer is locked out — which is exactly the population wanting out. Keep the
  dead address as a search key and never as a confirmation address.
- **Suppression versus deletion.** "Removed" and "suppressed from display" read
  identically and mean different things. Ask which. Suppression that survives a
  re-ingest is often the *better* outcome — do not reflexively demand deletion,
  because at some brokers deleting the record also deletes the record of the
  opt-out.
- **The scoped confirmation.** A removal confirmed for one hostname, from a
  company that runs four. See `_FAMILIES.md`.
- **Rows without edges.** At an identity broker, deleting identifier rows while
  keeping the links between them means the profile rebuilds at the next match.
  Ask about the edges specifically.

## When a broker pushes back

`${CLAUDE_PLUGIN_ROOT}/brokers/_DEFLECTIONS.md` has the answer to most of them.
The general technique that works:

**Pre-accept the unflattering answer.** Offer "we hold nothing", "that is the
client's record, go to them", "we only do a one-time removal" as complete and
acceptable answers. A desk that expects an argument has a reason to send the safe
non-answer. Removing the downside is what makes the honest one-line reply happen.
Then honour it, or the technique is poisoned for the next person.

**Cite another broker's practice.** "Another supplier keeps SHA-256 hashes of my
addresses purely to prevent re-adding" moves the request from *will you do me a
favour* to *this is normal*. It is the most reliable lever in the whole file.

**Concede the strong point first.** To a credit bureau: the credit file is a
regulated consumer report, state deletion rights do not reach it, I am not asking
you to delete it. Then ask about the marketing side, which is in scope. This
removes the easiest way to dispose of the letter.

**Get the register right.** "Did you also search email and phone?" is a fair
question. "You only searched name and address" is an accusation, and if you are
wrong you have spent credibility you need.

## Corrections

When you get something wrong — and you will, because you are inferring mechanism
from sparse evidence — record the correction in the knowledge file rather than
editing the error away. A pattern that explains the evidence is not thereby the
cause of it, and the tell is usually that the invented mechanism was more
interesting than the truth.

## Privacy of the record itself

If the user publishes their fork, the registry and playbooks are public. Run
`redact.py` before every commit. Playbooks quote brokers, never the user: mask
names, addresses, emails and phone numbers as `[FIRST LAST]`, `[TOWN]`,
`[EMAIL]`. The point of this project is to reduce how findable someone is; a
playbook that leaks their address defeats it.
