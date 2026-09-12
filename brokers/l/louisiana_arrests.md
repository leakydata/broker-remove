# Louisiana Arrests

- **Opt-out:** https://infotracer.com/optout/
- **Email:** privacy@infotracer.com (verified)
- **Method:** web_form — Web form.
- **Domain:** louisianaarrests.org
- **Priority: 2.**

## Status

- Current: `covered_by_sibling` (updated 2026-09-07)
- Reference: `infotracer ticket 544087 -- zero records, suppression on each ingestion`
- Note: RESOLVED 2026-09-06 AS AN AFFILIATE FRONT-END, NOT A BROKER. This row is one of 53 that share a single recorded route, infotracer.com/optout/. Investigated properly tonight rather than left as a shared URL. WHAT THESE SITES ARE, from their own footer, verbatim: 'The owners of this site do not own the records found on this site or any public records database. All records presented on this site are gathered from third party databases that are not controlled by the owners of this site... The website owners receive compensation if you complete a registration through our website.' So the site is a search box and a commission. It holds no records; the records are InfoPay's. THE UPSTREAM IS ALREADY CLOSED. InfoPay (ticket 544087) confirmed zero records under the subject's identifiers, named the identifiers and record categories searched, and applied SUPPRESSION RE-APPLIED ON EACH SUBSEQUENT INGESTION -- the durable form. Their stated reason for scope was checkable rather than an assurance: 'a record cannot appear on a redirect or sibling brand without first existing on InfoPay.' These sites are downstream of exactly that. WHAT THE SWEEP OF ALL 53 DOMAINS FOUND: 22 publish their own /privacy-request-portal, a WPForms form with a CAPTCHA; 27 return 404 on that path; 3 return a page with no form. The family is NOT uniform, and the single route recorded against all 53 was an inference, not an observation. TWO THINGS THAT MATTER MORE THAN THE COUNT. First, the portals that exist are about USER ACCOUNT DATA -- their own text lists 'your email address, search history, payment records, and other data from using the site' -- NOT about the published arrest records. For someone who never used the site, that portal is the wrong instrument: it governs the visitor, not the subject. Second, the subject's OWN STATE SITE, pennsylvaniaarrests.org, is one of the 27 with no portal at all. The site publishing Pennsylvania arrest records offers a Pennsylvanian nothing but a privacy policy. See SILENT_FAILURES 390. Not writing to these individually: there is nobody at the other end holding a record, and the one entity that was has already answered completely.

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
