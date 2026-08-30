#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Merge the hand-curated broker definitions with the scraped Optery directory
into a single data/brokers.json registry.

Curated entries win on every field. Optery-only entries land as priority-1
stubs with no opt-out URL yet, ready for enrichment.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURATED = ROOT / "data" / "curated_brokers.json"
SLUGS = ROOT / "data" / "optery_slugs.txt"
DOMAINS = ROOT / "data" / "optery_domain_candidates.json"
OUT = ROOT / "data" / "brokers.json"

# Optery slugs carry trailing disambiguators like "-2" and corporate suffixes.
SUFFIXES = re.compile(
    r"[-\s](llc|inc|ltd|limited|corp|corporation|gmbh|bv|b-v|sa|s-a|plc|co|"
    r"pty|ag|nv|n-v|spolka-akcyjna|t-a)$", re.I)


def slug_to_name(slug: str) -> str:
    s = re.sub(r"-\d+$", "", slug)          # drop "-2" style disambiguators
    return " ".join(w.capitalize() for w in s.split("-"))


def canonical_id(slug: str) -> str:
    s = re.sub(r"-\d+$", "", slug)
    s = SUFFIXES.sub("", s)
    return s.replace("-", "_")


def main():
    curated = json.loads(CURATED.read_text())["brokers"]
    by_id = {}
    # Index curated by id and by domain stem so Optery slugs dedupe against them.
    aliases = {}
    for b in curated:
        b.setdefault("source", "curated")
        by_id[b["id"]] = b
        aliases[b["id"]] = b["id"]
        stem = b["domain"].split(".")[0].replace("-", "_")
        aliases[stem] = b["id"]

    # Optery rows arrive as a slug and nothing else. scripts/resolve_optery_domains.py
    # derives a domain and verifies it (resolves + the site names the business);
    # only its confirmed verdicts are trusted here. Without this every Optery row
    # is permanently unroutable -- see that script's docstring.
    derived: dict[str, str] = {}
    if DOMAINS.exists():
        for slug, rec in json.loads(DOMAINS.read_text()).items():
            if rec.get("verdict") in ("CONFIRMED", "CONFIRMED_BY_SLUG") and rec.get("domain"):
                derived[slug] = rec["domain"]

    added = 0
    if SLUGS.exists():
        for line in SLUGS.read_text().splitlines():
            slug = line.strip().strip("/")
            # The slug file is scraped from a sitemap, so stray markup can survive
            # the extraction. "</loc>" reached the registry as a broker named
            # "</loc>" with no domain and no route -- a permanently pending row
            # that no pass could ever action. Reject anything that is not a
            # plausible slug rather than only the two known-bad values.
            if not slug or slug == "data-brokers":
                continue
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
                continue
            cid = canonical_id(slug)
            if cid in aliases or cid in by_id:
                # Already covered by a curated entry; just record the Optery slug.
                existing = by_id[aliases.get(cid, cid)]
                existing.setdefault("optery_slug", slug)
                # A curated row with no domain still benefits from a derived one,
                # but never overwrite a curated value with a guess.
                if not existing.get("domain") and slug in derived:
                    existing["domain"] = derived[slug]
                    existing["domain_source"] = "derived_from_optery_slug"
                continue
            by_id[cid] = {
                "id": cid,
                "name": slug_to_name(slug),
                "domain": derived.get(slug, ""),
                **({"domain_source": "derived_from_optery_slug"}
                   if slug in derived else {}),
                "priority": 1,
                "method": "unknown",
                "optout_url": "",
                "needs_email_confirm": None,
                "source": "optery",
                "optery_slug": slug,
                "optery_url": f"https://www.optery.com/data-brokers/{slug}/",
            }
            added += 1

    # ROUTE EVIDENCE: how strongly do we actually know this address works?
    #
    # `email_verified` was doing two jobs and hiding the difference. 613 rows
    # carry email_verified_by="ca_data_broker_registry", which means only that a
    # company FILED this address on a state register -- a one-time attestation
    # nobody revisits, which rots (_SILENT_FAILURES 173). 129 rows carry
    # "delivery_evidence", which means a message actually arrived. Both showed as
    # `verified: true`, so the flag read the same for an address proven to work
    # and an address proven only to have been typed into a form once.
    #
    # PureCars made the gap concrete: its registered contact autoresponds that it
    # "is not being monitored" (205). Filed, and unreachable, simultaneously.
    #
    # So this derives a tier rather than a boolean, in the GENERATED file only --
    # the source keeps the raw basis and this stays computed, so there is one
    # place to change the mapping.
    #
    #   replied    a human at the company answered -- the route demonstrably works
    #   delivered  a message arrived, or an autoresponder fired
    #   published  the company published the address itself (policy page)
    #   filed      it appears on a register and nothing more
    #   none       no evidence at all
    EVIDENCE_TIER = {
        "broker_reply": "replied",
        "delivery_evidence": "delivered",
        "broker_autoresponder": "delivered",
        "privacy_policy": "published",
        "published_policy": "published",
        "ca_data_broker_registry": "filed",
    }
    for b in by_id.values():
        if not b.get("email_to"):
            b["route_evidence"] = "none"
        elif not b.get("email_verified"):
            b["route_evidence"] = "none"
        else:
            by = (b.get("email_verified_by") or "").strip()
            b["route_evidence"] = EVIDENCE_TIER.get(by, "published" if by else "none")

    brokers = sorted(by_id.values(), key=lambda b: (-b.get("priority", 0), b["id"]))
    OUT.write_text(json.dumps(
        {"_comment": "Generated by scripts/build_registry.py - do not hand-edit; "
                     "edit data/curated_brokers.json instead.",
         "count": len(brokers),
         "brokers": brokers}, indent=2) + "\n")
    import collections
    tiers = collections.Counter(b.get("route_evidence") for b in brokers)
    print(f"wrote {OUT} : {len(brokers)} brokers "
          f"({len(curated)} curated, {added} from Optery)")
    print("  route evidence: " + ", ".join(
        f"{tiers[k]} {k}" for k in ("replied", "delivered", "published", "filed", "none")
        if tiers.get(k)))


if __name__ == "__main__":
    main()
