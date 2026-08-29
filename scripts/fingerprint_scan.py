#!/usr/bin/env python3
"""Cluster registry domains by shared third-party identifiers.

A white-label operator can rename a brand, buy a new domain, write a new phone
number and stand up a separate support mailbox. What it does not usually do is
provision a separate LiveChat account or a separate analytics property for each
front end -- those cost money and effort per brand and buy nothing, so one gets
reused across the whole estate. That reuse is visible in the page source.

Three identifiers, in rough order of how strongly they imply common ownership:

    window.__lc.license = N     LiveChat account. Strongest: a paid seat.
    UA-… / G-…                  Analytics property. Strong.
    GTM-…                       Tag Manager container. Good, but see the caveat.

CAVEAT, and it matters. A shared identifier is evidence of a shared OPERATOR,
which is usually but not always a shared OWNER. UA-7117339-4 came back linking
smacomm.com, bigbendtransit.com, fandominc.com, thepublicindex.com, torrelabs.com
and wellnesscom.com -- a transit authority, a wellness directory and a public
records site have no plausible common owner. That is far more likely one web
agency reusing its own property across client sites. Treat a cluster as a lead to
verify, never as a finding: corroborate with page structure, shared copy, or a
common contact address before writing to anyone as a family.

The control case: the ten-site California licensing family was already known and
already routed to a single address by other means, and the scan reproduced it
exactly. The find: courtrec.com and publicrecords.info turned out to be siblings
of three sites already written to separately under unrelated addresses.

Read-only. Prints clusters and changes nothing.
"""
import json,subprocess,re,concurrent.futures as cf
d=json.load(open("data/brokers.json"))
doms=[]
for b in d["brokers"]:
    dm=b.get("domain")
    if dm: doms.append((b["id"],dm))
def fp(t):
    i=t[0]; dm=t[1]
    try:
        h=subprocess.run(["curl","-sL","--max-time","14","-A","Mozilla/5.0","https://"+dm],
                         capture_output=True,text=True,timeout=20).stdout
    except Exception: return None
    if not h: return None
    lc=re.search(r'__lc\.license\s*=\s*(\d+)',h)
    gtm=set(re.findall(r'GTM-[A-Z0-9]{4,9}',h))
    ua=set(re.findall(r'UA-\d{6,12}-\d+',h))
    ga=set(re.findall(r'G-[A-Z0-9]{8,12}',h))
    if lc or gtm or ua or ga:
        return (i,dm,lc.group(1) if lc else "", ",".join(sorted(gtm)), ",".join(sorted(ua|ga)))
    return None
out=[]
with cf.ThreadPoolExecutor(16) as ex:
    for r in ex.map(fp,doms):
        if r: out.append(r)
print("scanned",len(doms),"domains; got fingerprints from",len(out))
from collections import defaultdict
by=defaultdict(list)
for i,dm,lc,gtm,ga in out:
    if lc: by["LC:"+lc].append((i,dm))
    for g in filter(None,gtm.split(",")): by["GTM:"+g].append((i,dm))
    for g in filter(None,ga.split(",")): by["GA:"+g].append((i,dm))
for k,v in sorted(by.items(), key=lambda kv:-len(kv[1])):
    if len(v)>1:
        print(f"\n{k}  ({len(v)} sites)")
        for i,dm in v: print(f"   {i:<34} {dm}")
