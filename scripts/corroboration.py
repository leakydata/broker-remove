#!/usr/bin/env python3
"""How much of "submitted" is actually corroborated?

§304: volume is not communication. §138: a send is not a receipt. §393 found
seven rows resting on a send and nothing else, and the obvious next question
is how many others do.

A row is CORROBORATED when something came back from the company: a reference
or ticket number, a reply in the thread, an acknowledgement, a confirmation
page quoted verbatim. It is UNCORROBORATED when the only evidence is that a
message left this side.

That distinction is the difference between "I asked" and "they heard", and it
is the one a status of `submitted` quietly elides. This script does not change
any status. It reports what the statuses are standing on.
"""
import json, re, sys
from collections import Counter

# things that only exist if the company produced them
TICKET = re.compile(
    r"\b(?:ticket|case|ref(?:erence)?|request|confirmation|rma|sr|inc)\s*"
    r"(?:number|no\.?|id|#)?\s*[:#]?\s*[A-Z0-9][A-Z0-9-]{4,}\b", re.I)
REPLIED = re.compile(
    r"\breplied\b|\breply\b|\bthey (?:said|wrote|answered|confirmed|told)\b|"
    r"\bauto[- ]?repl|\backnowledg|\bconfirmed by\b|\banswered\b|"
    r"\bresponded\b|\btheir (?:reply|answer|response)\b|"
    r"\bwe (?:have )?(?:received|completed)\b|"
    # a company speaking in the first person plural, quoted back into the note.
    # These were missed on the first pass and four `confirmed` rows that quote
    # an actual deletion were being scored as uncorroborated. See SF 399.
    r"\bwe (?:have|had|are|do not|don't|located|deleted|checked|agree|confirm)\b|"
    r"\bwe(?:'ve| have) (?:added|processed|removed|suppressed)\b|"
    r"\bour systems\b|\bcompletion email|\bhas been completed\b|"
    r"\bunable to (?:locate|find)\b|\bno (?:records?|match|data) (?:were |was )?found\b",
    re.I)

# a sentence quoted from the company is itself evidence something came back
QUOTED = re.compile(r"[\"'‘’“”][^\"'‘’“”]{25,}"
                    r"[\"'‘’“”]")
BOUNCE = re.compile(r"\bbounce|\b550\b|\b451\b|mailbox is full|address not found", re.I)
VERBATIM = re.compile(r"['\"‘’“”]")

# evidence produced by US rather than by the company: a search of their own
# interface, a query against the upstream source, a fetch that returned nothing.
# This is a THIRD kind of evidence and it was being scored as "a send and
# nothing else". It is not weaker than a company's word -- it is re-runnable,
# which their word is not -- but it only covers what the interface exposes.
# See _SILENT_FAILURES 401.
SELF_VERIFIED = re.compile(
    r"\bsearched (?:their|the|it|his|202\d)|\bqueried\b|\bI checked\b|"
    r"\bverified directly\b|\bchecked (?:properly|in a browser|their)\b|"
    r"\breturns? ['\"‘’“”]?no result|\bno (?:record|listing|entry) (?:for|found)|"
    r"\bthe (?:public )?API\b|\bfetched\b|\bre-?tested\b|"
    r"\bsettled at the source\b|\bnot a broker\b|\bholds? nothing\b",
    re.I)

SENT_ONLY = re.compile(
    r"statutory (?:delete|opt-out)|request emailed|letter sent|sent \d{4}-\d{2}-\d{2}|"
    r"^\d{4}-\d{2}-\d{2} sent", re.I)


def classify(rec):
    note = rec.get("note") or ""
    refs = rec.get("refs") or rec.get("confirmation_ref") or ""
    hist = rec.get("history") or []

    # a gmail: ref is our OWN sent message id -- it proves a send, not a receipt
    real_ref = bool(refs) and not re.fullmatch(r"\s*gmail:[0-9a-f]+\s*", str(refs))

    if real_ref:
        return "corroborated", "reference or confirmation recorded"
    if TICKET.search(note):
        return "corroborated", "ticket or case number in note"
    if REPLIED.search(note):
        return "corroborated", "reply described in note"
    if QUOTED.search(note) and re.search(r"\bwe\b|\bour\b|\byour (?:request|data|information)\b",
                                        note, re.I):
        return "corroborated", "company sentence quoted in note"
    if BOUNCE.search(note):
        return "adverse", "the only thing that came back was a bounce"
    if SELF_VERIFIED.search(note):
        return "self-verified", "checked directly rather than taken on their word"
    if len(hist) > 2:
        return "weak", f"{len(hist)} status changes but nothing quoted back"
    return "uncorroborated", "a send and nothing else"


def main():
    data = json.load(open("data/removal_status.json"))
    recs = data.get("records", data)

    want = sys.argv[1] if len(sys.argv) > 1 else "submitted"
    rows = {k: v for k, v in recs.items() if v.get("status") == want}

    buckets = Counter()
    detail = {}
    for k, v in rows.items():
        b, why = classify(v)
        buckets[b] += 1
        detail.setdefault(b, []).append((k, why))

    total = len(rows)
    print(f"status = {want}   ({total} rows)\n")
    for b in ("corroborated", "self-verified", "weak", "adverse",
              "uncorroborated"):
        n = buckets.get(b, 0)
        if not n:
            continue
        pct = 100.0 * n / total if total else 0
        print(f"  {b:16} {n:5}   {pct:5.1f}%")

    unc = detail.get("uncorroborated", [])
    if unc:
        print(f"\n=== resting on a send and nothing else ({len(unc)})")
        for k, _ in sorted(unc)[:60]:
            print(f"  {k}")
        if len(unc) > 60:
            print(f"  ... and {len(unc)-60} more")

    print("""
  self-verified means WE established it -- searched their site, queried the
  upstream source -- rather than the company saying so. Re-runnable, which
  their word is not; but it only covers what the interface exposes (SF 388).

  This is NOT a list of failures. A company that received a letter and has
  said nothing is inside its response window until it is not, and silence
  from a company that holds nothing about you is the commonest outcome in
  this project. What the number measures is how much of `submitted` is
  standing on our own outbox rather than on anything the other side did.
  See _SILENT_FAILURES 304, 138, 393.""")

    json.dump({b: [k for k, _ in v] for b, v in detail.items()},
              open("data/corroboration.json", "w"), indent=1)
    print("\nwrote data/corroboration.json")


if __name__ == "__main__":
    main()
