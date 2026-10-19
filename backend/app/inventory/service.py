import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_sku
from app.inventory.events import inventory_item_created
from app.inventory.models import InventoryItem
from app.inventory.repository import InventoryItemRepository

logger = logging.getLogger(__name__)


class InventoryItemService:
    def __init__(self, repo: InventoryItemRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> InventoryItem:
        cached = self.cache.get(f"inventory:{key}")
        if cached is not None:
            return cached
        inventory_item = self.repo.get(key)
        if inventory_item is None:
            raise NotFoundError("InventoryItem", key)
        self.cache.set(f"inventory:{key}", inventory_item)
        return inventory_item

    def create(self, payload: dict) -> InventoryItem:
        require_fields(payload, ("sku", "quantity"))
        validate_sku(payload["sku"])
        inventory_item = InventoryItem.from_dict(payload)
        self.repo.save(inventory_item)
        self.bus.publish(inventory_item_created(inventory_item))
        logger.info("created InventoryItem %s", inventory_item.id)
        return inventory_item

    def list(self, limit: int = 50) -> list[InventoryItem]:
        return self.repo.list(limit)

    def archive(self, key: str) -> InventoryItem:
        inventory_item = self.get(key)
        inventory_item.archive()
        self.repo.save(inventory_item)
        return inventory_item
