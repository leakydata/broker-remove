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

## Status

- Current: `submitted` (updated 2026-09-03)
- **2026-09-03 (§294):** THREE REMAINING REQUEST TYPES PRESSED BY EMAIL 2026-09-03 (SILENT_FAILURES 293/290). Two of five filed via the DSR portal: Delete my Personal Information (VNCPHY7L53) and Do Not Sell (HZRTNAEGLM). The portal takes ONE REQUEST TYPE PER SUBMISSION, so the remaining three -- Do Not Share/cross-context behavioural advertising, opt-out of profiling/automated decision-making, and 1798.121 limit-use of sensitive PI -- each need their own submission, reference, verification and clock. Named the effect: THE PERSON WHO WANTS THE MOST PROTECTION DOES THE MOST WORK, and each extra submission is another chance for one to lapse unnoticed. Argued all three are DIRECTIONS RATHER THAN LOOKUPS -- none asks them to find me, hand me anything, or change a record, only to say what not to do with what they hold -- and that the opt-out explicitly requires no verification under the CCPA regulations, with the same logic reaching 1798.121 and profiling. Asked them to record all three from the email, and offered the exit: if their position is that each must go through the portal, that is a clear statement of policy, I will record it, make the submissions and not raise it again. ALSO ASKED about the FIVE Epsil

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Epsilon Data Management, LLC
- **Registered address:** 6021 Connection Drive, Irving, TX, 75039
- **Filed contact email:** privacy@epsilon.com
- **Filed phone:** 8662673861
- **Website:** www.epsilon.com

*Source: `data/registries/registry.csv`.*

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Open the opt-out page:** https://legal.epsilon.com/dsr
2. **Search for yourself first if the page asks you to.** Match on more than the name: use age, current city, and at least one previous address. A common name will return other people, and removing their listing instead of yours helps nobody.
3. **Submit the form**, then watch for a confirmation email. Many brokers treat the request as void until a link in it is clicked.
4. **Or email `privacy@epsilon.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
5. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
6. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

## If they ignore you

Work down this list. Each rung costs them more than the one above it.

1. **Reply in the existing thread** after the statutory deadline. California
   allows 45 days for a deletion request (Cal. Civ. Code 1798.130), extendable
   once by a further 45 with notice. Quote the date you first wrote.
2. **Write to the legal entity at the registered address above**, by post, if
   email has failed. A letter to the address of record is harder to lose than a
   support ticket, and it establishes a paper trail.
3. **Complain to the California Attorney General**, who administers the data
   broker registry: <https://oag.ca.gov/contact/consumer-complaint-against-business-or-company>.
   A broker's registration is what obliges it to answer; a complaint referencing
   the registry entry is the pressure point.
4. **Complain to the FTC**: <https://reportfraud.ftc.gov>. Useful for a pattern
   of non-response rather than a single case.
5. **Your own state Attorney General.** Many states with no comprehensive
   privacy statute still have consumer-protection powers and will take a
   complaint about a business that ignores its own published policy.

**What not to bother with:** phoning a support line to argue. The person who
answers cannot change the policy and did not write it. The registry entry, the
statutory deadline and the regulator are what actually move a company.
