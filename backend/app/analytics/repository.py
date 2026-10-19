from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.analytics.models import Metric


class MetricRepository(BaseRepository):
    table = "analytics"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Metric | None:
        row = self.db.fetch_one(self.table, key)
        return Metric.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Metric]:
        return [Metric.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, metric: Metric) -> Metric:
        self.db.upsert(self.table, metric.id, metric.to_dict())
        return metric
