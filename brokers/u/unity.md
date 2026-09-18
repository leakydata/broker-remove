# Unity

- **Method:** unknown — Route not yet established.
- **Domain:** unity.com
- **Priority: 1.**

## Status

- Current: `replied` (updated 2026-09-17)
- Reference: `gmail:1a0a55ed60a41f81`
- Note: NEW DEFLECTION 2026-09-15, ticket #3498629, Maria: "As you declined to
  provide your advertising ID in your original request, we have no means of
  identifying the data associated with your device and are therefore unable to
  process an opt-out of advertising-related processing." This conflates two
  different things: a real technical limit (cannot search or suppress a device
  they have no Ad ID for) and an unsupported one (cannot honor an opt-out at
  all without it). 11 CCR 7026(f) forbids conditioning an opt-out on identity
  verification, and the request was never to identify a device — it was to
  record the opt-out against name/email/postal so it applies if those are ever
  matched to an Ad ID later. Replied 2026-09-17 drawing that line explicitly,
  accepting the technical limit, and re-asking for (1) the opt-out recorded
  against name/email/postal, confirmed network-wide, and (2) a plain
  cannot-search-on-these-keys or a result for each of the four systems (ad
  network, analytics, marketing/CRM, partner returns) still never itemised
  across three rounds.
- Prior: PARTIAL ANSWER 2026-09-07, ticket #3498629, from a named agent. THE ONE SENTENCE THAT IS AN ANSWER, verbatim: 'I do not see a Unity Account associated with the email(s) listed and therefore cannot take action on this request to erase your personal data.' Accepted for what it covers -- there is no Unity Account and nothing in their account system. THE REST OF THE MESSAGE IS THE PAGE THE LETTER WAS ABOUT. The remainder is the verbatim text of unity.com/legal/do-not-sell-my-personal-information, which the original letter had already quoted -- the Ad ID explanation, the three routes for players, developers and website visitors, and the sentence about not having enough information to locate records through an email request. The letter was an ARGUMENT about why that page does not answer a request from someone outside a game; receiving the page back does not advance it. Said so without rancour and assumed it was not intended. THE SCOPE PROBLEM, which is the substance: the letter named FIVE systems deliberately, because Unity's own page describes five relationships -- the ad network, analytics, developer/account systems, marketing and CRM, and whatever comes back from partners. THEY SEARCHED THE THIRD. Their own page says the ad network is where the data actually is, that the Ad ID 'may include information on you such as your location, the device you are using, and some of the activities you've completed in your game.' 'No Unity Account' and 'nothing about you at Unity' are different statements and only the first has been made. See SILENT_FAILURES 330, 358. THE OPT-OUT WAS NOT MENTIONED AT ALL. Pressed: 11 CCR 7026(f) forbids conditioning an opt-out on identity verification, so the absence of an account is a reason a DELETION cannot complete and is not a reason to decline an OPT-OUT. Asked for it recorded against name, email and postal address, confirmed in writing, and confirmed as NETWORK-WIDE rather than per-title, since their page scopes the in-game control to 'the game you are playing at that time' and a 1798.120 opt-out is not per-title. THE EXIT RESTATED AND STILL OPEN: if the truthful position is that the ad network is keyed to Ad IDs and cannot be searched by name, email or postal address, saying so in those words will be accepted, recorded and not argued with -- it would establish the data is pseudonymous in a way that makes the request unanswerable rather than merely declined. What cannot be recorded is a nil about the account system standing in for an answer about the ad network. Two things stated as closing this: the opt-out recorded network-wide and confirmed; and either an itemised nil across ad network, analytics, marketing/CRM and partner returns, or a plain statement that those cannot be searched on the keys given.

## Steps

*Written for anyone, not just the person who filed the original request.*

1. **Email `dpo@unity3d.com`** with a written request. Ask for four things explicitly — deletion, opt-out of sale and sharing, a direction to any third parties they sold to, and a **forward-looking suppression** so the record is not simply re-added at the next data import.
2. **List every address, email and phone number you have ever had**, not just current ones. Records are filed under whatever was current when they were created — a search on today's details misses them.
3. **Ask them to state which identifiers matched.** "We deleted your record" and "we searched and found nothing" are different outcomes, and a reply that does not distinguish them tells you nothing about whether you were ever in the file.

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

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Unity Technologies SF
- **Registered address:** 30 3rd Street, San Francisco, CA 94103, United
  States
- **Filed contact email:** dpo@unity3d.com
- **Website:** https://unity.com/
- **Opt-out route they filed:** We have provided instructions to opt-out
  and obtain data reports at
  https://unity3d.com/legal/do-not-sell-my-personal-information.
- **Route for protected individuals:** Submit a request to
  dpo@unity3d.com (Cal. Gov. Code 6208.1(b) / 6254.21(c)(1) — for
  survivors of domestic violence, stalking and similar, a stronger and
  faster route than the ordinary consumer request)
- **What they say they collect:** Please see our privacy policy at
  https://unity3d.com/legal/privacy-policy

*Source: `data/registries/complete-reg-data-brokers.csv`.*

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
