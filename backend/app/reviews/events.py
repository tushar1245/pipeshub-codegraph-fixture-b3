from ..shared.events import Event
from .models import Review


def review_created(review: Review) -> Event:
    return Event(name="reviews.created", payload=review.to_dict())


def review_archived(review: Review) -> Event:
    return Event(name="reviews.archived", payload={"id": review.id})
