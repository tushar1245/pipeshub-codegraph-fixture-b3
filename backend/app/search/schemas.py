from dataclasses import dataclass

from .models import SearchQuery


@dataclass
class SearchQueryIn:
    text: str
    limit: str

    @staticmethod
    def parse(body: dict) -> "SearchQueryIn":
        return SearchQueryIn(str(body.get("text", "")), str(body.get("limit", "")))


@dataclass
class SearchQueryOut:
    id: str
    status: str

    @staticmethod
    def from_model(search_query: SearchQuery) -> "SearchQueryOut":
        return SearchQueryOut(id=search_query.id, status=search_query.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
