from app.shared.base_repository import BaseRepository
from app.shared.db import Database
from app.search.models import SearchQuery


class SearchQueryRepository(BaseRepository):
    table = "search"

    def __init__(self, db: Database) -> None:
        super().__init__(db)

    def get(self, key: str) -> SearchQuery | None:
        row = self.db.fetch_one(self.table, key)
        return SearchQuery.from_dict(row) if row else None

    def list(self, limit: int = 50) -> list[SearchQuery]:
        return [SearchQuery.from_dict(row) for row in self.db.fetch_many(self.table, limit)]

    def save(self, search_query: SearchQuery) -> SearchQuery:
        self.db.upsert(self.table, search_query.id, search_query.to_dict())
        return search_query
