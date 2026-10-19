import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_amount
from app.payments.events import payment_created
from app.payments.models import Payment
from app.payments.repository import PaymentRepository

logger = logging.getLogger(__name__)


class PaymentService:
    def __init__(self, repo: PaymentRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Payment:
        cached = self.cache.get(f"payments:{key}")
        if cached is not None:
            return cached
        payment = self.repo.get(key)
        if payment is None:
            raise NotFoundError("Payment", key)
        self.cache.set(f"payments:{key}", payment)
        return payment

    def create(self, payload: dict) -> Payment:
        require_fields(payload, ("order_id", "amount"))
        validate_amount(payload["amount"])
        payment = Payment.from_dict(payload)
        self.repo.save(payment)
        self.bus.publish(payment_created(payment))
        logger.info("created Payment %s", payment.id)
        return payment

    def list(self, limit: int = 50) -> list[Payment]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Payment:
        payment = self.get(key)
        payment.archive()
        self.repo.save(payment)
        return payment
