from ..shared.events import Event
from .models import Product


def product_created(product: Product) -> Event:
    return Event(name="catalog.created", payload=product.to_dict())


def product_archived(product: Product) -> Event:
    return Event(name="catalog.archived", payload={"id": product.id})
