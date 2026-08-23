#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Generate brokers/_FAMILIES.md from the state registration filings.

Why this is its own document: the single most useful thing you can know before
writing to a data broker is whether it is one brand of several sharing an index.
It changes the letter (name the siblings), it changes how you read the reply (a
confirmation naming one hostname is not a confirmation), and it changes the
arithmetic (one exchange can cover five sites).

That relationship is close to invisible from outside. It is not invisible in a
regulatory filing, because a corporate family registers under one contact
address. See _SILENT_FAILURES.md #78 for how this was found.

Regenerate with:
    ./import_state_registries.py --fetch --families
    ./build_families_doc.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
from paths import state, outbox  # noqa: E402
FAM = ROOT / "data" / "broker_families.json"
REG = ROOT / "data" / "brokers.json"
OUT = ROOT / "brokers" / "_FAMILIES.md"
STATUS = state("removal_status.json")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def main():
    fam = json.loads(FAM.read_text())
    brokers = json.loads(REG.read_text())["brokers"]
    try:
        st = json.loads(STATUS.read_text())
        st = st.get("brokers", st)
    except FileNotFoundError:
        st = {}

    by_dom = {(b.get("domain") or "").lower(): b for b in brokers if b.get("domain")}
    by_name = {norm(b.get("name")): b for b in brokers if b.get("name")}

    groups = fam["families"]
    ordered = sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    total_filings = sum(len(v) for v in groups.values())

    L = []
    A = L.append
    A("# Corporate families, from the state registration filings")
    A("")
    A("**One company, several brands, one index — declared in a legal document.**")
    A("")
    A("Before writing to any broker on this list, check whether it belongs to a")
    A("family. It changes three things:")
    A("")
    A("1. **The letter.** Name the siblings and ask for one answer covering all of")
    A("   them. One exchange can close five sites.")
    A("2. **How you read the reply.** A confirmation naming a single hostname, from")
    A("   a company that runs four, is not a confirmation — see")
    A("   `_SILENT_FAILURES.md` §40 and §70.")
    A("3. **What a negative means.** \"We hold no record\" from one brand says")
    A("   nothing about the shared index behind it.")
    A("")
    A("## Where this comes from, and why it is stronger than the usual evidence")
    A("")
    A("Data brokers operating in California must register annually and publish a")
    A("primary contact email address. A corporate family files under **one**")
    A("address. Grouping registrants by the domain of that address therefore")
    A("recovers the family structure directly, from a sworn filing rather than an")
    A("inference.")
    A("")
    A("Compare the alternatives this project used before finding it:")
    A("")
    A("| Evidence | Strength | Problem |")
    A("|---|---|---|")
    A("| Shared Cloudflare nameserver pair | Suggestive | Shared hosting is common and proves nothing on its own |")
    A("| Byte-identical opt-out template | Strong | Vendors sell templates; two firms can buy the same one |")
    A("| Sequential Zendesk ticket IDs across brands | Near-conclusive | Only observable after you have filed with all of them |")
    A("| **Shared statutory contact address** | **Conclusive** | Only covers brokers with a California nexus |")
    A("")
    A("The last one is also the only one available **before** you write, which is")
    A("the whole point.")
    A("")
    A("### The find that made the case")
    A("")
    A("> **BeenVerified, Inc. registered using `privacy@moneybot5000.com`.**")
    A("")
    A("Nothing on either website connects them. This project had been")
    A("corresponding with MoneyBot5000 for days as an unrelated broker.")
    A("")
    A("### Two more tells in the same filings")
    A("")
    A("**The name field is often a brand list.** Registrants put their whole")
    A("portfolio in it — *\"Private Reports, Mugshot Look, Public Searcher\"* is one")
    A("registrant naming three properties. **The website field does it too**:")
    A("`weinform.org--www.truthrecord.org` is two sites in one cell. Splitting both")
    A(f"yielded {len(fam.get('brands_named_in_filings', []))} brand names, held as leads in")
    A("`data/broker_leads.json` until each has a domain and a route.")
    A("")
    A("### Caveats, stated plainly")
    A("")
    A("- **A shared contact address proves a shared filer, not a shared database.**")
    A("  A parent may file for subsidiaries that run genuinely separate systems. Ask")
    A("  rather than assert: *\"if these share an index, please confirm the removal")
    A("  covers all of them; if they are separate, say so and I will file")
    A("  separately.\"* Both answers are useful and only silence is not.")
    A("- **Absence proves nothing.** A broker with no California nexus never files.")
    A("  Vermont, Texas and Oregon run their own registries and are not yet mined.")
    A("- **Deregistration is a signal, not a deletion.** A registrant present in")
    A("  2024 and absent in 2026 may have been acquired, wound up, or simply not")
    A("  filed — and the obligation did not lapse with the paperwork.")
    A("")
    A("---")
    A("")
    A(f"## The {len(groups)} families ({total_filings} filings)")
    A("")
    A("`tracked` = already in this project's registry. `NEW` = surfaced by the")
    A("filing and not present in any broker list used here.")
    A("")

    for host, members in ordered:
        sites = sorted({m["domain"] for m in members if m["domain"]})
        A(f"### `{host}` — {len(members)} filings"
          + (f", {len(sites)} distinct sites" if sites else ""))
        A("")
        A("| Registrant | Site | Years filed | Status here |")
        A("|---|---|---|---|")
        for m in sorted(members, key=lambda x: (x["domain"] or "zzz", x["name"])):
            label = m["dba"] or m["name"]
            dom = m["domain"] or "—"
            hit = by_dom.get(dom) or by_name.get(norm(label))
            if hit:
                s = st.get(hit["id"], {}).get("status", "pending")
                mark = f"tracked · `{hit['id']}` · {s}"
            else:
                mark = "**NEW**"
            years = ", ".join(m["years"])
            A(f"| {label[:58]} | {dom} | {years} | {mark} |")
        A("")

    A("---")
    A("")
    A("*Generated by `scripts/build_families_doc.py` from")
    A("`data/broker_families.json`. Refresh with*")
    A("*`scripts/import_state_registries.py --fetch --families`.*")

    OUT.write_text("\n".join(L) + "\n")
    print(f"wrote {OUT} — {len(groups)} families, {total_filings} filings")


if __name__ == "__main__":
    raise SystemExit(main())
