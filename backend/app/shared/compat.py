import sys

try:
    import orjson

    def fast_dumps(value) -> bytes:
        return orjson.dumps(value)
except ImportError:
    import json

    def fast_dumps(value) -> bytes:
        return json.dumps(value, separators=(",", ":")).encode()

if sys.version_info >= (3, 11):
    from datetime import UTC, datetime

    def utcnow() -> datetime:
        return datetime.now(UTC)
else:
    from datetime import datetime, timezone

    def utcnow() -> datetime:
        return datetime.now(timezone.utc)
