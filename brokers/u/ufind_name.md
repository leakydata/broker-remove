# Ufind Name

- **Opt-out:** https://ufind.name/opt-out
- **Email:** support@ufind.name — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** ufind.name
- **Priority: 2.**

## Status

- Current: `captcha_blocked` (updated 2026-08-20)
- Note: Form staged 2026-08-20 08:05 UTC, blocked on CAPTCHA. Route: ufind.name/opt-out, which takes ONLY a page URL - no name, no email, no message field - plus a CAPTCHA. The page loads BOTH an hCaptcha and a reCAPTCHA widget (two textareas, h-captcha-response and g-recaptcha-response), which is unusual and may mean either will satisfy it or that one is vestigial. NO PUBLISHED EMAIL ANYWHERE on the site, so this form is the only route. THE SUBSTANTIVE FIND IS THE PAGE ITSELF: ufind.name/[PERSONAL]+[PERSONAL] is a name-aggregate carrying 331 records across many unrelated people of the same name, and it republishes HISTORICAL WHOIS REGISTRATION DATA - 30 domains with registrant name, contact address and phone as recorded before registrar redaction became standard. One of those entries carries a prior address from the profile. That is a data source not represented anywhere else in this project: pre-GDPR WHOIS snapshots are archived and resold by domain-intelligence firms, and a removal here does nothing about the upstream archives.

## Steps

`https://ufind.name/opt-out` is the only route — **the site publishes no email
address anywhere**.

The form takes a **page URL and nothing else**: no name, no email, no message
field, no way to identify individual records. Paste the aggregate page URL,
solve the CAPTCHA, submit.

## Gotchas

- **Both an hCaptcha and a reCAPTCHA load on the page** — two response
  textareas, `h-captcha-response` and `g-recaptcha-response`. Unusual; either
  one may satisfy it or one may be vestigial. Hand off regardless.
- **The page is a name-aggregate, not a profile.** `/{First}+{Last}` returns
  every record the site holds for that name — in this case 331 records across
  many unrelated people. Because the opt-out form operates on a URL, removal is
  necessarily at page granularity. That is the site's own design, not a choice
  the requester makes, but it is worth telling the human before they submit:
  strangers' records come down too. That is not a harm to them, but it should
  not be a surprise.
- **Read the page before submitting, because it names its sources.** This one
  carries CV and social-profile entries, vehicle and real-estate records, and —
  the find worth the whole exercise — a block of **historical WHOIS
  registrations** with registrant addresses and phone numbers (§67).
- **Do not confuse an aggregate hit with a match.** Most of the 331 records
  belong to other people with the same name. Establish which are actually the
  subject's by matching against known prior addresses before claiming any of
  them; see §60 on not asserting more than the evidence supports.

## Verification

Re-fetch `https://ufind.name/{First}+{Last}` cold and check whether the specific
records identified as the subject's are gone — matching on the prior addresses
that identified them, not on the name, since the name will still return other
people.
