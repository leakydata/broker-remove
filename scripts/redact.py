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
from paths import state, outbox  # noqa: E402
PROFILE = state("profile.json")


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


def _allowlist():
    """{term: {paths}} -- values that are permitted in named files only.

    This exists for exactly one situation: a value that is already public by the
    owner's own choice and that a file cannot do its job without. Publishing the
    project as a plugin means the marketplace manifest has to name the owner, and
    the owner's GitHub handle is the local-part of their email, so the scanner
    flags a string that is already the repository's own URL.

    Deliberately per-file and per-value, with no wildcard. A blanket exemption
    would silently cover every future file, which is how an allowlist stops being
    a decision and becomes a hole. Blocking the full email address is unaffected:
    only the exact literal listed is exempted, and only where it is listed."""
    f = ROOT / "data" / "redaction_allowlist.json"
    if not f.exists():
        return {}
    try:
        d = json.loads(f.read_text())
    except Exception:
        return {}
    return {e["value"].lower(): set(e.get("files", []))
            for e in d.get("allow", []) if e.get("value")}



# ---------------------------------------------------------------------------
# Other people's addresses.
#
# Everything above protects the person running this. This protects everyone
# else. State data-broker registries name an individual as the contact for
# roughly one company in six, and a writeup that quotes one -- or a playbook
# scaffolded from the recorded route -- republishes a real person's work address
# in a public repo about deleting personal data. It has happened three times: a
# table of seven registry contacts in _SILENT_FAILURES.md, and two playbooks
# scaffolded automatically the moment a letter was recorded.
#
# Two deliberate narrowings, because the first attempt at this flagged 747
# addresses and would have been switched off within a day.
#
# SCOPE: prose only -- markdown. The registry JSON and the vendor exports hold
# registry contacts because that is what they are for; the data files are the
# protected source, and stripping them would break the routes. The leak happens
# when an address is *quoted into an argument*, and arguments live in markdown.
#
# TEST: person-shaped, not "unrecognised". is_role_address() is a whitelist
# built to choose a good route, and as a publication filter it condemns every
# role mailbox nobody thought of -- notice@, research@, removals@, intelligence@
# were all flagged. So this asks the opposite question: does the local part look
# like a human name? Under-blocking is the right error here. This is a backstop;
# the primary control is the ROLE rule in discover_contacts.py.

EMAIL = re.compile(r"\b[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")

# first.last / f.last / flast-with-a-known-first-name are what registry contacts
# actually look like. A bare word is only person-shaped if it is not a role word,
# so the role list still does useful work -- as an exemption, not as the rule.
_PERSON = re.compile(r"""^(
      [a-z]+\.[a-z]+          # first.last
    | [a-z]\.[a-z]{2,}        # f.last
    | [a-z]+_[a-z]+           # first_last
)[0-9]*$""", re.X)

# A bare first name -- `richard@`, `chirag@` -- is the other common registry
# shape, and this rule does NOT catch it. Widening to bare words flags 196
# addresses in markdown alone, nearly all of them role mailboxes nobody thought
# to list: accounting@, removals@, notice@, leads@, safety@, requests@. A gate
# that noisy gets switched off, so it is worth less than the narrow one.
#
# The bare-name case is handled where it actually originates instead:
# scaffold_playbook.py masks a non-role contact at the moment it writes the
# file, which needs no heuristic at all because the provenance is known.


def _is_role(addr):
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from verify_emails import is_role_address
    except Exception:
        return True          # cannot judge -> do not block a commit on a guess
    return is_role_address(addr)


def _person_shaped(addr):
    local = addr.split("@")[0].lower()
    if _is_role(local + "@x.com"):
        return False
    return bool(_PERSON.match(local))


def _people_allowlist():
    f = ROOT / "data" / "people_allowlist.json"
    if not f.exists():
        return set()
    try:
        return {a.lower() for a in json.loads(f.read_text())}
    except Exception:
        return set()


