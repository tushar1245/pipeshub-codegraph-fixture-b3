import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_rating
from app.reviews.events import review_created
from app.reviews.models import Review
from app.reviews.repository import ReviewRepository

logger = logging.getLogger(__name__)


class ReviewService:
    def __init__(self, repo: ReviewRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Review:
        cached = self.cache.get(f"reviews:{key}")
        if cached is not None:
            return cached
        review = self.repo.get(key)
        if review is None:
            raise NotFoundError("Review", key)
        self.cache.set(f"reviews:{key}", review)
        return review

    def create(self, payload: dict) -> Review:
        require_fields(payload, ("product_id", "rating"))
        validate_rating(payload["rating"])
        review = Review.from_dict(payload)
        self.repo.save(review)
        self.bus.publish(review_created(review))
        logger.info("created Review %s", review.id)
        return review

    def list(self, limit: int = 50) -> list[Review]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Review:
        review = self.get(key)
        review.archive()
        self.repo.save(review)
        self.cache.invalidate(f"reviews:{key}")
        return review
