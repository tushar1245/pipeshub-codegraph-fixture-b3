from app.shared.cache import Cache
from app.shared.events import EventBus
from app.analytics.repository import MetricRepository
from app.analytics.service import MetricService
from tests.fakes import FakeDatabase


def make_service() -> MetricService:
    return MetricService(MetricRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"name": "x-1", "value": "value-1"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
