#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx"]
# ///
"""Turn an Optery slug into a verified domain, or leave it alone.

363 registry rows arrived from Optery's sitemap as a slug and nothing else -- no
domain, no opt-out URL, no email. A row with no domain has no route, so no pass
can ever action it; it sits `pending` forever and quietly inflates the backlog.

The slug usually encodes the domain ("1called-com" -> 1called.com), so the
derivation is mechanical. The derivation is also a GUESS, and this repo has
already sent one letter asserting a business a company did not have. So nothing
here is written to the registry on the strength of the pattern alone:

  1. derive candidate domains from the slug
  2. keep only candidates that RESOLVE (A record or MX)
  3. fetch the site and require it to look like the same business --
     the slug's words must appear in the page title, heading or body

Candidates that pass all three are written to a review file. Candidates that
fail are recorded WITH THE REASON, because "tried and could not confirm" is a
finding worth keeping -- it stops the next pass repeating the work.
"""
import asyncio, json, re, socket, sys
from pathlib import Path
import httpx

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "brokers.json"
LEDGER = ROOT / "data" / "removal_ledger.json"
OUT = ROOT / "data" / "optery_domain_candidates.json"

TLDS = ("com", "net", "org", "io", "co", "ca", "us", "info", "biz", "ai", "app",
        "me", "tv", "xyz", "online", "site", "pro", "name", "live", "cloud")
# Optery slugs are built from the LEGAL ENTITY name; domains almost never carry
# the corporate suffix. "altrata-inc" is altrata.com, not altratainc.com. Strip
# these progressively rather than all at once, because "allant-group-llc" may be
# allantgroup.com or allant.com and both are worth trying.
SUFFIXES = ("inc", "llc", "ltd", "limited", "corp", "corporation", "plc",
            "lp", "llp", "gmbh", "sa", "bv", "ag", "pty", "co", "company",
            "holdings", "group")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")


def candidates(slug: str) -> list[str]:
    """Ordered guesses, most likely first."""
    slug = re.sub(r"-\d+$", "", slug)      # "alumni-us-2" is a disambiguator
    out = []
    parts = slug.split("-")

    # A trailing TLD token means the slug IS the domain: "1called-com".
    if len(parts) > 1 and parts[-1] in TLDS:
        stem, tld = "-".join(parts[:-1]), parts[-1]
        out.append(f"{stem.replace('-', '')}.{tld}")
        if "-" in stem:
            out.append(f"{stem}.{tld}")
        return list(dict.fromkeys(out))

    # Otherwise try the whole slug, then peel corporate suffixes one at a time.
    stems, cur = [], list(parts)
    stems.append(list(cur))
    while len(cur) > 1 and cur[-1] in SUFFIXES:
        cur = cur[:-1]
        stems.append(list(cur))

    for st in stems:
        joined = "".join(st)
        out.append(f"{joined}.com")
        if len(st) > 1:
            out.append(f"{'-'.join(st)}.com")
        # A one-word stem left over from a suffix strip is often a .io/.ai/.co
        if len(st) == 1:
            out.extend(f"{joined}.{t}" for t in ("io", "ai", "co", "net"))
    return list(dict.fromkeys(out))


def resolves(domain: str) -> str | None:
    """Return 'A' or 'MX' if the domain exists at all, else None."""
    try:
        socket.getaddrinfo(domain, None)
        return "A"
    except OSError:
        pass
    # No A record is not the same as no domain -- a mail-only domain still exists.
    try:
        import subprocess
        r = subprocess.run(["dig", "+short", "MX", domain],
                           capture_output=True, text=True, timeout=8)
        return "MX" if r.stdout.strip() else None
    except Exception:
        return None


