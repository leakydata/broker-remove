# Background Alert Inc

- **Email:** info@BackgroundAlert.com (verified)
- **Method:** unknown — Route not yet established.
- **Domain:** backgroundalert.com
- **Priority: 1.**

## Status

- Current: `unreachable` (updated 2026-09-12)
- Note: HARD BOUNCE 2026-09-12, two seconds after sending: '550 5.1... the address couldn't be found, or is unable to receive mail' for info@backgroundalert.com. That address came from the Optery directory (SF 445) and is the first of the four test letters to fail. THE DOMAIN IS NOT DEAD, WHICH IS THE INTERESTING PART: backgroundalert.com has live MX records (mx1/mx2.emailsrvr.com, Rackspace), so mail is configured -- it is the specific local-part that does not exist. But the WEBSITE does not respond at all: both the front page and a control path return no HTTP response whatsoever (curl exit with 000, not a 4xx or 5xx). So the picture is a domain whose mail is provisioned and whose site is gone, which usually means a company that has folded or moved without releasing the domain. NO ALTERNATIVE ROUTE FOUND and none guessed: with the site down there is nothing to scrape for a form or a different address, and firing probes at privacy@ and support@ would produce more indistinguishable bounces, which is exactly the failure mode the enrichment script's own docstring warns about. Recorded unreachable rather than failed: there is no route a consumer can use today. Worth a re-probe if the site returns.

## Steps

<!-- Replace once the route is confirmed. What actually worked, in order. -->

## Gotchas

<!-- Fill in from their reply. Recurring things worth capturing:
     - Do they refuse email and point at a form? Which form?
     - Is a CAPTCHA on page load (blocks automation) or at submit (can hand off)?
     - Does the form silently drop values not committed with an Add/+ button?
     - Do they gate on state of residence? Does their own form contradict that?
     - What does the removal NOT cover — name search only? FCRA-exempt products?
     - Any upsell to a paid removal service? -->

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->
