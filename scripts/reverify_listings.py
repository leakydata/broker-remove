#!/usr/bin/env python3
"""Is the subject still listed on the sites that said they removed him?

Every `confirmed` row in this project is a claim about the day it was made. A
people-search index is rebuilt from supplier feeds on a cycle, and §400, §396
and §398 all converge on the same question: does a suppression persist, or does
the record come back? Nobody has checked.

This checks. It is READ-ONLY: it issues the same public search a stranger could
issue, submits no form, sends no identifier the site does not already claim to
hold, and stores nothing.

ON THE OBVIOUS OBJECTION -- that searching for the subject at a company we have
asked to hold less is itself an exposure. It is, slightly, and the trade is
worth naming rather than hiding:

  - A search query creates a log line at a company that sells search data.
  - Not searching means every `confirmed` row stays a claim about August.

The project already resolved this once, in favour of checking: §401 records
free_people_directory and npi_profile as SELF-VERIFIED nils, established by
searching the company's own interface rather than taking its word. The same
reasoning applies here, and a verification that can be re-run is worth more
than a confirmation that cannot. One query per site, once.

WHAT IT CANNOT TELL YOU: absence from a public search is not absence from the
file. §388 is the warning -- a search whose granularity is coarser than the
question returns an empty result that means "nobody looked", not "nothing is
there". A NOT-LISTED verdict here means the record is not being published, not
that it has been deleted. That is still the outcome the subject cares about
most, and it is checkable, which the other is not.
"""
import gzip, json, re, sys, time, zlib, urllib.parse, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# public search URL templates, {first} {last} {state} {city} substituted
# WHY SOME SITES CANNOT BE RE-VERIFIED BY THIS SCRIPT AT ALL.
# Recorded per site rather than left to reappear each run as an unexplained
# 403 or 404. A run that reports five failures without saying WHICH KIND of
# failure invites the reader to average them into "flaky", and they are not
# flaky -- they are three different permanent obstacles. Tested 2026-09-11
# with a full browser header set (Accept-Language, all four Sec-Fetch-*,
# Upgrade-Insecure-Requests): every 403 below returned 403 to that too, so
# none is a matter of header craft. See _SILENT_FAILURES 440.
UNCHECKABLE = {
    "checkpeople": "bot wall -- 403 to a full browser header set, needs a real session",
    "radaris":     "bot wall -- 403 to a full browser header set, needs a real session",
    "whitepages":  "bot wall -- 403 to a full browser header set, needs a real session",
    # ussearch was listed here for about ten minutes on the strength of a
    # single curl that returned 403. The script's own fetcher reached the same
    # URL and got a result page. One failed probe is not a property of a site
    # (SF 428), and I had just written a comment saying exactly that two lines
    # above. Removed -- it is checkable, and it is LISTED.
    "idstrong":    "search is POST-only (/searching/name-loading/, firstName+lastName), "
                   "so a read-only GET cannot reach a result page at all",
}

SITES = {
    "checkpeople":       "https://www.checkpeople.com/name/{first}-{last}/{state}",
    "radaris":           "https://radaris.com/p/{first}/{last}/",
    "whitepages":        "https://www.whitepages.com/name/{first}-{last}/{city}-{state}",
    # CORRECTED 2026-09-11: /name/{first}-{last}/ returned 404, which read as
    # "no such page" when the truth is a bot wall one path over. USSearch is
    # PeopleConnect, so it uses the same /results/ shape as TruthFinder -- and
    # that path answers 403. A stale URL had been hiding the real obstacle.
    "ussearch":          "https://www.ussearch.com/results/?firstName={first}&lastName={last}&state={state}",
    "truthfinder":       "https://www.truthfinder.com/results/?firstName={first}&lastName={last}&state={state}",
    "instantcheckmate":  "https://www.instantcheckmate.com/results?firstName={first}&lastName={last}&state={state}",
    "idstrong":          "https://www.idstrong.com/people/{first}-{last}/",
    # URLs below were DISCOVERED from each site's own search form rather than
    # guessed. The first five templates in this file were guesses and all five
    # returned 404 -- see _SILENT_FAILURES 409.
    "search_quarry":     "https://www.searchquarry.com/namesearch/search/?fname={first}&lname={last}&city={city}",
    "governmentregistry_org": "https://governmentregistry.org/?firstName={first}&lastName={last}&town={city}",
    # open-public-records.com is NOT searchable: both its "search" forms POST
    # to /click-ad.php and /opr-bc-redirect.php -- affiliate redirects, not a
    # query. Same shape as dobsearch (SF 390). Nothing to re-verify there.
}

# the subject appears
LISTED = re.compile(r"\b(view (?:full )?(?:report|profile)|possible relatives|"
                    r"age \d{2}|lives? in|current address|associated with)\b", re.I)
# the site says it has nothing
EMPTY = re.compile(r"no (?:results|records|matches|listings)(?: (?:were )?found)?|"
                   r"we (?:could|did) not find|0 results|nothing (?:was )?found|"
                   r"try (?:another|a different) search", re.I)
BLOCKED = re.compile(r"just a moment|enable javascript|verify you are human|"
                     r"access denied|unusual traffic|are you a robot|cf-browser", re.I)


