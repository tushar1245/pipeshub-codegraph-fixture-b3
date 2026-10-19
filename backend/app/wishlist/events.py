from ..shared.events import Event
from .models import WishlistItem


def wishlist_item_created(wishlist_item: WishlistItem) -> Event:
    return Event(name="wishlist.created", payload=wishlist_item.to_dict())


def wishlist_item_archived(wishlist_item: WishlistItem) -> Event:
    return Event(name="wishlist.archived", payload={"id": wishlist_item.id})
