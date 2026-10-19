from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.reviews.models import Review


class ReviewRepository(BaseRepository):
    table = "reviews"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Review | None:
        row = self.db.fetch_one(self.table, key)
        return Review.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Review]:
        return [Review.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, review: Review) -> Review:
        self.db.upsert(self.table, review.id, review.to_dict())
        return review
