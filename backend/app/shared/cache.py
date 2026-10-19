import time


class Cache:
    def __init__(self, ttl: float = 300.0) -> None:
        self.ttl = ttl
        self._items: dict[str, tuple[float, object]] = {}

    def get(self, key: str):
        hit = self._items.get(key)
        if hit is None or hit[0] < time.time():
            return None
        return hit[1]

    def set(self, key: str, value) -> None:
        self._items[key] = (time.time() + self.ttl, value)
