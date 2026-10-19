import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_required
from app.returns.events import return_request_created
from app.returns.models import ReturnRequest
from app.returns.repository import ReturnRequestRepository

logger = logging.getLogger(__name__)


class ReturnRequestService:
    def __init__(self, repo: ReturnRequestRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> ReturnRequest:
        cached = self.cache.get(f"returns:{key}")
        if cached is not None:
            return cached
        return_request = self.repo.get(key)
        if return_request is None:
            raise NotFoundError("ReturnRequest", key)
        self.cache.set(f"returns:{key}", return_request)
        return return_request

    def create(self, payload: dict) -> ReturnRequest:
        require_fields(payload, ("order_id", "reason"))
        validate_required(payload["order_id"])
        return_request = ReturnRequest.from_dict(payload)
        self.repo.save(return_request)
        self.bus.publish(return_request_created(return_request))
        logger.info("created ReturnRequest %s", return_request.id)
        return return_request

    def list(self, limit: int = 50) -> list[ReturnRequest]:
        return self.repo.list(limit)

    def archive(self, key: str) -> ReturnRequest:
        return_request = self.get(key)
        return_request.archive()
        self.repo.save(return_request)
        return return_request
