# Trustoria

- **Opt-out:** none reachable
- **Email:** removals@trustoria.com — undeliverable, no MX
- **Method:** none
- **Domain:** trustoria.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-20)

## Steps

None available. The domain is delegated and empty.

## Gotchas

**The fetch failure is not the finding — the DNS is.** `curl` against
`trustoria.com` returns HTTP 000 and zero bytes, which is exactly what it also
returns for a timeout, a TLS failure, and an aggressive bot block. Three of
those four states mean "try again differently" and only one means "stop", so the
fetch result on its own is not a conclusion.

Resolving settles it:

```
dig +short NS trustoria.com   →  dns1.p09.nsone.net.  dns2.  dns3.  dns4.
dig +short A  trustoria.com   →  (nothing)
dig +short MX trustoria.com   →  (nothing)
```

Delegated nameservers, no address record, no mail exchanger. Somebody is still
paying to hold the name and there is nothing behind it: no host to serve a page,
no mailbox to accept a request. Unlike a bot block, this will not yield to a
better User-Agent, and unlike a timeout it will not resolve on retry.

Recorded as `unreachable` with the evidence rather than left `pending`, so a
later pass does not spend three sends and a browser session rediscovering it.
See `_SILENT_FAILURES.md` §65, final row.

**An earlier pass nearly mis-attributed this domain.** A sweep loop that reused a
single temp file across iterations reported the *previous* page's content when a
fetch failed, which briefly made trustoria.com appear to share a privacy policy
with terminus.com. It did not. Caught before it reached a letter — §60 applies:
do not accuse a broker of a fault in your own pipeline.

## Verification

Re-check DNS periodically. If an A record or MX appears, the site is back and
the route should be re-derived from scratch.
