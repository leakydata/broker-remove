#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Import the official state data-broker registries.

Why this exists: every other source in this project is inferred. Optery's list is
a competitor's research, the domains are derived from slugs, and the addresses
are scraped off privacy pages. A state registry is none of those things. Data
brokers operating in California are *required by law* to register annually and to
publish a primary contact email address, and that address is a statutory point of
contact rather than a mailbox somebody happened to leave on a web page.

So the provenance here is the strongest available:

    ca_data_broker_registry  >  privacy_policy  >  derived_from_optery_slug

Four files, four different shapes, because the form changed every year:

    registry.csv                      2026 registrations (CPPA)
    registry2025.csv                  2025, with a spacer row above the header
    registry2024.csv                  2024, with a leading "Completion time"
    complete-reg-data-brokers.csv     2020-2023, administered by the CA DOJ, and
                                      the only one that obfuscates addresses as
                                      "privacy [at] example.com"

Deregistration is a signal, not a deletion. A broker that registered in 2024 and
not in 2026 may have been acquired, wound up, or simply not filed -- and the
third case is the interesting one, because the obligation did not go away. So
every year a broker appears in is recorded, and nobody is dropped for being
absent from the newest file.

Nothing is written unless you pass --apply.

    ./import_state_registries.py --fetch          # download the CSVs
    ./import_state_registries.py                  # propose
    ./import_state_registries.py --apply          # write to curated_brokers.json
