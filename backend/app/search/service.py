import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require, validate_required
from app.search.events import search_query_created
from app.search.models import SearchQuery
from app.search.repository import SearchQueryRepository

logger = logging.getLogger(__name__)


class SearchQueryService:
    def __init__(self, repo: SearchQueryRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> SearchQuery:
        cached = self.cache.get(f"search:{key}")
        if cached is not None:
            return cached
        search_query = self.repo.get(key)
        if search_query is None:
            raise NotFoundError("SearchQuery", key)
        self.cache.set(f"search:{key}", search_query)
        return search_query

    def create(self, payload: dict) -> SearchQuery:
        require(payload, ("text", "limit"))
        validate_required(payload["text"])
        search_query = SearchQuery.from_dict(payload)
        self.repo.save(search_query)
        self.bus.publish(search_query_created(search_query))
        logger.info("created SearchQuery %s", search_query.id)
        return search_query

    def list(self, limit: int = 50) -> list[SearchQuery]:
        return self.repo.list(limit)

    def archive(self, key: str) -> SearchQuery:
        search_query = self.get(key)
        search_query.archive()
        self.repo.save(search_query)
        self.cache.invalidate(f"search:{key}")
        return search_query
