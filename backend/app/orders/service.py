import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_amount
from app.orders.events import order_created
from app.orders.models import Order
from app.orders.repository import OrderRepository

logger = logging.getLogger(__name__)


class OrderService:
    def __init__(self, repo: OrderRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Order:
        cached = self.cache.get(f"orders:{key}")
        if cached is not None:
            return cached
        order = self.repo.get(key)
        if order is None:
            raise NotFoundError("Order", key)
        self.cache.set(f"orders:{key}", order)
        return order

    def create(self, payload: dict) -> Order:
        require_fields(payload, ("customer_id", "total"))
        validate_amount(payload["total"])
        order = Order.from_dict(payload)
        self.repo.save(order)
        self.bus.publish(order_created(order))
        logger.info("created Order %s", order.id)
        return order

    def list(self, limit: int = 50) -> list[Order]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Order:
        order = self.get(key)
        order.archive()
        self.repo.save(order)
        return order
