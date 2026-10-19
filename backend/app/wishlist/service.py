import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_required
from app.wishlist.events import wishlist_item_created
from app.wishlist.models import WishlistItem
from app.wishlist.repository import WishlistItemRepository

logger = logging.getLogger(__name__)


class WishlistItemService:
    def __init__(self, repo: WishlistItemRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> WishlistItem:
        cached = self.cache.get(f"wishlist:{key}")
        if cached is not None:
            return cached
        wishlist_item = self.repo.get(key)
        if wishlist_item is None:
            raise NotFoundError("WishlistItem", key)
        self.cache.set(f"wishlist:{key}", wishlist_item)
        return wishlist_item

    def create(self, payload: dict) -> WishlistItem:
        require_fields(payload, ("user_id", "product_id"))
        validate_required(payload["user_id"])
        wishlist_item = WishlistItem.from_dict(payload)
        self.repo.save(wishlist_item)
        self.bus.publish(wishlist_item_created(wishlist_item))
        logger.info("created WishlistItem %s", wishlist_item.id)
        return wishlist_item

    def list(self, limit: int = 50) -> list[WishlistItem]:
        return self.repo.list(limit)

    def archive(self, key: str) -> WishlistItem:
        wishlist_item = self.get(key)
        wishlist_item.archive()
        self.repo.save(wishlist_item)
        self.cache.invalidate(f"wishlist:{key}")
        return wishlist_item
