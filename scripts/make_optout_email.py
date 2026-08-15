#!/usr/bin/env python3
"""Generate statutory opt-out / deletion request emails.

Why this exists: most brokers put their CAPTCHA on the web form, but state privacy
law obliges them to honor a written request sent to their privacy address. Email
has no CAPTCHA, leaves a timestamped paper trail, and starts a statutory response
clock. For a gated site this is usually a better route than the form, not a worse one.

Usage:
    ./make_optout_email.py <broker_id> [--to privacy@example.com]
    ./make_optout_email.py --all-blocked      # every captcha/manual-blocked broker
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "outbox"

TEMPLATE = """To: {to}
Subject: Consumer Request to Delete and Opt Out of Sale of Personal Information — {name}

To the Privacy Officer at {broker},

I am submitting a consumer request regarding my personal information.

I request that you:
  1. DELETE all personal information you hold about me;
  2. OPT ME OUT of any sale or sharing of my personal information;
  3. DIRECT any service providers and third parties to whom you have sold,
     shared, or otherwise disclosed my personal information to do the same; and
  4. SUPPRESS my details so that my records are not re-added from future
     data sources.

To help you locate my records, my identifying details are:

  Name:            {name}
  Email:           {email}
  Phone:           {phone}
  Mailing address: {street}
                   {city}, {state} {zipc}

I am exercising rights available to me under applicable state consumer privacy
law, including the California Consumer Privacy Act as amended by the CPRA
(Cal. Civ. Code 1798.105 and 1798.120) where applicable, and comparable statutes
in other states. If you believe you are not subject to these statutes, I ask that
you honor this request as a matter of your published privacy policy.

Please confirm in writing when this request has been completed, and tell me the
categories of personal information you held about me at the time of deletion.

Please send all correspondence about this request, including any verification
step and your written confirmation, to {contact}.{contact_note}

Please do not ask me to create an account, and do not request a copy of a
government-issued identity document; less intrusive verification is sufficient
given the limited scope of this request.

I look forward to your confirmation within the period required by law.

Regards,
{name}
{contact}
"""

CONTACT_NOTE = ("\nThat address is a contact address for this request; the "
                "records to be deleted are\nthose associated with the details "
                "listed above.")


def load_profile():
    p = json.loads((ROOT / "data" / "profile.json").read_text())
    return {
        "name": f"{p['first_name'].title()} {p['last_name'].title()}",
        "email": p["email"].lower(),
        "phone": p["phone_number"],
        "street": p["address"],
        "city": p["city"].title(),
        "state": p["state"].upper(),
        "zipc": p["zip_code"],
    }


def guess_to(b):
    if b.get("email_to"):
        return b["email_to"]
    d = b.get("domain") or ""
    return f"privacy@{d}" if d else "privacy@<broker-domain>"


def render(b, prof, to=None, contact=None):
    """`contact` is the mailbox that will actually receive replies. When it differs
    from the profile email (e.g. sending from a different account than the one
    being scrubbed), say so explicitly so the broker searches the right identity
    but answers somewhere reachable."""
    contact = contact or prof["email"]
    return TEMPLATE.format(
        to=to or guess_to(b),
        broker=b.get("name", b["id"]),
        contact=contact,
        contact_note="" if contact == prof["email"] else CONTACT_NOTE,
        **prof)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("broker_id", nargs="?")
    ap.add_argument("--to")
    ap.add_argument("--contact", help="mailbox that will receive replies")
    ap.add_argument("--all-blocked", action="store_true")
    args = ap.parse_args()

    reg = {b["id"]: b for b in
           json.loads((ROOT / "data" / "brokers.json").read_text())["brokers"]}
    prof = load_profile()
    OUTDIR.mkdir(exist_ok=True)

    if args.all_blocked:
        sp = ROOT / "data" / "removal_status.json"
        state = json.loads(sp.read_text()) if sp.exists() else {}
        targets = [bid for bid, r in state.items()
                   if r.get("status") in {"captcha_blocked", "manual_required"}]
    elif args.broker_id:
        targets = [args.broker_id]
    else:
        raise SystemExit("give a broker_id or --all-blocked")

    for bid in targets:
        b = reg.get(bid)
        if not b:
            print(f"  skip unknown broker: {bid}")
            continue
        path = OUTDIR / f"{bid}.eml.txt"
        path.write_text(render(b, prof, args.to, args.contact))
        print(f"  wrote {path}")

    print(f"\n{len(targets)} email(s) in {OUTDIR}/ — review the To: address before sending.")


if __name__ == "__main__":
    main()
