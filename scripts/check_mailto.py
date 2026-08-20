#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx"]
# ///
"""Compare every mailto: href on a page against the text of its own link.

Why this exists: a link is two independent claims -- where it points, and what
it says it points at -- and a page can be right about one and wrong about the
other. SourceIT's privacy policy links the text `dataprivacy2026@...` to
`mailto:dataprivacy@...`; the visible one is live and the clicked one bounces.
See _SILENT_FAILURES.md #66.

Extracting addresses from raw HTML and pooling them hides this: both addresses
are "on the page", so a checker that asks "does the registry address appear?"
confirms the dead one and stops looking. A false CONFIRMED is worse than a
NO_EMAIL, because NO_EMAIL sends you to look.

Also decodes HTML character entities first (#64) -- the working address is
sometimes published only as entities while the machine-readable one is stale.
"""
import html, re, sys, asyncio, httpx

PATHS = ["/privacy-policy", "/privacy", "/privacy-policy/", "/legal/privacy",
         "/ccpa", "/do-not-sell", "/contact", "/"]
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
ANCHOR = re.compile(r'<a[^>]*mailto:([^"\'?>]+)[^>]*>(.*?)</a>', re.I | re.S)
ADDR = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')


async def one(client, domain, path):
    for host in (f"https://www.{domain}", f"https://{domain}"):
        try:
            r = await client.get(host + path, timeout=12, follow_redirects=True)
        except Exception:
            continue
        if r.status_code == 200:
            return path, html.unescape(r.text)
    return path, None


async def scan(domain):
    findings, plain = [], set()
    async with httpx.AsyncClient(headers={"User-Agent": UA}) as client:
        pages = await asyncio.gather(*(one(client, domain, p) for p in PATHS))
    for path, body in pages:
        if not body:
            continue
        for href, inner in ANCHOR.findall(body):
            text = ADDR.findall(re.sub(r"<[^>]*>", " ", inner))
            href = href.strip().lower()
            for t in text:
                if t.lower() != href:
                    findings.append((path, href, t))
        # addresses stated in running text, not inside a link -- the tie-break
        stripped = re.sub(r"<a[^>]*>.*?</a>", " ", body, flags=re.I | re.S)
        plain |= {a.lower() for a in ADDR.findall(re.sub(r"<[^>]*>", " ", stripped))}
    return findings, plain


async def main(domains):
    for d in domains:
        findings, plain = await scan(d)
        if not findings:
            print(f"ok   {d}")
            continue
        print(f"MISMATCH {d}")
        for path, href, text in findings:
            mark = ""
            if text.lower() in plain:
                mark = "  <- text also appears unlinked in prose; prefer it"
            print(f"       {path}: href={href}  text={text}{mark}")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
