from app.payments.checks import is_refundable
from app.shared.validation import validate


def authorize(payload: dict) -> float:
    return validate(payload.get("amount"), "amount")


def can_refund(payload: dict) -> bool:
    return is_refundable(payload.get("status", ""))
