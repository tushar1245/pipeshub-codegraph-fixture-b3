from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.auth.models import Session


class SessionRepository(BaseRepository):
    table = "auth"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Session | None:
        row = self.db.fetch_one(self.table, key)
        return Session.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Session]:
        return [Session.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, session: Session) -> Session:
        self.db.upsert(self.table, session.id, session.to_dict())
        return session
