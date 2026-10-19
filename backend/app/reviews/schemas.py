from dataclasses import dataclass

from .models import Review


@dataclass
class ReviewIn:
    product_id: str
    rating: str

    @staticmethod
    def parse(body: dict) -> "ReviewIn":
        return ReviewIn(str(body.get("product_id", "")), str(body.get("rating", "")))


@dataclass
class ReviewOut:
    id: str
    status: str

    @staticmethod
    def from_model(review: Review) -> "ReviewOut":
        return ReviewOut(id=review.id, status=review.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
