#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Re-open earlier requests that were searched against an incomplete identifier list.

The identifier list in data/profile.json grew during the campaign. Brokers
contacted before it grew were searched against fewer keys than brokers contacted
after -- and their "no records found" replies are correspondingly weaker evidence.

This is not a hypothetical. BDEX reported that four of twelve email addresses
matched their records, and every one of the four was a mailbox that had been out
of service for years. All four of those addresses were added to the profile AFTER
the early letters went out. So the identifiers most likely to match were precisely
the ones the early requests did not carry.

A supplementary letter is cheap and the argument is easy to state: you already
processed a request from me, here are additional identifiers that were not in it,
please run them against the same request rather than treating this as a new one.

Usage:
    ./supplement_identifiers.py --before 2026-08-20 --summary
    ./supplement_identifiers.py --before 2026-08-20 --size 10
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from paths import state  # noqa: E402
from make_optout_email import load_profile  # noqa: E402
from letter_html import to_html  # noqa: E402

REGISTRY = ROOT / "data" / "brokers.json"

# Statuses where a supplementary letter is worth sending. A broker that never
# received anything is handled by queue_batch instead; one that is unreachable or
# form-only cannot be helped by another email.
WORTH_SUPPLEMENTING = {"submitted", "not_found", "confirmed"}

TEMPLATE = """To the Privacy Officer at {broker},

I wrote to you on {when} with a consumer request to delete and opt out of the sale
of my personal information{ref}. **This is not a new request** — please treat it as
completing the one already on file rather than restarting the clock.

Since writing, I have identified further identifiers of mine that were **not
included in that letter**. I am supplying them now because a search run without
them may have missed records that do exist.

{added_block}
Why this matters more than it may sound
-----------------------------------------
These are old identifiers — addresses and numbers I no longer use — and in my
experience they are the ones that actually match.

One company searched all twelve of my email addresses and reported back that
**four matched. Every one of the four was a mailbox that had been out of service
for years, and not one of my current addresses matched at all.** All four of those
addresses are in the list below, and none of them were in my original letter to
you.

So if your earlier answer was that no records were found, that answer was
accurate for the identifiers it was given — and may still be incomplete. I am not
disputing it. I am asking you to re-run the same request against the additional
keys.

What I am asking
------------------
Please apply the request already on file — deletion, opt-out of sale or sharing,
onward direction to recipients, and forward-looking suppression — to these
additional identifiers as well, and confirm.

If it helps, **please list the identifiers you searched.** A confirmation that
enumerates what was checked lets me see the request is complete without having to
ask again; a bare "processed" leaves both of us where we started. Two companies
have done this and in both cases it revealed an omission neither of us would
otherwise have noticed.

If the answer remains that nothing is held under any of them, please say so — that
is a complete reply, I will record it and will not write again.

My full identifier list, with the additions marked
----------------------------------------------------
{full_block}

Please send all correspondence to {contact}. Please do not ask me to create an
account, and do not request a copy of a government-issued identity document.

Regards,
{name}
{contact}
"""


def sibling_block(siblings):
    """Name every brand registered against this address, when there is more
    than one. Silence here is how one reply ends up covering one brand."""
    if not siblings:
        return ""
    names = "\n".join(f"    {n}" for n in siblings)
    return (
        "This address is the published privacy contact for more than one of your\n"
        "properties, so to be explicit about scope: I am asking for this to be\n"
        "applied to that one **and** to\n\n"
        f"{names}\n\n"
        "If those are separate controllers with separate files, please say so and\n"
        "I will write to each. If they share an index, one answer covering all of\n"
        "them is exactly what I am asking for -- please confirm against each by\n"
        "name, because a reply naming one brand leaves me unable to tell whether\n"
        "the others were looked at.\n\n")


def load_state():
    p = state("removal_status.json")
    return json.loads(p.read_text()) if p.exists() else {}


