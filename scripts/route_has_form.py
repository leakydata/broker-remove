#!/usr/bin/env python3
"""Does a recorded removal route actually contain a way to make a request?

route_check.py answers "does this URL resolve." That was already known to be
insufficient -- SILENT_FAILURES 354 found URLs that return 200 by redirecting
away from the specific page to a generic one. 388 found a second way for it to
be insufficient, and a worse one: PeopleSearchNow's /optout returns 200,
renders a styled page on the company's own domain, and is a SURNAME SEARCH.
The site routes /<word> as a last name, so the page reads "Find people with the
last name Optout". Nothing redirects. Nothing errors. The path contains the
right word. Every check passes.

The discriminator that survives both failures is not the status code and not
the URL. It is whether there is anything on the page a person could USE:

    a <form>, or
    a request widget delegated to a known privacy portal, or
    a mailto: for privacy, or
    failing all of those, prose that is at least ABOUT removal rather than
    about people

A route with none of those is a claim, not a route.

Output is deliberately conservative. NO-FORM is not the same as broken -- many
legitimate routes are JS widgets that render nothing to a fetch, and those are
reported separately as WIDGET-LIKELY rather than being called failures. What
this is hunting for is the specific case where a page is confidently, styledly
about something else entirely.
"""
import gzip, io, json, re, sys, time, zlib
import urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# a path segment that means "this page is about exercising a right"
# A path segment that means "this page is about exercising a right".
# FIRST VERSION OF THIS LIST OVER-FIRED: it omitted privacy-center and
# privacy-choices, so eight redirects that land on a company's REAL privacy
# centre were reported as redirect-aways. A redirect from /opt-out to
# /privacy-center is a route moving, not a route vanishing. Fixed before the
# number was believed -- see _SILENT_FAILURES 408.
SPECIFIC = re.compile(r"opt[-_]?out|do[-_]?not[-_]?sell|remove|removal|suppress|delete|"
                      r"dsar|data[-_]?request|ccpa|subject[-_]?request|erase|"
                      r"block[-_]?record|privacy[-_ ]?(?:request|cent(?:er|re)|choices|"
                      r"portal|rights)|your[-_]?privacy|consumer[-_]?(?:rights|choices)|"
                      r"suppression[-_]?cent(?:er|re)", re.I)

PORTAL_HOSTS = ("saymine.io", "onetrust.com", "osano.com", "trustarc.com",
                "ketch.com", "securiti.ai", "transcend.io", "didomi.io",
                "usercentrics.com", "relyance.ai", "datagrail.io",
                "privacyportal", "privacy-central", "ethicspoint.com")

# words that mean the page is about exercising a right
REMOVAL_WORDS = re.compile(
    r"opt[- ]?out|do not sell|do not share|delete my|remove my|removal request|"
    r"privacy request|data subject|erase my|suppress|right to know|"
    r"right to delete|exercise your rights|exercise my rights", re.I)

# the page rendered nothing yet: a client-side app, not an answer either way
SHELL = re.compile(r"loading\.\.\.|checking for any bots|please enable javascript|"
                   r"boilerplate|you need to enable javascript", re.I)

# the host is shedding load -- says nothing about whether a route exists
RATELIMIT = re.compile(r"requested too many times|rate limit|too many requests|"
                       r"slow down|try again later", re.I)

# words that mean the page is the product, not the remedy
PRODUCT_WORDS = re.compile(
    r"find people with the last name|search results for|people named|"
    r"browse (?:by )?surname|showing results for|no results were found", re.I)


def fetch(url, timeout=20):
    # Accept-Encoding must be declared AND decoded. Without this some servers
    # gzip anyway and the body arrives as binary, which every text check then
    # reads as gibberish and reports as an off-topic page. Two routes were
    # mis-verdicted that way on the first run.
    # ASK FOR identity. Requesting gzip and decompressing on the header alone
    # is the bug that made radaris arrive as binary noise in reverify_listings
    # (SF 409) -- some servers compress without declaring it. This script had
    # the same latent defect and its verdicts have been quoted all day. These
    # pages are small; the compression was never worth the failure mode.
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": "text/html",
        "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read(600_000)
        enc = (r.headers.get("Content-Encoding") or "").lower()
        try:
            if "gzip" in enc:
                raw = gzip.decompress(raw)
            elif "deflate" in enc:
                raw = zlib.decompress(raw, -zlib.MAX_WBITS)
        except Exception:
            pass  # truncated stream: fall through and read what we can
        return r.getcode(), r.geturl(), raw.decode("utf-8", "replace")


