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
- **One listing per request.** Multiple listings per person are common; each needs its own submission.
- reCAPTCHA is on the submit step and cannot be automated. Pre-fill the form and hand off.
- Spokeo states data may reappear as new public records are ingested — re-check quarterly.
- Prior addresses in the result listing are a good identity signal: match them against
  the phone area code (814 = central PA) rather than trusting the name alone.
