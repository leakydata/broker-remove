#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Redaction helpers + a scanner for personal data in tracked files.

The repository is public. Everything committed is permanent and indexable, so
personal data must never reach a tracked file — not in a playbook, not in a
generated note, not in a commit message.

The subtle failure this exists to prevent: tooling that *copies* text from a
gitignored source (tracker notes, profile) into a tracked destination
(brokers/<id>.md). The source is protected; the destination is not; the copy
launders the data straight into git.

Used by scaffold_playbook.py (to redact before writing) and validate.py (to
fail a commit that would leak).
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILE = ROOT / "data" / "profile.json"


def _terms():
    """Every literal string from the profile that must not appear in a tracked
    file. Derived from the profile itself so it stays correct as it grows."""
    if not PROFILE.exists():
        return []
    p = json.loads(PROFILE.read_text())
    out = []

    def add(v):
        if isinstance(v, str) and len(v.strip()) > 3:
            out.append(v.strip())
        elif isinstance(v, list):
            for x in v:
                add(x)
        elif isinstance(v, dict):
            for x in v.values():
                add(x)

    for k, v in p.items():
        if k.startswith("_"):
            continue
        add(v)

    # Digit-only and punctuated forms of every phone number.
    for n in list(out):
        d = re.sub(r"\D", "", n)
        if len(d) == 10:
            out += [d, f"({d[:3]}) {d[3:6]}-{d[6:]}", f"{d[:3]}.{d[3:6]}.{d[6:]}"]

    # Local-parts of emails leak on their own ("scholyx", "nej105").
    for e in list(out):
        if "@" in e:
            out.append(e.split("@")[0])

    # Street name without the number, city names, and the surname alone are all
    # identifying in combination.
    if p.get("address"):
        out.append(re.sub(r"^\d+\s+", "", p["address"]))
    return sorted({t for t in out if len(t) > 3}, key=len, reverse=True)


def redact(text: str) -> str:
    """Replace every profile-derived literal with a typed placeholder."""
    if not text:
        return text
    for t in _terms():
        if not t:
            continue
        kind = ("EMAIL" if "@" in t else
                "PHONE" if re.fullmatch(r"[\d().\- ]{7,}", t) else
                "PERSONAL")
        text = re.sub(re.escape(t), f"[{kind}]", text, flags=re.I)
    # Bare 4-digit years that match the birth year.
    p = json.loads(PROFILE.read_text()) if PROFILE.exists() else {}
    dob = (p.get("date_of_birth") or "")[:4]
    if dob.isdigit():
        text = re.sub(rf"\b{dob}\b", "[YEAR]", text)
    return text


def scan_tracked():
    """Return [(path, lineno, term)] for personal data in git-tracked files."""
    terms = _terms()
    if not terms:
        return []
    try:
        files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                               text=True, check=True).stdout.split()
    except Exception:
        return []
    # The profile template and this scanner legitimately mention field names.
    skip = {"data/profile.example.json", "scripts/redact.py"}
    hits = []
    for f in files:
        if f in skip:
            continue
        fp = ROOT / f
        try:
            content = fp.read_text(errors="replace")
        except Exception:
            continue
        for i, line in enumerate(content.splitlines(), 1):
            # The repository's own URL necessarily contains the owner's handle.
            # That is public by construction and not a leak we can fix here.
            if "github.com/" in line:
                continue
            for t in terms:
                if len(t) > 4 and re.search(re.escape(t), line, re.I):
                    hits.append((f, i, t))
                    break
    return hits


if __name__ == "__main__":
    hits = scan_tracked()
    for f, i, t in hits:
        print(f"  {f}:{i}  contains profile value: {t[:28]!r}")
    print(f"\n{len(hits)} personal-data occurrence(s) in tracked files")
    sys.exit(1 if hits else 0)
