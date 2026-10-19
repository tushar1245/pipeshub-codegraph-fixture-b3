from pricing_native import compute_discount

from app.shared.validation import validate_amount


def quote(total, tier: str) -> float:
    amount = validate_amount(total)
    return round(amount - compute_discount(amount, tier), 2)
