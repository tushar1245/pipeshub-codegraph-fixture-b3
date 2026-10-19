from dataclasses import dataclass

from .models import WishlistItem


@dataclass
class WishlistItemIn:
    user_id: str
    product_id: str

    @staticmethod
    def parse(body: dict) -> "WishlistItemIn":
        return WishlistItemIn(str(body.get("user_id", "")), str(body.get("product_id", "")))


@dataclass
class WishlistItemOut:
    id: str
    status: str

    @staticmethod
    def from_model(wishlist_item: WishlistItem) -> "WishlistItemOut":
        return WishlistItemOut(id=wishlist_item.id, status=wishlist_item.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
