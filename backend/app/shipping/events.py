from ..shared.events import Event
from .models import Shipment


def shipment_created(shipment: Shipment) -> Event:
    return Event(name="shipping.created", payload=shipment.to_dict())


def shipment_archived(shipment: Shipment) -> Event:
    return Event(name="shipping.archived", payload={"id": shipment.id})
