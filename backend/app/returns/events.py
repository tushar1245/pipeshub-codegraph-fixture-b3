from ..shared.events import Event
from .models import ReturnRequest


def return_request_created(return_request: ReturnRequest) -> Event:
    return Event(name="returns.created", payload=return_request.to_dict())


def return_request_archived(return_request: ReturnRequest) -> Event:
    return Event(name="returns.archived", payload={"id": return_request.id})
