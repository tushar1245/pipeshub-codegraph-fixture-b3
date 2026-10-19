from app.catalog.models import Product
from app.shared.importing import Base


class CsvImporter(Base):
    def __init__(self) -> None:
        self.products: list[Product] = []

    def handle_row(self, row: dict) -> None:
        self.products.append(Product.from_dict(row))


def import_csv(raw: str) -> int:
    return CsvImporter().run(raw)
