#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Produce the next batch of statutory removal emails to send.

Sending is deliberately paced. A personal mailbox tops out around 500 recipients
a day, and a sudden burst of near-identical messages is what spam heuristics look
for -- getting the sending account limited costs more than the batch gains. Work
through the list steadily instead.

Emits JSON on stdout: [{id, name, to, subject, body}, ...]

Usage:
    ./queue_batch.py --size 15
    ./queue_batch.py --size 15 --min-priority 3
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_optout_email import TEMPLATE, CONTACT_NOTE, load_profile  # noqa: E402
from check_email_domains import deliverable  # noqa: E402


def load_dead_addresses():
    """Addresses observed to hard-bounce. Absent file means nothing is known
    yet, not that everything is fine -- so an empty set, never an error."""
    f = ROOT / "data" / "dead_addresses.json"
    if not f.exists():
        return set()
    return {a.lower() for a in json.loads(f.read_text()).get("addresses", {})}

ROOT = Path(__file__).resolve().parent.parent
from paths import state, outbox  # noqa: E402
REGISTRY = ROOT / "data" / "brokers.json"
STATE = state("removal_status.json")

# Statuses meaning "already handled -- don't re-contact".
# Statuses that mean "do not put this in an email batch". Two groups:
#   - already handled: a request is in flight or the outcome is known;
#   - already ruled out by email: the address bounced, or the only route left is
#     a phone call, a form, or a person.
# The second group was missing, so brokers whose email route had already been
# proved dead kept surfacing at the top of the queue -- and a batch that re-sends
# to a known-bad address spends the daily cap on guaranteed bounces.
DONE = {"submitted", "confirmed", "not_found", "unreachable", "email_pending",
        "failed", "manual_required", "captcha_blocked"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=15)
    ap.add_argument("--min-priority", type=int, default=1)
    ap.add_argument("--summary", action="store_true",
                    help="print a human summary instead of JSON")
    ap.add_argument("--daily-cap", type=int, default=120,
                    help="max emails to send per calendar day (UTC)")
    args = ap.parse_args()

    brokers = json.loads(REGISTRY.read_text())["brokers"]
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    prof = load_profile()

    # Count today's sends from the attempt history so an unattended loop cannot
    # exceed the mailbox's daily limit. Tripping Gmail's abuse detection would
    # cost far more than the extra batch gains.
    today = datetime.now(timezone.utc).date().isoformat()

    # Count today's *email* sends. The channel is recorded on the history entry
    # (tracker.py --via email). Entries predating that flag fall back to the old
    # mailto: heuristic, and anything still unattributable is counted anyway --
    # over-counting pauses sending a little early, under-counting risks the
    # mailbox itself, and only one of those is recoverable.
    #
    # This counted 17 of 94 sends on the day it was written, because the mailto:
    # heuristic depended on a URL the recording step did not set. A cap that
    # silently measures nothing is worse than no cap: it reports a comfortable
    # number while the real figure runs away.
    sent_today = 0
    for rec in state.values():
        legacy_email = "mailto:" in (rec.get("optout_url_used") or "")
        for h in rec.get("history", []):
            if not h.get("at", "").startswith(today):
                continue
            if h.get("status") != "submitted":
                continue
            via = h.get("via")
            # Only fresh outbound letters count. A 'reply' is a message into a
            # thread that already exists, so it costs the recipient nothing new
            # and must not consume the budget for contacting brokers who have
            # never been written to.
            if via == "email" or (via is None and legacy_email) or via is None:
                sent_today += 1
    remaining = max(0, args.daily_cap - sent_today)
    if remaining == 0:
        print(f"daily cap reached ({sent_today}/{args.daily_cap} sent today) - "
              f"stop sending until tomorrow", file=sys.stderr)
        if not args.summary:
            json.dump([], sys.stdout)
        return 0

    # An address whose corporate relationship to the broker is unconfirmed must
    # never be auto-sent. These letters carry a full identifier set -- every
    # prior address, every prior phone number, a date of birth -- so a wrong
    # route is not a wasted send, it is a disclosure to an unrelated company
    # caused by the removal effort itself. firstadvantage.com redirects to a
    # real-estate brokerage, and the scrape duly proposed a real-estate software
    # vendor's support desk as First Advantage Corporation's privacy contact.
    # See verify_emails.py DISCOVERED_OFFDOMAIN.
    HOLD = {"offdomain_needs_confirmation", "domain_corrected_needs_rediscovery"}
    held = [b["id"] for b in brokers
            if b.get("email_to") and b.get("email_verified_by") in HOLD
            and state.get(b["id"], {}).get("status", "pending") not in DONE]
    # One address, one letter. The state filings frequently register a corporate
    # family under a single contact -- "Alliant" and "Alliant Cooperative Data
    # Solutions LLC" are one company on one mailbox, and Stirista's registration
    # names thirteen brands behind one address. Left alone, the queue writes to
    # that mailbox once per row.
    #
    # A second letter to a desk that has already answered is not a free retry. It
    # reads as either not having read the reply or as pressure, it spends a slot
    # from the daily cap, and it costs the credibility the next letter depends on.
    # So an address already spoken for by a broker in a non-pending state is
    # skipped -- the earlier thread is the live one, and any sibling should be
    # raised inside it rather than opened as a new request.
    spoken_for = {}
    for b in brokers:
        e = (b.get("email_to") or "").lower()
        if e and state.get(b["id"], {}).get("status", "pending") != "pending":
            spoken_for.setdefault(e, b["id"])
    dup = [(b["id"], spoken_for[(b.get("email_to") or "").lower()]) for b in brokers
           if (b.get("email_to") or "").lower() in spoken_for
           and state.get(b["id"], {}).get("status", "pending") == "pending"]
    if dup:
        print(f"holding {len(dup)} broker(s) whose contact address already has an "
              f"open thread: " + ", ".join(f"{a}->{c}" for a, c in sorted(dup)[:6])
              + (" ..." if len(dup) > 6 else ""), file=sys.stderr)
    dup_ids = {a for a, _ in dup}

    pool = [
        b for b in brokers
        if b.get("email_to")
        and not b.get("duplicate_of")
        and b["id"] not in dup_ids
        and b.get("email_verified_by") not in HOLD
        and b.get("priority", 0) >= args.min_priority
        and state.get(b["id"], {}).get("status", "pending") not in DONE
    ]
    if held:
        # Never drop a bounded set silently: a queue that quietly excludes work
        # reads as "nothing left to do".
        print(f"holding {len(held)} broker(s) whose address is on another "
              f"company's domain and unconfirmed: {', '.join(sorted(held)[:8])}"
              + (" ..." if len(held) > 8 else ""), file=sys.stderr)
    # Highest leverage first: aggregators before niche sites.
    pool.sort(key=lambda b: (-b.get("priority", 0), b["id"]))

    # Check deliverability on the way out, not once in a while.
    #
    # arrakis.ai was NXDOMAIN and crawlbee.com published a null MX -- an explicit
    # RFC 7505 refusal of all mail -- and both were queued and sent to anyway,
    # because nothing consulted the checker at send time. A domain that died
    # after the last sweep is indistinguishable from one that was never swept,
    # and the cost is not just a wasted send: the broker gets marked `submitted`
    # and the request is believed to be in flight when it never left.
    #
    # Only the batch is checked, not the whole pool, so this stays a handful of
    # DNS lookups. `None` (lookup failed) is treated as sendable on purpose --
    # condemning a broker on a transient resolver error is the expensive
    # direction of this mistake.
    #
    # The domain check is only half of it. A domain can resolve, answer on its
    # MX, and still have no such mailbox -- privacy@researchusallc.com and
    # privacy@databaseusa.com both 550 while every domain-level check passes,
    # and both are the addresses those companies filed with California as their
    # consumer contact. Nothing short of sending finds that out, so once a
    # bounce has been seen it gets written into data/dead_addresses.json and
    # consulted here. Otherwise the knowledge lives only in removal_status,
    # which the send path never reads -- which is exactly how a letter went to
    # ops@findtrueowner.com a day after that broker was marked unreachable.
    dead_addrs = load_dead_addresses()

    batch, dead, dead_mailbox = [], [], []
    for b in pool:
        if len(batch) >= min(args.size, remaining):
            break
        addr = (b.get("email_to") or "").lower().strip()
        if addr in dead_addrs:
            dead_mailbox.append((b["id"], addr))
            continue
        domain = addr.split("@")[-1]
        verdict = deliverable(domain) if domain else None
        if verdict is False:
            dead.append((b["id"], domain))
            continue
        batch.append(b)
    if dead_mailbox:
        print(f"holding {len(dead_mailbox)} broker(s) whose address has already "
              f"hard-bounced: "
              + ", ".join(f"{i} ({a})" for i, a in dead_mailbox[:6])
              + (" ..." if len(dead_mailbox) > 6 else "")
              + " -- find another address before spending a send",
              file=sys.stderr)
    if dead:
        print(f"holding {len(dead)} broker(s) whose contact domain accepts no "
              f"mail (NXDOMAIN or null MX): "
              + ", ".join(f"{i} ({d})" for i, d in dead[:6])
              + (" ..." if len(dead) > 6 else "")
              + " -- mark these unreachable or find another address",
              file=sys.stderr)

    out = []
    for b in batch:
        subject = ("Consumer Request to Delete and Opt Out of Sale of "
                   f"Personal Information — {prof['name']}")
        body = TEMPLATE.format(
            to=b["email_to"], broker=b.get("name", b["id"]),
            contact=prof["email"], contact_note="", **prof)
        # Drop the To:/Subject: header lines -- the mail tool sets those.
        body = body.split("\n", 2)[2].lstrip("\n")
        out.append({"id": b["id"], "name": b.get("name", b["id"]),
                    "to": b["email_to"], "priority": b.get("priority"),
                    "subject": subject, "body": body})

    if args.summary:
        print(f"{len(pool)} brokers still to contact by email.")
        print(f"sent today: {sent_today}/{args.daily_cap} "
              f"(room for {remaining} more)\n")
        for r in out:
            print(f"  p{r['priority']}  {r['id']:32} {r['to']}")
    else:
        json.dump(out, sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
