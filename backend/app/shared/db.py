"""Thin wrapper over the SQL driver."""
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, dsn: str) -> None:
        self.dsn = dsn
        self._rows: dict[str, dict[str, dict]] = {}

    def fetch_one(self, table: str, key: str) -> dict | None:
        return self._rows.get(table, {}).get(key)

    def fetch_many(self, table: str, limit: int) -> list[dict]:
        return list(self._rows.get(table, {}).values())[:limit]

    def upsert(self, table: str, key: str, row: dict) -> None:
        logger.debug("upsert %s/%s", table, key)
        self._rows.setdefault(table, {})[key] = row

    def delete(self, table: str, key: str) -> bool:
        return self._rows.get(table, {}).pop(key, None) is not None

    @contextmanager
    def transaction(self):
        yield self
