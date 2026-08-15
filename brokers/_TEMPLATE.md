# <Broker Name>

- **Opt-out:** <url>
- **Method:** web_form | web_form_captcha | email | account_required | postal | phone
- **Email fallback:** <verified address — not a guess>
- **Phone / postal fallback:** <if published>
- **Priority: <1-5>.** <one line on why — upstream aggregator? widely scraped?>

## Steps

1. <Each step. Note whether a search is needed first, and how to identify the
   right record when the name is common.>
2. <...>

## Gotchas

<Delete what doesn't apply. Keep what cost you time.>

- **CAPTCHA:** where is it — page load or submit? Page-load gates block automation
  entirely; submit gates can be handed to a human at the last moment.
- **Commit-then-continue:** does the form silently drop values that weren't added
  to a list with a "+" or "Add" button?
- **Controlled inputs:** if setting values programmatically doesn't stick, say so —
  React/Vue forms often need real typed key events.
- **Email confirmation:** is the request void until a link is clicked?
- **Scope limits:** what does this *not* remove? Name-search only? Public-facing
  products only? Anything exempt under the FCRA?
- **Reappearance:** does the broker say data may return from new source records?
- **Upsell:** does the flow push a paid removal service over the free path?

## Verification

<How to check it worked — the search URL to re-run, and how long the broker says
it takes.>
