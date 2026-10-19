from dataclasses import dataclass

from .models import InventoryItem


@dataclass
class InventoryItemIn:
    sku: str
    quantity: str

    @staticmethod
    def parse(body: dict) -> "InventoryItemIn":
        return InventoryItemIn(str(body.get("sku", "")), str(body.get("quantity", "")))


@dataclass
class InventoryItemOut:
    id: str
    status: str

    @staticmethod
    def from_model(inventory_item: InventoryItem) -> "InventoryItemOut":
        return InventoryItemOut(id=inventory_item.id, status=inventory_item.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
