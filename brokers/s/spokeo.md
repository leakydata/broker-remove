# Spokeo

- **Opt-out:** https://www.spokeo.com/optout
- **Method:** web_form + reCAPTCHA
- **Email fallback:** privacy@spokeo.com

## Steps
1. Spokeo needs a *profile URL*, not a name. Search first:
   `https://www.spokeo.com/{First}-{Last}/{State}/{City}` (e.g. `/Jane-Smith/Texas/Houston`)
2. Result links look like `/Jane-Smith/Texas/Houston/p12345678`. Grab the `pNNNN` URL.
3. On `/optout`: paste profile URL, enter email, tick reCAPTCHA, click OPT OUT.
4. Confirmation email arrives — the link must be clicked or the request is void.

## Gotchas
- **`form_input` silently fails here.** The inputs are React-controlled: setting
  `.value` directly reports success and then re-renders back to empty. Click the
  field and *type* so real key events fire. Always screenshot to verify a field
  actually holds its value before handing off for a CAPTCHA — a stale "success"
  from form_input will otherwise waste the user's solve.
- **One listing per request.** Multiple listings per person are common; each needs its own submission.
- reCAPTCHA is on the submit step and cannot be automated. Pre-fill the form and hand off.
- Spokeo states data may reappear as new public records are ingested — re-check quarterly.
- Prior addresses in the result listing are a good identity signal: match them against
  the phone area code (814 = central PA) rather than trusting the name alone.

## Who they are, and how to reach them

*Filed by the company itself with a state data broker registry — a public
record they are legally required to keep current. Use the **legal entity**
name in any formal demand; it is frequently not the brand on the website.*

- **Legal entity:** Spokeo, Inc.
- **Trading as:** freepeopledirectory.com, peoplewin.com, thatsthem.com
- **Registered address:** 199 S. Los Robles Avenue, Suite 711, Pasadena,
  CA
- **Filed contact email:** legal@spokeo.com
- **Website:** https://www.spokeo.com

*Source: `data/registries/registry2024.csv`.*

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
