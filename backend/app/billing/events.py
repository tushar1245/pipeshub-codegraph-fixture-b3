from ..shared.events import Event
from .models import Invoice


def invoice_created(invoice: Invoice) -> Event:
    return Event(name="billing.created", payload=invoice.to_dict())


def invoice_archived(invoice: Invoice) -> Event:
    return Event(name="billing.archived", payload={"id": invoice.id})