def scan_people(files, skip):
    """Return [(path, lineno, addr)] for named individuals' addresses in prose."""
    allowed = _people_allowlist()
    hits = []
    for f in files:
        if f in skip or not f.endswith(".md"):
            continue
        try:
            content = (ROOT / f).read_text(errors="replace")
        except Exception:
            continue
        for i, line in enumerate(content.splitlines(), 1):
            for addr in EMAIL.findall(line):
                a = addr.lower()
                if a in allowed or not _person_shaped(a):
                    continue
                hits.append((f, i, addr))
    return hits


def scan_tracked():
    """Return [(path, lineno, term)] for personal data in files git will publish.

    That means tracked files AND untracked files git is not ignoring -- a
    distinction that cost us a real leak. `git ls-files` alone lists only what is
    already tracked, so a brand-new playbook is invisible to this scan right up
    until the commit that publishes it. The check ran, reported zero, and the
    file went public in the same breath: the one moment a new file most needs
    scanning is the one moment ls-files cannot see it.

    Gitignored paths stay out of scope. They are where personal data is supposed
    to live."""
    terms = _terms()
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=ROOT,
                                 capture_output=True, text=True,
                                 check=True).stdout.split()
        # -o lists untracked, --exclude-standard respects .gitignore, so this is
        # exactly "files that would be published if you committed everything".
        untracked = subprocess.run(
            ["git", "ls-files", "-o", "--exclude-standard"], cwd=ROOT,
            capture_output=True, text=True, check=True).stdout.split()
        files = tracked + untracked
    except Exception:
        return [], []
    # The profile template and this scanner legitimately mention field names.
    skip = {"data/profile.example.json", "scripts/redact.py",
            "data/redaction_allowlist.json"}
    allowed = _allowlist()
    hits = []
    for f in files if terms else []:
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
                # (?<![A-Za-z]) -- the term must not be the tail of a longer word.
                # Without it "NATHAN" matches inside "Jonathan", and the gate fired
                # on a broker contact's own first name. A gate that cries wolf is a
                # gate that eventually gets overridden, which is the failure mode
                # 179 exists to prevent.
                #
                # Only the LEADING side is bounded, deliberately. A trailing bound
                # would miss "nathanjones@..." and concatenated forms, and a miss
                # here is far worse than a false positive.
                if len(t) > 4 and re.search(r"(?<![A-Za-z])" + re.escape(t), line, re.I):
                    if f in allowed.get(t.lower(), ()):
                        continue
                    hits.append((f, i, t))
                    break
    return hits, scan_people(files, skip)


if __name__ == "__main__":
    hits, people = scan_tracked()
    for f, i, t in hits:
        print(f"  {f}:{i}  contains profile value: {t[:28]!r}")
    print(f"\n{len(hits)} personal-data occurrence(s) in files git would publish")
    if people:
        print()
        for f, i, a in people:
            print(f"  {f}:{i}  third party's address: {a}")
        print(f"\n{len(people)} named individual's address(es) in files git would "
              f"publish")
        print(
            "\nThese belong to other people -- usually a registry contact. Mask the\n"
            "local part ([named individual]@company.com) or use the company's role\n"
            "address instead. The point of a writeup is never the person's name.\n"
            "\n"
            "If an address really is a role mailbox this rule misreads, add it to\n"
            "data/people_allowlist.json."
        )
    if hits:
        # Every catch so far has had the same cause: quoting a real value while
        # writing up a finding, to make the evidence concrete. The finding has
        # never actually needed the value -- a placeholder carries the same
        # point. Say so here rather than only refusing, because the person
        # reading this is mid-writeup and about to reach for a workaround.
        print(
            "\nThis is almost always a quoted value in a writeup. Replace it with a\n"
            "placeholder -- [name], [current address], 'one of the twelve email\n"
            "addresses' -- rather than trimming the sentence. The argument reads the\n"
            "same without the value, and the value is the only part that cannot be\n"
            "unpublished.\n"
            "\n"
            "If a specific value genuinely IS the finding, add it to\n"
            "data/redaction_allowlist.json for that one file. Do not widen the\n"
            "allowlist to make a commit pass."
        )
    sys.exit(1 if (hits or people) else 0)
