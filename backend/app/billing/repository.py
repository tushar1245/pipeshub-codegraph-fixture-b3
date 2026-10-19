from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.billing.models import Invoice


class InvoiceRepository(BaseRepository):
    table = "billing"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Invoice | None:
        row = self.db.fetch_one(self.table, key)
        return Invoice.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Invoice]:
        return [Invoice.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, invoice: Invoice) -> Invoice:
        self.db.upsert(self.table, invoice.id, invoice.to_dict())
        return invoice
