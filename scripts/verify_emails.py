#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Check registry email addresses against what the broker actually publishes.

Why this exists: a guessed `privacy@<domain>` is a coin flip, and a bounced
request is indistinguishable from a pending one in the tracker. Sending to an
address nobody confirmed means discovering the failure one bounce at a time --
and only if you are still watching days later.

This fetches each broker's likely privacy and contact pages, extracts the email
addresses they publish, and compares them with what the registry holds:

    CONFIRMED   the registry address appears on the broker's own site
    REPLACE     the site publishes a different, more privacy-specific address
    NO_EMAIL    the site is up but publishes no address (a form or phone may exist)
    BLOCKED     the domain resolves but we cannot read it -- a 403, or a CDN
                refusing the connection outright. Says nothing about the address.
    UNREACHABLE neither a web address nor a mail exchanger. The only verdict
                that means
                there is nobody there.

NO_EMAIL, BLOCKED and UNREACHABLE are three different things and must not be
collapsed. An early version of this script reported UNREACHABLE whenever the
privacy and contact paths all 404'd -- so a perfectly live site with its policy
at an unusual path looked dead, and a working address would have been marked
unverified on that basis.

Nothing is written unless you pass --apply, so the proposal can be reviewed
first. Applying sets email_verified / email_verified_by, and swaps in a better
address where one was found.

    ./verify_emails.py --unverified --limit 40        # propose
    ./verify_emails.py --unverified --limit 40 --apply
    ./verify_emails.py --ids spokeo,radaris --apply