def fetch(url, timeout=25):
    # DO NOT request compression. Asking for gzip/deflate made radaris return
    # a body this client could not decode, and every text check then read the
    # result as binary noise. Plain `curl` with no Accept-Encoding gets clean
    # HTML from the same URL. The compression was never worth the failure mode:
    # these pages are small and the point is to read them, not to save bytes.
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": "text/html",
        "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read(500_000)
        enc = (r.headers.get("Content-Encoding") or "").lower()
        # Decompress on the MAGIC BYTES, not on the header. radaris returned a
        # gzip body with no Content-Encoding and every text check read the
        # result as binary noise -- the same class of bug as the one fixed in
        # route_has_form (SF 389), recurring because the fix was made in one
        # script and not carried to the next.
        if raw[:2] == b"\x1f\x8b" or "gzip" in enc:
            try:
                raw = gzip.decompress(raw)
            except Exception:
                pass
        elif "deflate" in enc:
            try:
                raw = zlib.decompress(raw, -zlib.MAX_WBITS)
            except Exception:
                pass
        return r.getcode(), r.geturl(), raw.decode("utf-8", "replace")


def strip(h):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", h)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)).strip()


def check(item, subject):
    bid, tmpl = item
    url = tmpl.format(**subject)
    try:
        code, final, html = fetch(url)
    except urllib.error.HTTPError as e:
        return (bid, f"HTTP-{e.code}", url, "")
    except Exception as e:
        return (bid, "ERROR", url, type(e).__name__)

    text = strip(html)
    if BLOCKED.search(text[:3000]):
        return (bid, "BLOCKED", url, text[:90])
    # the subject's own name appearing next to profile furniture
    name_present = re.search(rf"{subject['first']}\s+\w*\s*{subject['last']}", text, re.I)
    if EMPTY.search(text[:6000]) and not name_present:
        return (bid, "NOT-LISTED", url, "")
    # A NAME MATCH IS NOT A PERSON MATCH. A people-search /p/<first>/<last>/
    # page returns everyone of that name -- 233 in one state alone --
    # and the first version of this check called that LISTED. It nearly went
    # into the record as "the removal has been undone". The subject's own city
    # appeared ZERO times on that page. See _SILENT_FAILURES 409, and §380 and
    # §388 before it: a result at the wrong granularity is not an answer.
    locality = re.search(rf"\b({re.escape(subject['city'])}|{re.escape(subject['zip'])})\b",
                         text, re.I) if subject.get("zip") else \
               re.search(rf"\b{re.escape(subject['city'])}\b", text, re.I)
    if name_present and LISTED.search(text) and locality:
        return (bid, "LISTED", url, text[max(0, locality.start()-90):
                                         locality.start()+120])
    if name_present and LISTED.search(text):
        return (bid, "NAME-ONLY", url,
                "name page for everyone of this name; subject's city absent")
    if len(text) < 400:
        return (bid, "JS-SHELL", url, "")
    return (bid, "UNCLEAR", url, text[:90])


def main():
    prof = json.load(open("data/profile.json"))
    subject = {
        "first": prof["first_name"].title(),
        "last":  prof["last_name"].title(),
        "state": prof["state"].upper(),
        "city":  prof["city"].title(),
        "zip":   str(prof.get("zip_code", "")),
    }
    only = sys.argv[1:] or None
    items = [(k, v) for k, v in SITES.items() if not only or k in only]
    print(f"re-verifying {len(items)} public listings, read-only, one query each\n")

    out = []
    with ThreadPoolExecutor(max_workers=3) as ex:
        for res in ex.map(lambda i: check(i, subject), items):
            out.append(res)

    order = ["LISTED", "NAME-ONLY", "UNCLEAR", "BLOCKED", "JS-SHELL",
             "NOT-LISTED"]
    out.sort(key=lambda r: (order.index(r[1]) if r[1] in order else 99, r[0]))
    for bid, verdict, url, detail in out:
        print(f"{verdict:12} {bid:26} {url[:64]}")
        if detail:
            print(f"{'':12} {detail[:110]}")
    unchecked = sorted(k for k in SITES if k in UNCHECKABLE)
    print(f"\n=== CANNOT BE CHECKED BY THIS METHOD ({len(unchecked)} of {len(SITES)})")
    print("    Standing obstacles, not failures of this run. Retested 2026-09-11")
    print("    with a full browser header set; none is a matter of header craft.")
    for k in unchecked:
        print(f"  {k:24s} {UNCHECKABLE[k]}")
    print(f"\n    So a clean run verifies at most {len(SITES) - len(unchecked)} of {len(SITES)} rows.")
    print("    Read any headline count against that, not against the site total.")

    print("""
  LISTED is the one to act on: the SUBJECT -- name and city both -- is being
  published again on a site that confirmed a removal. Re-open that row.
  NAME-ONLY means the site has a page for everyone of that name and the
  subject's own locality is absent from it. That is not a listing.
  BLOCKED and JS-SHELL are not verdicts -- the check could not see the page.
  NOT-LISTED means not published; it does NOT mean deleted (SF 388).""")
    json.dump([{"id": b, "verdict": v, "url": u} for b, v, u, _ in out],
              open("data/reverify.json", "w"), indent=1)
    print("\nwrote data/reverify.json")


if __name__ == "__main__":
    main()