def strip(html):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def is_portal_host(host):
    return any(p in host for p in PORTAL_HOSTS)


# Unambiguous parking signatures. Precise on purpose: each of these is a page
# whose entire content is an instruction to go somewhere else, which no real
# route ever is. Anything less certain than these is left to a human.
PARKED_SIG = re.compile(
    r'window\.location\.href\s*=\s*["\']/?lander|'
    r'>\s*Click here to enter\s*<|'
    r'parking(?:crew|page)|sedoparking|bodis\.com|afternic',
    re.I)

# An Incapsula / Imperva style bot interstitial: a tiny body that is nothing but
# an iframe, marked noindex. Served with a 200, so it is invisible to a status
# check, and it means "a browser might get through where this did not" -- which
# is a different thing from "there is no route here".
WAF_SHELL = re.compile(r'NOINDEX,\s*NOFOLLOW', re.I)


def answers_everything(final, html):
    """Does this host return the same page for a path that cannot exist?

    An HTTP 200 does not mean "this page exists", it means "something
    answered" (SF 427). But THIS SIGNAL DOES NOT IDENTIFY WHAT ANSWERED, and
    three unrelated conditions produce it identically: a parked domain, a WAF
    interstitial, and a single-page app whose routing runs in the browser.

    I tried twice to make it decide a verdict and it was wrong both times --
    first flagging 44 routes including Acxiom, Equifax, Intelius and
    TruthFinder, several with COMPLETED removals through those exact URLs;
    then, after gating it on <script>, missing the parked domains outright
    because their lander redirect is itself a script. Whichever way the
    boolean was set it destroyed information.

    So it no longer decides anything. It ANNOTATES: the verdict comes from
    what the page contains, and this is appended as a note for a human or a
    browser check to weigh. A signal that cannot distinguish three causes has
    no business choosing between them. See _SILENT_FAILURES 428.
    """
    try:
        base = urlparse(final)
        _, _, bogus = fetch(f"{base.scheme}://{base.netloc}/zzz-not-a-real-page-9137/")
    except urllib.error.HTTPError:
        return ""            # a 4xx here is CORRECT: the host discriminates
    except Exception:
        return ""            # control unreachable: say nothing
    if abs(len(bogus) - len(html)) < 200:
        return f" [host also answers 200 for a nonexistent path, {len(bogus)}B]"
    return ""


def classify(bid, url):
    try:
        code, final, html = fetch(url)
    except urllib.error.HTTPError as e:
        return (bid, url, f"HTTP-{e.code}", "", "")
    except Exception as e:
        return (bid, url, "ERROR", type(e).__name__, "")

    text = strip(html)
    host = urlparse(final).netloc.lower()

    # REDIRECT-AWAY MUST BE CHECKED BEFORE LOOKING FOR A FORM. route_check.py
    # already flagged dobsearch's /people-finder/block-record-request.php as
    # redirecting to a blog article -- and THIS script called it "FORM",
    # because the article carries eight site-search boxes. Two scanners, one
    # right and one wrong, and the wrong one was the newer. A page that has
    # stopped being about removal is not a route however many forms are on it.
    # See _SILENT_FAILURES 408.
    # match against host AND path: a redirect to suppression.peopleconnect.us
    # keeps its meaning in the HOSTNAME, and a path-only check called that a
    # redirect-away too. Second over-fire of the same detector in ten minutes.
    def specific(u):
        p = urlparse(u)
        return bool(SPECIFIC.search(p.netloc + p.path))

    started = specific(url)
    ended = specific(final)
    if started and not ended and not is_portal_host(host):
        return (bid, url, "REDIRECT-AWAY", strip(html)[:110], final)

    # a real form with at least one text-ish input
    forms = re.findall(r"(?is)<form\b.*?</form>", html)
    real_form = any(re.search(r'<(input|textarea|select)\b', f, re.I) and
                    not re.search(r'action=["\'][^"\']*(search|login|signin)', f, re.I)
                    for f in forms)

    delegated = is_portal_host(host) or \
        any(p in html.lower() for p in PORTAL_HOSTS)
    privacy_mailto = bool(re.search(
        r'mailto:[^"\'>\s]*(privacy|dpo|ccpa|optout|opt-out|dsar|compliance)',
        html, re.I))

    product = bool(PRODUCT_WORDS.search(text[:3000]))
    removal = bool(REMOVAL_WORDS.search(text[:6000]))

    # PARKED is positive evidence and outranks everything: the page's whole
    # content is a redirect to a parking lander. Seventeen arrests.org domains
    # sat behind exactly this and were briefly queued as human form-fills.
    if PARKED_SIG.search(html):
        return (bid, url, "PARKED", strip(html)[:60] or "redirects to a parking lander", final)
    if WAF_SHELL.search(html) and len(text) < 400:
        return (bid, url, "BOT-BLOCKED", "interstitial served as 200; try a browser", final)
    if RATELIMIT.search(text[:2000]):
        return (bid, url, "RATE-LIMITED", text[:110], final)
    if not real_form and (SHELL.search(text[:2000]) or len(text) < 400):
        return (bid, url, "JS-SHELL",
                text[:110] + answers_everything(final, html), final)
    if product and not real_form:
        return (bid, url, "PRODUCT-PAGE", text[:110], final)
    if real_form:
        return (bid, url, "FORM", "", final)
    if delegated:
        return (bid, url, "DELEGATED", host, final)
    if privacy_mailto:
        return (bid, url, "MAILTO", "", final)
    if not removal:
        return (bid, url, "OFF-TOPIC",
                text[:110] + answers_everything(final, html), final)
    # talks about removal, no form element -- almost always a JS widget
    return (bid, url, "WIDGET-LIKELY", "", final)


