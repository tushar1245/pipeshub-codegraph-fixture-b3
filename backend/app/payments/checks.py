def validate(amount) -> bool:
    return float(amount) > 0


def is_refundable(status: str) -> bool:
    return status in ("captured", "settled")
