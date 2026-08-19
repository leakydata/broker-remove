# Paramount Direct Marketing

- **Email:** ccpa@paramountdirectmarketing.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** paramountdirectmarketing.com
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-08-19)
- Note: Direct-mail list compilation and brokerage; same suppression-first shape as outward_media with the sensitive-select list named individually and the delete-not-flag distinction spelled out. Brokerage adds one wrinkle worth keeping: their copy is one of many and usually not the one that reaches the subject, so recipients-and-direct-them matters more here than the deletion itself. Asked which brands the ccpa@ mailbox covers.

## Steps

1. Write to `ccpa@paramountdirectmarketing.com`.
   Their MX is Microsoft 365 and delivers.
2. Same suppression-first ordering as `outward_media.md`.

## Gotchas

All of the `outward_media.md` gotchas apply — suppression before deletion,
source and consent wording, the individually-named sensitive selects, and the
delete-rather-than-flag distinction.

**Brokerage adds one thing.** Where a business brokers other people's lists as
well as compiling its own, its copy is one of many and usually *not* the one that
reaches the subject. So the recipients ask — every party the details were rented,
brokered, licensed or sold to, with a direction to each to delete — carries more
weight than the deletion itself.

Ask which brands and list properties the `ccpa@` mailbox serves. A shared
compliance alias across several entities is common in this category, and a
confirmation scoped to one entity looks identical to a complete removal.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->


## Outcome: the address does not exist, and the bounce named the parent

`ccpa@paramountdirectmarketing.com` — the address they publish for CCPA requests —
returned **Recipient Unknown**. An address named for the exact purpose it cannot
serve.

The bounce was worth more than the letter would have been. It came from
**`postmaster@paramountlists.com`**, naming the Office 365 tenant that hosts the
domain, and therefore a sibling brand that appears nowhere on the website.

> **A non-delivery report is a family-detection signal.** The sending tenant is on
> the envelope even when the site says nothing about who owns it. Read the
> postmaster domain on every bounce, not just the error code.

## The web form, which is better than most

Two things this operator gets right and most do not:

**Separate `/do-not-sell-ca` and `/do-not-sell-non-ca` routes.** The
jurisdiction question never arises: a non-California resident is not asked to
claim a statute that does not apply to them, and is not turned away for lacking
one.

**Request types are multi-select checkboxes** — *Right to Opt Out* and *Right to
Delete* can both be asked for in a single submission. Compare Data Axle and
Path2Response, where a single-select control silently halves the request unless
you run the form twice.

Gates: reCAPTCHA on submit, and a geolocation check stated on the page —
*"For fraud prevention, the state you select is compared against the general
location of your connection."* That has a practical consequence worth recording:
**this form cannot be completed on someone's behalf from another state**, and a
VPN exit node will fail it.
