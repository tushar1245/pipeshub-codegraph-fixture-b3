import re

from app.shared.errors import ValidationError

_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_SKU = re.compile(r"^SKU-\d{3,}$")


def require_fields(payload: dict, fields: tuple[str, ...]) -> None:
    missing = [f for f in fields if payload.get(f) in (None, "")]
    if missing:
        raise ValidationError(f"missing fields: {', '.join(missing)}")


def validate_email(value: str) -> str:
    if not _EMAIL.match(value or ""):
        raise ValidationError(f"invalid email: {value!r}")
    return value.lower()


def validate_amount(value) -> float:
    amount = float(value)
    if amount < 0:
        raise ValidationError("amount must not be negative")
    return round(amount, 2)


def validate_sku(value: str) -> str:
    if not _SKU.match(value or ""):
        raise ValidationError(f"invalid sku: {value!r}")
    return value


def validate_rating(value) -> int:
    rating = int(value)
    if not 1 <= rating <= 5:
        raise ValidationError("rating must be between 1 and 5")
    return rating


def validate_percent(value) -> int:
    percent = int(value)
    if not 0 < percent <= 100:
        raise ValidationError("percent must be between 1 and 100")
    return percent


def validate_required(value):
    if value in (None, ""):
        raise ValidationError("value is required")
    return value


def validate(value, kind: str):
    checks = {"email": validate_email, "amount": validate_amount, "sku": validate_sku}
    return checks[kind](value)
