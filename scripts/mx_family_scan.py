#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Find corporate families by shared mail infrastructure.

The domain-based family scan (family_scan.py) groups brokers whose registered
contact addresses share a domain. That finds the obvious cases and misses the
interesting one: a company that was acquired, kept its old brand domain, and had
its mail quietly re-pointed at the parent's mail cluster. The domains differ, the
branding differs, the registry filings differ -- and the MX records are identical.

privacy@bvdinfo.com bounced 550 while bvdinfo.com and moodys.com resolved to the
same Proofpoint tenant (mxa-00520701.gslb.pphosted.com). The mailbox was
decommissioned after the acquisition; the mail cluster still says who now owns
the domain. That is a supplier-disclosure-grade hint obtained without asking
anyone anything.

Generic shared hosting proves nothing -- half the internet is on
*.mail.protection.outlook.com or aspmx.l.google.com. What carries signal is a
TENANT-SPECIFIC hostname: a per-customer label in the MX name that only that
customer's domains use. Proofpoint's mx[ab]-<8 digits>, Mimecast's
<tenant>.mimecast.com, Barracuda's per-account hosts, and any
<something>-com.mail.protection.outlook.com (which encodes the domain itself).

Usage:
Two tiers of result, and the distinction is the whole point:

  CONFIRMED  a provider-issued tenant identifier that only one customer's
             domains resolve to (Proofpoint's mx[ab]-<digits>, an M365 tenant
             label belonging to a DIFFERENT domain than the one asking).
  WEAK       two domains merely sharing a mail host. Most shared hosts are
             shared infrastructure -- SendGrid, MailChannels, Zendesk pods,
             Mimecast's inbound pool, a reseller's Exchange box -- and grouping
             on them invents families that do not exist. Reported separately,
             never merged into the confirmed set, never acted on alone.

The earlier duplicate-domain sweep taught this the hard way: it grouped six
unrelated brokers because their opt-out pages all redirected to one interstitial.
A matcher whose false positives are plausible is worse than one that misses, and
here the cost is asymmetric -- a wrong letter is embarrassing and visible, a
wrongly suppressed one is invisible and permanent.

Usage:
    ./mx_family_scan.py                 # report families
    ./mx_family_scan.py --json out.json
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "brokers.json"

# Hostnames that say nothing about who owns a domain: shared infrastructure that
# millions of unrelated customers land on. Grouping by these would produce one
# enormous meaningless "family" and drown the real ones.
GENERIC = re.compile(
    r"""(
      ^aspmx.*\.google(mail)?\.com$
    | ^alt\d+\.aspmx.*$
    | ^.*\.googlemail\.com$
    | ^mx\d*\.zoho\.(com|eu)$
    | ^mx\.yandex\.net$
    | ^.*\.messagingengine\.com$
    | ^.*\.secureserver\.net$
    | ^.*\.registrar-servers\.com$
    | ^.*\.privateemail\.com$
    | ^mx\.ovh\.net$
    | ^.*\.hostedemail\.com$
    | ^.*\.emailsrvr\.com$
    | ^.*\.mailhostbox\.com$
    | ^.*\.improvmx\.com$
    | ^.*\.forwardemail\.net$
    | ^.*\.qq\.com$
    | ^.*\.protonmail\.ch$
    | ^.*\.pphosted\.com$      # only the bare form; tenant form handled below
    | ^mx\d+-[a-z0-9]+\.ppe-hosted\.com$   # Proofpoint Essentials shared pool
    | ^.*\.mimecast\.com$                   # inbound pool is shared by every tenant
    | ^mx\.sendgrid\.net$
    | ^mx\d*\.mailchannels\.net$
    | ^mail-pod-\d+\.int\.zendesk\.com$
    | ^.*\.mxrecord\.(io|mx)$
    | ^.*\.oxcs\.net$                       # Open-Xchange resellers
    | ^.*\.serverdata\.net$                 # Intermedia shared Exchange
    | ^.*\.hostedserver\.net$
    | ^.*\.fireeyecloud\.com$               # Trellix ETP shared pool
    | ^.*\.mailanyone\.net$
    | ^.*\.antispamcloud\.com$
    | ^.*\.spamexperts\.com$
    | ^.*\.mailgun\.org$
    | ^.*\.cloudflare\.net$
    | ^.*\.trendmicro\.(com|eu)$
    | ^.*\.sophos\.com$
    | ^.*\.hornetsecurity\.com$
    | ^.*\.mailprotect\.be$
    )""",
    re.X | re.I,
)

