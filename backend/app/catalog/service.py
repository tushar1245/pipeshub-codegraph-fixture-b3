import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require, validate_sku
from app.catalog.events import product_created
from app.catalog.models import Product
from app.catalog.repository import ProductRepository

logger = logging.getLogger(__name__)


class ProductService:
    def __init__(self, repo: ProductRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Product:
        cached = self.cache.get(f"catalog:{key}")
        if cached is not None:
            return cached
        product = self.repo.get(key)
        if product is None:
            raise NotFoundError("Product", key)
        self.cache.set(f"catalog:{key}", product)
        return product

    def create(self, payload: dict) -> Product:
        require(payload, ("sku", "title"))
        validate_sku(payload["sku"])
        product = Product.from_dict(payload)
        self.repo.save(product)
        self.bus.publish(product_created(product))
        logger.info("created Product %s", product.id)
        return product

    def list(self, limit: int = 50) -> list[Product]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Product:
        product = self.get(key)
        product.archive()
        self.repo.save(product)
        self.cache.invalidate(f"catalog:{key}")
        return product
