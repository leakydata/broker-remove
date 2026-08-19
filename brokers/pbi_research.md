# Pbi Research

- **Email:** CCPARequests@pbinfo.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** pbinfo.com
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-19)
- Note: Death-audit and beneficiary-location services for insurers and pension plans - a category that needs a different letter from a marketing broker, so it got one. Led with DISCLOSURE rather than deletion: whether the subject appears in any deceased or death-match file, including a partial, probabilistic or later-resolved match. False positives in Death Master File matching are a known and serious harm - benefits suspended, accounts frozen, credit files flagged, usually with no notice and no visible cause - and a clean deletion would remove the evidence while leaving a bad flag propagating downstream. So correction was asked for ahead of deletion, plus categories of client recipient with a direction to correct their copies too. Also pre-empted the GLBA angle alongside FCRA, since that is the exemption this category actually reaches for, and explicitly refused to send an SSN.

## Steps

1. Write to `CCPARequests@pbinfo.com`. Their MX is Mimecast
   and delivers.
2. **Lead with disclosure and correction, not deletion** — see below.

## Gotchas

**This is a category where deletion can be the wrong first ask.** Death-audit
and beneficiary-location services match individuals against the Social Security
Death Master File, obituary data and similar sources. False positives are a known
and serious harm: a living person wrongly matched can find benefits suspended,
accounts frozen and credit files flagged, usually with no notice and no visible
cause.

If such a flag exists, a clean deletion removes the evidence and leaves the flag
propagating through every client who already received it. So ask, in this order:

1. **Am I in any deceased or death-match file** — including a partial,
   probabilistic, or later-resolved match?
2. **Which clients received it**, and will you direct them to correct their
   copies?
3. Only then, delete and suppress.

**Search the locate files, not just a marketing list.** Records held for locate
purposes are assembled from credit header data, change-of-address feeds and
prior-address chains — sources a marketing suppression never touches. The prior
addresses are the point of the request here.

**Pre-empt GLBA as well as FCRA.** Vendors serving insurers and pension plans
reach for the Gramm-Leach-Bliley exemption more often than the FCRA one, and a
letter that only anticipates FCRA invites a partial answer.

**Refuse the SSN.** This category will ask, because SSN is their matching key.
Sending one to get data deleted creates a more sensitive record than the one
being removed.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
