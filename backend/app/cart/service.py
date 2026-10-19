from app.cart.models import Cart
from app.pricing.quote import quote


def checkout(cart: Cart, tier: str = "standard") -> float:
    return quote(cart.total(), tier)
