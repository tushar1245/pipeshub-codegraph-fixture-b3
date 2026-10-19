from dataclasses import dataclass

from app.shared.entity import Entity


@dataclass
class Session(Entity):
    user_id: str = ""
    token: str = ""
    status: str = "active"

    def is_active(self) -> bool:
        return self.status == "active"

    def archive(self) -> None:
        self.status = "archived"
