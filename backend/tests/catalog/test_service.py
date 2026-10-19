from app.shared.cache import Cache
from app.shared.events import EventBus
from app.catalog.repository import ProductRepository
from app.catalog.service import ProductService
from tests.fakes import FakeDatabase


def make_service() -> ProductService:
    return ProductService(ProductRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"sku": "SKU-1001", "title": "title-1"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
