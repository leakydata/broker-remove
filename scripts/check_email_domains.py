#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Find contact addresses whose domain cannot receive mail at all.

verify_emails.py asks whether an address is the *right* one. This asks the
cruder question first: can anything be delivered to that domain? A domain with
no MX and no A record has nowhere to put a message, so a letter to it is not a
slow request, it is no request -- and Gmail reports the failure as a temporary
delay for 48 hours first, so the tracker reads `submitted` the whole time.

Why this is worth a separate pass: the state registration filings are typed by
hand, and hands make typos. B.I Science (2009) Ltd registered
`dpo@bisceince.com`. Their actual domain is `biscience.com` -- the `e` and `i`
are transposed. The bad domain has no mail records; the real one has Microsoft
365. Nothing in the earlier tooling caught it, because the address is
well-formed, the local-part is a perfect privacy contact, and the provenance is
the strongest in the project.

**A registered address is only as good as the typing.** That is the lesson, and
it costs one DNS lookup per broker to check.

Where the row already carries a `domain`, a suggested correction is offered when
the contact domain is undeliverable and the broker's own domain is not.

    ./check_email_domains.py            # report
    ./check_email_domains.py --apply    # rewrite the local-part onto the good domain
"""

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURATED = ROOT / "data" / "curated_brokers.json"
REGISTRY = ROOT / "data" / "brokers.json"


def deliverable(domain):
    """Can mail be delivered here? MX, or an A record as the implicit fallback.

    Returns True / False / None, where None means the lookup itself failed and
    the domain must NOT be condemned -- guessing 'dead' is the expensive
    direction of this error."""
    try:
        mx = subprocess.run(["dig", "+short", "MX", domain], capture_output=True,
                            text=True, timeout=10)
        if mx.returncode != 0:
            return None
        if any(l.strip() for l in mx.stdout.splitlines()):
            return True
        # No MX. RFC 5321 says fall back to the A record, so this is not formally
        # undeliverable -- but in practice a company that runs a website and no
        # mail server has nothing listening on port 25, and the sender spends two
        # days retrying before giving up. `calibrant.com` behaved exactly that
        # way: site up, no MX, and a delivery-delay notice rather than either a
        # bounce or a delivery.
        #
        # Reported as "weak" rather than folded into either verdict, because the
        # two errors are asymmetric: calling it deliverable wastes a send and two
        # days of a false `submitted`, while calling it dead could write off a
        # broker whose mail genuinely arrives via the A record.
        a = subprocess.run(["dig", "+short", "A", domain], capture_output=True,
                           text=True, timeout=10)
        if a.returncode != 0:
            return None
        return "weak" if any(l.strip() for l in a.stdout.splitlines()) else False
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--workers", type=int, default=10)
    args = ap.parse_args()

    brokers = json.loads(REGISTRY.read_text())["brokers"]
    rows = [b for b in brokers if b.get("email_to") and "@" in b["email_to"]]
    hosts = sorted({b["email_to"].split("@")[-1].lower() for b in rows})
    print(f"checking {len(hosts)} distinct contact domain(s)...", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        verdicts = dict(zip(hosts, ex.map(deliverable, hosts)))

    dead, weak, unknown = [], [], 0
    for b in rows:
        h = b["email_to"].split("@")[-1].lower()
        if verdicts.get(h) is None:
            unknown += 1
            continue
        if verdicts[h] == "weak":
            weak.append((b["id"], b["email_to"]))
            continue
        if verdicts[h]:
            continue
        own = (b.get("domain") or "").lower()
        # Only suggest the broker's own domain if it can actually take mail.
        fix = None
        if own and own != h and verdicts.get(own, deliverable(own)):
            fix = b["email_to"].split("@")[0] + "@" + own
        dead.append((b["id"], b["email_to"], fix))

    print(f"\n{len(dead)} contact address(es) on a domain that cannot receive mail:")
    for bid, addr, fix in dead:
        print(f"  {bid:34} {addr:38} -> {fix or 'NO SUGGESTION'}")
    if weak:
        print(f"\n{len(weak)} address(es) on a domain with NO MX but a live A record."
              f"\n  Formally deliverable via A-record fallback; in practice usually a"
              f"\n  website with no mail server, which costs two days of retries."
              f"\n  Not rewritten - verify before spending a send:")
        for bid, addr in weak:
            print(f"    {bid:32} {addr}")
    if unknown:
        print(f"\n({unknown} address(es) skipped - DNS lookup failed, not condemned)")

    if not args.apply:
        print("\n(report only - pass --apply to rewrite where a suggestion exists)")
        return 0

    d = json.loads(CURATED.read_text())
    by_id = {b["id"]: b for b in d["brokers"]}
    n = 0
    for bid, addr, fix in dead:
        b = by_id.get(bid)
        if not b or not fix:
            continue
        b["email_alt"] = addr + " (UNDELIVERABLE - domain has no MX and no A)"
        b["email_to"] = fix
        b["email_verified"] = False
        b["email_verified_by"] = "domain_typo_corrected"
        b["notes"] = ((b.get("notes") or "") + " " + (
            f"The registered contact {addr} is undeliverable - that domain publishes "
            f"no mail records at all. Almost certainly a typo in the filing. Rewritten "
            f"onto the broker's own domain; unverified until a reply arrives.")).strip()
        n += 1
    CURATED.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    print(f"\nrewrote {n} address(es) - now run scripts/build_registry.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
