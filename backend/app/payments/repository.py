from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.payments.models import Payment


class PaymentRepository(BaseRepository):
    table = "payments"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Payment | None:
        row = self.db.fetch_one(self.table, key)
        return Payment.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Payment]:
        return [Payment.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, payment: Payment) -> Payment:
        self.db.upsert(self.table, payment.id, payment.to_dict())
        return payment