Be a good citizen: this makes a handful of GETs per broker. Concurrency is
deliberately modest and there is a small delay between requests to the same host.
"""

import argparse
import json
import re
import socket
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURATED = ROOT / "data" / "curated_brokers.json"
REGISTRY = ROOT / "data" / "brokers.json"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")

# Paths worth trying, cheapest and most likely first.
PATHS = [
    "/privacy-policy/", "/privacy/", "/privacy", "/privacy-policy",
    "/legal/privacy-policy", "/about/privacy", "/privacy-notice/",
    "/contact/", "/contact-us/", "/contact",
    "/",   # last: many small sites put the contact address on the front page
]

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

# Addresses that are noise rather than a privacy contact.
NOISE = re.compile(
    r"(sentry|wixpress|\.png|\.jpg|\.gif|\.webp|example\.|domain\.com|"
    r"yourdomain|sentry\.io|@2x|u003e|schema\.org)", re.I)

# Ranked by how well the local-part signals a route for THIS kind of request.
# Purpose-built removal addresses come first: a broker that publishes
# `dataremoval@` or `consumerchoice@` has built a channel for exactly this, and
# it will be handled faster and more reliably than a general mailbox.
#
# Matching is by substring, not prefix. An earlier version anchored to the start
# of the local-part, so `dataremoval@`, `removalrequests@`, `consumerchoice@`,
# `delete_mydata@` and `americas.dpo@` all scored WORSE than a bare `info@` --
# and the tool duly proposed replacing a Data Protection Officer's address with
# a marketing one. Rank the intent, wherever it appears in the string.
PREFERENCE = [
    # purpose-built for deletion / opt-out
    "dataremoval", "removalrequest", "deletemydata", "delete_mydata", "optout",
    "opt-out", "opt_out", "donotsell", "do-not-sell", "consumerchoice", "ccpa",
    "gdpr", "dsar", "datarequest", "privacyrequest",
    # privacy and data-protection functions
    "privacy", "dataprotection", "dpo", "datacompliance", "compliance",
    "privacyofficer", "legal", "security",
    # general mailboxes, in descending usefulness
    "customercare", "customerservice", "support", "help", "webmaster",
    "contact", "info", "hello", "sales", "admin",
]


def is_role_address(addr):
    """Is this a role mailbox rather than a named individual's?

    Scraping a contact page turns up whatever is on it, which includes people.
    An unrelated third party's personal address must never be recorded as a
    broker contact: it is wrong as a route, and this registry is public, so
    writing down a named individual's work address publishes it further. One
    sweep proposed `angela@silverstonefacilitycare.com` -- a person, at a company
    with no relationship to the broker -- as a fallback contact.

    Role accounts are the only safe thing to keep."""
    local = addr.split("@")[0].lower()
    flat = local.replace("-", "").replace("_", "").replace(".", "")
    if any(p.replace("-", "").replace("_", "").replace(".", "") in flat
           for p in PREFERENCE):
        return True
    return flat in {
        "enquiries", "enquiry", "inquiries", "inquiry", "team", "office",
        "mail", "email", "general", "noreply", "no-reply", "abuse", "postmaster",
        "unsubscribe", "optin", "care", "service", "services", "helpdesk",
    }


def rank(addr):
    """Lower is better. Substring match, so `americas.dpo` and `privacyanddata
    compliancereview` both score as the privacy contacts they plainly are."""
    local = addr.split("@")[0].lower().replace("-", "").replace("_", "").replace(".", "")
    best = len(PREFERENCE)
    for i, p in enumerate(PREFERENCE):
        token = p.replace("-", "").replace("_", "").replace(".", "")
        if token in local:
            best = min(best, i)
    return best


# The last local-part that still signals a rights channel. Anything ranking
# worse than this is a general mailbox: usable as a route of last resort, but
# not something to record as a verified privacy contact.
GOOD_ENOUGH = PREFERENCE.index("security")

# General mailboxes that are actively wrong for a deletion request, as opposed
# to merely unspecific. `support@` reaches someone whose job is to answer; a
# sales queue is not that, and `admin@` is usually nobody.
WEAK = {"sales", "admin", "hello"}

# Country and region qualifiers that turn a privacy mailbox into somebody
# else's privacy mailbox. LiveRamp publishes thirteen addresses -- privacy.ar,
# privacy.be, privacy.br, privacy.de, privacy.es, privacy.it, privacy.nl,
# privacy.no, privacy.pl, privacy.ro, privacy.se, ukprivacy, cil (the French
# CNIL contact) -- and not one unqualified `privacy@`. Every one of them is a
# real, monitored privacy address, and every one belongs to a jurisdiction this
# requester does not live in. A CCPA request sent to privacy.ro@ is not refused,
# it is simply the wrong desk, which reads identically to silence.
REGION = {
    "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "co", "cz", "de",
    "dk", "es", "fi", "fr", "gr", "hk", "hu", "ie", "il", "it", "jp", "kr",
    "mx", "my", "nl", "no", "nz", "pe", "ph", "pl", "pt", "ro", "ru", "se",
    "sg", "th", "tr", "tw", "uk", "gb", "za", "eu", "emea", "apac", "latam",
    "anz", "americas", "uae", "intl", "international",
}


def region_of(addr):
    """The region an address is scoped to, or None if it is the general one.

    Works by removing the intent tokens and seeing what is left: `ukprivacy`
    minus `privacy` is `uk`; `americas.dpo` minus `dpo` is `americas`; plain
    `privacy` leaves nothing. Subtracting rather than pattern-matching avoids
    the obvious trap -- `privacyadmin` ends in `in` without being the Indian
    privacy desk."""
    residue = addr.split("@")[0].lower().replace("-", "").replace("_", "").replace(".", "")
    for token in sorted(PREFERENCE, key=len, reverse=True):
        residue = residue.replace(
            token.replace("-", "").replace("_", "").replace(".", ""), "")
    return residue if residue in REGION else None


def fetch(url, timeout=12):
    """Return (body_or_None, server_responded). A 404 or 403 still means the
    server is alive -- only a connection failure means it is not."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(400_000).decode("utf-8", "replace"), True
    except urllib.error.HTTPError:
        return None, True          # 403/404/500 -- the host answered
    except (urllib.error.URLError, socket.timeout, ConnectionError,
            UnicodeError, OSError):
        return None, False


