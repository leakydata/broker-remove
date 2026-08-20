# Paramount Direct Marketing

- **Email:** ccpa@paramountdirectmarketing.com — **unverified, may bounce**
- **Method:** email — Statutory request by email. No web form needed.
- **Domain:** paramountdirectmarketing.com
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-08-19)
- Note: The emailed letter bounced: ccpa@paramountdirectmarketing.com is Recipient Unknown - an address published for CCPA requests that does not exist. The bounce itself was the useful part: it came from postmaster@PARAMOUNTLISTS.COM, naming the Office 365 tenant behind the domain and therefore a sibling brand nobody advertised. A non-delivery report is a family-detection signal in its own right; the sending tenant is on the envelope even when the website says nothing. Their web form is better than most in two ways: separate CA and NON-CA routes, so the jurisdiction question never arises, and the request types are MULTI-SELECT checkboxes - Right to Opt Out and Right to Delete can both be asked for in one submission rather than needing two runs. Both ticked, form filled and verified; reCAPTCHA gates submission. Also note they geolocate: 'the state you select is compared against the general location of your connection', so this cannot be submitted on someone's behalf from elsewhere.

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
