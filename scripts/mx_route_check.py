#!/usr/bin/env python3
"""Which contact addresses in the corpus cannot receive mail?

_SILENT_FAILURES §266. A letter to an address published in a company's own privacy
policy bounced. That is worth catching before the send rather than after, so this
checks every `email_to` domain in curated_brokers.json for a usable mail route.

Two rules learned by getting it wrong the first time:

  1. Check EVERY MX host, not the lowest-priority one. onetrust.com publishes four;
     the priority-5 host does not resolve and the others do. Judging the domain on
     the first host produced a false "undeliverable" for a company whose mail
     plainly works.

  2. Retry before declaring absence. A sweep of 964 domains produced NO-MX for
     addirectinc.com, which has two perfectly good Proofpoint records -- a transient
     resolver failure, indistinguishable from a real answer if you only ask once.

Both defects had the same shape: a single negative observation reported as a fact
about the world. See also §263.

This says a route EXISTS. It cannot say a MAILBOX exists -- only a send can, which
is §236's correction. A domain that passes here can still return 550 No Such User.
"""
import argparse, json, re, subprocess, sys, collections
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from paths import ROOT  # noqa: E402


def dig(name, rtype, tries=3):
    """Resolve, retrying so a transient failure is not read as an empty answer."""
    for _ in range(tries):
        try:
            out = subprocess.run(["dig", "+short", "+time=3", "+tries=2", rtype, name],
                                 capture_output=True, text=True, timeout=15).stdout
        except (subprocess.TimeoutExpired, OSError):
            continue
        vals = [l.strip().rstrip(".") for l in out.splitlines() if l.strip()]
        if vals:
            return vals
    return []


def route(domain):
    """Return (verdict, detail). A domain is routable if ANY MX host resolves."""
    mx = dig(domain, "MX")
    hosts = []
    for line in mx:
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit():
            hosts.append((int(parts[0]), parts[1].lower()))
    if not hosts:
        # No MX is not fatal: RFC 5321 permits falling back to the A/AAAA record.
        if dig(domain, "A") or dig(domain, "AAAA"):
            return "implicit-mx", f"no MX; falls back to {domain} itself"
        return "NO-ROUTE", "no MX and no address record"
    live = [h for _, h in sorted(hosts) if dig(h, "A") or dig(h, "AAAA")]
    if not live:
        return "NO-ROUTE", "MX host(s) do not resolve: " + ", ".join(h for _, h in hosts)
    dead = [h for _, h in sorted(hosts) if h not in live]
    detail = live[0] + (f"  ({len(dead)} of {len(hosts)} MX hosts dead)" if dead else "")
    return "routable", detail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--only-bad", action="store_true")
    args = ap.parse_args()

    cur = json.loads((ROOT / "data" / "curated_brokers.json").read_text())
    rows = cur if isinstance(cur, list) else cur.get("brokers", [])
    st = json.loads((ROOT / "data" / "removal_status.json").read_text())

    by_dom = collections.defaultdict(list)
    for r in rows:
        e = (r.get("email_to") or "").strip().lower()
        if "@" in e:
            by_dom[e.split("@", 1)[1]].append(r)
    domains = sorted(by_dom)
    print(f"checking mail routes for {len(domains)} contact domains", flush=True)

    results = {}
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for d, res in zip(domains, ex.map(route, domains)):
            results[d] = res

    tally = collections.Counter(v for v, _ in results.values())
    print("\n=== routes")
    for k, v in tally.most_common():
        print(f"  {k:14} {v:4}")

    bad = [(d, det) for d, (v, det) in results.items() if v == "NO-ROUTE"]
    print(f"\n=== {len(bad)} domain(s) with no mail route at all")
    for d, det in sorted(bad):
        for r in by_dom[d]:
            s = st.get(r["id"], {}).get("status", "pending")
            flag = "  <-- MARKED SUBMITTED, so this row is not actually contacted" \
                   if s == "submitted" else ""
            print(f"  {d:<32} {r['id']:<28} {s:<14} {det}{flag}")

    # A route proves the domain accepts mail for SOME mailbox, never that this one
    # exists (§236). Say so where the number is printed, not in a footnote.
    print("\n  note: 'routable' means the DOMAIN accepts mail. It does not mean the "
          "ADDRESS exists --\n  only a successful send shows that. See §236, §266.")


if __name__ == "__main__":
    main()
