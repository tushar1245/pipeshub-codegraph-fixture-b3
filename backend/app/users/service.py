import logging

from app.shared.cache import Cache
from app.shared.errors import NotFoundError
from app.shared.events import EventBus
from app.shared.validation import require_fields, validate_email
from app.users.events import user_created
from app.users.models import User
from app.users.repository import UserRepository

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, repo: UserRepository, bus: EventBus, cache: Cache) -> None:
        self.repo = repo
        self.bus = bus
        self.cache = cache

    def get(self, key: str) -> User:
        cached = self.cache.get(f"users:{key}")
        if cached is not None:
            return cached
        user = self.repo.get(key)
        if user is None:
            raise NotFoundError("User", key)
        self.cache.set(f"users:{key}", user)
        return user

    def create(self, payload: dict) -> User:
        require_fields(payload, ("email", "name"))
        validate_email(payload["email"])
        user = User.from_dict(payload)
        self.repo.save(user)
        self.bus.publish(user_created(user))
        logger.info("created User %s", user.id)
        return user

    def list(self, limit: int = 50) -> list[User]:
        return self.repo.list(limit)

    def archive(self, key: str) -> User:
        user = self.get(key)
        user.archive()
        self.repo.save(user)
        return user