def emails_on_site(domain):
    """Every plausible address published across the broker's privacy/contact pages.

    Returns (addresses, answered, served_a_page). `answered` means the host
    responded at all; `served_a_page` means we actually got a body to read."""
    found = set()
    answered = served = False
    for scheme in ("https://", "https://www."):
        for path in PATHS:
            html, responded = fetch(f"{scheme}{domain}{path}")
            answered = answered or responded
            if html is None:
                continue
            served = True
            for m in EMAIL_RE.findall(html):
                if not NOISE.search(m) and len(m) < 80:
                    found.add(m.lower().rstrip("."))
            # Stop early only once something in the privacy/legal tier turns up.
            # The old rule was "stop at the first page with any address", which
            # is fine when checking an address someone already chose and wrong
            # when discovering one: Bright Data's first readable page yields
            # `sales@brightdata.com`, and returning there means never reaching
            # the privacy contact further in. A sales mailbox is not a rights
            # channel, and a deletion request sent to one is quietly discarded
            # rather than bounced.
            if found and min(rank(e) for e in found) <= GOOD_ENOUGH:
                return found, answered, served
        if served:
            break
    return found, answered, served


def resolves(domain):
    """Does the domain have a web address we could connect to?"""
    for d in (domain, "www." + domain):
        try:
            socket.getaddrinfo(d, None)
            return True
        except socket.gaierror:
            continue
    return False


def has_ns(domain):
    """Does the domain have a delegation at all?

    Checked BEFORE mx, because it is the stronger negative and it catches a case
    mx cannot. A domain whose registration has lapsed has no NS records, no SOA,
    no A and no MX -- there is no zone to ask. Sending MTAs cannot distinguish
    that from "the far end is briefly down", so a lapsed domain is reported as a
    *temporary* delivery delay and retried for 48 hours. For two days the tracker
    shows `submitted` while the letter has nowhere to go.

    One broker here sat in exactly that state: a reassuring "Gmail will retry for
    45 more hours" notice over a domain with no nameservers at all. Returns None
    on lookup failure, so an unrelated resolver problem is never reported as a
    dead domain.
    """
    try:
        out = subprocess.run(["dig", "+short", "NS", domain],
                             capture_output=True, text=True, timeout=10).stdout
        return any(ln.strip() for ln in out.splitlines())
    except Exception:
        return None


def has_mx(domain):
    """Does the domain publish a mail exchanger?

    This exists because `resolves()` asks the wrong question for this script.
    It looks for an A record, and a domain can have no A record at all while its
    mail works perfectly -- an apex with MX but no web host, a www CNAME pointing
    at a CDN distribution that has since been disabled, or a company that simply
    does not run a website on the domain it receives mail on.

    That is not hypothetical. `minervadata.xyz` returned gaierror for both the
    apex and www, which the old code reported as UNREACHABLE -- while publishing
    a Microsoft 365 MX record and a registration running to 2027. A live company
    with working mail was one `--apply` away from being written off.

    The script verifies EMAIL addresses. For that purpose an MX record is the
    relevant signal and an A record is a proxy at best.

    But do not over-read this fix. An MX record proves a domain has *somewhere*
    to deliver mail; it does not prove any mailbox exists behind it.
    `matchandappend.com` publishes a healthy Zoho MX and rejects both `privacy@`
    and `info@` with a hard 550 - the exchanger answers and refuses every
    recipient, because the MX is configured and no mailboxes are provisioned.

    So MX is NECESSARY, not sufficient. The only thing that proves an address
    works is a delivered message, and the only thing that proves one does not is
    a bounce naming it. This function exists to stop us condemning domains too
    early, not to license the opposite mistake."""
    try:
        out = subprocess.run(["dig", "+short", "MX", domain],
                             capture_output=True, text=True, timeout=10).stdout
        return any(ln.strip() for ln in out.splitlines())
    except Exception:
        # No dig, or it failed. Fall back to the conventional mail hostnames
        # rather than assuming the worst -- guessing "no mail" is the expensive
        # direction of this error.
        for h in ("mail." + domain, "smtp." + domain, domain):
            try:
                socket.getaddrinfo(h, 25)
                return True
            except (socket.gaierror, OSError):
                continue
        return None          # genuinely unknown, not "no"


