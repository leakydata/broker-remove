#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Generate a protected-person removal request for current or former law
enforcement officers, judges, and public officials.

Several brokers (PeopleConnect, LexisNexis, Whitepages) run a protected-person
track that is broader and faster than the ordinary consumer opt-out. It is
usually offered as company policy rather than compelled by statute, and most
programs explicitly cover *retired* as well as active personnel.

Accuracy matters more here than in an ordinary opt-out. State the role, the
dates, and whether it has ended. Do not describe a former role in the present
tense, and do not cite a statute as compelling removal when it does not.
A request that overstates gets declined, and the broker keeps the record.

Usage:
    ./make_protected_person_request.py --to privacy@peopleconnect.us
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "outbox"

# Per-state supporting authority. These establish that the state treats the
# officer's home address as protected. They bind government agencies, not
# private brokers -- so they are offered as SUPPORT for a policy-based request,
# never as a claim that the broker is legally compelled.
STATE_AUTHORITY = {
    "PA": (
        "Pennsylvania's Right-to-Know Law exempts the home address of a law\n"
        "enforcement officer from public disclosure (65 P.S. 67.708(b)(6)).\n"
        "Pennsylvania constables fall within that protection, and the exemption\n"
        "is not conditioned on the officer's retirement status."
    ),
}

TEMPLATE = """To: {to}
Subject: Protected Person Removal Request — {name}, former {role}, {state}

To the Privacy / Legal Team at {broker},

I am requesting removal of my personal information under your protected person
policy for judges, law enforcement officers, and public officials.

PROTECTED STATUS
  Role:            {role}
  Jurisdiction:    {state}
  Status:          Former — service ended {end_year}
  Basis:           {basis_label}

I want to be precise that this role has ended; I am not claiming to be a serving
officer. I am submitting under your published policy, which covers retired as
well as active personnel.

SUPPORTING AUTHORITY
{authority}

I am not asserting that this statute compels you to act. I offer it as evidence
that my jurisdiction treats the home address of a person in my former role as
protected information, including after service ends.

IDENTIFYING INFORMATION
  Full name:       {name}
  Date of birth:   {dob}
  City / State:    {city}, {state}
  Phone:           {phone}
  Home address:    {street}
                   {city}, {state} {zipc}
  Email addresses: {emails}

REQUESTED ACTION
  1. Remove or suppress my home address, phone number, and associated records
     from all public-facing products and search results.
  2. Apply the removal across every property you operate, not only the site
     where my record was found.
  3. Suppress the record against reintroduction from future data sources.
  4. Confirm in writing once complete.

Please send all correspondence to {contact}.

If you are unable to process this under your protected person policy, please
treat it in the alternative as an ordinary consumer deletion and opt-out
request, and tell me which basis you applied.

Regards,
{name}
{contact}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--to", required=True)
    ap.add_argument("--broker", default="your organization")
    ap.add_argument("--slug", default="protected_person")
    ap.add_argument("--role", default="Pennsylvania State Constable")
    ap.add_argument("--end-year", default="2022")
    ap.add_argument("--dob", default="<REQUIRED — fill in before sending>")
    args = ap.parse_args()

    p = json.loads((ROOT / "data" / "profile.json").read_text())
    state = p["state"].upper()
    emails = [e.lower() for e in p.get("all_emails") or [p["email"]]]
    authority = STATE_AUTHORITY.get(
        state, "  (No state-specific authority recorded for this state.)")

    body = TEMPLATE.format(
        to=args.to,
        broker=args.broker,
        name=f"{p['first_name'].title()} {p['last_name'].title()}",
        role=args.role,
        state=state,
        end_year=args.end_year,
        basis_label=f"Former elected/appointed {args.role}",
        authority="\n".join("  " + ln for ln in authority.splitlines()),
        dob=args.dob,
        city=p["city"].title(),
        phone=p["phone_number"],
        street=p["address"],
        zipc=p["zip_code"],
        emails=("\n" + " " * 19).join(emails),
        contact=(p.get("confirmation_email") or p["email"]).lower(),
    )

    OUTDIR.mkdir(exist_ok=True)
    path = OUTDIR / f"{args.slug}.eml.txt"
    path.write_text(body)
    print(f"wrote {path}")
    if "REQUIRED" in args.dob:
        print("\n  NOTE: date of birth is still a placeholder. Most protected-person\n"
              "  programs require it to locate records. Fill it in before sending.")


if __name__ == "__main__":
    main()
