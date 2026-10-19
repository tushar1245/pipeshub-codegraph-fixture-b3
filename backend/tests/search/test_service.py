from app.shared.cache import Cache
from app.shared.events import EventBus
from app.search.repository import SearchQueryRepository
from app.search.service import SearchQueryService
from tests.fakes import FakeDatabase


def make_service() -> SearchQueryService:
    return SearchQueryService(SearchQueryRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"text": "x-1", "limit": "limit-1"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
