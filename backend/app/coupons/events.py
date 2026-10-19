from ..shared.events import Event
from .models import Coupon


def coupon_created(coupon: Coupon) -> Event:
    return Event(name="coupons.created", payload=coupon.to_dict())


def coupon_archived(coupon: Coupon) -> Event:
    return Event(name="coupons.archived", payload={"id": coupon.id})
