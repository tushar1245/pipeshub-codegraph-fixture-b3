import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_percent
from app.coupons.models import Coupon
from app.coupons.repository import CouponRepository

logger = logging.getLogger(__name__)


class CouponService:
    def __init__(self, repo: CouponRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Coupon:
        cached = self.cache.get(f"coupons:{key}")
        if cached is not None:
            return cached
        coupon = self.repo.get(key)
        if coupon is None:
            raise NotFoundError("Coupon", key)
        self.cache.set(f"coupons:{key}", coupon)
        return coupon

    def create(self, payload: dict) -> Coupon:
        require_fields(payload, ("code", "percent"))
        validate_percent(payload["percent"])
        coupon = Coupon.from_dict(payload)
        self.repo.save(coupon)
        logger.info("created Coupon %s", coupon.id)
        return coupon

    def list(self, limit: int = 50) -> list[Coupon]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Coupon:
        coupon = self.get(key)
        coupon.archive()
        self.repo.save(coupon)
        return coupon
