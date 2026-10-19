import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_amount
from app.billing.events import invoice_created
from app.billing.models import Invoice
from app.billing.repository import InvoiceRepository

logger = logging.getLogger(__name__)


class InvoiceService:
    def __init__(self, repo: InvoiceRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Invoice:
        cached = self.cache.get(f"billing:{key}")
        if cached is not None:
            return cached
        invoice = self.repo.get(key)
        if invoice is None:
            raise NotFoundError("Invoice", key)
        self.cache.set(f"billing:{key}", invoice)
        return invoice

    def create(self, payload: dict) -> Invoice:
        require_fields(payload, ("customer_id", "amount"))
        validate_amount(payload["amount"])
        invoice = Invoice.from_dict(payload)
        self.repo.save(invoice)
        self.bus.publish(invoice_created(invoice))
        logger.info("created Invoice %s", invoice.id)
        return invoice

    def list(self, limit: int = 50) -> list[Invoice]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Invoice:
        invoice = self.get(key)
        invoice.archive()
        self.repo.save(invoice)
        self.cache.invalidate(f"billing:{key}")
        return invoice
