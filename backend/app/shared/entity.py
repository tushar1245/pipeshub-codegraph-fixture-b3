"""Base type for every persisted record."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field

from app.shared.clock import now
from app.shared.ids import new_id


@dataclass
class Entity:
    id: str = field(default_factory=new_id)
    created_at: float = field(default_factory=now)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Entity":
        known = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        return cls(**known)
