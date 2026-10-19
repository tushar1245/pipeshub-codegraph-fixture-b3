from ..shared.events import Event
from .models import InventoryItem


def inventory_item_created(inventory_item: InventoryItem) -> Event:
    return Event(name="inventory.created", payload=inventory_item.to_dict())


def inventory_item_archived(inventory_item: InventoryItem) -> Event:
    return Event(name="inventory.archived", payload={"id": inventory_item.id})
