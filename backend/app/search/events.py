from ..shared.events import Event
from .models import SearchQuery


def search_query_created(search_query: SearchQuery) -> Event:
    return Event(name="search.created", payload=search_query.to_dict())


def search_query_archived(search_query: SearchQuery) -> Event:
    return Event(name="search.archived", payload={"id": search_query.id})
