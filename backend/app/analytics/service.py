import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_required
from app.analytics.events import metric_created
from app.analytics.models import Metric
from app.analytics.repository import MetricRepository

logger = logging.getLogger(__name__)


class MetricService:
    def __init__(self, repo: MetricRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Metric:
        cached = self.cache.get(f"analytics:{key}")
        if cached is not None:
            return cached
        metric = self.repo.get(key)
        if metric is None:
            raise NotFoundError("Metric", key)
        self.cache.set(f"analytics:{key}", metric)
        return metric

    def create(self, payload: dict) -> Metric:
        require_fields(payload, ("name", "value"))
        validate_required(payload["name"])
        metric = Metric.from_dict(payload)
        self.repo.save(metric)
        self.bus.publish(metric_created(metric))
        logger.info("created Metric %s", metric.id)
        return metric

    def list(self, limit: int = 50) -> list[Metric]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Metric:
        metric = self.get(key)
        metric.archive()
        self.repo.save(metric)
        self.cache.invalidate(f"analytics:{key}")
        return metric
