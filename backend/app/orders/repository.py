from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.orders.models import Order


class OrderRepository(BaseRepository):
    table = "orders"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Order | None:
        row = self.db.fetch_one(self.table, key)
        return Order.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Order]:
        return [Order.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, order: Order) -> Order:
        self.db.upsert(self.table, order.id, order.to_dict())
        return order
