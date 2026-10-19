import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_required
from app.shipping.events import shipment_created
from app.shipping.models import Shipment
from app.shipping.repository import ShipmentRepository

logger = logging.getLogger(__name__)


class ShipmentService:
    def __init__(self, repo: ShipmentRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Shipment:
        cached = self.cache.get(f"shipping:{key}")
        if cached is not None:
            return cached
        shipment = self.repo.get(key)
        if shipment is None:
            raise NotFoundError("Shipment", key)
        self.cache.set(f"shipping:{key}", shipment)
        return shipment

    def create(self, payload: dict) -> Shipment:
        require_fields(payload, ("order_id", "carrier"))
        validate_required(payload["order_id"])
        shipment = Shipment.from_dict(payload)
        self.repo.save(shipment)
        self.bus.publish(shipment_created(shipment))
        logger.info("created Shipment %s", shipment.id)
        return shipment

    def list(self, limit: int = 50) -> list[Shipment]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Shipment:
        shipment = self.get(key)
        shipment.archive()
        self.repo.save(shipment)
        return shipment
