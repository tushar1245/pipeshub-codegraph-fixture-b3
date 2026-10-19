from app.shared.cache import Cache
from app.shared.events import EventBus
from app.users.repository import UserRepository
from app.users.service import UserService
from tests.fakes import FakeDatabase


def make_service() -> UserService:
    return UserService(UserRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"email": "ada@example.com", "name": "name-1"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
