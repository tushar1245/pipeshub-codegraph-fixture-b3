from dataclasses import dataclass

from .models import Product


@dataclass
class ProductIn:
    sku: str
    title: str

    @staticmethod
    def parse(body: dict) -> "ProductIn":
        return ProductIn(str(body.get("sku", "")), str(body.get("title", "")))


@dataclass
class ProductOut:
    id: str
    status: str

    @staticmethod
    def from_model(product: Product) -> "ProductOut":
        return ProductOut(id=product.id, status=product.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
