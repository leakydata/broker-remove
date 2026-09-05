# SmartBackgroundChecks

- **Opt-out:** https://www.smartbackgroundchecks.com/optoutcheck
- **Method:** web_form — Web form.
- **Domain:** smartbackgroundchecks.com
- **Priority: 4.**

## Status

- Current: `captcha_blocked` (updated 2026-09-05)
- Note: Staged 2026-09-05, blocked on reCAPTCHA. The opt-out URL on file (/optoutcheck) is a 404; the live route is footer 'Do Not Sell or Share My Personal Information' -> /do-not-sell -> 'Opt-Out Form' -> /optout. Email and the subject/authorization checkbox are filled. Two structural notes. (1) FIVE-RECORD CAP per pass: after the CAPTCHA you search and may select at most five records, so a common name needs repeated passes and the count left behind has to be tracked or the removal silently ends up partial. (2) THEIR NOTICE DISCLAIMS DURABILITY IN WRITING: 'our products and services use publicly available information, which is not covered by State Privacy Laws ... we will try to apply your request to the publicly available information we collect, as a courtesy ... we regularly receive new public records so even if you opt out, your publicly available information may appear in our data products again in the future. We recommend you periodically refresh your opt-out request.' That is a company stating that its own opt-out expires. Needs a diary re-run, and a 'confirmed' here would mean something weaker than it does anywhere else. Also: the page prints 'This site is exceeding reCAPTCHA Enterprise free quota', so a CAPTCHA that will not complete is their quota rather than a dead route. Phone alternative in the notice: 800-571-0614.

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
