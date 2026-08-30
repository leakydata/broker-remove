#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
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
from paths import state, outbox  # noqa: E402
OUTDIR = outbox()

TEMPLATE = """To: {to}
Subject: Consumer Request to Delete and Opt Out of Sale of Personal Information — {name}

To the Privacy Officer at {broker},

I am submitting a consumer request regarding my personal information.

{ident_intro}

I request that you:
  1. DELETE all personal information you hold about me;
  2. OPT ME OUT of any sale or sharing of my personal information;
  3. DIRECT any service providers and third parties to whom you have sold,
     shared, or otherwise disclosed my personal information to do the same; and
  4. SUPPRESS my details so that my records are not re-added from future
     data sources.

To help you locate my records, my identifying details are:

  Name:            {name}
  Also known as:   {aliases}
  Date of birth:   {dob}
  Phone:           {phone}
  Mailing address: {mailing_block}
  Email addresses: {emails}
{profile_block}{prior_block}
{scope_block}

{prior_rationale}
{suppress_block}
I am exercising rights available to me under applicable state consumer privacy
law, including the California Consumer Privacy Act as amended by the CPRA
(Cal. Civ. Code 1798.105 and 1798.120) where applicable, and comparable statutes
in other states. If you believe you are not subject to these statutes, I ask that
you honor this request as a matter of your published privacy policy.

Please confirm in writing when this request has been completed, and tell me the
categories of personal information you held about me at the time of deletion.

Three things I would ask the confirmation to state, because they are what make
it mean something:

  1. WHICH of the identifiers above matched. "We deleted your record" and "we
     searched and found nothing" are different outcomes, and both are fine -- but
     a confirmation that does not distinguish them tells me nothing about whether
     I was ever in your file. If some identifiers matched and others did not,
     saying which is the single most useful sentence you can write.

  2. WHICH SYSTEMS WERE SEARCHED, not only whether something was found. A
     support desk naturally searches the system it owns, and "we found nothing"
     is entirely truthful about that system while silent about the others -- a
     verification team searches verification records, a marketing team searches
     the marketing database, and neither is the whole answer. Naming the systems
     costs you a sentence and tells me what the result actually covers.

  3. WHETHER THE SUPPRESSION IS KEYED TO ME OR TO THE IDENTIFIERS I SENT. If your
     system builds results on demand rather than storing a record, then a
     suppression cannot attach to "my record" -- it can only attach to the keys I
     supplied, and anything outside that set is not suppressed but merely
     un-searched. That matters because somebody looking me up does not search my
     current address; they search the one they have. If that is how your system
     works, please apply the suppression across every identifier listed above.

{cap_block}

Please send all correspondence about this request, including any verification
step and your written confirmation, to {contact}.{contact_note}

Please do not ask me to create an account, and do not request a copy of a
government-issued identity document; less intrusive verification is sufficient
given the limited scope of this request.

{minimise_tail}

I look forward to your confirmation within the period required by law.

Regards,
{name}
{contact}
"""

CONTACT_NOTE = ("\nThat address is a contact address for this request; the "
                "records to be deleted are\nthose associated with the details "
                "listed above.")

# A public profile is re-scraped continuously, so a deletion that leaves nothing
# keyed against the SOURCE is undone at the next crawl and the person never
# learns of it. The profile URL is the only identifier the subject can supply
# that is also stable over time and is itself the collection input -- the exact
# opposite of a device ID, which the subject structurally cannot produce. It also
# reaches records the subject could never name, such as work addresses derived
# from an employment history rather than collected. See _SILENT_FAILURES.md #90.
SUPPRESS_BLOCK = """
Please also add the public profile URL listed above to any internal suppression
list you maintain, and please make that suppression:

  (a) forward-looking -- applied against future ingestion, not only against the
      records you hold today, so that a re-crawl of that page does not simply
      re-create what you have deleted; and
  (b) exclude-only -- used to keep me out, never as a match key to identify me in
      an incoming feed.

I am not objecting to your retaining the URL for the first purpose. I am asking
you to confirm which of the two it is used for, because the same string does
opposite work depending on the answer.

If you hold any email address for me that was DERIVED rather than collected -- a
first.last@employer pattern constructed from my name and employment history
rather than one I have ever used -- that is a record about me and it is within
this request. I cannot list such addresses, because I have never owned them. You
can generate them from the same public profile they were built from.
"""


