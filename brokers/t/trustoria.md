# Trustoria

- **Opt-out:** none reachable
- **Email:** removals@trustoria.com — undeliverable, no MX
- **Method:** none
- **Domain:** trustoria.com
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-20)
- Note: Domain resolves to nothing: NS delegated to nsone.net but NO A record and NO MX (2026-08-20). Site does not load and the domain accepts no mail. Not a bot block - there is no host to block.

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

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
