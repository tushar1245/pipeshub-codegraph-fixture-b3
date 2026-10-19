from ..shared.events import Event
from .models import Payment


def payment_created(payment: Payment) -> Event:
    return Event(name="payments.created", payload=payment.to_dict())


def payment_archived(payment: Payment) -> Event:
    return Event(name="payments.archived", payload={"id": payment.id})
