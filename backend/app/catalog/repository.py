from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.catalog.models import Product


class ProductRepository(BaseRepository):
    table = "catalog"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Product | None:
        row = self.db.fetch_one(self.table, key)
        return Product.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Product]:
        return [Product.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, product: Product) -> Product:
        self.db.upsert(self.table, product.id, product.to_dict())
        return product
