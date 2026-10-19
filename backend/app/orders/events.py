from ..shared.events import Event
from .models import Order


def order_created(order: Order) -> Event:
    return Event(name="orders.created", payload=order.to_dict())


def order_archived(order: Order) -> Event:
    return Event(name="orders.archived", payload={"id": order.id})
