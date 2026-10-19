from dataclasses import dataclass

from .models import Shipment


@dataclass
class ShipmentIn:
    order_id: str
    carrier: str

    @staticmethod
    def parse(body: dict) -> "ShipmentIn":
        return ShipmentIn(str(body.get("order_id", "")), str(body.get("carrier", "")))


@dataclass
class ShipmentOut:
    id: str
    status: str

    @staticmethod
    def from_model(shipment: Shipment) -> "ShipmentOut":
        return ShipmentOut(id=shipment.id, status=shipment.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
