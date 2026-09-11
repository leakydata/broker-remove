"""Where the read-only reference data ends up, and where *your* data goes.

This project is installed as a Claude Code plugin, which means the two halves of
it live in different places and must never be confused:

    ROOT       the plugin itself -- the broker registry, the playbooks, the
               knowledge files. Shared by everyone who installs it, read-only in
               practice, and safe to publish.

    WORKSPACE  one person's removal campaign -- their profile, their per-broker
               status, their handoff queue, their drafted letters. Private, never
               committed, and different for every user.

Before the plugin existed these were the same directory, which was fine for one
person working in a clone and wrong the moment anyone else installed it: their
identity would have been written inside the plugin, and a plugin update would
have clobbered their progress.

Set BROKER_REMOVE_WORKSPACE to choose where your data lives. If it is unset the
two collapse back to the repo, so working in a clone behaves exactly as before.
"""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

_ws = os.environ.get("BROKER_REMOVE_WORKSPACE")
WORKSPACE = Path(_ws).expanduser().resolve() if _ws else ROOT


def state(name: str) -> Path:
    """A file that belongs to the person running this, not to the plugin."""
    return WORKSPACE / "data" / name


def outbox() -> Path:
    return WORKSPACE / "outbox"


def ensure_workspace() -> Path:
    """Create the workspace skeleton. Safe to call repeatedly."""
    (WORKSPACE / "data").mkdir(parents=True, exist_ok=True)
    outbox().mkdir(parents=True, exist_ok=True)
    return WORKSPACE


# ---------------------------------------------------------------------------
# Playbook location.
#
# brokers/ held 1,260 files in one flat directory. Git does not mind, and a
# clone gets every one of them -- but GITHUB'S WEB UI LISTS AT MOST 1,000
# ENTRIES PER DIRECTORY and silently stops there, with no "and 260 more". So
# anyone browsing the repository saw a complete-looking list that was missing a
# fifth of the brokers, which is exactly the kind of quiet truncation this
# project exists to write about.
#
# Sharded on the first character of the broker id, digits collapsed into one
# bucket: 27 directories, largest 112 files, room to grow several times over.
# The knowledge documents (brokers/_*.md) stay at the top level, because they
# are what a person actually opens and they should not be hidden a level down.

PLAYBOOKS = ROOT / "brokers"


def shard(bid: str) -> str:
    """Which subdirectory a broker id lives in."""
    c = (bid or "?")[0].lower()
    if c.isdigit():
        return "0-9"
    return c if "a" <= c <= "z" else "other"


def playbook(bid: str) -> Path:
    """Path to a broker's playbook, sharded.

    Falls back to the old flat location when a sharded file is absent, so a
    half-migrated tree and any caller this change missed both keep working
    rather than silently creating a second copy in the wrong place.
    """
    sharded = PLAYBOOKS / shard(bid) / f"{bid}.md"
    if sharded.exists():
        return sharded
    flat = PLAYBOOKS / f"{bid}.md"
    if flat.exists():
        return flat
    return sharded          # new files are written sharded
