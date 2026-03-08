from __future__ import annotations

import re

import bleach
import markdown


_ALLOWED_TAGS = [
    "a",
    "blockquote",
    "br",
    "code",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "li",
    "ol",
    "p",
    "pre",
    "strong",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "tr",
    "ul",
]

_ALLOWED_ATTRIBUTES = {
    "a": ["href", "rel", "target", "title"],
}

_ALLOWED_PROTOCOLS = ["http", "https", "mailto"]


def _normalize_markdown(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = re.sub(r"(?m)^(\s*(?:[-*+]|\d+[.)]))\s*$\n+(\S)", r"\1 \2", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def render_markdown_to_html(text: str) -> str:
    normalized = _normalize_markdown(text)
    raw_html = markdown.markdown(
        normalized,
        extensions=["extra", "sane_lists"],
        output_format="html5",
    )

    return bleach.clean(
        raw_html,
        tags=_ALLOWED_TAGS,
        attributes=_ALLOWED_ATTRIBUTES,
        protocols=_ALLOWED_PROTOCOLS,
        strip=True,
    )