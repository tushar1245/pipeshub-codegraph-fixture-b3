"""Utilities for writing code that runs on Python 2 and 3 (vendored)."""
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


def get(mapping, key, default=None):
    return mapping.get(key, default)


def ensure_text(value, encoding="utf-8"):
    return value.decode(encoding) if isinstance(value, bytes) else value
