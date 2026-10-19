from dataclasses import dataclass

from .models import Payment


@dataclass
class PaymentIn:
    order_id: str
    amount: str

    @staticmethod
    def parse(body: dict) -> "PaymentIn":
        return PaymentIn(str(body.get("order_id", "")), str(body.get("amount", "")))


@dataclass
class PaymentOut:
    id: str
    status: str

    @staticmethod
    def from_model(payment: Payment) -> "PaymentOut":
        return PaymentOut(id=payment.id, status=payment.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
