from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.coupons.models import Coupon


class CouponRepository(BaseRepository):
    table = "coupons"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Coupon | None:
        row = self.db.fetch_one(self.table, key)
        return Coupon.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Coupon]:
        return [Coupon.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, coupon: Coupon) -> Coupon:
        self.db.upsert(self.table, coupon.id, coupon.to_dict())
        return coupon
