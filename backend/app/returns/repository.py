from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.returns.models import ReturnRequest


class ReturnRequestRepository(BaseRepository):
    table = "returns"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> ReturnRequest | None:
        row = self.db.fetch_one(self.table, key)
        return ReturnRequest.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[ReturnRequest]:
        return [ReturnRequest.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, return_request: ReturnRequest) -> ReturnRequest:
        self.db.upsert(self.table, return_request.id, return_request.to_dict())
        return return_request
