"""The pre-2023 HTTP shim, kept for the nightly batch jobs."""
import urllib.request


def get(url: str, timeout: float = 10.0) -> bytes:
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return response.read()