def looks_like(slug: str, html: str) -> bool:
    """Does the page belong to the business the slug names?

    Requires the slug's significant words to appear in the page. A parked page,
    a domain squatter or an unrelated business that happens to own the name will
    resolve fine and fail this.
    """
    # Corporate suffixes are dropped from the domain and often from the branding
    # too, so requiring "inc" to appear on altrata.com would reject a correct
    # match. Judge on the distinctive words only.
    slug = re.sub(r"-\d+$", "", slug)
    words = [w for w in slug.split("-")
             if w not in TLDS and w not in SUFFIXES and len(w) > 2]
    if not words:
        return False
    text = re.sub(r"<[^>]*>", " ", html).lower()
    title = " ".join(re.findall(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)).lower()
    joined = slug.replace("-", "").lower()
    if joined in title.replace(" ", "") or joined in text.replace(" ", "")[:20000]:
        return True
    return all(w in text[:20000] for w in words)


async def check(client: httpx.AsyncClient, slug: str) -> dict:
    """Try every candidate; return the first CONFIRMED, else the best failure.

    An earlier version returned on the first candidate that merely RESOLVED,
    which mis-scored "amedisys-inc": amedisysinc.com resolves and is somebody
    else's parked page, so the correct amedisys.com further down the list was
    never reached. Resolving is not the success condition -- confirming is.
    """
    cands = candidates(slug)
    # When the slug ends in a TLD token the domain is STATED, not guessed, so a
    # bot block or a 403 says nothing about whether the domain is right.
    slug_states_domain = len(cands) == 1 and slug.split("-")[-1] in TLDS
    best = None

    def keep(result: dict, rank: int) -> None:
        nonlocal best
        if best is None or rank < best[0]:
            best = (rank, result)

    for dom in cands:
        how = resolves(dom)
        if not how:
            continue
        try:
            r = await client.get(f"https://{dom}/", timeout=15,
                                 follow_redirects=True, headers={"User-Agent": UA})
            html = r.text
        except Exception as e:
            keep({"slug": slug, "domain": dom,
                  "verdict": "CONFIRMED_BY_SLUG" if slug_states_domain
                             else "RESOLVES_NO_FETCH",
                  "detail": (f"{how} record exists; fetch failed "
                             f"({type(e).__name__}); "
                             + ("slug names this domain explicitly"
                                if slug_states_domain else "unverified"))}, 1)
            continue
        if r.status_code >= 400:
            keep({"slug": slug, "domain": dom,
                  "verdict": "CONFIRMED_BY_SLUG" if slug_states_domain
                             else "RESOLVES_HTTP_ERROR",
                  "detail": (f"HTTP {r.status_code} (often a bot block); "
                             + ("slug names this domain explicitly"
                                if slug_states_domain else "unverified"))}, 1)
            continue
        if looks_like(slug, html):
            return {"slug": slug, "domain": dom, "verdict": "CONFIRMED",
                    "detail": f"resolved via {how}; slug words present in page"}
        keep({"slug": slug, "domain": dom, "verdict": "RESOLVES_WRONG_SITE",
              "detail": "page does not mention the slug's words - parked, "
                        "squatted, or a different business"}, 2)

    if best:
        return best[1]
    return {"slug": slug, "domain": None, "verdict": "NO_DOMAIN",
            "detail": f"none of {cands} resolve"}


async def main() -> int:
    brokers = json.loads(REGISTRY.read_text())["brokers"]
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}
    todo = [b for b in brokers
            if not b.get("domain") and b.get("optery_slug")
            and ledger.get(b["id"], {}).get("status", "pending") == "pending"]
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else len(todo)
    todo = todo[:limit]
    print(f"resolving {len(todo)} slug(s) with no domain...")

    sem = asyncio.Semaphore(12)
    async with httpx.AsyncClient() as client:
        async def one(b):
            async with sem:
                return await check(client, b["optery_slug"])
        results = await asyncio.gather(*(one(b) for b in todo))

    prev = json.loads(OUT.read_text()) if OUT.exists() else {}
    for r in results:
        prev[r["slug"]] = r
    OUT.write_text(json.dumps(prev, indent=2, sort_keys=True) + "\n")

    counts: dict[str, int] = {}
    for r in results:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    for v in sorted(counts):
        print(f"  {v:22} {counts[v]}")
    print(f"\nwrote {OUT.relative_to(ROOT)} ({len(prev)} slug(s))")
    print("CONFIRMED rows are candidates for the registry - review before applying.")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
