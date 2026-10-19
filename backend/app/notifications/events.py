from ..shared.events import Event
from .models import Notification


def notification_created(notification: Notification) -> Event:
    return Event(name="notifications.created", payload=notification.to_dict())


def notification_archived(notification: Notification) -> Event:
    return Event(name="notifications.archived", payload={"id": notification.id})
