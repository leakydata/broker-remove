#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Is this address worth spending a letter on?

The Optery directory gave 93 rows a privacy contact they did not have (SF 445).
The first four letters went out as a deliberate test and one bounced instantly:
info@backgroundalert.com, 550, no such address -- while the DOMAIN had live MX
and a dead website. So the source is good but not perfect, and a bounce costs
more than the letter: it is indistinguishable from silence in the ledger unless
someone reads the mailbox, and a run of them makes the sender look like a
spammer to every receiving domain at once.

This checks the cheap, decisive things before sending, and NOTHING ELSE. It does
not verify that a mailbox exists -- that cannot be done without sending, and SMTP
probing is both unreliable and rude. What it can say:

    NO-MX        the domain publishes no mail exchanger. A letter WILL bounce.
    MX-ONLY      mail is configured but the website does not respond. Exactly
                 the backgroundalert.com shape: often a folded company whose
                 domain is still parked with mail. Send if you like, but expect
                 a dead local-part and treat a bounce as informative.
    LIVE         MX present and the site answers. Normal case.
    NO-DOMAIN    does not resolve at all. Nothing to write to.

Deliberately conservative about the negative: only NO-MX and NO-DOMAIN are
predictions of failure. Everything else is a letter worth sending, because the
one thing this cannot see is whether the local-part exists.
"""
import json
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")


def dig(name, rtype):
    try:
        out = subprocess.run(["dig", "+short", name, rtype],
                             capture_output=True, text=True, timeout=12).stdout
        return [l for l in out.splitlines() if l.strip()]
    except Exception:
        return []


def site_answers(domain):
    for scheme in ("https://", "http://"):
        try:
            req = urllib.request.Request(f"{scheme}{domain}/",
                                         headers={"User-Agent": UA,
                                                  "Accept-Encoding": "identity"})
            with urllib.request.urlopen(req, timeout=15) as r:
                return r.getcode()
        except urllib.error.HTTPError as e:
            return e.code          # a 403 is still an answer
        except Exception:
            continue
    return None


def classify(row):
    bid, site, email = row
    # DELIVERABILITY IS A PROPERTY OF THE ADDRESS'S DOMAIN, NOT THE SITE'S.
    # The first version of this checked the registry `domain` field for MX and
    # got four rows wrong in one run: bay_collective_ip is bayparcels.com with
    # info@baycollective.com, click_search is clicksearch.us with an address at
    # clicksearchsolutions.com, mississippi_people_records is
    # mississippipeoplerecords.org with privacy@mississippi.org. Each was about
    # to be written off as "letter will bounce" on the strength of a lookup
    # against a domain the letter was never going to be sent to.
    maildom = (email or "@").split("@")[-1].lower()
    site = (site or maildom).lower()
    if not (dig(maildom, "A") or dig(maildom, "AAAA") or dig(maildom, "MX")):
        return (bid, maildom, email, "NO-DOMAIN", "address domain does not resolve")
    mx = dig(maildom, "MX")
    code = site_answers(site)
    note = f"site {code}" if code else "site does not answer"
    if maildom != site:
        note += f" [mail domain {maildom} differs from site {site}]"
    if not mx:
        return (bid, maildom, email, "NO-MX", "letter will bounce -- " + note)
    if code is None:
        return (bid, maildom, email, "MX-ONLY", "mail configured, " + note)
    return (bid, maildom, email, "LIVE", note)


def main():
    st = json.loads((ROOT / "data" / "removal_status.json").read_text())
    reg = json.loads((ROOT / "data" / "brokers.json").read_text())["brokers"]
    rows = [(b["id"], (b.get("domain") or "").lower(), b.get("email_to"))
            for b in reg
            if b.get("email_verified_by") == "optery_directory"
            and b["id"] not in st and b.get("email_to")]
    only = sys.argv[1:]
    if only:
        rows = [r for r in rows if r[0] in only]
    print(f"pre-checking {len(rows)} unwritten rows with a directory-sourced address\n",
          file=sys.stderr)

    with ThreadPoolExecutor(max_workers=8) as p:
        res = list(p.map(classify, rows))

    order = {"LIVE": 0, "MX-ONLY": 1, "NO-MX": 2, "NO-DOMAIN": 3}
    res.sort(key=lambda r: (order.get(r[3], 9), r[0]))
    counts = {}
    for _, _, _, v, _ in res:
        counts[v] = counts.get(v, 0) + 1
    for bid, dom, em, verdict, why in res:
        print(f"  {verdict:10s} {bid:30s} {dom[:26]:28s} {em or '':32s} {why}")
    print("\n=== summary")
    for k in ("LIVE", "MX-ONLY", "NO-MX", "NO-DOMAIN"):
        if counts.get(k):
            print(f"  {k:10s} {counts[k]}")
    print("\n  Only NO-MX and NO-DOMAIN predict failure. MX-ONLY is worth a letter")
    print("  but expect a dead local-part. Whether the mailbox exists cannot be")
    print("  known without sending, and probing for it would be both unreliable")
    print("  and rude.")
    out = ROOT / "data" / "contact_precheck.json"
    out.write_text(json.dumps(
        [{"id": b, "domain": d, "email": e, "verdict": v, "why": w}
         for b, d, e, v, w in res], indent=1) + "\n")
    print(f"\nwrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
