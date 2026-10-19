import json

from requests import get

from app.shared.retry import retry_with_backoff


def fetch_carrier_status(url: str) -> dict:
    response = retry_with_backoff(lambda: get(url, timeout=5))
    return json.loads(response.text)
