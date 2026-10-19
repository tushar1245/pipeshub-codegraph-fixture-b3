from app.shared import validation as v
from app.shared.validation import validate_email as check_email


def normalise_contact(email: str, backup: str) -> tuple[str, str]:
    return v.validate_email(email), check_email(backup)
