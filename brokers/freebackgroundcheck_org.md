# Freebackgroundcheck Org

- **Opt-out:** https://new-members.freebackgroundcheck.org/removeMyData/
- **Email:** support@freebackgroundcheck.org (verified)
- **Method:** web_form — Web form.
- **Domain:** freebackgroundcheck.org
- **Priority: 2.**

## Status

- Current: `submitted` (updated 2026-08-18)
- Note: Background/public-record. Disclosure and source of any criminal or court entry rather than removal alone; FCRA exemption pre-empted by asking which products they claim it for and to reconcile it with any consumer-reporting-agency disclaimer in their own terms; relatives-and-associates listings; and asked whether the site shares an index with any sibling property so one letter can cover them.

## Steps

1. Email `support@freebackgroundcheck.org`.
2. Search every former address and disconnected number.
3. Ask for **disclosure and source** of any criminal or court entry, not only
   removal.
4. Pre-empt the FCRA exemption.
5. Ask whether the site shares an index with any sibling property.

## Gotchas

As `fastbackgroundcheck.md`: **ask for disclosure before deletion** on anything
criminal or court-derived, because a common name is easily matched to the wrong
person and an entry hidden rather than corrected returns at the next ingest.

**Pre-empt the FCRA exemption** rather than waiting for it, and ask them to
reconcile it with any consumer-reporting-agency disclaimer in their own terms —
that disclaimer is common, because it serves a different commercial purpose, and
nobody inside the company reconciles the two documents. See `_DEFLECTIONS.md` §18.

The extra ask here is **sibling properties**. A `.org` background-check site is
frequently one skin over an index shared with several others, and asking them to
name the rest turns one letter into coverage of a family. `family_scan.py` finds
this from shared contact addresses, but only when the siblings are already in the
registry — asking the operator finds the ones that are not.

## Verification

Re-run the public search on **each** former address and each old number
separately, not just on the name. Then search a relative's listing for the
subject's name in the related-persons block — that is where a profile-scoped
removal leaves residue, and no confirmation will mention it.

Where a criminal or court entry was disclosed, keep the disclosure: it is the
evidence for a correction at source, which outlasts any removal here.

## The privacy policy links its own opt-out to the Internet Archive

`support@freebackgroundcheck.org`, the address on their home page, hard-bounces
with a 550. So the policy is the next place to look — and it is where this gets
strange.

Their Privacy Policy, dated **effective March 1, 2025**, has essentially every
actionable link rewritten to point at **web.archive.org snapshots taken in October
2024**:

| Link | Times |
|---|---|
| `members.freebackgroundcheck.org/optout` | 2 |
| the help page | 3 |
| terms, privacy | 2 |
| **`mailto:privacy@freebackgroundcheck.org`** | 2 |

A consumer clicking "opt out" in the privacy policy is sent to the Archive's
photograph of a form from last October, which cannot submit anything. Clicking the
privacy contact opens the Archive rather than a mail client. And the live opt-out
URL now **redirects back to the privacy policy**, so arriving from anywhere else
is a loop.

The net effect: **the site publishes no working removal route at all.** The
address on the home page bounces, and every route the policy offers is an archived
copy of itself.

It does not look deliberate. The likeliest explanation is that the policy page was
rebuilt from an archived version of their own site and the Archive's link
rewriting was left in — a lazy restore rather than a designed obstacle. But intent
does not change the outcome: anybody who has tried to opt out since March has
failed, and almost none of them will know it.

**What works:** the domain has live Google MX, so mail to
`privacy@freebackgroundcheck.org` is delivered even though the link to it is not.
Write there directly, and say what is broken — a fault this visible is worth
reporting, and it is also exactly the kind of thing a regulator complaint is built
on.

**The general lesson.** A published route can fail in a way that leaves the page
looking maintained: dated this year, professionally worded, comprehensive. Check
that the links *go somewhere live* before recording a route as available, and
treat an archive.org URL in a privacy policy as a dead route rather than a quirk.

