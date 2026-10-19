from abc import ABC, abstractmethod

from app.shared.db import Database
from app.shared.entity import Entity


class BaseRepository(ABC):
    table: str = ""

    def __init__(self, db: Database) -> None:
        self.db = db

    @abstractmethod
    def get(self, key: str) -> Entity | None: ...

    @abstractmethod
    def list(self, limit: int = 50) -> list[Entity]: ...

    @abstractmethod
    def save(self, entity: Entity) -> Entity: ...

    def delete(self, key: str) -> bool:
        return self.db.delete(self.table, key)

    def exists(self, key: str) -> bool:
        return self.get(key) is not None
