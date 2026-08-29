#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Validate data/curated_brokers.json before a commit or pull request.

Catches the mistakes that are expensive precisely because they fail quietly:
a duplicate id silently overwrites another broker, and a guessed contact address
produces a bounce that is indistinguishable from a pending request.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from redact import scan_tracked  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
from paths import state as state_file, outbox  # noqa: E402
CURATED = ROOT / "data" / "curated_brokers.json"
PLAYBOOKS = ROOT / "brokers"

METHODS = {"web_form", "web_form_captcha", "email", "account_required",
           "postal", "phone", "unknown"}
REQUIRED = ["id", "name", "domain", "priority", "method", "optout_url"]
ID_RE = re.compile(r"^[a-z0-9_]+$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Addresses shaped like a guess. Not wrong by definition, but worth a look --
# these are exactly the ones that bounce.
GUESSY_LOCAL = {"privacy", "support", "info", "contact", "legal", "admin"}

errors, warnings = [], []


def _dead_addresses():
    """Addresses observed to bounce, keyed lowercase. Missing file means nothing
    is known yet, not that everything is fine -- so an empty dict, never a crash."""
    f = ROOT / "data" / "dead_addresses.json"
    if not f.exists():
        return {}
    try:
        raw = json.loads(f.read_text()).get("addresses", {})
    except (json.JSONDecodeError, OSError):
        return {}
    return {a.lower(): (v if isinstance(v, dict) else {}) for a, v in raw.items()}


DEAD_ADDRS = _dead_addresses()


def main():
    data = json.loads(CURATED.read_text())
    brokers = data["brokers"]

    seen_ids, seen_domains = {}, {}
    for i, b in enumerate(brokers):
        where = f"[{i}] {b.get('id', '<no id>')}"

        bid = b.get("id", "")
        for f in REQUIRED:
            if not b.get(f) and b.get(f) != 0:
                # An email-only broker legitimately has no web opt-out page.
                if f == "optout_url" and b.get("method") == "email" and b.get("email_to"):
                    continue
                # And a broker with NO ROUTE AT ALL has no opt-out page either.
                # This is a real state, not a gap in the data: a site with no MX
                # record, no published address and placeholder legal links cannot
                # be written to or submitted to by anyone. Forcing a URL into the
                # field to satisfy the schema would record a route that does not
                # exist -- the one thing this file must never do. Allowed only
                # when the dead end is documented in a playbook, so the claim is
                # always accompanied by the evidence for it.
                if (f == "optout_url" and b.get("method") == "unknown"
                        and not b.get("email_to")
                        and (PLAYBOOKS / f"{bid}.md").exists()):
                    continue
                errors.append(f"{where}: missing required field '{f}'")

        if bid and not ID_RE.match(bid):
            errors.append(f"{where}: id must be lowercase letters/digits/underscores")
        if bid in seen_ids:
            errors.append(f"{where}: duplicate id, collides with entry [{seen_ids[bid]}]")
        seen_ids[bid] = i

        dom = b.get("domain", "")
        if dom:
            if dom.startswith(("http://", "https://")) or "/" in dom:
                errors.append(f"{where}: domain should be a bare hostname, got '{dom}'")
            if dom in seen_domains:
                warnings.append(
                    f"{where}: domain '{dom}' already used by [{seen_domains[dom]}] "
                    f"- intentional only if they're genuinely separate properties")
            seen_domains[dom] = i

        pr = b.get("priority")
        if not isinstance(pr, int) or not 1 <= pr <= 5:
            errors.append(f"{where}: priority must be an int 1-5, got {pr!r}")

        m = b.get("method")
        if m not in METHODS:
            errors.append(f"{where}: method {m!r} not one of {sorted(METHODS)}")

        url = b.get("optout_url", "")
        if url and not url.startswith("https://"):
            warnings.append(f"{where}: optout_url is not https - '{url}'")

        to = b.get("email_to")
        if to:
            if not EMAIL_RE.match(to):
                errors.append(f"{where}: email_to '{to}' is not a valid address")
            elif to.split("@")[0].lower() in GUESSY_LOCAL and not b.get("email_verified"):
                warnings.append(
                    f"{where}: email_to '{to}' is unverified. Verify it against the "
                    f"privacy policy or a state registry before relying on it. "
                    f"A bounce is invisible in the tracker.")
            # "verified" has to mean something. It once defaulted to true for every
            # bulk-imported entry, so 504 of 536 addresses claimed verification
            # nobody had performed -- and this check, which keys off the flag,
            # silently passed on all of them. Four of the first thirteen such
            # addresses hard-bounced.
            # A KNOWN-DEAD ADDRESS MUST NOT BE PRESENTED AS A LIVE ROUTE.
            #
            # data/brokers.json is one large JSON blob shared between two agents.
            # Git will happily accept a stale whole-file snapshot as a legitimate
            # new version: there is nothing for it to flag, so an older copy simply
            # wins and every correction made since is reverted in silence. That
            # happened on 2026-08-29 and it reverted ten fixes, including one whose
            # only job was to stop a full identifier set being posted to a company
            # that had bought a lapsed broker's domain (_SILENT_FAILURES 169).
            #
            # dead_addresses.json is the record that survived, because the other
            # agent had no reason to touch it. So it is the right thing to check
            # against: if an address is known to bounce and the registry still
            # offers it as a verified route, something has overwritten a repair.
            # This is an ERROR rather than a warning precisely because the failure
            # mode is silence -- a warning would scroll past in a list of 1,390.
            # A KNOWN-DEAD ADDRESS MUST NOT BE PRESENTED AS A LIVE ROUTE.
            #
            # Keeping a dead address in email_to is fine and common: the entry is
            # marked email_verified false / verified_by "bounced", queue_batch holds
            # it on the dead-address list, and the row still records what was tried.
            # That is a warning at most.
            #
            # What is an ERROR is a dead address carrying a LIVE verification flag,
            # because that combination cannot be produced by anyone who knows the
            # address is dead -- it means a repair has been overwritten.
            #
            # It happened on 2026-08-29 twice over. data/brokers.json is GENERATED
            # from data/curated_brokers.json, and hand edits had been going into the
            # generated file, so every one of them was due to vanish at the next
            # build; a stale snapshot from the other agent merely got there first
            # and reverted ten at once, including the note whose only job was to
            # stop a full identifier set reaching a company that had bought a lapsed
            # broker's domain. See _SILENT_FAILURES 169.
            #
            # dead_addresses.json is the right thing to check against because it is
            # append-only, hand-maintained, and was the one file that survived.
            if to.lower() in DEAD_ADDRS:
                d = DEAD_ADDRS[to.lower()]
                when = d.get("observed") or "date not recorded"
                if b.get("email_verified") and b.get("email_verified_by") != "bounced":
                    repl = (d.get("replacement") or "").split(";")[0].strip()
                    errors.append(
                        f"{where}: email_to '{to}' is recorded DEAD in "
                        f"dead_addresses.json ({when}) yet email_verified is true "
                        f"via '{b.get('email_verified_by')}'. Two things produce "
                        f"this. Usually an overwrite: nobody who knew the address "
                        f"was dead would set a live verification flag, so check "
                        f"whether the edit landed in data/brokers.json (generated) "
                        f"instead of data/curated_brokers.json (source), and check "
                        f"git log. But it also fires honestly the moment a "
                        f"previously-good address dies -- response_solutions hit it "
                        f"the same hour an autoresponder revealed the named contact "
                        f"had left the company. Either way the registry now points "
                        f"at a dead route; the check does not need to tell the two "
                        f"apart to be worth acting on."
                        + (f" Known replacement: {repl}." if repl else ""))
                else:
                    warnings.append(
                        f"{where}: email_to '{to}' is a known-dead address ({when}), "
                        f"correctly flagged. queue_batch holds it; retained for the "
                        f"record.")

            if b.get("email_verified") and not b.get("email_verified_by"):
                warnings.append(
                    f"{where}: email_verified is true but email_verified_by is unset. "
                    f"Record how it was verified (delivery_evidence, privacy_policy, "
                    f"state_registry, broker_reply) or the flag asserts nothing.")

        if b.get("method") == "email" and not to:
            errors.append(f"{where}: method is 'email' but no email_to given")

        if b.get("needs_email_confirm") is None and b.get("method") != "unknown":
            warnings.append(f"{where}: needs_email_confirm unset - "
                            f"unclear whether the request is void until confirmed")

    # Any broker we have ACTED on must have a playbook. This is the gap that
    # opens silently: playbooks get written while working browser forms, then
    # skipped during email batches -- which is exactly when the knowledge is
    # freshest and a reply is about to need interpreting.
    state_path = state_file("removal_status.json")
    if state_path.exists():
        state = json.loads(state_path.read_text())
        # Every status except 'pending' means something happened worth writing
        # down. An earlier version listed only the in-flight ones, so a broker
        # that reached 'confirmed', 'not_found' or 'unreachable' -- the outcomes
        # a reader most wants explained -- could lose its playbook silently.
        alias_path = ROOT / "data" / "playbook_aliases.json"
        aliases = (json.loads(alias_path.read_text()).get("aliases", {})
                   if alias_path.exists() else {})
        for bid, rec in state.items():
            if rec.get("status") in (None, "pending"):
                continue
            if (PLAYBOOKS / f"{bid}.md").exists():
                continue
            covered_by = aliases.get(bid)
            if covered_by and (PLAYBOOKS / f"{covered_by}.md").exists():
                continue
            errors.append(
                f"{bid}: status '{rec.get('status')}' but no brokers/{bid}.md - "
                f"run scripts/scaffold_playbook.py --missing")

    # A high-priority broker with no playbook is the biggest documentation gap.
    for b in brokers:
        if (b.get("priority", 0) >= 4 and b.get("source") != "optery_scrape"
                and not (PLAYBOOKS / f"{b['id']}.md").exists()):
            warnings.append(f"{b['id']}: priority {b['priority']} but no "
                            f"brokers/{b['id']}.md playbook")

    # The repository is public. A tracked file containing personal data is a
    # permanent, indexable leak - treat it as a hard failure, never a warning.
    leaks, people = scan_tracked()
    for f, ln, term in leaks:
        errors.append(f"PRIVACY LEAK {f}:{ln} contains a profile value "
                      f"({term[:20]!r}) - this repo is public. Redact it.")
    # Someone else's address is a leak too, just not of our data. A registry
    # contact quoted into a playbook republishes a real person's work address.
    for f, ln, addr in people:
        errors.append(f"THIRD-PARTY ADDRESS {f}:{ln} names an individual "
                      f"({addr}) - mask the local part or use a role address.")

    for w in warnings:
        print(f"  warn: {w}")
    for e in errors:
        print(f"  ERROR: {e}", file=sys.stderr)

    print(f"\n{len(brokers)} curated brokers | {len(errors)} errors | {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
