from dataclasses import dataclass

from .models import Notification


@dataclass
class NotificationIn:
    user_id: str
    channel: str

    @staticmethod
    def parse(body: dict) -> "NotificationIn":
        return NotificationIn(str(body.get("user_id", "")), str(body.get("channel", "")))


@dataclass
class NotificationOut:
    id: str
    status: str

    @staticmethod
    def from_model(notification: Notification) -> "NotificationOut":
        return NotificationOut(id=notification.id, status=notification.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
