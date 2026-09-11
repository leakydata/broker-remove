# Broker playbooks

One file per broker: what its opt-out route actually is, what it asks for, what
it does when you use it, and what it did when we did.

## Why the subdirectories

This directory held 1,260 files flat. Git is untroubled by that and `git clone`
fetches every one — but **GitHub's web interface lists at most 1,000 entries per
directory and then stops**, with no "and 260 more". Anyone browsing the
repository saw a complete-looking list that was missing a fifth of the brokers.

Nothing was ever absent from the repository. It was absent from the *view*,
which is worse, because a truncated list looks exactly like a full one. That is
the failure this project exists to document, and it turned out to be living in
the repository layout.

Playbooks are now sharded on the first character of the broker id, digits
collapsed into `0-9/`:

    brokers/a/acxiom.md
    brokers/s/spokeo.md
    brokers/0-9/5x5.md

27 directories, the largest holding 112 files. Room to grow several times over
before anything is hidden again.

## The knowledge documents stay here

Files beginning with `_` are not about one broker and remain at this level,
because they are what a person actually opens:

| File | What it is |
|---|---|
| `_SILENT_FAILURES.md` | Numbered findings on requests that appear to succeed and do not. The core artifact. |
| `_SILENT_FAILURES_INDEX.md` | Titles and numbers, for finding your way around the above. |
| `_CATEGORY_VARIANTS.md` | How the letter changes by broker type. |
| `_FAMILIES.md`, `_BROKER_FAMILIES.md` | Multi-brand operators and the fingerprints that expose undeclared ones. |
| `_SUPPLY_CHAIN.md` | Who names whom as a source. |
| `_DEFLECTIONS.md` | The refusals, and which are lawful. |
| `_CLOUDFLARE_GATED.md` | Routes that need a real browser. |
| `_PRIVACYCOMPLIANCE_FAMILY.md` | One shared intake form, many registrants. |
| `_TEMPLATE.md` | Start here when writing a new playbook. |

## Finding a playbook

Don't guess the shard — ask:

```python
from scripts.paths import playbook
playbook("acxiom")     # -> brokers/a/acxiom.md
```

`playbook()` falls back to the old flat location if a sharded file is missing,
so a partially-migrated tree keeps working rather than silently writing a second
copy in the wrong place.
