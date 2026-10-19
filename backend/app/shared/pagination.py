from dataclasses import dataclass


@dataclass
class Page:
    items: list
    page: int
    size: int
    total: int

    def to_dict(self) -> dict:
        return {"items": self.items, "page": self.page, "size": self.size, "total": self.total}


def paginate(items: list, page: int, size: int) -> dict:
    start = (page - 1) * size
    return Page(items[start:start + size], page, size, len(items)).to_dict()
