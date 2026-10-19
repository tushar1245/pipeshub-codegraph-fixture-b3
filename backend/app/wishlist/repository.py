from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.wishlist.models import WishlistItem


class WishlistItemRepository(BaseRepository):
    table = "wishlist"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> WishlistItem | None:
        row = self.db.fetch_one(self.table, key)
        return WishlistItem.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[WishlistItem]:
        return [WishlistItem.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, wishlist_item: WishlistItem) -> WishlistItem:
        self.db.upsert(self.table, wishlist_item.id, wishlist_item.to_dict())
        return wishlist_item
