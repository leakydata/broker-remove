#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Build a verification worklist: which removals are due for re-checking, and how.

A submission is not a removal. Brokers process late, process partially, or
re-add a record when new source data arrives that they cannot match to the
suppression. The only way to know is to look again.

This is the step almost nobody does, and it is the difference between "I opted
out" and "I am not listed". It also produces the evidence you need to escalate:
a broker that confirmed removal and still lists you is a materially different
conversation from one that never replied.

    ./verify_removals.py                 # what is due now
    ./verify_removals.py --all           # every submitted broker, due or not
    ./verify_removals.py --due-in 3      # what becomes due within 3 days
    ./verify_removals.py --mark <id> gone|still_listed|not_found
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
from paths import state, outbox  # noqa: E402
REGISTRY = ROOT / "data" / "brokers.json"
STATE = state("removal_status.json")
PROFILE = state("profile.json")

# How long to wait before re-checking, by what the broker told us.
# Most state 3 days; the 45-day statutory window is the outer bound.
DEFAULT_WAIT_DAYS = 7

# Brokers whose listing can be checked by URL. {id: template}
# Placeholders: {first} {last} {First} {Last} {state} {ST} {city} {City}
SEARCH_TEMPLATES = {
    "spokeo":            "https://www.spokeo.com/{First}-{Last}/{state}/{City}",
    "radaris":           "https://radaris.com/ng/search?ff={First}&fl={Last}&fs={ST}&fc={City}",
    "checkpeople":       "https://checkpeople.com/name/{first}-{last}/in-{ST}/{city}",
    "truepeoplesearch":  "https://www.truepeoplesearch.com/results?name={First}%20{Last}&citystatezip={City}%2C%20{ST}",
    "fastpeoplesearch":  "https://www.fastpeoplesearch.com/name/{first}-{last}_{city}-{ST}",
    "searchpeoplefree":  "https://www.searchpeoplefree.com/find/{first}-{last}/{ST}/{city}",
    "thatsthem":         "https://thatsthem.com/name/{First}-{Last}/{City}-{ST}",
    "usphonebook":       "https://www.usphonebook.com/{first}-{last}",
    "nuwber":            "https://nuwber.com/search?name={First}%20{Last}&state={ST}",
    "clustrmaps":        "https://clustrmaps.com/persons/{First}-{Last}",
    "peoplefinders":     "https://www.peoplefinders.com/name/{first}-{last}/{ST}/{city}",
    "beenverified":      "https://www.beenverified.com/people/{first}-{last}/{ST}/{city}/",
    "familytreenow":     "https://www.familytreenow.com/search/genealogy/results?first={First}&last={Last}&citystatezip={City}%2C+{ST}",
    "whitepages":        "https://www.whitepages.com/name/{First}-{Last}/{City}-{ST}",
    "ownerly":           "https://www.ownerly.com/name/{first}-{last}/{ST}/{city}",
    "neighborwho":       "https://www.neighborwho.com/name/{first}-{last}/{ST}/{city}",
    "spydialer":         "https://www.spydialer.com/",
    "veripages":         "https://veripages.com/name/{First}-{Last}/",
    "cocofinder":        "https://cocofinder.com/name/{first}-{last}",
    "peekyou":           "https://www.peekyou.com/{first}_{last}",
}

# Brokers with NO public listing to search. Verification by lookup is impossible;
# their written confirmation is the only available evidence. Saying "check
# manually" here would send someone hunting for a page that does not exist.
NO_PUBLIC_LISTING = {
    "acxiom", "lexisnexis", "epsilon", "dataaxle", "melissa", "corelogic",
    "experian_marketing", "equifax", "transunion", "liveramp", "oracle_datacloud",
    "affinity_solutions", "affinity_answers", "aidentified", "adttribution",
    "33across", "360_media_direct", "33_mile_radius", "ach_address_clearing_house",
    "ad_direct", "agr_marketing_solutions", "ace_agents", "aged_lead_store",
    "academixdirect", "deep_sync", "lotame", "criteo", "quantcast", "bombora",
    "plaid", "windfall", "dun_bradstreet", "enformion",
}


def load(p, default):
    return json.loads(p.read_text()) if p.exists() else default


def profile_bits():
    p = load(PROFILE, {})
    if not p:
        return None
    first, last = p.get("first_name", ""), p.get("last_name", "")
    return {
        "first": first.lower(), "last": last.lower(),
        "First": first.title(), "Last": last.title(),
        "city": p.get("city", "").lower(), "City": p.get("city", "").title(),
        "ST": p.get("state", "").upper(),
        "state": {"PA": "Pennsylvania"}.get(p.get("state", "").upper(), p.get("state", "")),
    }


