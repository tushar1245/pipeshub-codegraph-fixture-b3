import random
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def backoff_delay(attempt: int, base: float = 0.2, cap: float = 5.0) -> float:
    return min(cap, base * (2 ** attempt)) * (0.5 + random.random() / 2)


def retry_with_backoff(fn: Callable[[], T], attempts: int = 4) -> T:
    last: Exception | None = None
    for attempt in range(attempts):
        try:
            return fn()
        except Exception as exc:
            last = exc
            time.sleep(backoff_delay(attempt))
    assert last is not None
    raise last
