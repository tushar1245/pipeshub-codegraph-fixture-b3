from ..shared.events import Event
from .models import Session


def session_created(session: Session) -> Event:
    return Event(name="auth.created", payload=session.to_dict())


def session_archived(session: Session) -> Event:
    return Event(name="auth.archived", payload={"id": session.id})