"""

import argparse
import csv
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGDIR = ROOT / "data" / "registries"
CURATED = ROOT / "data" / "curated_brokers.json"
REGISTRY = ROOT / "data" / "brokers.json"

BASE = "https://cppa.ca.gov/data_broker_registry/"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")

# (filename, year label, rows to skip before the header, column names)
SOURCES = [
    ("registry.csv", "2026", 0, {
        "name": "Data broker name:", "dba": "Doing Business As (DBA), if applicable:",
        "site": "Data broker primary website:",
        "email": "Data broker primary contact email address:"}),
    ("registry2025.csv", "2025", 1, {
        "name": "Data broker\xa0name:", "dba": "Doing Business As (DBA), if applicable:",
        "site": "Data broker primary website:",
        "email": "Data broker primary contact email address:"}),
    ("registry2024.csv", "2024", 0, {
        "name": "Business name", "dba": "Doing Business As (DBA), if applicable [optional]",
        "site": "Business primary website",
        "email": "Business primary contact email address"}),
    ("complete-reg-data-brokers.csv", "2020-2023", 0, {
        "name": "Data Broker Name", "dba": None,
        "site": "Website URL", "email": "Email Address"}),
]

# Corporate suffixes to drop when turning a legal entity name into an id.
SUFFIX = re.compile(
    r"[,\s]+(inc|llc|l\.l\.c|ltd|limited|corp|corporation|co|company|lp|llp|plc|"
    r"pbc|gmbh|holdings|group|usa|us)\.?$", re.I)


def deobfuscate(addr):
    """`privacy [at] VDX.tv` -> `privacy@vdx.tv`.

    Only the 2020-2023 DOJ file does this, and it does it inconsistently. An
    address that still has no @ after unmasking is not an address; returning it
    anyway would put a non-deliverable string in the email_to field, which is
    worse than an empty one because empty is visibly missing."""
    if not addr:
        return ""
    a = addr.strip()
    a = re.sub(r"\s*[\[\(]\s*at\s*[\]\)]\s*", "@", a, flags=re.I)
    a = re.sub(r"\s*[\[\(]\s*dot\s*[\]\)]\s*", ".", a, flags=re.I)
    a = a.replace(" ", "")
    if "@" not in a or "." not in a.split("@")[-1]:
        return ""
    return a.lower().strip(".,;")


def domain_of(url):
    """Registry websites are typed by hand into a form, so expect anything:
    bare hosts, missing schemes, trailing paths, stray whitespace, uppercase."""
    if not url:
        return ""
    u = url.strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = u.split("/")[0].split("?")[0].strip()
    if not re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", u or ""):
        return ""
    return u


def slug_of(name):
    n = SUFFIX.sub("", (name or "").strip())
    n = SUFFIX.sub("", n)          # "Foo Data Corp, Inc." has two
    n = re.sub(r"[^a-z0-9]+", "_", n.lower()).strip("_")
    return n[:60]


def norm_name(name):
    """For matching only. Aggressive on purpose: a company files as
    'Exponential Interactive, Inc. doing business as VDX.tv' one year and
    'VDX.tv' the next."""
    n = SUFFIX.sub("", (name or "").lower())
    n = re.sub(r"\bdoing business as\b|\bd/?b/?a\b", " ", n)
    # "BeenVerified, Inc. and its subsidiaries and affiliates" is BeenVerified.
    # Registrants often scope the filing to a corporate family in the name field
    # itself, and without stripping it the company is imported as a stranger --
    # twice over, since the Inc and LLC entities each file their own version.
    n = re.sub(r"\s*(,|and)?\s*its\s+(subsidiaries|affiliates)"
               r"(\s+and\s+(subsidiaries|affiliates))?\s*$", " ", n)
    n = re.sub(r"\s*(,|and)\s+(subsidiaries|affiliates)\s*$", " ", n)
    # Companies file under their trading name with the TLD attached one year
    # ("AgedLeadStore.com") and without it the next ("Aged Lead Store"). Without
    # stripping it the two are different keys and the broker is imported twice,
    # once as a duplicate of a record already being worked.
    n = re.sub(r"\.(com|net|org|io|ai|co|us|inc)$", "", n.strip())
    n = re.sub(r"[^a-z0-9]", "", n)
    return re.sub(r"(com|net|org)$", "", n) if len(n) > 8 else n


def fetch():
    REGDIR.mkdir(parents=True, exist_ok=True)
    for fn, *_ in SOURCES:
        req = urllib.request.Request(BASE + fn, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=90) as r:
            (REGDIR / fn).write_bytes(r.read())
        print(f"  fetched {fn} ({(REGDIR / fn).stat().st_size:,} bytes)", file=sys.stderr)


def load():
    """Every registrant across every year, keyed by domain where there is one and
    by normalised name where there is not. Newest year wins on conflicting
    fields, because a 2020 contact address has had six years to rot."""
    out = {}
    for fn, year, skip, cols in SOURCES:
        path = REGDIR / fn
        if not path.exists():
            print(f"  missing {fn} -- run with --fetch", file=sys.stderr)
            continue
        with path.open(encoding="utf-8-sig", newline="") as fh:
            rows = list(csv.reader(fh))
        rows = rows[skip:]
        header = [c.strip() for c in rows[0]]
        idx = {}
        for key, label in cols.items():
            if label is None:
                continue
            want = label.replace("\xa0", " ").strip()
            for i, h in enumerate(header):
                if h.replace("\xa0", " ").strip() == want:
                    idx[key] = i
                    break
        if "name" not in idx:
            print(f"  {fn}: could not find the name column -- skipped", file=sys.stderr)
            continue
        for row in rows[1:]:
            if len(row) <= idx["name"]:
                continue
            name = (row[idx["name"]] or "").strip()
            if not name:
                continue
            dba = (row[idx["dba"]] or "").strip() if "dba" in idx and len(row) > idx["dba"] else ""
            site = row[idx["site"]] if "site" in idx and len(row) > idx["site"] else ""
            email = row[idx["email"]] if "email" in idx and len(row) > idx["email"] else ""
            dom = domain_of(site)
            key = dom or norm_name(dba or name)
            if not key:
                continue
            rec = out.setdefault(key, {"years": set(), "name": name, "dba": dba,
                                       "domain": dom, "email": ""})
            rec["years"].add(year)
            # Newest file is processed first, so only fill blanks afterwards.
            for field, val in (("name", name), ("dba", dba), ("domain", dom),
                               ("email", deobfuscate(email))):
                if val and not rec.get(field):
                    rec[field] = val
    return out


def families(regs):
    """Registrants grouped by the domain of their statutory contact address.

    This is the part of the registry nobody uses, and it is worth more than the
    broker list itself. Corporate families are invisible from the outside -- the
    whole difficulty of the sibling problem is that four brands can share one
    index and nothing on the sites says so. But a data broker filing with the
    state has to name a contact, and the family files under one.

    BeenVerified, Inc. registered with `privacy@moneybot5000.com`. Nothing on
    either site connects them. The filing does, in a legal document.

    Two further tells in the same field:

      * the name field is often a brand list. "Private Reports, Mugshot Look,
        Public Searcher" is one registrant naming three properties, and
        "Checksecrets, PeopleSearchUSA, inmate searcher, Sealed Records" is four.
        Splitting it surfaces brands no list contains.
      * the website field is sometimes several sites crammed into one cell
        ("weinform.org--www.truthrecord.org"), for the same reason.

    Stronger evidence than a shared nameserver or a shared Zendesk counter,
    because it is a sworn filing rather than an inference."""
    fam = {}
    for r in regs.values():
        if not r["email"]:
            continue
        host = r["email"].split("@")[-1].lower()
        fam.setdefault(host, []).append({
            "name": r["name"], "dba": r["dba"], "domain": r["domain"],
            "years": sorted(r["years"]), "email": r["email"]})
    return {h: v for h, v in fam.items() if len(v) > 1}


BRAND_SPLIT = re.compile(r"\s*[;,]\s*|\s+dba\s+|\s+d/b/a\s+", re.I)


def brands(regs):
    """Brand names pulled out of multi-brand registrant names and website cells."""
    out = set()
    for r in regs.values():
        for field in (r["name"], r["dba"]):
            if not field or len(BRAND_SPLIT.split(field)) < 2:
                continue
            for part in BRAND_SPLIT.split(field):
                part = SUFFIX.sub("", part.strip()).strip()
                if 2 < len(part) < 40 and not re.fullmatch(r"(inc|llc|and its.*)", part, re.I):
                    out.add(part)
        for sep in ("--", " and ", "|"):
            if r["domain"] and sep in r["domain"]:
                for part in r["domain"].split(sep):
                    d = domain_of(part)
                    if d:
                        out.add(d)
    return sorted(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fetch", action="store_true", help="download the CSVs first")
    ap.add_argument("--apply", action="store_true", help="write to curated_brokers.json")
    ap.add_argument("--limit", type=int, default=0, help="cap new additions (0 = no cap)")
    ap.add_argument("--families", action="store_true",
                    help="write data/broker_families.json and stop")
    args = ap.parse_args()

    if args.fetch:
        fetch()

    regs = load()
    print(f"{len(regs)} distinct registrants across all years", file=sys.stderr)

    if args.families:
        fam = families(regs)
        out = {"_source": "California data broker registry, grouped by the domain "
                          "of each registrant's statutory contact address",
               "families": fam, "brands_named_in_filings": brands(regs)}
        (ROOT / "data" / "broker_families.json").write_text(
            json.dumps(out, indent=2, ensure_ascii=False) + "\n")
        print(f"{len(fam)} families covering {sum(len(v) for v in fam.values())} "
              f"filings; {len(out['brands_named_in_filings'])} brand names pulled "
              f"out of registrant names", file=sys.stderr)
        return 0

    brokers = json.loads(REGISTRY.read_text())["brokers"]
    by_domain = {(b.get("domain") or "").lower(): b for b in brokers if b.get("domain")}
    by_name = {norm_name(b.get("name")): b for b in brokers if b.get("name")}

    new, upgrade, matched = [], [], 0
    for key, r in sorted(regs.items()):
        existing = by_domain.get(r["domain"]) or by_name.get(norm_name(r["dba"] or r["name"]))
        if existing:
            matched += 1
            # A statutory contact address outranks a scraped one. Only propose
            # the swap when we actually have an address to swap in.
            if r["email"] and (existing.get("email_to") or "").lower() != r["email"]:
                upgrade.append((existing["id"], existing.get("email_to") or "-", r))
        else:
            new.append((slug_of(r["dba"] or r["name"]), r))

    print(f"  already known: {matched}")
    print(f"  new brokers:   {len(new)}")
    print(f"  email upgrades to known brokers: {len(upgrade)}")
    withmail = sum(1 for _, r in new if r["email"])
    print(f"  of the new ones, {withmail} come with a statutory contact address")

    for i, (sid, r) in enumerate(new[:25]):
        print(f"    NEW  {sid:34} {r['domain'] or '(no domain)':32} {r['email'] or '-'}")
    if len(new) > 25:
        print(f"    ... and {len(new) - 25} more")

    if not args.apply:
        print("\n(dry run - pass --apply to write these to data/curated_brokers.json)")
        return 0

    d = json.loads(CURATED.read_text())
    # Guard against the whole registry, not just the curated file. Most broker
    # ids live only in the generated registry, and colliding with one of those
    # would silently create a second entry for a broker already being worked --
    # which then gets its own letter, its own status, and its own confusion.
    have = {b["id"] for b in d["brokers"]} | {b["id"] for b in brokers}
    by_id = {b["id"]: b for b in d["brokers"]}
    added = changed = 0

    pool = new[: args.limit] if args.limit else new
    for sid, r in pool:
        if not sid or sid in have:
            continue
        d["brokers"].append({
            "id": sid,
            "name": r["dba"] or r["name"],
            "domain": r["domain"],
            "priority": 2,
            "method": "email" if r["email"] else "unknown",
            "optout_url": "",
            "needs_email_confirm": None,
            "source": "ca_data_broker_registry",
            "optery_slug": None,
            "email_to": r["email"] or None,
            "email_verified": bool(r["email"]),
            "email_verified_by": "ca_data_broker_registry" if r["email"] else None,
            "registry_years": sorted(r["years"]),
            "legal_name": r["name"] if r["dba"] else None,
        })
        have.add(sid)
        added += 1

    for bid, old, r in upgrade:
        b = by_id.get(bid)
        if not b:
            continue
        b["email_alt"] = old if old != "-" else b.get("email_alt")
        b["email_to"] = r["email"]
        b["email_verified"] = True
        b["email_verified_by"] = "ca_data_broker_registry"
        b["registry_years"] = sorted(r["years"])
        changed += 1

    CURATED.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    print(f"\nadded {added} broker(s), upgraded {changed} address(es)"
          f" - now run scripts/build_registry.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
