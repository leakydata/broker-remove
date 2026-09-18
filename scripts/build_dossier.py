#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Give every playbook a CONTACT DOSSIER and a numbered removal procedure.

The point of this repository is that anyone should be able to open one file,
read it, and get their own data removed. Measured on 2026-09-17, only 28% of
playbooks had a filled `## Steps` section. The rest recorded what happened to
one person's request, which is a good archive and a poor instruction sheet.

This fills the gap from data the brokers themselves filed.

WHAT GOES IN, AND WHY IT IS ALL CORPORATE
-----------------------------------------
Everything here comes from the state data broker registries -- California's
(Civ. Code 1798.99.80 et seq.) and the equivalent filings -- which are public
records a broker is legally REQUIRED to file. The columns are:

    legal entity name .... the name to use in a legal demand, which is often
                           not the brand name on the website (Baron App for
                           Cameo, Zipstorm for SeekOut). This is the single
                           most useful field and almost nobody knows it.
    physical address ..... the corporate address of record, for postal demands
                           and for identifying the registered agent
    contact email ........ filed under penalty of the registry requirement
    phone ................ the business line, where filed
    opt-out method ....... the broker's own description of how to submit
    practices statement .. their own account of what they collect

DELIBERATELY NOT IN SCOPE: individual employees' personal contact details --
home addresses, personal phone numbers, or a dossier keyed to a named person.
Where a human being's name appears in a reply, this project already redacts it
(see scripts/redact.py and the [named individual] placeholders throughout).

That is not squeamishness, it is the argument. This project's whole case is
that assembling scattered public facts about a person into a profile is itself
the injury, distinct from any one fact being known. That argument does not
survive doing the same thing to a support agent at a people-search company,
who is a wage earner following a script and not the author of the policy.
Conceding it would cost more than any phone number could return.

The corporate route is also simply better. A registered agent must accept
service. A regulator complaint creates a docket number and a response
obligation. A named clerk's mobile number creates neither.

Usage:
    ./build_dossier.py                 # every broker with a registry match
    ./build_dossier.py spokeo acxiom   # named brokers
    ./build_dossier.py --report        # coverage only, write nothing
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from paths import playbook  # noqa: E402
from scaffold_playbook import _mask_people as mask_personal_addresses  # noqa: E402

REG = ROOT / "data" / "registries"

# Each registry export uses different column names for the same facts.
COLUMN_SETS = [
    {"file": "registry.csv", "name": "Data broker name:", "dba": "Doing Business As (DBA), if applicable:",
     "site": "Data broker primary website:", "email": "Data broker primary contact email address:",
     "phone": "Data broker primary phone number: [optional]",
     "street": "Data broker primary street address:", "city": "Data broker city:",
     "state": "Data broker state:", "zip": "Data broker zip code:"},
    {"file": "registry2024.csv", "name": "Business name", "dba": "Doing Business As (DBA), if applicable [optional]",
     "site": "Business primary website", "email": "Business primary contact email address",
     "phone": "Business primary phone number [optional]", "street": "Business primary street address",
     "city": "Business city", "state": "Business state abbreviation ", "zip": None},
    {"file": "complete-reg-data-brokers.csv", "name": "Data Broker Name", "dba": None,
     "site": "Website URL", "email": "Email Address", "phone": None,
     "street": "Physical Address", "city": None, "state": None, "zip": None,
     "optout": "How a consumer may opt out of sale or submit requests under the CCPA",
     "protected": ("How a protected individual can demand deletion of information posted "
                   "online under Gov. Code sections 6208.1(b) or 6254.21(c)(1)"),
     "practices": "Additional information about data collecting practices"},
]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def host(u):
    u = (u or "").lower()
    u = re.sub(r"^https?://", "", u).split("/")[0]
    return re.sub(r"^www\.", "", u).strip()