def search_url(bid, bits):
    t = SEARCH_TEMPLATES.get(bid)
    if not t or not bits:
        return None
    try:
        return t.format(**bits)
    except KeyError:
        return None


def cmd_list(args):
    reg = {b["id"]: b for b in load(REGISTRY, {"brokers": []})["brokers"]}
    st = load(STATE, {})
    bits = profile_bits()
    now = datetime.now(timezone.utc)

    rows = []
    for bid, rec in st.items():
        if rec.get("status") not in {"submitted", "confirmed"}:
            continue
        # Verification results live alongside the status so re-checks accumulate.
        checks = rec.get("verifications", [])
        last = checks[-1]["at"] if checks else rec.get("updated", "")
        try:
            since = (now - datetime.fromisoformat(last)).days
        except Exception:
            since = 999
        due_in = DEFAULT_WAIT_DAYS - since
        if not args.all and due_in > args.due_in:
            continue
        b = reg.get(bid, {})
        rows.append((due_in, bid, b.get("name", bid), b.get("priority", 0),
                     search_url(bid, bits), checks[-1]["result"] if checks else None,
                     bid in NO_PUBLIC_LISTING))

    rows.sort(key=lambda r: (r[0], -r[3]))
    if not rows:
        print(f"nothing due for verification "
              f"(re-check {DEFAULT_WAIT_DAYS} days after submission)")
        return 0

    print(f"{len(rows)} broker(s) to verify — a submission is not a removal\n")
    checkable = [r for r in rows if not r[6]]
    opaque = [r for r in rows if r[6]]

    if checkable:
        print("VERIFIABLE BY SEARCH — re-run the lookup and see if you are listed\n")
        for due_in, bid, name, pri, url, lastres, _ in checkable:
            when = "DUE NOW" if due_in <= 0 else f"in {due_in}d"
            prev = f"  [last: {lastres}]" if lastres else ""
            print(f"  {when:>8}  p{pri}  {bid:26}{prev}")
            print(f"            {url if url else 'search URL unknown — find it on the site'}")

    if opaque:
        print(f"\nNO PUBLIC LISTING ({len(opaque)}) — nothing to search; their written")
        print("confirmation is the only evidence. Chase any that never replied.\n")
        for due_in, bid, name, pri, url, lastres, _ in opaque:
            prev = f"  [last: {lastres}]" if lastres else ""
            print(f"            p{pri}  {bid}{prev}")
    print(f"\nRecord an outcome:  ./verify_removals.py --mark <id> "
          f"gone|still_listed|not_found")
    return 0


def cmd_mark(args):
    bid, result = args.mark
    if result not in {"gone", "still_listed", "not_found"}:
        sys.exit("result must be: gone | still_listed | not_found")
    st = load(STATE, {})
    if bid not in st:
        sys.exit(f"no recorded attempt for {bid}")
    rec = st[bid]
    entry = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "result": result}
    if args.note:
        entry["note"] = args.note
    rec.setdefault("verifications", []).append(entry)

    # A record that came back is the finding worth surfacing: it means the
    # broker's suppression did not hold, which is escalation-worthy and tells
    # you this broker needs a recurring sweep rather than a one-time request.
    if result == "gone":
        rec["status"] = "confirmed"
        msg = "confirmed removed"
    elif result == "still_listed":
        prior = [v for v in rec["verifications"][:-1] if v["result"] == "gone"]
        if prior:
            rec["status"] = "pending"
            msg = ("REAPPEARED — was previously confirmed gone. Suppression did not "
                   "hold; re-file and cite the earlier confirmation")
        else:
            msg = "still listed — not yet processed, or the request was not matched"
    else:
        rec["status"] = "not_found"
        msg = "no record found"
    STATE.write_text(json.dumps(st, indent=2, ensure_ascii=False) + "\n")
    print(f"{bid}: {msg}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--due-in", type=int, default=0,
                    help="also show checks becoming due within N days")
    ap.add_argument("--mark", nargs=2, metavar=("BROKER_ID", "RESULT"))
    ap.add_argument("--note")
    args = ap.parse_args()
    return cmd_mark(args) if args.mark else cmd_list(args)


if __name__ == "__main__":
    sys.exit(main())