# Tenant-specific patterns. The captured group is the tenant key -- what makes
# this host belong to ONE customer rather than to the provider's whole book.
TENANT = [
    # Proofpoint: mxa-00520701.gslb.pphosted.com -> tenant 00520701
    (re.compile(r"^mx[a-z]?-(\d{6,10})\.[a-z.]*pphosted\.com$", re.I), "proofpoint:{}"),
    # Microsoft 365: acme-com.mail.protection.outlook.com -> tenant acme-com
    (re.compile(r"^([a-z0-9-]+)\.mail\.protection\.outlook\.com$", re.I), "m365:{}"),
    # Mimecast: eu-smtp-inbound-1.mimecast.com is generic; <tenant>.mimecast.com is not
    (re.compile(r"^(?!.*(?:smtp-inbound|smtp\d))([a-z0-9-]+)\.mimecast\.com$", re.I), "mimecast:{}"),
    # Barracuda Essentials per-account
    (re.compile(r"^mx[0-9a-z-]*\.([a-z0-9-]+)\.barracudanetworks\.com$", re.I), "barracuda:{}"),
    # Cisco/IronPort hosted, per-customer label
    (re.compile(r"^mx[0-9]*\.([a-z0-9-]+)\.iphmx\.com$", re.I), "iphmx:{}"),
]


def mx_hosts(domain):
    try:
        out = subprocess.run(
            ["dig", "+short", "+time=3", "+tries=1", "MX", domain],
            capture_output=True, text=True, timeout=12,
        ).stdout
    except Exception:
        return None                      # never condemn a domain on a dig failure
    hosts = []
    for line in out.splitlines():
        parts = line.strip().rstrip(".").split()
        if len(parts) == 2 and parts[0].isdigit():
            hosts.append(parts[1].lower())
    return hosts


def tenant_keys(hosts):
    """Tenant keys for these MX hosts, ignoring generic shared infrastructure.

    An M365 tenant key derived from the domain's own name (acme-com for
    acme.com) is worthless on its own -- it is just the domain restated. It only
    becomes evidence when a DIFFERENT domain points at it, which is exactly what
    the grouping step tests, so it is kept here and filtered later.
    """
    keys = set()
    for h in hosts:
        for pat, fmt in TENANT:
            m = pat.match(h)
            if m:
                keys.add(fmt.format(m.group(1).lower()))
                break
        else:
            if not GENERIC.match(h):
                # A bare shared host is a hint, not a finding. Kept, but tagged
                # so the caller cannot accidentally treat it as evidence.
                keys.add("weak:" + h)
    return keys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", type=Path)
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()

    rows = json.loads(REGISTRY.read_text())["brokers"]
    by_domain = defaultdict(list)
    for r in rows:
        e = (r.get("email_to") or "").strip().lower()
        if "@" in e:
            by_domain[e.split("@", 1)[1]].append(r["id"])

    domains = sorted(by_domain)
    print(f"resolving MX for {len(domains)} contact domains...", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        results = dict(zip(domains, ex.map(mx_hosts, domains)))

    groups = defaultdict(set)
    for d, hosts in results.items():
        if not hosts:
            continue
        for k in tenant_keys(hosts):
            groups[k].add(d)

    # A tenant key shared by ONE domain tells us nothing new. The finding is a
    # key that two or more otherwise-unrelated contact domains both point at.
    def pack(k, doms):
        return {
            "tenant": k,
            "confidence": "weak" if k.startswith("weak:") else "confirmed",
            "domains": doms,
            "brokers": sorted({b for d in doms for b in by_domain[d]}),
        }

    confirmed, weak = [], []
    for k, v in groups.items():
        if len(v) < 2:
            continue
        doms = sorted(v)
        # An M365 tenant label is derived from a domain name, so a group whose
        # only members are the domain that owns the label plus nothing else is
        # self-referential. Two DIFFERENT domains on one label is the finding.
        (weak if k.startswith("weak:") else confirmed).append(pack(k, doms))

    confirmed.sort(key=lambda g: -len(g["domains"]))
    weak.sort(key=lambda g: -len(g["domains"]))

    def show(title, groups_, note):
        print(f"\n=== {title}: {len(groups_)} group(s) ===")
        print(note)
        for g in groups_:
            print(f"\n  {g['tenant']}")
            print(f"    domains : {', '.join(g['domains'])}")
            print(f"    brokers : {', '.join(g['brokers'][:8])}"
                  + (" ..." if len(g["brokers"]) > 8 else ""))

    show("CONFIRMED (provider-issued tenant id)", confirmed,
         "  A tenant identifier is issued to one customer. Two brand domains on\n"
         "  one identifier means one organisation runs both mail domains.")
    show("WEAK (shared host only -- corroborate before believing)", weak,
         "  Most of these are shared infrastructure, not corporate families.\n"
         "  Treat as a lead to check, never as evidence on its own.")
    out = confirmed + weak
    if args.json:
        args.json.write_text(json.dumps(out, indent=2) + "\n")
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
