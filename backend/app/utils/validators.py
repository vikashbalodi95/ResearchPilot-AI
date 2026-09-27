"""Validation helpers used across the research workflow."""

import re


def is_valid_question(question: str) -> bool:
    text = (question or "").strip()
    return len(text) >= 5 and len(text) <= 1000


def sanitize_filename(filename: str) -> str:
    if not filename:
        return "document.pdf"
    cleaned = re.sub(r"[^a-zA-Z0-9_.-]", "_", filename)
    return cleaned or "document.pdf"
