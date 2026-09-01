#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Pull the parts of the California register that are not an address.

For a long time this project treated `data/registries/*.csv` as a source of two
things: a company name and an email address. It is not. Every registrant answers
a questionnaire under a filing obligation, and the answers are far more useful
than the contact details:

  * whether they collect **minors' data**, **precise geolocation**, or
    **reproductive health care data** -- three of the sharpest categories there
    are, self-declared;
  * whether they claim **FCRA / GLBA / IIPPA / CMIA / HIPAA** regulation, and for
    each one, *the types of personal information*, *the specific products*, and
    *the approximate proportion of their business* it covers -- which is the
    activity-scoping argument in the registrant's own words, filed in advance of
    any deflection they later send me;
  * **request metrics** for the prior year: how many deletion, know, know-sold,
    opt-out and limit-sensitive requests they received, how many they complied
    with in whole, in part, and **denied**, plus median and mean days to respond;
  * a free-text description of their data collection practices.

WINR Data and Online Media Group were the rows that forced this. Both were sitting
in a "blank site, nothing to write about" bucket. WINR's free text described the
whole business -- prize draws and coupon sites feeding fintech identity resolution
-- and Online Media Group's DBA field named MixRank, a product a dead domain had
hidden. The letters wrote themselves once the filing was read. See
`_SILENT_FAILURES.md` §239.

Usage:
    python3 scripts/register_profile.py            # build data/register_profiles.json
    python3 scripts/register_profile.py --report   # and print what it found
    python3 scripts/register_profile.py --show ID  # one broker's filing
