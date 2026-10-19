from dataclasses import dataclass

from .models import Order


@dataclass
class OrderIn:
    customer_id: str
    total: str

    @staticmethod
    def parse(body: dict) -> "OrderIn":
        return OrderIn(str(body.get("customer_id", "")), str(body.get("total", "")))


@dataclass
class OrderOut:
    id: str
    status: str

    @staticmethod
    def from_model(order: Order) -> "OrderOut":
        return OrderOut(id=order.id, status=order.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
