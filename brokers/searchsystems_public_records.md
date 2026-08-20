# Searchsystems Public Records

- **Opt-out:** https://publicrecords.searchsystems.net/opt-out.php
- **Email:** webmaster@searchsystems.net — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** publicrecords.searchsystems.net
- **Priority: 2.**

## Status

- Current: `unreachable` (updated 2026-08-20)
- Note: ALL THREE PUBLISHED ROUTES ARE DEAD. (1) webmaster@searchsystems.net -> 550 address not found. (2) info@searchsystems.net, printed on their own Contact page -> 550 5.1.1 address not found. Domain has live Zoho MX, so mail is accepted for the domain and refused at the mailbox. (3) The Contact page form is DECORATIVE: there is no <form> element on the page at all, the Send Message control is <button type='button'> with onclick null, and no script references the field ids. Filling it and clicking Send makes no request of any kind and produces no error -- the page simply sits. Only remaining routes are two telephone numbers, (805) 574-9367 and 1-888-717-3223. MITIGATING: their own homepage FAQ states unprompted that they hold nothing -- 'SearchSystems.net is a directory - it links you directly to the official government source where records are maintained. We do not aggregate, scrape, or resell personal information.' So the practical exposure is likely nil; what is unreachable is the ability to have that confirmed.

## Steps

**There is no working route.** All three published ones fail — see Gotchas. What
was tried, in order:

1. `webmaster@searchsystems.net` (the address carried in broker lists) → **550**.
2. `info@searchsystems.net`, printed on their own Contact page → **550 5.1.1**.
3. The Contact page form → **decorative**; clicking Send makes no request at all.

Two telephone numbers remain and have not been tried: **(805) 574-9367** and
**1-888-717-3223**.

Before spending anything further on this entry, read the Verification section: the
site's own FAQ may already be the answer.

## Gotchas

- **Both published addresses hard-bounce**, and the domain has live Zoho MX — so
  mail is accepted for the domain and refused at the mailbox. `5.1.1` is
  user-unknown rather than a policy rejection, which is why a second local part was
  worth trying; it failed too.
- **The Contact form is pure markup.** There is no `<form>` element on the page,
  the Send control is `<button type="button">` with `onclick` null, and no script
  references the field ids. It accepts input and then does nothing, with no error.
  See [[_SILENT_FAILURES]] §62.
- Do **not** queue that form for a human. A gated form may work for a person; a
  form with no handler will not work for anyone.
- The site links out to a separate background-check property. That is a different
  operator and needs its own entry — do not let this one's null result cover it.

## Verification

Nothing was submitted, so there is nothing to verify. The entry is `unreachable` on
route availability, not on a refusal.

**The mitigating fact worth recording alongside it** is that their own homepage
answers the substantive question unprompted, and more clearly than most operators
manage when asked directly:

> "SearchSystems.net is a **directory** — it links you directly to the official
> government source where records are maintained. **We do not aggregate, scrape, or
> resell personal information.** People-search sites compile data from many sources
> into profiles and charge you to view them. We point you to the primary source."

If that is accurate, the exposure here is nil and the only thing genuinely lost is
the ability to have it confirmed for a specific person.

**Re-check by testing the two email addresses again**, and by re-inspecting the
Contact page for a real `<form>` element. Both are one command each, and the form
is the kind of fault that gets fixed silently in a redesign.
