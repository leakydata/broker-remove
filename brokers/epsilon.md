# Epsilon

- **Working route:** https://legal.epsilon.com/dsr  ← the only route they accept
- **Phone (US):** +1-866-267-3861
- **Email: REFUSED**, and emphatically: *"We do not accept privacy requests
  received via email... responses to this message will not be answered."*
  Replies come from `privacy_EPS@publicisresources.com` (Publicis Groupe).
- **Priority: 5.** One of the largest US marketing data aggregators — upstream, so
  a removal here reduces re-population downstream.

## The portal takes ONE request type per submission

> *"Only one request per submission. Multiple submissions are accepted."*

Eight types are offered, and they are **not** interchangeable:

1. Do not sell my Personal Information
2. Do not share / Opt-out of Cross-Context Behavioral or Targeted Advertising
3. Access my Personal Information & 3rd Party Disclosures
4. Correct my Personal Information
5. **Delete my Personal Information**
6. Opt-out of Profiling / Automated Decision-Making
7. Opt-out / Revoke Consent for Sensitive Personal Information
8. Appeal a prior request

**Submitting only "Delete" leaves the opt-outs unexercised.** Budget for several
passes: Delete first, then Do Not Sell, Do Not Share, Profiling, and Sensitive PI.

## Progress
- [x] Delete my Personal Information — *Request Received Successfully*
- [x] Do not sell my Personal Information — *Request Received Successfully*
- [ ] Do not share / Opt-out of Cross-Context Behavioral or Targeted Advertising
- [ ] Opt-out of Profiling / Automated Decision-Making
- [ ] Opt-out / Revoke Consent for Sensitive Personal Information

## Route
`/dsr` → Country: **United States** → pick one request type → I am a: **Consumer**
→ Email / First / Last / Street / City / State / ZIP → **Submit request**.
Success: *"Request Received Successfully."* An invisible reCAPTCHA runs; no click.

## Gotchas
- **The cookie banner offers a real "Decline"** — take it. Note their own text:
  *"Submitting your request below will attempt to access your device to read your
  cookie ID... cookie IDs are unique per browser so you will need to repeat this
  process on each browser/device you use."* That is a genuine limitation: a
  submission from one browser does not cover your other devices.
- **Dismissing the cookie banner shifts the page**, which silently moved every
  value down one field in testing — name into Last Name, address into City, and
  the typed city landed in the State dropdown, changing it to **California**. That
  would have misstated residency on a legal request. Screenshot and verify every
  field before submitting.
- Employees/applicants use a different address: privacyofficer@publicisgroupe.com.
- **`form_input` by element ref does not populate the text fields** on this form —
  it reports success and leaves them empty, while the State dropdown accepts it
  fine. Click by coordinate and type instead, then screenshot to confirm.
