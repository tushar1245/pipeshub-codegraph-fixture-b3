from app.shared.cache import Cache
from app.shared.events import EventBus
from app.notifications.repository import NotificationRepository
from app.notifications.service import NotificationService
from tests.fakes import FakeDatabase


def make_service() -> NotificationService:
    return NotificationService(NotificationRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"user_id": "x-1", "channel": "channel-1"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
