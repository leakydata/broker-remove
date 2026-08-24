#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Find registry rows that are the same company reached by different domains.

queue_batch already refuses to write twice to one contact address. That catches
a family registered under a single mailbox. It does not catch the other shape:
**one company registered twice, under two domains and two addresses.**

    app_science   appscience.inc   privacy@appscience.inc
    appscience    appsci.io        privacy@appsci.io

Different ids, different domains, different contacts, nothing in common to match
on -- and both redirect to `www.appscience.ai`. A letter had already gone to the
first when the second came up in the queue.

The tell is the **final URL after redirects**. A company that has collected
several domains over its life points them all at one site, and that is visible
for the price of one request per domain.

Writes `duplicate_of` onto the row that is NOT already in progress, which
queue_batch then holds out of the send queue. Nothing is deleted: the second
registration is a real filing and its contact address may be the better route,
so the row stays and carries a pointer.

    ./find_duplicate_domains.py            # propose
    ./find_duplicate_domains.py --apply
"""

import argparse
import json
import socket
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
from paths import state  # noqa: E402

CURATED = ROOT / "data" / "curated_brokers.json"
REGISTRY = ROOT / "data" / "brokers.json"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")

# Hosts that many unrelated companies legitimately land on. A shared landing page
# here is a parking service or a platform, not a corporate relationship, and
# treating it as one would silently suppress letters to real separate brokers.
GENERIC = {
    "sites.google.com", "www.godaddy.com", "godaddy.com", "sedo.com",
    "www.sedo.com", "wix.com", "www.wix.com", "squarespace.com",
    "www.squarespace.com", "hugedomains.com", "www.hugedomains.com",
    "afternic.com", "www.afternic.com", "dan.com", "www.dan.com",
    "shopify.com", "www.shopify.com", "notion.site", "carrd.co",
}


def final_host(domain, timeout=12):
    """The host a domain actually lands on after redirects, or None."""
    for scheme in ("https://", "http://"):
        try:
            req = urllib.request.Request(scheme + domain,
                                         headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                host = urllib.parse.urlparse(r.geturl()).hostname or ""
                return host.lower().lstrip(".") or None
        except urllib.error.HTTPError as e:
            # A 4xx/5xx still reveals where we were redirected to.
            try:
                host = urllib.parse.urlparse(e.geturl()).hostname or ""
                return host.lower() or None
            except Exception:
                return None
        except (urllib.error.URLError, socket.timeout, ConnectionError,
                UnicodeError, OSError):
            continue
    return None


def main():
    import urllib.parse  # noqa: F401  (used via urllib.parse above)
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    brokers = json.loads(REGISTRY.read_text())["brokers"]
    st = json.loads(state("removal_status.json").read_text())
    st = st.get("brokers", st)

    rows = [b for b in brokers if b.get("domain") and not b.get("duplicate_of")]
    if args.limit:
        rows = rows[: args.limit]
    print(f"resolving {len(rows)} domain(s)...", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        hosts = list(ex.map(lambda b: final_host(b["domain"]), rows))

    groups = {}
    for b, h in zip(rows, hosts):
        if not h or h in GENERIC:
            continue
        groups.setdefault(h.removeprefix("www."), []).append(b)

    def rank(b):
        """Prefer keeping the row that is already in progress, then the one whose
        own domain matches the landing host, then the curated one."""
        s = st.get(b["id"], {}).get("status", "pending")
        return (0 if s != "pending" else 1,
                0 if b.get("source") != "ca_data_broker_registry" else 1,
                b["id"])

    dupes = []
    for host, members in sorted(groups.items()):
        if len(members) < 2:
            continue
        members.sort(key=rank)
        keep = members[0]
        for other in members[1:]:
            dupes.append((other["id"], keep["id"], host))

    print(f"{len(dupes)} row(s) resolve to a domain another row already covers:")
    for a, keep, host in dupes:
        print(f"  {a:38} -> {keep:28} (both land on {host})")

    if not args.apply:
        print("\n(dry run - pass --apply to write duplicate_of)")
        return 0

    d = json.loads(CURATED.read_text())
    by_id = {b["id"]: b for b in d["brokers"]}
    n = 0
    for a, keep, host in dupes:
        b = by_id.get(a)
        if not b:
            continue
        b["duplicate_of"] = keep
        b["notes"] = ((b.get("notes") or "") + " " + (
            f"Resolves to {host}, the same site as {keep}. Same company "
            f"registered twice under different domains and contact addresses. "
            f"Held out of the send queue; raise any sibling question inside the "
            f"{keep} thread rather than opening a second request.")).strip()
        n += 1
    CURATED.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    print(f"\nmarked {n} row(s) - now run scripts/build_registry.py")
    return 0


if __name__ == "__main__":
    import urllib.parse
    sys.exit(main())
