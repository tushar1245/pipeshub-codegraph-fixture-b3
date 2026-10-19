from app.shared.cache import Cache
from app.shared.events import EventBus
from app.shipping.repository import ShipmentRepository
from app.shipping.service import ShipmentService
from tests.fakes import FakeDatabase


def make_service() -> ShipmentService:
    return ShipmentService(ShipmentRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"order_id": "x-1", "carrier": "carrier-1"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
