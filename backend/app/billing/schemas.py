from dataclasses import dataclass

from .models import Invoice


@dataclass
class InvoiceIn:
    customer_id: str
    amount: str

    @staticmethod
    def parse(body: dict) -> "InvoiceIn":
        return InvoiceIn(str(body.get("customer_id", "")), str(body.get("amount", "")))


@dataclass
class InvoiceOut:
    id: str
    status: str

    @staticmethod
    def from_model(invoice: Invoice) -> "InvoiceOut":
        return InvoiceOut(id=invoice.id, status=invoice.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
