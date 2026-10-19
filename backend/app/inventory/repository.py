from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.inventory.models import InventoryItem


class InventoryItemRepository(BaseRepository):
    table = "inventory"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> InventoryItem | None:
        row = self.db.fetch_one(self.table, key)
        return InventoryItem.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[InventoryItem]:
        return [InventoryItem.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, inventory_item: InventoryItem) -> InventoryItem:
        self.db.upsert(self.table, inventory_item.id, inventory_item.to_dict())
        return inventory_item
