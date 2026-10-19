import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require, validate_required
from app.auth.events import session_created
from app.auth.models import Session
from app.auth.repository import SessionRepository

logger = logging.getLogger(__name__)


class SessionService:
    def __init__(self, repo: SessionRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> Session:
        cached = self.cache.get(f"auth:{key}")
        if cached is not None:
            return cached
        session = self.repo.get(key)
        if session is None:
            raise NotFoundError("Session", key)
        self.cache.set(f"auth:{key}", session)
        return session

    def create(self, payload: dict) -> Session:
        require(payload, ("user_id", "token"))
        validate_required(payload["user_id"])
        session = Session.from_dict(payload)
        self.repo.save(session)
        self.bus.publish(session_created(session))
        logger.info("created Session %s", session.id)
        return session

    def list(self, limit: int = 50) -> list[Session]:
        return self.repo.list(limit)

    def archive(self, key: str) -> Session:
        session = self.get(key)
        session.archive()
        self.repo.save(session)
        self.cache.invalidate(f"auth:{key}")
        return session
