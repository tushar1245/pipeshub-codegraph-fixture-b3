from app.shared.cache import Cache
from app.shared.events import EventBus
from app.billing.repository import InvoiceRepository
from app.billing.service import InvoiceService
from tests.fakes import FakeDatabase


def make_service() -> InvoiceService:
    return InvoiceService(InvoiceRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"customer_id": "customer_id-1", "amount": "12.50"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
