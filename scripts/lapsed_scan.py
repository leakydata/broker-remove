#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Sweep every PENDING broker whose registry filings have lapsed, and say whether
it is safe to write to.

_SILENT_FAILURES 163 established the rule: a broker that filed for 2020-2023 or 2024
and never again either died or was absorbed, and in both cases the address on file is
the least trustworthy field in the row. The danger is 157's -- a lapsed domain gets
re-registered by somebody else, and a letter carrying twelve email addresses, sixteen
former home addresses and a date of birth arrives at a company that has never held
any of it.

That check fired on nearly every batch for a week, which is the tell that it is not a
per-batch check at all: it is a property of a cohort, and cohorts should be swept.
Run over all 32 at once it produced routing for ten successions in a single pass and,
more usefully, cleared twelve brokers to be sent with no further thought (170).

Four verdicts, needing four different responses:

    LIVE, name matches      send normally
    REDIRECTS -> host       a successor; write there, or ask which entity holds the
                            file. "(NAME NOT FOUND)" means the redirect proves where
                            the domain points and NOT who owns the data -- ask, do
                            not assume
    SITE-DEAD / MX-LIVE     a maintained mail tenant with no website (the nymblr
                            shape). Safe, and email is the only channel -- say so in
                            the letter so it is not mistaken for skipping a form
    PLACEHOLDER / NO-MX     stop. A parked or for-sale domain. smacomm.com was found
                            listed on HugeDomains this way

Deliberately read-only: it prints, and changes nothing. The judgement about what a
redirect means belongs to whoever writes the letter, and a script that auto-adopted a
successor address would be making exactly the assumption 163 exists to prevent.

Usage:
    ./lapsed_scan.py
"""
import json,sys,re,html,subprocess,urllib.request,ssl
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,"scripts")
from paths import state
UA=("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36")
HDR={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,*/*;q=0.8","Accept-Language":"en-US,en;q=0.9"}
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE

def mx(d):
    try:
        r=subprocess.run(["dig","+short","MX",d],capture_output=True,text=True,timeout=8)
        return bool([l for l in r.stdout.splitlines() if l.strip()])
    except Exception: return None

def fetch(url):
    try:
        req=urllib.request.Request(url,headers=HDR)
        with urllib.request.urlopen(req,timeout=10,context=ctx) as r:
            return r.status, r.geturl(), r.read(200_000).decode("utf-8","replace")
    except Exception as e:
        return None, str(e)[:60], ""

def words(name):
    return [w.lower() for w in re.findall(r"[A-Za-z]{4,}", name or "")
            if w.lower() not in {"inc","llc","corp","company","group","data","media","technologies","solutions","the","and"}]

def classify(b):
    dom=(b.get("domain") or "").strip().lower().replace("www.","")
    if not dom: return (b["id"],"NO-DOMAIN","","")
    st_,final,body=fetch("https://"+dom)
    has_mx=mx(dom)
    if st_ is None:
        return (b["id"],"SITE-DEAD" + (" / MX-LIVE" if has_mx else " / NO-MX"), final, "")
    txt=re.sub(r"(?is)<(script|style|svg|noscript)[^>]*>.*?</\1>"," ",body)
    txt=re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]*>"," ",txt)))
    host=re.sub(r"^https?://(www\.)?","",final).split("/")[0].lower()
    redirected = dom not in host
    ws=words(b.get("name",""))
    hit=[w for w in ws if w in txt.lower()]
    placeholder = bool(re.search(r"coming soon|under construction|domain is for sale|buy this domain|parked", txt, re.I)) or len(txt.strip())<160
    if placeholder:
        v="PLACEHOLDER" + (" / MX-LIVE" if has_mx else " / NO-MX")
    elif redirected:
        v="REDIRECTS -> "+host + (" (name matches)" if hit else " (NAME NOT FOUND - check)")
    elif hit:
        v="LIVE, name matches"
    else:
        v="LIVE, NAME NOT FOUND - check"
    return (b["id"], v, final, txt[:90])

st=json.loads(state("removal_status.json").read_text())
reg=json.load(open("data/brokers.json"))["brokers"]
pend=[b for b in reg if b["id"] not in st and (b.get("email_to") or "").strip()]
lap=[b for b in pend if (b.get("registry_years") or []) and not ({"2025","2026"} & set(b.get("registry_years")))]
print(f"scanning {len(lap)} lapsed pending brokers\n")
with ThreadPoolExecutor(max_workers=10) as ex:
    for bid,v,final,snip in sorted(ex.map(classify,lap), key=lambda r:r[1]):
        print(f"{bid:30} {v}")
        if "check" in v.lower() or "DEAD" in v or "PLACEHOLDER" in v:
            print(f"     -> {final}")
            if snip: print(f"        {snip}")