def main():
    brokers = json.load(open("data/brokers.json"))
    if isinstance(brokers, dict):
        brokers = brokers.get("brokers") or list(brokers.values())
    if isinstance(brokers, dict):
        brokers = list(brokers.values())

    jobs = []
    for r in brokers:
        if not isinstance(r, dict):
            continue
        u = (r.get("optout_url") or "").strip()
        if u.startswith("http"):
            jobs.append((r["id"], u))

    only = sys.argv[1:] or None
    if only:
        jobs = [j for j in jobs if j[0] in only]

    # FETCH EACH DISTINCT URL ONCE. Whole families of brokers share a single
    # route -- one platform serves ~20 state-arrest sites from the same
    # /optout page. Fetching per broker sent 20 concurrent requests at one
    # host, which rate-limited, which the first run then recorded as 20
    # brokers with an off-topic route. The scanner had manufactured its own
    # finding. See _SILENT_FAILURES 389.
    by_url = {}
    for bid, u in jobs:
        by_url.setdefault(u, []).append(bid)
    print(f"checking {len(jobs)} recorded routes "
          f"({len(by_url)} distinct URLs) for something usable\n")

    results = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        for url, res in zip(by_url, ex.map(
                lambda u: classify(by_url[u][0], u), by_url)):
            results[url] = res

    out = []
    for url, ids in by_url.items():
        _, _, verdict, detail, final = results[url]
        for bid in ids:
            out.append((bid, url, verdict, detail, final))

    order = ["PRODUCT-PAGE", "REDIRECT-AWAY", "OFF-TOPIC", "JS-SHELL",
             "RATE-LIMITED",
             "WIDGET-LIKELY", "HTTP-403",
             "HTTP-404", "ERROR", "MAILTO", "PARKED", "BOT-BLOCKED",
             "DELEGATED", "FORM"]
    out.sort(key=lambda r: (order.index(r[2]) if r[2] in order else 99, r[0]))

    counts = {}
    for _, _, v, _, _ in out:
        counts[v] = counts.get(v, 0) + 1

    for bid, url, verdict, detail, final in out:
        if verdict in ("FORM", "DELEGATED", "MAILTO", "JS-SHELL"):
            continue
        print(f"{verdict:14} {bid:34} {url}")
        if detail:
            print(f"{'':14} -> {detail}")

    print("\n=== summary")
    for k in sorted(counts, key=lambda x: -counts[x]):
        print(f"  {k:16} {counts[k]}")
    print("""
  PRODUCT-PAGE is the one to act on: the page returns 200, sits on the
  company's own domain, and is ABOUT PEOPLE rather than about removal --
  the site's routing has claimed the path. See _SILENT_FAILURES 388.
  WIDGET-LIKELY is not a failure: it talks about removal but renders its
  form in JavaScript, so a fetch cannot see it. Check those in a browser.
  JS-SHELL and RATE-LIMITED are NOT verdicts about the route. The first
  means the page had not rendered; the second means the host was shedding
  load. Both mean 'ask again', not 'no route here'.""")

    json.dump([{"id": b, "url": u, "verdict": v, "detail": d, "final": f}
               for b, u, v, d, f in out],
              open("data/route_has_form.json", "w"), indent=1)
    print("\nwrote data/route_has_form.json")


if __name__ == "__main__":
    main()
