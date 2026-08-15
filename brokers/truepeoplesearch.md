# TruePeopleSearch

- **Working route:** https://www.truepeoplesearch.com/privacy-rights  ← use this
- **Bot-gated:** https://www.truepeoplesearch.com/removal (Cloudflare blocks page load)
- **Do Not Sell:** https://www.truepeoplesearch.com/do-not-sell
- **Email: refused.** support@truepeoplesearch.com replies that it "does not process
  privacy requests received via email."
- **Priority: 5.**

## The circular trap — and the way out

Three routes, two of which dead-end:

1. **Email** → auto-reply: privacy requests not processed by email, use the form.
2. **`/privacy-rights` → "Right to Delete"** → *no form appears at all*, just text
   saying they can't delete third-party data, redirecting you to `/removal`.
3. **`/removal`** → Cloudflare challenge that blocks the page from loading.

**The way through:** on `/privacy-rights`, select **"Right to Know"** instead of
"Right to Delete". That reveals the full form and submits successfully. The
Turnstile widget on this page auto-passes; the one on `/removal` does not.

A Right to Know still has teeth — it compels disclosure of what they hold, creates
a dated record, and the same form offers **"I want to appeal the handling of my
privacy request"**, which gives you a documented basis to escalate.

## Form
`/privacy-rights` → Request category: *access, delete, or correct* → Request type:
**Right to Know** → Context: *no direct relationship* → First/Last/Email/
Requestor type (*subject of this request*)/Phone/Street/City/State/Zip → Submit.
Success page: `privacyrightsconfirmation?success=True`.

## Gotchas
- Their state dropdown lists **all 50 states including Pennsylvania**, even though
  their email implies only "states with a consumer privacy law" qualify. Fill it in
  regardless of state.
- They claim data "is not stored by us... retrieved from third-party data providers
  at the time you perform the search." Treat that as a position, not a fact — the
  listing still displays and still needs suppressing.
