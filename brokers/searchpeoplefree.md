# SearchPeopleFREE

- **Opt-out:** https://www.searchpeoplefree.com/opt-out
- **Method:** two-stage — name+email → emailed link → full form
- **Gate:** Cloudflare Turnstile on the first stage, but it **auto-passes**
  (observed showing "Success!" without interaction). Page itself is not blocked.
- **Priority: 4.**

## Route
1. `/opt-out` → First / **Middle** / Last / Email + consent checkbox →
   **Begin removal process**
2. A link is emailed. **Expires in 24 hours** — after that, request a new one.
3. The linked form takes the full record details. Their guidance is explicit:
   *"Omitting information or providing inaccurate information on the opt-out form
   will only hinder the opt-out process."* Fill everything, including middle name.
4. Confirmation page + confirmation email. **3 days** to full removal.

Same two-stage shape as PeopleFinders — see `brokers/peoplefinders.md`, whose
pre-filled-name trap is worth re-reading before doing this one.

## Gotchas
- **Their matching is strict.** From their own FAQ: *"If our system cannot match
  the provided information to a record, the information will not be removed."* A
  near-miss silently fails rather than erroring — supply prior addresses and old
  phone numbers.
- To verify, they instruct you to **clear browser cache first**, then search again.
  A cached page will show a stale listing and look like failure.
- Heavy third-party ads on the page shift the layout as they load, which
  invalidates element references mid-form. Re-locate fields immediately before
  typing, and screenshot to confirm values landed.

## Lead worth following
Their own page advertises **EnformionGO** as the partner API behind their data
("Fast Developer API for Contact Enrichment, Sales, and Marketing Intelligence").
**Enformion is the upstream source** — removal here does not touch it. Worth
adding Enformion to the registry and filing separately; upstream removals reduce
re-population downstream.
