from dataclasses import dataclass

from app.shared.entity import Entity


@dataclass
class SearchQuery(Entity):
    text: str = ""
    limit: str = ""
    status: str = "active"

    def is_active(self) -> bool:
        return self.status == "active"

    def archive(self) -> None:
        self.status = "archived"