"""

import csv
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "register_profiles.json")
CURATED = os.path.join(ROOT, "data", "curated_brokers.json")

# The 2025 file has a junk first row and the real header on row 2; the 2024 file
# has its header on row 1. Both are keyed by position, not by name, because the
# header text differs between years and is riddled with non-breaking spaces.
LAYOUTS = {
    "registry2025.csv": {
        "header_row": 1,
        "name": 0, "dba": 1, "site": 2, "email": 3,
        "minors": 11, "geo": 12, "repro": 13, "rights_url": 14,
        "regimes": {
            "FCRA": (15, 16, 17, 18), "GLBA": (19, 20, 21, 22),
            "IIPPA": (23, 24, 25, 26), "CMIA": (27, 28, 29, 30),
            "HIPAA": (31, 32, 33, 34),
        },
        # (received, whole, part, denied, median_days, mean_days)
        "metrics": {
            "delete": (35, 36, 37, 38, 39, 40),
            "know": (41, 42, 43, 44, 45, 46),
            "know_sold_shared": (47, 48, 49, 50, 51, 52),
            "opt_out": (53, 54, 55, 56, 57, 58),
            "limit_sensitive": (59, 60, 61, 62, 63, 64),
        },
        "notes_metrics": 65, "notes_practices": 66,
    },
    "registry2024.csv": {
        "header_row": 0,
        "name": 1, "dba": 2, "site": 3, "email": 4,
        "minors": 12, "geo": 13, "repro": 14, "rights_url": 15,
        "regimes": {
            "FCRA": (16, 17), "GLBA": (18, 19), "IIPPA": (20, 21),
            "CMIA": (22, 23), "HIPAA": (24, 25),
        },
        "metrics": {},
        "notes_metrics": None, "notes_practices": 26,
    },
}


def _clean(s):
    if s is None:
        return ""
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()


def _yes(s):
    return _clean(s).lower().startswith("y")


def _num(s):
    s = _clean(s).replace(",", "")
    if re.fullmatch(r"-?\d+(\.\d+)?", s):
        return float(s) if "." in s else int(s)
    return None


def _get(row, i):
    return _clean(row[i]) if i is not None and i < len(row) else ""


def _slug(s):
    """Loose key for matching a filing to a curated row."""
    s = _clean(s).lower()
    s = re.sub(r"\b(inc|llc|ltd|corp|corporation|company|co|gmbh|bv|b\.v|"
               r"pty|plc|lp|llp|holdings|group|the)\b", " ", s)
    return re.sub(r"[^a-z0-9]", "", s)


def _domain(url):
    d = _clean(url).lower()
    d = re.sub(r"^https?://", "", d)
    d = d.split("/")[0].split(";")[0].split(",")[0].strip()
    return re.sub(r"^www\.", "", d)


def parse_file(path, layout):
    rows = list(csv.reader(io.open(path, encoding="utf-8-sig", errors="replace")))
    out = []
    for row in rows[layout["header_row"] + 1:]:
        name = _get(row, layout["name"])
        if not name:
            continue
        rec = {
            "name": name,
            "dba": _get(row, layout["dba"]),
            "site": _get(row, layout["site"]),
            "email": _get(row, layout["email"]),
            "rights_url": _get(row, layout["rights_url"]),
            "collects": {
                "minors": _yes(_get(row, layout["minors"])),
                "precise_geolocation": _yes(_get(row, layout["geo"])),
                "reproductive_health": _yes(_get(row, layout["repro"])),
            },
            "regimes": {},
            "metrics": {},
            "notes_practices": _get(row, layout["notes_practices"]),
            "notes_metrics": _get(row, layout["notes_metrics"]),
        }
        for regime, cols in layout["regimes"].items():
            if not _yes(_get(row, cols[0])):
                continue
            if len(cols) == 4:
                rec["regimes"][regime] = {
                    "info_types": _get(row, cols[1]),
                    "products": _get(row, cols[2]),
                    "proportion": _get(row, cols[3]),
                }
            else:
                rec["regimes"][regime] = {"extent": _get(row, cols[1])}
        for kind, cols in layout["metrics"].items():
            vals = [_num(_get(row, c)) for c in cols]
            if any(v for v in vals):
                rec["metrics"][kind] = dict(zip(
                    ("received", "whole", "part", "denied",
                     "median_days", "mean_days"), vals))
        out.append(rec)
    return out


def build():
    profiles = {}
    for fname, layout in LAYOUTS.items():
        path = os.path.join(ROOT, "data", "registries", fname)
        if not os.path.exists(path):
            continue
        year = re.search(r"(\d{4})", fname).group(1)
        for rec in parse_file(path, layout):
            rec["year"] = year
            profiles.setdefault(_slug(rec["name"]), []).append(rec)

    curated = json.loads(io.open(CURATED, encoding="utf-8").read())
    rows = curated["brokers"] if isinstance(curated, dict) else curated

    by_domain, by_slug = {}, {}
    for key, recs in profiles.items():
        by_slug[key] = recs
        for r in recs:
            d = _domain(r["site"])
            if d:
                by_domain.setdefault(d, recs)

    matched, out = 0, {}
    for r in rows:
        recs = by_domain.get((r.get("domain") or "").lower())
        if not recs:
            for cand in (r.get("legal_name"), r.get("name")):
                if cand and _slug(cand) in by_slug:
                    recs = by_slug[_slug(cand)]
                    break
        if not recs:
            continue
        matched += 1
        # newest filing first -- the older ones are kept, because the 2024 form
        # asked for a free-text "extent" the 2025 form replaced with three
        # structured fields, and the prose is often more useful than the fields.
        out[r["id"]] = sorted(recs, key=lambda x: x["year"], reverse=True)

    with io.open(OUT, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    return out, matched, len(rows)


def report(profiles):
    def flag(key):
        return [bid for bid, recs in profiles.items()
                if any(r["collects"][key] for r in recs)]

    print("=== self-declared collection ===")
    for key, label in (("minors", "minors' personal information"),
                       ("precise_geolocation", "precise geolocation"),
                       ("reproductive_health", "reproductive health care data")):
        ids = sorted(flag(key))
        print("  %-32s %3d  %s" % (label, len(ids), ", ".join(ids[:8])))

    print("\n=== claimed regulation (with self-stated scope) ===")
    counts = {}
    for recs in profiles.values():
        for r in recs:
            for regime in r["regimes"]:
                counts[regime] = counts.get(regime, 0) + 1
    for regime, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print("  %-6s %3d filings" % (regime, n))

    # A metrics row is only evidence if it is arithmetically possible. Registrants
    # routinely paste the same total into every box -- Giant Partners filed 19,343
    # received / 19,343 complied IN WHOLE / 19,343 DENIED, which cannot all be
    # true. Sorting by denial rate without this check produces a dramatic and
    # entirely false list of brokers that "deny every request". See §239.
    def consistent(m):
        rec = m.get("received") or 0
        if rec <= 0:
            return False
        n = lambda k: m.get(k) or 0
        # Two readings of the form are both common and both coherent. Some
        # registrants treat whole/part/denied as a partition of the total; others
        # treat "complied in part" as a restatement of the same requests counted
        # under "in whole", so only whole+denied should sum to the total. Accept
        # either. Reject only a row that fails both -- those are the ones where
        # the same figure was pasted into every box.
        return (n("whole") + n("part") + n("denied") <= rec
                or n("whole") + n("denied") <= rec)

    print("\n=== deletion requests denied (arithmetically coherent filings only) ===")
    hard, incoherent = [], []
    for bid, recs in profiles.items():
        for r in recs:
            m = r["metrics"].get("delete")
            if not m or not m.get("received"):
                continue
            if not consistent(m):
                incoherent.append((bid, r["year"], m))
                continue
            denied, rec = m.get("denied") or 0, m["received"]
            if denied and denied / rec >= 0.25:
                hard.append((denied / rec, bid, denied, rec, r["year"]))
    for rate, bid, denied, rec, year in sorted(hard, reverse=True)[:20]:
        print("  %-28s %5d/%-6d denied (%3.0f%%) in %s" %
              (bid, denied, rec, rate * 100, year))
    if not hard:
        print("  (none at or above 25%)")

    print("\n=== filings whose own numbers do not add up (%d) ===" % len(incoherent))
    print("  Treat these as unusable, NOT as denials. compliance totals exceed the")
    print("  number of requests received, so the boxes were filled with one figure.")
    for bid, year, m in incoherent[:8]:
        print("    %-28s recv %s | whole %s | part %s | denied %s (%s)" %
              (bid, m.get("received"), m.get("whole"), m.get("part"),
               m.get("denied"), year))

    print("\n=== slowest substantive response to a deletion request ===")
    print("  (read notes_metrics before relying on any of these -- several are")
    print("   explained in the filing itself, e.g. a platform migration)")
    slow = []
    for bid, recs in profiles.items():
        for r in recs:
            m = r["metrics"].get("delete")
            if m and (m.get("mean_days") or 0) > 45:
                slow.append((m["mean_days"], bid, r["year"],
                             bool(r["notes_metrics"])))
    for days, bid, year, noted in sorted(slow, reverse=True)[:15]:
        print("  %-28s mean %s days in %s%s" %
              (bid, days, year, "  [explained in filing]" if noted else ""))
    if not slow:
        print("  (none above the 45-day statutory window)")

    # OPT-OUT DENIALS are a different animal from deletion or access denials, and
    # worth their own pass. An opt-out of sale or sharing is not a verifiable
    # consumer request: the regulations bar requiring a consumer to verify identity
    # as a condition of honouring one, because demanding proof of identity in order
    # to stop a sale would defeat the right. A business may still deny where it has
    # a good-faith, documented belief the request is fraudulent, and may require
    # proof of authorisation from an agent -- so a high rate is a QUESTION, not a
    # verdict. The notes field usually says which. See §242.
    print("\n=== opt-out requests denied (>=50%, coherent filings) ===")
    print("  An opt-out needs no identity verification. A high rate is a question;")
    print("  read the notes column before drawing any conclusion.")
    oo = []
    for bid, recs in profiles.items():
        for r in recs:
            m = r["metrics"].get("opt_out")
            if not m or not consistent(m):
                continue
            rec, den = m["received"], m.get("denied") or 0
            if den and den / rec >= 0.5:
                oo.append((den / rec, den, rec, bid, r["year"],
                           r.get("notes_metrics") or ""))
    for rate, den, rec, bid, year, note in sorted(oo, reverse=True):
        print("  %-28s %5d/%-6d (%3.0f%%) %s" % (bid, den, rec, rate * 100, year))
        if note:
            print("      %s" % note[:160])
    if not oo:
        print("  (none)")

    # SCOPING AND DISCLAIMING STATEMENTS. The free-text box is where a registrant
    # says which part of itself the filing is about, or denies collecting the thing
    # you are about to ask after. Growbots' 2024 filing says it collects "names, job
    # titles, and corporate email addresses" and "do not collect or process personal
    # email addresses (e.g., @gmail.com)" -- which is precisely what Hunter told me
    # only after two rounds of correspondence, and it was published two years
    # earlier. T-Mobile names the one division that made its registration necessary,
    # twice. Reading this before writing scopes the letter and picks the key. See
    # §250.
    _SCOPE_PAT = re.compile(
        r"(only division|line of business|the only part|only the \S+ (?:division|"
        r"business|unit)|do(?:es)? not (?:sell|collect|compile|maintain|process)|"
        r"we are a (?:business-to-business )?service provider|not collect .{0,40}"
        r"directly)", re.I)

    print("\n=== registrants whose free text scopes or disclaims the business ===")
    print("  Read these BEFORE writing. They say which division the filing covers,")
    print("  or deny holding the identifier class you were about to search on.")
    scoped = []
    for bid, recs in profiles.items():
        for r in recs:
            txt = r.get("notes_practices") or ""
            if len(txt) > 80 and _SCOPE_PAT.search(txt):
                scoped.append((bid, r["year"], re.sub(r"\s+", " ", txt)))
                break
    for bid, year, txt in sorted(scoped):
        print("  %-30s (%s) %s" % (bid, year, txt[:150]))
    print("  -- %d registrants" % len(scoped))

    prose = [bid for bid, recs in profiles.items()
             if any(len(r["notes_practices"]) > 120 for r in recs)]
    print("\n=== %d brokers wrote a substantive free-text description ===" % len(prose))
    print("  read one with: scripts/register_profile.py --show <id>")


def show(profiles, bid):
    recs = profiles.get(bid)
    if not recs:
        print("no register filing on record for %r" % bid)
        return 1
    for r in recs:
        print("=" * 72)
        print("%s  (%s filing)" % (r["name"], r["year"]))
        if r["dba"]:
            print("  DBA: %s" % r["dba"])
        print("  site: %s | email: %s" % (r["site"], r["email"]))
        if r["rights_url"]:
            print("  rights: %s" % r["rights_url"])
        on = [k for k, v in r["collects"].items() if v]
        print("  collects: %s" % (", ".join(on) if on else "(none declared)"))
        for regime, d in r["regimes"].items():
            print("  -- %s --" % regime)
            for k, v in d.items():
                if v:
                    print("     %s: %s" % (k, v))
        for kind, m in r["metrics"].items():
            print("  %-18s recv %s | whole %s | part %s | denied %s | mean %s d"
                  % (kind, m.get("received"), m.get("whole"), m.get("part"),
                     m.get("denied"), m.get("mean_days")))
        if r["notes_practices"]:
            print("  PRACTICES: %s" % r["notes_practices"])
        if r["notes_metrics"]:
            print("  METRICS NOTE: %s" % r["notes_metrics"])
    return 0


def main():
    args = sys.argv[1:]
    profiles, matched, total = build()
    print("%d register filings attached to %d of %d curated brokers -> %s"
          % (sum(len(v) for v in profiles.values()), matched, total,
             os.path.relpath(OUT, ROOT)))
    if "--show" in args:
        return show(profiles, args[args.index("--show") + 1])
    if "--report" in args:
        report(profiles)
    return 0


if __name__ == "__main__":
    sys.exit(main())
