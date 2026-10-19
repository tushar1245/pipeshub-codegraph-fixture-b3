from app.shared.cache import Cache
from app.shared.events import EventBus
from app.auth.repository import SessionRepository
from app.auth.service import SessionService
from tests.fakes import FakeDatabase


def make_service() -> SessionService:
    return SessionService(SessionRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"user_id": "x-1", "token": "token-1"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
