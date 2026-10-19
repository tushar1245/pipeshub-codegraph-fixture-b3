from app.shared.cache import Cache
from app.shared.events import EventBus
from app.coupons.repository import CouponRepository
from app.coupons.service import CouponService
from tests.fakes import FakeDatabase


def make_service() -> CouponService:
    return CouponService(CouponRepository(FakeDatabase()), EventBus(), Cache())


def test_create_then_get():
    service = make_service()
    created = service.create({"code": "code-1", "percent": "10"})
    assert service.get(created.id).id == created.id


def test_get_missing_raises():
    service = make_service()
    try:
        service.get("missing")
    except Exception as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("expected a NotFoundError")