# ---------------------------------------------------------------- key policy
#
# WHAT IDENTIFIER SET TO SEND, AND WHY IT IS NOT ALWAYS "ALL OF THEM".
#
# Nexxen's privacy team wrote back on 2026-08-30: "your initial request may have
# included personal data that we do not hold including name, address, email,
# date of birth, phone numbers, etc. Please do not send us personal data which
# we do not collect or process." They were right (_SILENT_FAILURES 195).
#
# The maximal list exists for a real reason. bdex itemised its matches and found
# the subject on FOUR long-dead email addresses and none of the current ones --
# a letter listing only working addresses would have drawn a truthful and
# completely wrong "no record found" (195, 194, 189a). Against a compiler keyed
# to names and postal addresses, sending everything is the difference between a
# search and a false negative.
#
# Against a platform keyed to cookies, device IDs, CTV IDs and bid-stream
# signals, a postal address cannot match anything. It can only be ADDED. There
# the same list is not a search key at all, it is purely a disclosure.
#
# So the policy is per-recipient, and DELIBERATELY ASYMMETRIC:
#
#   full        default. Over-sending costs disclosure -- bad, bounded, and the
#               requester's own to bear.
#   email-only  emails and name only. Under-sending costs a FALSE NIL, which
#               settles a broker wrongly and is terminal (161a). Much worse.
#
# Because the two failure modes are not equal, this never minimises silently.
# The heuristic only SUGGESTS, on stderr; choosing email-only is an explicit act.
_IDENTIFIER_KEYED = (
    "adtech", "identity_graph", "dsp", "ssp", "exchange", "programmatic",
    "dmp", "attribution", "retargeting", "audience", "ctv", "bidstream",
    "bid stream", "ad tech", "advertising platform", "identity resolution",
)


def suggest_keys(b):
    """Return 'email-only' if this looks identifier-keyed rather than name-keyed."""
    hay = " ".join(str(b.get(k) or "") for k in
                   ("category", "name", "domain", "notes", "email_note")).lower()
    return "email-only" if any(w in hay for w in _IDENTIFIER_KEYED) else "full"


