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

## Progress — all five applicable types filed

- [x] Delete my Personal Information — *Request Received Successfully*
- [x] Do not sell my Personal Information — *Request Received Successfully*
- [x] Do not share / Opt-out of Cross-Context Behavioral or Targeted Advertising
- [x] Opt-out of Profiling / Automated Decision-Making
- [x] Opt-out / Revoke Consent for Sensitive Personal Information

(Type 3 "Access" and type 4 "Correct" were not filed: an access request asks them
to compile and send a copy of the profile, which is the opposite of the goal, and
there is nothing to correct in a record you want deleted. Type 8 "Appeal" only
applies once a request has been refused.)

**The confirmation page shows no reference number, but one does arrive by email.**
Within a minute or two OneTrust sends "(Request ID: XXXXXXXXXX) Request logged
successfully" from `noreply@m.onetrust.com`, branded *Publicis Global*. That email
is the artifact worth keeping, and it names the request type back to you — which
is the only practical way to confirm the portal recorded what you intended.

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
  it reports success and leaves them empty, while the *dropdowns* (Country,
  State/Province, "I am a...") accept it fine. Use `form_input` for every `select`
  and keyboard entry for every text box.
- **The page scrolls itself while you work it.** Selecting a request type expands
  the form, and the browser re-anchors the viewport several times as content
  loads. Twice in testing a click landed on the intended field, the page moved a
  few hundred pixels before the keystrokes arrived, and the text went nowhere —
  leaving a field silently blank. It also put the wrong radio button under the
  cursor once, selecting "Sensitive Personal Information" when the intent was
  "Do not share".

### The reliable way to fill this form

Coordinates are the problem, so use them exactly once:

1. **Radio buttons and dropdowns: address them by element ref**, never by
   coordinate. A ref survives the page moving underneath it; a coordinate does not.
2. **Click the Email box once** (the only unavoidable coordinate), screenshot to
   confirm the caret is actually in it, then **Tab between every remaining field**:
   Email → First → Last → Street → City → State → ZIP → Submit.
   Tab order matches visual order exactly.
3. The State dropdown responds to typing its full name while focused, so the
   whole run — including the select and the final submit via Return — can be done
   without touching the mouse again.

That sequence filled and submitted the form correctly on the first attempt, after
two coordinate-driven attempts had lost fields.

## The failure that cost three submissions: the radio that only *looks* selected

Three separate "Delete" submissions came back from OneTrust as **"Do not sell my
Personal Information"**. The requests were real and were logged — they were just
the wrong type, and nothing on screen said so.

The cause is visible only at pixel level. Clicking a radio **by element ref** gives
it a focus ring but does **not** check it; the previously-checked option stays
checked, and "Do not sell" is the one the form lands on. A focused-but-unchecked
radio and a selected one look nearly identical:

| Appearance | Meaning |
|---|---|
| Ring around an empty circle | focused only — **not** selected |
| Solid filled circle | actually selected |

Two things follow, and both are cheap:

- **Click request-type radios by coordinate, not by ref.** Refs work fine for the
  dropdowns (Country, State, "I am a...", the date-of-birth selects); they do not
  work for these radios.
- **Screenshot the radio group and confirm the circle is filled before filling in
  anything else.** Without the emailed Request ID naming the type back, this error
  is undetectable — the confirmation page is word-for-word identical no matter
  which type you submitted.

Pressing Space to select a focused radio does not work either: it scrolls the page
and resets the form.

## "Delete" is a different form from the other request types

Selecting Delete does not just swap a label — it changes the form:

- **No "I am a..." dropdown.** It goes straight to the fields.
- **Different field order**: First Name, Last Name, Email, Street, City, State,
  ZIP — Email is *third*, not first. A Tab-chain written for the other types will
  put your email in the wrong box.
- **Date of Birth (Month/Day/Year) is required.** Submitting without it fails with
  *"Date of Birth fields are required"*. The rest of the form survives the failed
  submit, so just fill the three selects and submit again.
- The page states: *"Deletion and Correction requests require verification via
  email."*

### Delete is not filed until you click the link in the email

Instead of "Request Received Successfully" you get **"One More Step! Your identity
needs to be verified."** OneTrust then emails a **Confirm email** button, and only
after clicking it does the page say *"Your request is confirmed!"*

Until that click, the deletion request does not exist as far as Epsilon is
concerned — but a tracker updated at submit time will happily show it as done.
Treat the "Delete" submission and its verification click as one step; a Delete
recorded without the confirmation is a Delete that never happened.

## Restarting for the next request type

The confirmation page has a **"< Start new request"** link. It resets the form
completely — **Country reverts to blank** and must be set to United States again
before the request-type radios will render at all. If the radios seem to be
missing, that is why.
