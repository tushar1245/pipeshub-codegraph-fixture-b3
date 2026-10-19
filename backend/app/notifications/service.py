import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_required
from app.notifications.events import notification_created
from app.notifications.models import Notification
from app.notifications.repository import NotificationRepository

logger = logging.getLogger(__name__)


class NotificationService:
    def __init__(self, repo: NotificationRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Notification:
        cached = self.cache.get(f"notifications:{key}")
        if cached is not None:
            return cached
        notification = self.repo.get(key)
        if notification is None:
            raise NotFoundError("Notification", key)
        self.cache.set(f"notifications:{key}", notification)
        return notification

    def create(self, payload: dict) -> Notification:
        require_fields(payload, ("user_id", "channel"))
        validate_required(payload["user_id"])
        notification = Notification.from_dict(payload)
        self.repo.save(notification)
        self.bus.publish(notification_created(notification))
        logger.info("created Notification %s", notification.id)
        return notification

    def list(self, limit: int = 50) -> list[Notification]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Notification:
        notification = self.get(key)
        notification.archive()
        self.repo.save(notification)
        return notification