def load_registry():
    """{normalised key: record}, keyed by both company name and website host."""
    by_name, by_host = {}, {}
    for cs in COLUMN_SETS:
        p = REG / cs["file"]
        if not p.exists():
            continue
        for row in csv.DictReader(open(p, encoding="utf-8-sig")):
            get = lambda k: (row.get(cs[k]) or "").strip() if cs.get(k) else ""  # noqa: E731
            name = get("name")
            if not name:
                continue
            rec = {
                "entity": name, "dba": get("dba"), "site": get("site"),
                "email": get("email").replace(" [at] ", "@").replace("[at]", "@"),
                "phone": get("phone"),
                "address": ", ".join(x for x in [get("street"), get("city"),
                                                 get("state"), get("zip")] if x),
                "optout": get("optout"), "protected": get("protected"),
                "practices": get("practices"), "source": cs["file"],
            }
            for key, tgt in ((norm(name), by_name), (norm(get("dba")), by_name),
                             (host(get("site")), by_host)):
                if key and key not in tgt:
                    tgt[key] = rec
    return by_name, by_host


def match(b, by_name, by_host):
    for k in (norm(b.get("name")), norm(b.get("id", "").replace("_", ""))):
        if k in by_name:
            return by_name[k]
    h = host(b.get("domain") or "")
    if h in by_host:
        return by_host[h]
    return None


def wrap(label, value, width=74):
    """One '- **Label:** value' bullet, wrapped, for long registry prose.

    Every value passes through mask_personal_addresses first. Roughly one
    registry filing in six gives a named employee's mailbox rather than a role
    address, and this script republished 52 of them on its first run before
    validate.py caught it -- in a document arguing that scattered facts about a
    person should not be compiled. The company and the fact that its only
    published contact is an individual both stay; the person's name goes.
    """
    value = mask_personal_addresses(re.sub(r"\s+", " ", value or "").strip())
    if not value:
        return []
    out, line = [], f"- **{label}:** "
    for word in value.split():
        if len(line) + len(word) + 1 > width and line.strip() != f"- **{label}:**":
            out.append(line.rstrip())
            line = "  "
        line += word + " "
    out.append(line.rstrip())
    return out


def dossier(b, rec):
    """The 'Who they are' block. Corporate facts only, from their own filing."""
    L = ["## Who they are, and how to reach them", "",
         "*Filed by the company itself with a state data broker registry — a public",
         "record they are legally required to keep current. Use the **legal entity**",
         "name in any formal demand; it is frequently not the brand on the website.*",
         ""]
    L += wrap("Legal entity", rec["entity"])
    if rec["dba"] and norm(rec["dba"]) != norm(rec["entity"]):
        L += wrap("Trading as", rec["dba"])
    L += wrap("Registered address", rec["address"])
    if rec["email"]:
        L += wrap("Filed contact email", rec["email"])
    if rec["phone"]:
        L += wrap("Filed phone", rec["phone"])
    if rec["site"]:
        L += wrap("Website", rec["site"])
    if rec["optout"]:
        L += wrap("Opt-out route they filed", rec["optout"])
    if rec["protected"]:
        L += wrap("Route for protected individuals", rec["protected"]
                  + "  (Cal. Gov. Code 6208.1(b) / 6254.21(c)(1) — for survivors of "
                    "domestic violence, stalking and similar, a stronger and faster "
                    "route than the ordinary consumer request)")
    if rec["practices"]:
        L += wrap("What they say they collect", rec["practices"][:600])
    L += ["", f"*Source: `data/registries/{rec['source']}`.*", ""]
    return "\n".join(L)


ESCALATION = """## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
"""