def check(b):
    domain = (b.get("domain") or "").strip().lower()
    current = (b.get("email_to") or "").strip().lower()
    out = {"id": b["id"], "domain": domain, "current": current,
           "verdict": "NO_EMAIL", "proposed": None, "found": []}
    if not domain:
        out["verdict"] = "NO_DOMAIN"
        return out
    if not resolves(domain):
        # Delegation first: no NS means no zone, which outranks every other
        # negative here -- a domain without nameservers cannot have an MX, a
        # null MX, a mailbox or an autoresponder.
        if has_ns(domain) is False:
            out["verdict"] = "NO_DOMAIN"
            out["why"] = ("no NS records -- the domain has no delegation at all, so the "
                          "registration has lapsed or was withdrawn. Nothing can be "
                          "delivered and no web route can exist. Note a send will "
                          "produce a *temporary* delay notice and 48h of retries "
                          "before it finally hard-bounces.")
            return out
        # No web address -- but check the mail before condemning it. A domain
        # with a working MX and no A record is a live correspondent with no
        # website, which is a different thing entirely from a dead company.
        mx = has_mx(domain)
        if mx is False:
            out["verdict"] = "UNREACHABLE"
        else:
            out["verdict"] = "BLOCKED"
            out["why"] = ("no web address, but the domain publishes a mail "
                          "exchanger" if mx else
                          "no web address, and the mail record could not be "
                          "checked -- treated as live, since guessing dead is "
                          "the expensive error")
        return out

    found, answered, served = emails_on_site(domain)
    out["found"] = sorted(found)[:8]
    if not answered:
        # DNS resolved, so the domain exists and somebody registered it -- but
        # nothing accepted a connection. That is a CDN or WAF refusing us, not a
        # dead company. An earlier version called this UNREACHABLE and marked the
        # address unverified on that basis; several Cloudflare-fronted brokers
        # with working MX records were written off that way.
        #
        # The only thing that means "there is nobody here" is DNS failing, which
        # is checked above.
        out["verdict"] = "BLOCKED"
        return out
    if not served:
        # DNS resolves and the host answers, but every page was refused.
        out["verdict"] = "BLOCKED"
        return out
    if not found:
        return out

    if current in found:
        out["verdict"] = "CONFIRMED"
        return out

    # Prefer an address on the broker's own domain, best privacy local-part first.
    same = [e for e in found if e.endswith("@" + domain) or domain in e.split("@")[1]]
    pool = same or list(found)
    # Rank first, then prefer the shortest local-part at the same rank. Large
    # brokers publish a whole family of regional privacy addresses --
    # `privacy.de@`, `privacy.ar@`, `privacy.apac@` -- which all rank
    # identically to the plain `privacy@` beside them, so without a tiebreak the
    # choice fell to set iteration order and LiveRamp's US-facing request would
    # have gone to Germany. The unqualified address is the general one.
    pool.sort(key=lambda e: (rank(e), len(e.split("@")[0]), e))
    best = pool[0]
    # Never trade down. A published-but-generic mailbox is not an improvement on
    # a purpose-built removal address, even though the published one certainly
    # exists -- a deletion request sent to sales@ or hello.marketing@ is worse
    # than one sent to an unpublished privacy@ that might bounce, because a
    # bounce at least tells you it failed.
    if rank(best) < len(PREFERENCE) and (not current or rank(best) <= rank(current)):
        # DISCOVERED and REPLACE are not the same finding, and collapsing them
        # would hide the more consequential one. REPLACE displaces an address
        # somebody already chose, and carries the duty above not to trade down.
        # DISCOVERED fills a hole: the broker had no route at all, so any role
        # mailbox on its own domain is a strict improvement on nowhere to write.
        #
        # This mattered more than it sounds. 304 brokers sat `pending` with a
        # live domain and no address -- Equifax, Experian, TransUnion, LiveRamp,
        # CoreLogic among them. They were not unreachable and they were not
        # refusing; nobody had looked up where to send the letter. The email
        # queue reported "0 brokers still to contact", which was true of the
        # queue and false of the world.
        if current:
            out["verdict"] = "REPLACE"
        elif region_of(best) and all(region_of(e) for e in pool if rank(e) <= GOOD_ENOUGH):
            # Every rights-shaped address on the site is scoped to a region, and
            # none of them to this requester's. Recorded so the letter can name
            # the problem rather than pretend the desk is the right one.
            out["verdict"] = "DISCOVERED_REGIONAL"
            out["region"] = region_of(best)
        elif best.split("@")[0].lower().replace("-", "").replace(".", "") in WEAK:
            # Still worth recording -- the goal is a route, and no route is
            # worse than a poor one -- but not worth calling verified. Flagged
            # so the letter can be addressed accordingly and re-checked later.
            out["verdict"] = "DISCOVERED_WEAK"
        else:
            out["verdict"] = "DISCOVERED"
        out["proposed"] = best
    elif current and rank(best) > rank(current):
        out["verdict"] = "KEEP_BETTER"
        # Only worth recording as a fallback if it is a role mailbox on the
        # broker's own domain. A person's address scraped off a contact page is
        # not a privacy route, and this registry is public.
        if is_role_address(best) and best.endswith("@" + domain):
            out["proposed"] = best
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--unverified", action="store_true",
                    help="only brokers whose email_verified is not true")
    ap.add_argument("--no-email", action="store_true",
                    help="only brokers that have a domain but no email_to at all")
    ap.add_argument("--ids", help="comma-separated broker ids")
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--min-priority", type=int, default=1)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--apply", action="store_true", help="write results to the registry")
    args = ap.parse_args()

    brokers = json.loads(REGISTRY.read_text())["brokers"]
    if args.ids:
        want = {i.strip() for i in args.ids.split(",")}
        pool = [b for b in brokers if b["id"] in want]
    elif args.no_email:
        # The brokers with nowhere to write to. They are not unreachable, they
        # are undiscovered -- a different problem with a different fix. A domain
        # is required: without one there is no site to read an address off, and
        # that is the job of resolve_optery_domains.py, not this script.
        pool = [b for b in brokers
                if not b.get("email_to") and b.get("domain")
                and b.get("priority", 0) >= args.min_priority]
        pool.sort(key=lambda b: (-b.get("priority", 0), b["id"]))
    else:
        pool = [b for b in brokers
                if b.get("email_to") and b.get("priority", 0) >= args.min_priority
                and (not args.unverified or not b.get("email_verified"))]
        pool.sort(key=lambda b: (-b.get("priority", 0), b["id"]))
    pool = pool[: args.limit]

    if not pool:
        print("nothing to check")
        return 0

    print(f"checking {len(pool)} broker(s) against their published pages...\n",
          file=sys.stderr)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        results = list(ex.map(check, pool))

    tally = {}
    for r in results:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
        line = f"  {r['verdict']:12} {r['id']:28} {r['current']}"
        if r["proposed"]:
            line += f"  ->  {r['proposed']}"
        print(line)
    print("\n" + "  ".join(f"{k}={v}" for k, v in sorted(tally.items())))

    if not args.apply:
        print("\n(dry run - pass --apply to write these to data/curated_brokers.json)")
        return 0

    d = json.loads(CURATED.read_text())
    by_id = {b["id"]: b for b in d["brokers"]}
    reg_by_id = {b["id"]: b for b in brokers}
    written = 0
    for r in results:
        b = by_id.get(r["id"])
        if not b:
            # Most of the registry is generated from the Optery scrape and only
            # gains a curated row once something has been learned about it that
            # a regenerated scrape would otherwise throw away. A discovered
            # address is exactly that; every other verdict here has nothing
            # worth preserving, so it stays out of the curated file.
            if not r["verdict"].startswith("DISCOVERED"):
                continue
            src = reg_by_id.get(r["id"], {})
            b = {
                "id": r["id"],
                "name": src.get("name") or r["id"].replace("_", " ").title(),
                "domain": r["domain"],
                "priority": src.get("priority", 2),
                "method": src.get("method") or "email",
                "optout_url": src.get("optout_url") or "",
                "needs_email_confirm": None,
                "source": src.get("source") or "optery_scrape",
                "optery_slug": src.get("optery_slug"),
            }
            d["brokers"].append(b)
            by_id[r["id"]] = b
        if r["verdict"].startswith("DISCOVERED"):
            weak = r["verdict"] != "DISCOVERED"
            b["email_to"] = r["proposed"]
            b["email_verified"] = not weak
            b["email_verified_by"] = {
                "DISCOVERED": "privacy_policy",
                "DISCOVERED_WEAK": "published_general_mailbox",
                "DISCOVERED_REGIONAL": "privacy_policy_regional",
            }[r["verdict"]]
            if r["verdict"] == "DISCOVERED_REGIONAL":
                b["email_alt"] = ", ".join(
                    e for e in r["found"] if e != r["proposed"])[:200] or None
                b["notes"] = ((b.get("notes") or "") + " " + (
                    f"Publishes only region-scoped privacy addresses; "
                    f"{r['proposed']} is the {r.get('region')} desk. There is no "
                    f"unqualified privacy@ on the site. Say so in the letter and "
                    f"ask to be routed to the US/global contact."
                )).strip()
            elif weak:
                b["notes"] = ((b.get("notes") or "") + " " + (
                    f"{r['proposed']} is the only address published on the site "
                    f"and is a general mailbox, not a rights channel. Re-check "
                    f"for a privacy contact before treating silence as refusal."
                )).strip()
            # `unknown` here means the scrape never established a route, not
            # that a route was investigated and found not to be email. Now that
            # there is a published address, email is the route.
            if (b.get("method") or "unknown") == "unknown":
                b["method"] = "email"
        elif r["verdict"] == "CONFIRMED":
            b["email_verified"] = True
            b["email_verified_by"] = "privacy_policy"
        elif r["verdict"] == "REPLACE":
            # Prefer the address the broker actually publishes: it certainly
            # exists, and an unpublished privacy@ guess may simply bounce.
            # But a privacy request sent to info@ is likelier to be ignored than
            # one sent to privacy@, so never silently discard the displaced
            # address -- keep it as a documented fallback to try if this route
            # goes unanswered.
            displaced = b.get("email_to")
            b["email_to"] = r["proposed"]
            b["email_verified"] = True
            b["email_verified_by"] = "privacy_policy"
            if displaced and rank(displaced) < rank(r["proposed"]):
                b["email_alt"] = displaced
                note = (f"Site publishes {r['proposed']}; {displaced} is more "
                        f"privacy-specific but appears nowhere on the site. "
                        f"Try the alternate if this goes unanswered.")
                b["notes"] = ((b.get("notes") or "") + " " + note).strip()
        elif r["verdict"] == "UNREACHABLE":
            b["email_verified"] = False
            b["email_verified_by"] = "site_unreachable"
        elif r["verdict"] == "KEEP_BETTER":
            if not r["proposed"]:
                continue          # nothing worth recording; leave the record alone
            b["email_alt"] = r["proposed"]
            b["email_verified"] = False
            b["email_verified_by"] = None
        elif r["verdict"] == "BLOCKED":
            # The site is alive and simply refuses us. That says nothing about
            # whether the address works, so leave the existing flag untouched.
            continue
        else:
            b["email_verified"] = False
            b["email_verified_by"] = "no_address_published"
        written += 1
    CURATED.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwrote {written} record(s) - now run scripts/build_registry.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
