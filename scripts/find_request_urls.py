#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Find the privacy-request URL a broker publishes on its own website.

WHY. A portal-gated broker usually mails you a link. That link passes through an
email pipeline, and Throtle's arrived corrupted -- the "=" separators and the
leading characters of all three UUIDs destroyed in transit, so the form could not
identify which organisation the request belonged to. Asking them to resend failed:
their autoresponder fired again, verbatim, at the message reporting the problem.

The intact link was on their own privacy page the whole time
(_SILENT_FAILURES 203a). The vendor generates one URL and it gets pasted in both
places -- and only one of those two paths runs through something that can corrupt
it.

So this sweeps the portal-gated rows and pulls the request URL straight from the
site: /privacy/, /privacy-policy/, /your-privacy-choices/, then the homepage. It
matches the known DSAR vendors (OneTrust, TrustArc, Osano, Ketch, Transcend,
Securiti, DataGrail, PrivacyPillar, my.datasubject) plus the self-hosted patterns
(/do-not-sell, /ccpa, /privacy-request, /your-privacy-choices).

First run, 2026-08-30: 22 of 58 portal-gated rows yielded a URL. Each one turns a
handoff item from "find the form" into a direct link, which is the difference
between a task a person can clear in a minute and one they have to research.

A URL FOUND BY THIS SWEEP IS NOT AUTOMATICALLY BETTER THAN THE ONE ALREADY ON
FILE. Applying the first run overwrote Koddi's queued OneTrust webform with a
`/do-not-sell-my-personal-information/` page found on their own site -- a
downgrade, because a vendor webform URL is the actual submission endpoint while a
site page is usually just something that links to one. When merging results,
prefer a vendor URL (OneTrust, datasubject, PrivacyPillar, TrustArc, Osano, Ketch,
Transcend, Securiti, DataGrail) over a site landing page, and keep the other as an
alternate rather than discarding it -- vendor links do expire.

Read-only. Prints; changes nothing.
"""
import json,re,subprocess,concurrent.futures as cf
d=json.load(open("data/brokers.json"))["brokers"]; by={b["id"]:b for b in d}
st=json.load(open("data/removal_status.json")); st=st.get("brokers",st)
s={k:(v.get("status") if isinstance(v,dict) else v) for k,v in st.items()}
tgt=[(k,by[k]["domain"]) for k,v in s.items()
     if v in ("manual_required","captcha_blocked") and by.get(k,{}).get("domain")]
VENDOR=re.compile(r'https?://[^"\'<> ]*(privacyportal\.privacypillar|onetrust|trustarc|osano|ketch\.com|transcend\.io|securiti|datagrail|my\.datasubject|dsar|privacyrequest|submit-request|/ccpa|do-?not-?sell|your-privacy-choices|privacy-choices)[^"\'<> ]*', re.I)
def probe(t):
    bid,dm=t
    hits=set()
    for path in ("/privacy/","/privacy-policy/","/your-privacy-choices/","/"):
        try:
            h=subprocess.run(["curl","-sL","--compressed","--max-time","12","-A",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
                f"https://{dm}{path}"],capture_output=True,text=True,timeout=18,errors="replace").stdout
        except Exception: continue
        if not h: continue
        for m in VENDOR.findall(h): pass
        for m in re.findall(VENDOR.pattern,h,re.I):
            pass
        for m in VENDOR.finditer(h):
            u=m.group(0).replace("&amp;","&")
            if len(u)<400: hits.add(u)
        if hits: break
    return bid,dm,sorted(hits)[:3]
out=[]
with cf.ThreadPoolExecutor(10) as ex:
    for bid,dm,hits in ex.map(probe,tgt):
        if hits: out.append((bid,dm,hits))
print(f"{len(out)}/{len(tgt)} portal-gated rows have a request URL on their own site\n")
for bid,dm,hits in sorted(out):
    print(f"== {bid}  ({dm})")
    for u in hits: print(f"     {u}")