def first_contact(rec):
    best = None
    for e in rec.get("history") or []:
        if e.get("status") in {"submitted", "confirmed", "not_found",
                               "manual_required", "captcha_blocked", "failed"}:
            d = (e.get("at") or "")[:10]
            if d and (best is None or d < best):
                best = d
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", required=True,
                    help="first-contact date before which the short list was used")
    ap.add_argument("--added", nargs="*", default=None,
                    help="identifiers added since; default reads _late_identifiers "
                         "from profile.json")
    ap.add_argument("--size", type=int, default=10)
    ap.add_argument("--broker", action="append", default=None,
                    help="generate for these broker ids only. send_plan.py\ndecides what to send; this flag lets it drive the generator instead of the\ngenerator re-deciding with a different filter.")
    ap.add_argument("--summary", action="store_true")
    args = ap.parse_args()

    reg = {b["id"]: b for b in json.loads(REGISTRY.read_text())["brokers"]}
    st = load_state()
    prof = load_profile()

    raw = json.loads(state("profile.json").read_text())
    added = args.added
    if added is None:
        added = raw.get("_late_identifiers") or []
    late_addr = raw.get("_late_addresses") or []
    late_ph = raw.get("_late_phones") or []
    if not added:
        sys.exit("no added identifiers given and profile.json has no "
                 "_late_identifiers list -- pass --added explicitly")

    cand = []
    for bid, rec in st.items():
        if rec.get("status") not in WORTH_SUPPLEMENTING:
            continue
        d = first_contact(rec)
        if not d or d >= args.before:
            continue
        b = reg.get(bid)
        if not b or not b.get("email_to"):
            continue
        # send_plan.py already refuses these; the generator must refuse them
        # too. When only one of the two filtered, a broker skipped on purpose
        # (shared mailbox with a broker already written to) came back at the
        # top of the generator's list -- one copy-paste from a duplicate
        # letter to an address that had already had one.
        if rec.get("supplemented") or rec.get("supplement_skipped"):
            continue
        if args.broker and bid not in args.broker:
            continue
        cand.append((bid, b, rec, d))

    cand.sort(key=lambda t: (-(t[1].get("priority") or 0), t[0]))

    print(f"{len(cand)} broker(s) contacted before {args.before} and worth "
          f"supplementing", file=sys.stderr)
    if args.summary:
        for bid, b, rec, d in cand[:args.size]:
            print(f"  {d}  {rec.get('status'):12} {bid:38} {b['email_to']}",
                  file=sys.stderr)
        return

    parts = ["These were not in my earlier letter:", ""]
    parts += ["  Email addresses:"] + [f"    {a}" for a in added]
    if late_addr:
        parts += ["", "  Prior addresses:"] + [f"    {a}" for a in late_addr]
    if late_ph:
        parts += ["", "  Prior telephone numbers:"] + [f"    {n}" for n in late_ph]
    added_block = "\n".join(parts) + "\n"
    full = []
    for e in prof["emails"].split("\n" + " " * 19):
        mark = "   <-- NOT in my earlier letter" if e.strip().split()[0] in added else ""
        full.append(f"    {e.strip()}{mark}")
    full_block = "\n".join(full)

    # One address, one letter -- and here that is not merely about avoiding a
    # duplicate, it is a better letter. Corporate families register several
    # brands against a single contact: operations@ignitevisibility.com is the
    # address for 33 Mile Radius, Keyword Connects and Remodeling.com, and
    # privacyrequest@whitepages.com covers both 411.com and PeopleSearch. Sending
    # three near-identical letters to one desk reads as a mail-merge and invites
    # one reply covering whichever brand the reader happened to open. Sending one
    # that NAMES all three makes the scope explicit and asks them to confirm
    # against each -- which is the answer we actually want.
    by_addr = {}
    for bid, b, rec, d in cand:
        by_addr.setdefault(b["email_to"].lower(), []).append((bid, b, rec, d))

    out = []
    for addr, members in list(by_addr.items())[:args.size]:
        bid, b, rec, d = members[0]          # earliest-contacted drives the date
        siblings = [m[1].get("name", m[0]) for m in members[1:]]
        ref = ""
        if rec.get("confirmation_ref"):
            ref = f" (your reference {rec['confirmation_ref']})"
        body = TEMPLATE.format(
            broker=b.get("name", bid), when=d, ref=ref,
            added_block=(sibling_block(siblings) + added_block),
            full_block=full_block,
            contact=prof["email"], name=prof["name"])
        out.append({
            "id": bid,
            "covers": [m[0] for m in members],
            "siblings": siblings,
            "to": b["email_to"],
            "subject": ("Additional identifiers for my existing privacy request "
                        f"— {prof['name']}"),
            "body": body,
            # Send this, not `body`. Gmail rewrites bare domains in a plain-text
            # body and replaces the VISIBLE text with a google.com/url redirect
            # -- see scripts/letter_html.py.
            "html_body": to_html(body),
        })
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
