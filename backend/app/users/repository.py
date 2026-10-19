from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.users.models import User


class UserRepository(BaseRepository):
    table = "users"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> User | None:
        row = self.db.fetch_one(self.table, key)
        return User.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[User]:
        return [User.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, user: User) -> User:
        self.db.upsert(self.table, user.id, user.to_dict())
        return user
