#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Render a plain-text letter as HTML, because Gmail rewrites the plain one.

A letter to 411.com went out opening:

    To the Privacy Officer at https://www.google.com/url?q=http://411.com&
    source=gmail&ust=1787832692238000&sa=E,

Gmail's linkifier found the bare domain in the salutation and replaced the
VISIBLE TEXT with a tracking redirect. Not a link with sensible text -- the URL
itself, as the first line of a privacy request, which is the letter where looking
legitimate matters most. Corporate mail filters also score google.com/url
redirects.

Tested directly (2026-08-26), sending the same text both ways:

    plain body: 411.com -> visible text becomes the full redirect URL
    html body:  411.com -> <a href="...redirect...">411.com</a>, text intact

So the rule is: send letters as HTML. The link wrapper is unavoidable and
harmless; losing the visible text is neither. Bare domains elsewhere in the same
message (Remodeling.com, Addresses.com mid-sentence) were left alone in both
forms, so the trigger is narrow -- but narrow is not the same as predictable, and
guessing which names are safe is more fragile than just sending HTML.

Letters are written as plain text with hard-wrapped lines, so the conversion has
to preserve the wrapping: newlines become <br/>, leading spaces become &nbsp; or
indentation collapses and every identifier list turns into one paragraph.
"""

import html as _html
import re as _re

# Letters use markdown-style emphasis for the one or two sentences that carry
# the request. In plain text the asterisks read as emphasis; in HTML they read
# as a typo, so convert them. Emphasis can span a hard-wrapped line break, so
# this runs over the whole escaped text before it is split -- <strong> around a
# <br/> is legal and renders correctly.
_BOLD = _re.compile(r"\*\*(.+?)\*\*", _re.S)
_ITALIC = _re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", _re.S)


def to_html(text):
    """Plain-text letter -> HTML that renders identically."""
    esc_all = _html.escape(text, quote=False)
    esc_all = _BOLD.sub(r"<strong>\1</strong>", esc_all)
    esc_all = _ITALIC.sub(r"<em>\1</em>", esc_all)
    out = []
    for esc in esc_all.split("\n"):
        # Leading whitespace is significant: the identifier lists and the
        # sibling-brand block are indented, and HTML would eat it.
        stripped = esc.lstrip(" ")
        pad = "&nbsp;" * (len(esc) - len(stripped))
        out.append(pad + stripped)
    return "<div>" + "<br/>\n".join(out) + "</div>"


if __name__ == "__main__":
    import sys
    sys.stdout.write(to_html(sys.stdin.read()))
