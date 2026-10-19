from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.notifications.models import Notification


class NotificationRepository(BaseRepository):
    table = "notifications"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> Notification | None:
        row = self.db.fetch_one(self.table, key)
        return Notification.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[Notification]:
        return [Notification.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, notification: Notification) -> Notification:
        self.db.upsert(self.table, notification.id, notification.to_dict())
        return notification
