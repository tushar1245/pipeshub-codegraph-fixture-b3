from app.shared.cache import Cache
from app.shared.events import EventBus
from app.reviews.repository import ReviewRepository
from app.reviews.service import ReviewService
from tests.fakes import FakeDatabase


def make_service() -> ReviewService:
    return ReviewService(ReviewRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"product_id": "product_id-1", "rating": "5"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
