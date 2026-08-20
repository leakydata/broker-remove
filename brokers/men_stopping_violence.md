# Men Stopping Violence

- **Opt-out:** https://www.menstoppingviolence.org/opt-out/
- **Email:** info@menstoppingviolence.org — **unverified, may bounce**
- **Method:** web_form — Web form.
- **Domain:** menstoppingviolence.org
- **Priority: 2.**

## Status

- Current: `confirmed` (updated 2026-08-19)
- Note: CONFIRMED: 'Your Removal Request is Confirmed. Men Stopping Violence is now working to remove all records for [name]. We will completely wipe the entry below and any other personal details from our systems in the next 24 hours.' The confirmation names the record back - name, age, city - and repeats the profile link, so it is unambiguous which record was actioned. Note the scope wording is unusually wide: 'the entry below AND ANY OTHER PERSONAL DETAILS from our systems', not merely the one profile page.

## Steps

1. Do NOT dismiss this entry on the name. See below — it is not what it sounds like.
2. Opt-out is at `/opt-out/` and is **URL-keyed**: it wants a profile link in the
   form `/people/<name>/<hash>/`.
3. Find the profile via their own name search, then submit the link and click the
   confirmation email they send.

## Gotchas

The domain is a repurposed charity, the site is Cloudflare-gated to plain fetches, and
the removal needs a profile URL rather than a name. Below.

## Verification

<!-- How to check it worked: the search URL to re-run, and their stated timeframe. -->

## This is not the charity whose name it wears

Men Stopping Violence was a real organisation working to end male violence against
women for over four decades. Its own site now says:

> *"Dear visitor! We regret to inform you that the Men Stopping Violence (MSV)
> initiative has closed mid-2024 after over four decades of work to end male violence
> against women and girls."*

Directly beneath that notice is a people-search product:

> *"301 Million People / 140 Million Criminal Record / 340 Million Phone Numbers /
> 305 Million Email Addresses / 442 Million Social Profiles"*

The charity's name, its `.org`, and pages of domestic-violence statistics are kept as
the surrounding content — a background-check funnel wearing the credibility of the
organisation that used to be there. See `_BROKER_FAMILIES.md` for the detection
pattern.

**The near-miss is the lesson.** This entry was about to be dropped from a send batch
as an obvious false positive — the reasoning being that one does not send a data-broker
deletion demand to a domestic-violence charity. That reasoning was correct about the
*name* and wrong about the *entity*, and one page load settled it. A registry entry
that looks absurd deserves thirty seconds of checking before it is dismissed, because
an expired-domain repurposing is invisible from the name and the name is the whole
point.

## Practicalities

Plain HTTP fetches get a **403** behind Cloudflare; the browser reaches it fine. Their
own first-name/last-name search did not navigate under automation, so the profile URL
could not be obtained — which is what the opt-out requires. Queued as a judgement call
rather than guessed at, on the same reasoning as Lookups.io: submitting a wrong profile
link removes a stranger's listing.