def load_profile():
    p = json.loads((state("profile.json")).read_text())
    emails = [e.lower() for e in p.get("all_emails") or [p["email"]]]
    indent = "\n" + " " * 19

    # Prior addresses and old numbers are how brokers index records. Omitting
    # them lets a broker search only current details and truthfully report a
    # partial result.
    prior = []
    if p.get("prior_addresses"):
        prior.append("  Prior addresses:")
        prior += [" " * 19 + a for a in p["prior_addresses"]]
    if p.get("prior_phones"):
        prior.append("  Prior phone numbers:")
        prior += [" " * 19 + n for n in p["prior_phones"]]
    prior_block = ("\n" + "\n".join(prior) + "\n") if prior else "\n"

    # Two independent annotations, and conflating them cost us a real finding.
    #
    # CLOSED: still matches records but can no longer receive mail. Marked so no
    # broker sends a verification link to a mailbox nobody can open -- a silent
    # failure that looks identical to being ignored.
    #
    # WORK-DOMAIN: an address at an employer, university or other organisational
    # domain, as opposed to a consumer mail provider. This is a fact about the
    # KIND of identifier, not about whose it is or whether it still works, and a
    # B2B database is keyed to exactly this kind. SalesIntel found a live record
    # under one -- a university address that had been annotated only as "closed
    # mailbox" for weeks, while a letter in the same thread asserted that every
    # address supplied was personal (_SILENT_FAILURES 129). The note was accurate
    # about deliverability and silent about type, so the type went unnoticed.
    #
    # Classified by exclusion: anything not on the consumer-provider list is
    # treated as organisational. That errs toward flagging, which is the cheap
    # direction -- a wrongly flagged address invites a broader search, while a
    # missed one invites a confident and wrong claim.
    CONSUMER_MAIL = {
        "gmail.com", "googlemail.com", "hotmail.com", "outlook.com", "live.com",
        "msn.com", "yahoo.com", "ymail.com", "aol.com", "icloud.com", "me.com",
        "mac.com", "proton.me", "protonmail.com", "gmx.com", "mail.com",
        "zoho.com", "fastmail.com", "webtv.net", "iwon.com", "att.net",
        "gateway.net", "verizon.net", "comcast.net", "sbcglobal.net",
        "bellsouth.net", "cox.net", "earthlink.net", "juno.com", "netzero.net",
    }
    closed = {e.lower() for e in p.get("closed_emails") or []}

    def annotate(e):
        notes = []
        if e.lower() not in CONSUMER_MAIL and e.lower().split("@")[-1] not in CONSUMER_MAIL:
            notes.append("organisational address — a work identifier, "
                         "the kind a B2B file is keyed to")
        if e.lower() in closed:
            notes.append("closed mailbox — a search key only, not a reply address")
        return e + ("   (" + "; ".join(notes) + ")" if notes else "")

    email_lines = [annotate(e) for e in emails]

    profiles = p.get("public_profiles") or []
    if profiles:
        label = "  Public profile:" if len(profiles) == 1 else "  Public profiles:"
        profile_block = ("\n" + label + " " * (19 - len(label) + 2) +
                         indent.join(profiles) + "\n")
    else:
        profile_block = ""

    mid = (p.get("middle_name") or "").title()
    full = " ".join(x for x in [p["first_name"].title(), mid, p["last_name"].title()] if x)
    aliases = p.get("variants", {}).get("name_forms") or [full]

    return {
        "name": f"{p['first_name'].title()} {p['last_name'].title()}",
        "full_name": full,
        "aliases": ", ".join(aliases),
        "dob": p.get("dob_display") or p.get("date_of_birth") or "(not provided)",
        "prior_block": prior_block,
        "ident_intro": (
            "I am the consumer, writing about my own data. I am not an authorized "
            "agent acting\nfor anyone else, and every email address, address and "
            "telephone number listed\nbelow is mine. I list them all so that each "
            "can be searched, because records are\nfrequently held against details "
            "a person no longer uses."),
        "prior_rationale": (
            "I have listed prior addresses and old telephone numbers deliberately. "
            "Records are\nfrequently indexed against a former address or a "
            "disconnected number rather than\na current one, and a search limited "
            "to my present details will miss them.\n\nTo be clear about the scope "
            "of that: I am asking you to SEARCH on those prior\naddresses and "
            "numbers, and to suppress the records that turn out to be ABOUT ME.\n"
            "I am not asking you to suppress an address or a telephone number in "
            "itself. Other\npeople live at those addresses now, and those numbers "
            "have been reassigned --\nsuppressing them outright would remove "
            "strangers from your file, which is not\nsomething I am entitled to "
            "ask for on their behalf."),
        "cap_block": (
            "One limit on that, which I would ask you to respect even though it "
            "costs me\nsomething: other people live at my former addresses now and "
            "several of those\ntelephone numbers have been reassigned. Please "
            "suppress the ASSOCIATION between\nthose details and me -- keyed to my "
            "name and date of birth -- and never the\naddress or number in itself. "
            "If your system can only exclude a bare value, please\ndo not apply it "
            "to the former ones at all. I would rather remain findable than\nhave "
            "a stranger's record suppressed on my account."),
        "minimise_tail": (
            "The identifiers above are supplied solely as search keys. If any of "
            "them is a\ncategory you do not otherwise process -- date of birth, "
            "postal addresses and\ntelephone numbers are the usual ones -- please "
            "do not retain it beyond what you\nneed to evidence that you handled "
            "this request. I would rather not have supplied\nyou with data you did "
            "not previously hold, and I list everything only because I\ncannot tell "
            "from outside which keys you use."),
        "mailing_block": (p["address"] + indent +
                          f"{p['city']}, {p['state']} {p['zip_code']}"),
        "scope_block": (
            "This request covers records associated with ANY of the identifiers "
            "listed above —\nevery email address, every prior address, and every "
            "prior telephone number, not\nonly the current ones. Please search "
            "each of them."),
        "email": (p.get("confirmation_email") or p["email"]).lower(),
        "emails": indent.join(email_lines),
        "profile_block": profile_block,
        "suppress_block": SUPPRESS_BLOCK if profiles else "",
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


MINIMISED_NOTE = """
A NOTE ON WHAT I HAVE NOT SENT YOU

I have deliberately left out my date of birth, my postal addresses and my
telephone numbers.

If your records are keyed to cookies, device or connected-TV identifiers, hashed
emails or bid-stream signals -- as I believe they are -- then none of those could
match anything in your systems. They would not be search keys; they would only be
new personal data arriving at a company that did not previously hold it. Sending
them would enlarge exactly the footprint I am writing to reduce.

So this letter carries only my name and my email addresses. If you can in fact
resolve on something else, tell me which identifier types your systems use and I
will supply those and nothing more.
"""


def render(b, prof, to=None, contact=None, keys="full"):
    """`contact` is the mailbox that will actually receive replies. When it differs
    from the profile email (e.g. sending from a different account than the one
    being scrubbed), say so explicitly so the broker searches the right identity
    but answers somewhere reachable."""
    contact = contact or prof["email"]
    prof = dict(prof)
    if keys == "email-only":
        # Strip the name-keyed identifiers and say why, rather than silently
        # sending a thinner letter that reads like an oversight.
        prof["prior_block"] = "\n" + MINIMISED_NOTE
        # The prose that assumes a full identifier list has to go with the data.
        # A minimised letter that still says "I have listed prior addresses
        # deliberately" while listing none reads as careless, and undermines the
        # one thing the minimisation is trying to demonstrate: that the omission
        # was a decision. Caught by reading a generated letter before sending it
        # to 28 recipients (_SILENT_FAILURES 196a).
        prof["ident_intro"] = (
            "I am the consumer, writing about my own data. I am not an authorized "
            "agent acting\nfor anyone else, and every email address listed below is "
            "mine. I list them all so\nthat each can be searched, because records "
            "are frequently held against an address\na person no longer uses.")
        prof["prior_rationale"] = (
            "Several of those addresses are at services that no longer exist. I "
            "list them\nbecause they are exactly the records I cannot check myself "
            "-- nothing sent to them\nwill ever be read by anyone -- and because an "
            "old file is keyed to the address\nsomebody had when the record was "
            "made, not the one they use now.")
        prof["cap_block"] = (
            "One limit, which I would ask you to respect even though it costs me "
            "something:\nif you hold a postal address or telephone number for me, "
            "please suppress the\nASSOCIATION between it and me rather than the "
            "value itself. Other people live at\nmy former addresses now and "
            "several of my old numbers have been reassigned, so\nexcluding a bare "
            "value would remove a stranger from your file. If your system can\n"
            "only exclude bare values, please leave the former ones alone. I would "
            "rather\nremain findable than have someone else suppressed on my "
            "account.")
        prof["minimise_tail"] = (
            "The addresses above are supplied solely as search keys, and nothing "
            "else was\nsupplied at all. If you retain any of them, please retain "
            "only what you need to\nevidence that you handled this request.")
        prof["scope_block"] = (
            "This request covers records associated with any of the email "
            "addresses listed\nabove. Please search each of them, in plaintext "
            "and hashed — MD5, SHA-1 and\nSHA-256, lowercased and trimmed. I "
            "have not computed the hashes myself; you\nshould not have to trust "
            "my arithmetic.")
        # Show these as explicitly withheld rather than dropping the lines:
        # a shorter letter reads like an oversight, a marked one reads like a
        # decision, and the decision is the point.
        for f in ("dob", "phone", "mailing_block"):
            prof[f] = "(withheld -- see the note below)"
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
    ap.add_argument("--keys", choices=("full", "email-only"), default=None,
                    help="identifier set to disclose. 'full' (default) sends "
                         "everything, correct for a name-keyed compiler where a "
                         "partial search returns a false nil. 'email-only' sends "
                         "name and emails only, for a platform keyed to cookies "
                         "or device IDs where postal details cannot match and "
                         "would only be a disclosure. Never inferred silently: "
                         "see suggest_keys().")
    ap.add_argument("--all-blocked", action="store_true")
    args = ap.parse_args()

    reg = {b["id"]: b for b in
           json.loads((ROOT / "data" / "brokers.json").read_text())["brokers"]}
    prof = load_profile()
    OUTDIR.mkdir(exist_ok=True)

    if args.all_blocked:
        sp = state("removal_status.json")
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
        # Never minimise on a guess. The heuristic warns; the operator decides.
        # Over-sending is a bounded disclosure the requester chose to make;
        # under-sending draws a truthful false nil and settles the broker for
        # good. See suggest_keys() and _SILENT_FAILURES 195.
        keys = args.keys or "full"
        hint = suggest_keys(b)
        if hint == "email-only" and keys == "full":
            print(f"  NOTE {bid}: looks identifier-keyed (cookie/device/CTV). "
                  f"A postal address cannot match there and would only be a "
                  f"disclosure -- consider --keys email-only.")
        elif hint == "full" and keys == "email-only":
            print(f"  WARNING {bid}: looks NAME-keyed, but --keys email-only was "
                  f"given. A partial search here can return a truthful 'no "
                  f"record found' that is simply wrong.")
        path = OUTDIR / f"{bid}.eml.txt"
        path.write_text(render(b, prof, args.to, args.contact, keys))
        print(f"  wrote {path}  [keys={keys}]")

    print(f"\n{len(targets)} email(s) in {OUTDIR}/ — review the To: address before sending.")


if __name__ == "__main__":
    main()
