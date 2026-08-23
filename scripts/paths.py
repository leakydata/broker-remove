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
