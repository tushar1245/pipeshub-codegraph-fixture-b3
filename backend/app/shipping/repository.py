from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.shipping.models import Shipment


class ShipmentRepository(BaseRepository):
    table = "shipping"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Shipment | None:
        row = self.db.fetch_one(self.table, key)
        return Shipment.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Shipment]:
        return [Shipment.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, shipment: Shipment) -> Shipment:
        self.db.upsert(self.table, shipment.id, shipment.to_dict())
        return shipment