def steps_for(b, rec):
    """A numbered procedure a stranger can follow, from the route we know."""
    method = (b.get("method") or "unknown").lower()
    url = b.get("optout_url") or (rec or {}).get("optout") or ""
    # Masked here too, not only in wrap(). The first fix covered the dossier
    # block and missed this one, so the raw address went on being printed in
    # the Steps section -- the part a stranger is most likely to copy.
    email = mask_personal_addresses(b.get("email_to") or (rec or {}).get("email") or "")
    S = ["## Steps", "",
         "*Written for anyone, not just the person who filed the original request.*", ""]
    n = 1
    if url.startswith("http"):
        S.append(f"{n}. **Open the opt-out page:** {url}"); n += 1
        if "captcha" in method:
            S.append(f"{n}. **Expect a CAPTCHA.** Note whether it appears on page load "
                     f"or only at submit — a load-time gate means the whole flow has to "
                     f"be done by hand."); n += 1
        S.append(f"{n}. **Search for yourself first if the page asks you to.** Match on "
                 f"more than the name: use age, current city, and at least one previous "
                 f"address. A common name will return other people, and removing their "
                 f"listing instead of yours helps nobody."); n += 1
        S.append(f"{n}. **Submit the form**, then watch for a confirmation email. Many "
                 f"brokers treat the request as void until a link in it is clicked."); n += 1
    if email:
        S.append(f"{n}. **{'Or email' if url.startswith('http') else 'Email'} "
                 f"`{email}`** with a written request. Ask for four things "
                 f"explicitly — deletion, opt-out of sale and sharing, a direction to "
                 f"any third parties they sold to, and a **forward-looking suppression** "
                 f"so the record is not simply re-added at the next data import."); n += 1
        S.append(f"{n}. **List every address, email and phone number you have ever had**, "
                 f"not just current ones. Records are filed under whatever was current "
                 f"when they were created — a search on today's details misses them."); n += 1
    if not url.startswith("http") and not email:
        S.append(f"{n}. **No route is confirmed for this broker yet.** Check the registry "
                 f"block above for a filed contact, and see `## Gotchas`."); n += 1
    S.append(f"{n}. **Ask them to state which identifiers matched.** \"We deleted your "
             f"record\" and \"we searched and found nothing\" are different outcomes, and "
             f"a reply that does not distinguish them tells you nothing about whether you "
             f"were ever in the file.")
    S.append("")
    return "\n".join(S)


def splice(text, header, block):
    """Replace a '## header' section, or append the block if it isn't there."""
    pat = re.compile(rf"^## {re.escape(header)}\b.*?(?=^## |\Z)", re.S | re.M)
    if pat.search(text):
        return pat.sub(block.rstrip() + "\n\n", text, count=1)
    return text.rstrip() + "\n\n" + block.rstrip() + "\n"


def is_placeholder(text, header):
    m = re.search(rf"^## {re.escape(header)}\b(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return True
    body = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S).strip()
    return len(body) < 40


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--report", action="store_true", help="coverage only, write nothing")
    a = ap.parse_args()

    by_name, by_host = load_registry()
    reg = json.load(open(ROOT / "data" / "brokers.json"))["brokers"]
    if a.ids:
        reg = [b for b in reg if b["id"] in set(a.ids)]

    # Worst first: the registry-listed people-search and compiler rows are the
    # ones whose records are public and searchable by anyone.
    HARM = {"people_search": 0, "compiler": 1, "b2b_contact": 2, "list_broker": 2}
    reg.sort(key=lambda b: (HARM.get(b.get("category"), 5), b.get("priority", 9) * -1))

    matched = wrote = 0
    for b in reg:
        rec = match(b, by_name, by_host)
        if rec:
            matched += 1
        p = playbook(b["id"])
        if a.report or not p.exists():
            continue
        t = orig = p.read_text(errors="replace")
        if rec:
            t = splice(t, "Who they are, and how to reach them", dossier(b, rec))
        if is_placeholder(t, "Steps"):
            t = splice(t, "Steps", steps_for(b, rec))
        if "## If they ignore you" not in t:
            t = t.rstrip() + "\n\n" + ESCALATION
        if t != orig:
            p.write_text(t)
            wrote += 1

    print(f"{len(reg)} brokers | {matched} matched a state registry filing "
          f"({matched * 100 // max(len(reg), 1)}%) | {wrote} playbooks updated")
    if a.report:
        print("  --report: nothing written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
