# ThatsThem

- **Opt-out:** https://thatsthem.com/optout
- **Method:** web_form, no CAPTCHA. Fully automatable.

## Steps
Single page form, all fields required:
Full Name / Street Address / City / State (select, 2-letter) / ZIP / Email / Phone
→ "Submit Opt-Out Request". Success renders inline: "Request Submitted!"

## Gotchas
- No search step and no CAPTCHA — one of the easiest. Good first target.
- State field is a `<select>` keyed on the 2-letter code.
- Confirmation email within 72h; processing stated at 72h.
