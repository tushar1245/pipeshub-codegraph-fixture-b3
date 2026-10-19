from app.shared.cache import Cache
from app.shared.events import EventBus
from app.inventory.repository import InventoryItemRepository
from app.inventory.service import InventoryItemService
from tests.fakes import FakeDatabase


def make_service() -> InventoryItemService:
    return InventoryItemService(InventoryItemRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"sku": "SKU-1001", "quantity": "quantity-1"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
