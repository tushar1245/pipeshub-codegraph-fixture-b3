from app.legacy.requests import get
from app.legacy.retry import retry_with_backoff


def pull_feed(url: str) -> bytes:
    return retry_with_backoff(lambda: get(url))
