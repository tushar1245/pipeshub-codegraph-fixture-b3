from ..shared.events import Event
from .models import User


def user_created(user: User) -> Event:
    return Event(name="users.created", payload=user.to_dict())


def user_archived(user: User) -> Event:
    return Event(name="users.archived", payload={"id": user.id})
