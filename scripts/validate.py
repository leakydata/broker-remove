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

    # An address that dies gets email_verified_by overwritten with the CAUSE of death
    # ("bounced", "declared_unmonitored_by_company"), which destroys the record of what
    # the address was trusted on in the first place. That made the obvious question --
    # do register-filed addresses fail more often than policy-published ones? --
    # unanswerable from the data, because failure erased the evidence. 27 of them were
    # recoverable from git history; the rest are gone. See _SILENT_FAILURES 206.
    #
    # The rule now: when demoting a verified address, move the old basis to
    # email_verified_was before writing the cause of death over it.
    # Only bases that imply the address once WORKED. "no_address_published" and
    # "site_unreachable" are discovery outcomes -- 88 rows were born carrying them and
    # never had a prior basis to lose, so warning on those would be 88 false positives.
    _DEATH_BASIS = {"bounced", "hard_bounce", "declared_unmonitored_by_company"}
    for _b in brokers:
        _by = (_b.get("email_verified_by") or "")
        if _by in _DEATH_BASIS and not _b.get("email_verified_was"):
            warnings.append(
                f"[{_b['id']}]: email_verified_by={_by!r} records the cause of "
                "death but the prior basis is lost; set email_verified_was "
                "when demoting")
    by_id = {b["id"]: b for b in brokers if b.get("id")}

    # Status lives in a gitignored state file, so it is loaded defensively: a
    # missing or malformed file must not turn every check below into a crash.
    _state_raw = {}
    _sp = state_file("removal_status.json")
    if _sp.exists():
        try:
            _s = json.loads(_sp.read_text())
            _state_raw = _s.get("brokers", _s)
        except Exception:
            _state_raw = {}

    def _status(bid):
        rec = _state_raw.get(bid)
        if isinstance(rec, dict):
            return rec.get("status") or "pending"
        return rec or "pending"

    # A letter must not tell a company it is on a state register unless the row says so.
    # I told OneTrust and Transcend exactly that on 2026-08-31, from rows whose
    # registry_years were empty, and had to write to both again to withdraw it. The
    # distinguishing field was there the whole time. See _SILENT_FAILURES 214/214a.
    _REG_WORDS = ("data broker register", "registered as a data broker",
                  "registered data broker", "ca data broker registration")
    for _b in brokers:
        if _b.get("registry_years"):
            continue
        _r = _state_raw.get(_b["id"]) or {}
        _notes = " ".join((e.get("note") or "") for e in (_r.get("history") or [])).lower()
        if any(w in _notes for w in _REG_WORDS) and "correction" not in _notes:
            warnings.append(
                f"[{_b['id']}]: notes assert a data broker registration but registry_years "
                "is empty (listing_basis=" + str(_b.get("listing_basis")) + ") - verify "
                "before any letter repeats it")

    # PLACEHOLDER NAMES. The register's "Doing Business As, if applicable" field is
    # answered "None" or "N/A" by registrants that have no DBA, and the importer took
    # that answer as the company name. FinThrive -- continuously registered since 2020
    # and self-declaring reproductive health care data collection in its 2024 filing --
    # sat in this file under the name "None" for weeks. A letter addressed to a company
    # called "No" is not a letter anyone answers. See _SILENT_FAILURES 240.
    _PLACEHOLDER = re.compile(r"^(none|n/?a|na|null|not applicable|nil|[-.\s])$", re.I)
    for _b in brokers:
        if _PLACEHOLDER.match((_b.get("name") or "").strip()):
            errors.append(
                f"[{_b['id']}]: name is the placeholder {_b.get('name')!r} -- almost "
                "certainly the register's empty-DBA answer imported as a company name. "
                "Set it from the filing's business-name column before writing.")

    # SUCCESSION FAMILIES -- one operating business registered under several corporate
    # parents across years, each row a different domain and contact. Picking a row by
    # name recognition rather than by recency lands you on a lapsed filing whose address
    # may since have died: the Valassis 2024 "a Vericast Business" contact hard-bounced,
    # while the 2025-2026 "an RRD Company" row was live the whole time. See 216.
    def _name_stem(n):
        n = (n or "").lower()
        n = re.split(r",|\ban?\b\s+\w+\s+(?:company|business)|\bllc\b|\binc\b|\bcorp", n)[0]
        return re.sub(r"[^a-z0-9]+", " ", n).strip()

    def _latest_year(b):
        ys = b.get("registry_years") or []
        return max((int(y[-4:]) for y in ys if y[-4:].isdigit()), default=0)

    _fam = {}
    for _b in brokers:
        if _b.get("registry_years") and _name_stem(_b.get("name")):
            _fam.setdefault(_name_stem(_b["name"]), []).append(_b)
    for _stem, _rows in _fam.items():
        if len(_rows) < 2 or len({r["domain"] for r in _rows}) < 2:
            continue
        _newest = max(_latest_year(r) for r in _rows)
        for _b in _rows:
            if _latest_year(_b) < _newest:
                _cur = [r["id"] for r in _rows if _latest_year(r) == _newest]
                warnings.append(
                    f"[{_b['id']}]: lapsed registration ({_b.get('registry_years')}) for a "
                    f"business still registered as {_cur} - prefer the current registrant's "
                    "contact; a lapsed filing's address is the one most likely to be dead")

    # ORPHAN STATUS ROWS. A note can be written against any key at all -- the tracker
    # is a dict and nothing validates the id. On 2026-08-31 I recorded an Altrata
    # acknowledgement under "boardex_altrata", which is not a broker, not an alias and
    # has no playbook. The note was real, the work was real, and it landed somewhere
    # nothing would ever read it. See 219.
    #
    # A status row that is NOT a registry id is usually legitimate: a sibling brand
    # named inside a parent's letter gets its own row so per-brand coverage is
    # recorded. Those have a playbook file. The discriminator is therefore the
    # playbook, not the registry -- an orphan with no document behind it is a typo.
    _ids = {b["id"] for b in brokers}
    try:
        _al = json.loads((ROOT / "data" / "playbook_aliases.json").read_text())["aliases"]
        _known = _ids | set(_al) | set(_al.values())
    except Exception:
        _known = _ids
    for _bid in _state_raw:
        if _bid in _known or (PLAYBOOKS / f"{_bid}.md").exists():
            continue
        warnings.append(
            f"[{_bid}]: status row for an id that is not a broker, not an alias and has "
            "no playbook - a note filed here will never be read; check for a typo")

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

            # A duplicate_of row that is still pending while its canonical is
            # settled AT THE SAME ADDRESS is a queued second letter to a mailbox
            # that already has the request. 56 of these had accumulated silently
            # by 2026-08-29 -- about a tenth of the pending count. See
            # _SILENT_FAILURES 177. Where the two addresses DIFFER this is not a
            # duplicate at all but a second route into an acquired entity, and
            # that is left alone deliberately.
            canon = b.get("duplicate_of")
            if canon and canon in by_id:
                other = by_id[canon]
                a1 = (b.get("email_to") or "").lower().strip()
                a2 = (other.get("email_to") or "").lower().strip()
                if a1 and a1 == a2 and _status(b["id"]) == "pending" \
                        and _status(canon) in ("submitted", "confirmed"):
                    warnings.append(
                        f"{where}: pending, but duplicate_of '{canon}' is already "
                        f"{_status(canon)} at the identical address {a1}. Sending "
                        f"would put a second letter in a mailbox that has the "
                        f"request. Mark it covered, or drop the duplicate_of link "
                        f"if these are genuinely different companies.")

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

    # SF 309: four letters reached one mailbox in 24 hours because four rows
    # resolved to one address and nothing in the send path looked at the address.
    # The duplicate_of check above only fires where somebody already noticed the
    # link. This catches the ones nobody noticed -- an unsent row sharing an
    # address with a row that has already been written to.
    _by_addr = {}
    for b in brokers:
        a = (b.get("email_to") or "").lower().strip()
        if a:
            _by_addr.setdefault(a, []).append(b["id"])
    _SENT = {"submitted", "email_pending", "confirmed", "replied", "acknowledged", "suppressed"}
    for a, ids in sorted(_by_addr.items()):
        if len(ids) < 2:
            continue
        unsent = [i for i in ids if _status(i) == "pending"]
        already = [i for i in ids if _status(i) in _SENT]
        if unsent and already:
            warnings.append(
                f"[mailbox] {a}: {len(unsent)} row(s) still pending ({', '.join(sorted(unsent)[:3])})"
                f" share this address with {len(already)} already written to. A new letter here "
                f"repeats one the mailbox has. Reply in the existing thread, or cover the pending "
                f"rows by naming them in it -- run scripts/mailbox_guard.py {a}")

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

        # A TERMINAL STATUS WITH NO NOTE IS AN UNFALSIFIABLE CLAIM.
        #
        # 'not_found' and 'confirmed' settle a broker: the queue never offers it
        # again, and no later pass revisits it. So the note is the only surviving
        # record of WHY. On 2026-08-30 an audit found two rows -- mrss and
        # permutive -- carrying not_found with a completely empty note. Both
        # turned out to be sound, recovered from the mailbox: one was an
        # unqualified nil plus a forward commitment, the other was a scoped nil
        # pushed on until the company confirmed it had searched client records
        # too. One of the better exchanges in the project, and the ledger said
        # nothing at all (_SILENT_FAILURES 200).
        #
        # The evidence lived in a Gmail mailbox. This file already documents
        # mailboxes that accept everything and read nothing (165), and four full
        # inboxes on a single alias (181) -- mailboxes are not durable storage.
        # If that one goes, an unevidenced terminal row is indistinguishable
        # from a mistake.
        #
        # This project spends most of its effort demanding that companies say
        # what they searched and what they found. The same standard has to apply
        # inward: a status is a claim, and a claim without its evidence is worth
        # what a broker's unelaborated confirmation is worth.
        # THE FIELD THE CHECK READS AND THE FIELD I HAD BEEN WRITING DIVERGED.
        #
        # A tracker row has a top-level `note` -- what this check inspects, and what a
        # human reads first -- and a `history` list, which is the log. My recording
        # helpers appended to history and never touched `note`, so 152 rows had an
        # EMPTY top-level note with everything in the log, and 70 more had a stale one
        # that predated the outcome.
        #
        # It surfaced only when a terminal row was created that way, because the check
        # below looks at terminal rows alone. Everything non-terminal drifted in silence.
        # See _SILENT_FAILURES 225.
        for _bid, _rec in state.items():
            if not isinstance(_rec, dict):
                continue
            _hn = [(e.get("note") or "").strip()
                   for e in (_rec.get("history") or []) if (e.get("note") or "").strip()]
            if not _hn:
                continue
            _top = (_rec.get("note") or "").strip()
            if not _top:
                warnings.append(
                    f"{_bid}: history has {len(_hn)} note(s) but the top-level `note` is "
                    "empty - that is the field this validator and a human both read first")
            elif _top != _hn[-1] and _hn[-1] not in _top:
                warnings.append(
                    f"{_bid}: top-level `note` is older than the last history entry - "
                    "the log advanced and the summary did not")

        # 'suppressed' settles a broker exactly as the other two do -- the queue
        # stops offering it -- so it needs the same unfalsifiable-claim guard.
        # `submitted` is not terminal, so the guard below never saw it -- and it
        # is the status the entire coverage figure rests on. 113 rows once
        # asserted it with nothing behind them but "Adopted from the shared
        # ledger... No detail is carried across", which is honest and still an
        # unfalsifiable claim. Warn rather than error: the ledger is a legitimate
        # source and the fix (scripts/backfill_notes.py) recovers the evidence
        # from committed playbooks, but the count should never be invisible again.
        # See _SILENT_FAILURES §273.
        _thin = [b for b, r in state.items()
                 if r.get("status") == "submitted"
                 and r.get("history")
                 and all((h.get("note") or "").startswith("Adopted from")
                         or not (h.get("note") or "")
                         for h in r["history"])]
        if _thin:
            warnings.append(
                f"[{len(_thin)}] rows are 'submitted' with no evidence in their "
                f"history -- only a ledger-adoption placeholder. Run "
                f"scripts/backfill_notes.py --apply to recover what the "
                f"committed playbooks hold: {', '.join(sorted(_thin)[:8])}"
                + (" ..." if len(_thin) > 8 else ""))

        # HOW MANY NILS ARE ASSERTED RATHER THAN DEMONSTRATED.
        #
        # A company that searched carefully and a company whose query silently
        # returned zero send the identical sentence, so from outside every nil is
        # unfalsifiable -- until one of them runs a positive control and says so
        # (§289). One company in this corpus has. Reporting the count keeps the
        # distinction visible instead of letting `not_found` read as settled.
        #
        # This is not a warning about the brokers. It is a warning about what the
        # corpus can support, and the number should be quoted whenever the totals
        # are.
        _nil = re.compile(r"found no|no record|nothing on file|do ?n'?o?t have|"
                          r"not have any|unable to (find|locate)|no match|"
                          r"searched and found", re.I)
        _demo = re.compile(r"positive control|ran (the same query|a control)|"
                           r"control returned", re.I)
        _asserted = []
        for _b, _r in state.items():
            if _r.get("status") not in ("not_found", "suppressed"):
                continue
            _n = " ".join((h.get("note") or "") for h in _r.get("history", []))
            if _nil.search(_n) and not _demo.search(_n):
                _asserted.append(_b)
        if _asserted:
            warnings.append(
                f"[{len(_asserted)}] nil results are ASSERTED, not demonstrated -- "
                f"no evidence the search could have found anything (see §289). "
                f"Not a fault of the brokers; a limit on what this corpus proves.")

        TERMINAL = {"not_found", "confirmed", "suppressed"}
        for bid, rec in state.items():
            if rec.get("status") not in TERMINAL:
                continue
            note = (rec.get("note") or "").strip()
            if len(note) < 40:
                errors.append(
                    f"{bid}: status '{rec.get('status')}' is TERMINAL but its "
                    f"note is {'empty' if not note else f'only {len(note)} chars'}. "
                    f"Record what was searched and what was found, or the row "
                    f"cannot be reviewed later. See _SILENT_FAILURES 200.")
                continue

            # A LONG NOTE IS NOT THE SAME AS AN EVIDENCED ONE.
            #
            # The length rule above passes a note that describes the OUTGOING
            # LETTER in detail and never records the reply. apollo_io sat at
            # 'confirmed' with a note reading "first contact, sent to the address
            # discovered by the verify_emails sweep" -- 121 characters about a
            # send, while the actual reply (deletion actioned plus an unprompted
            # suppression, four minutes later) went unrecorded entirely. Same
            # shape at 'experience', whose note enumerates what was ASKED.
            #
            # So this looks for any sign the note records an ANSWER rather than a
            # dispatch: a quotation, or a word describing what the company did.
            # Deliberately generous -- it is a prompt to write the outcome down,
            # not a grammar check, and a false pass costs nothing that the length
            # rule was not already going to miss (_SILENT_FAILURES 202).
            ANSWERED = ("confirm", "replied", "reply", "answered", "said",
                        "response", "responded", "ticket", "wrote back",
                        "not found", "no record", "deleted", "suppress",
                        "'", '"', "\u2019")
            if not any(w in note.lower() for w in ANSWERED):
                warnings.append(
                    f"{bid}: status '{rec.get('status')}' is TERMINAL and its "
                    f"note is substantial but shows no sign of recording a "
                    f"REPLY -- no quotation, no description of what the company "
                    f"did. Check it is not describing the outgoing letter "
                    f"instead. See _SILENT_FAILURES 202.")

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
