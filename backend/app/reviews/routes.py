from app.shared.http import Router
from app.shared.pagination import paginate
from app.reviews.schemas import ReviewIn, ReviewOut
from app.reviews.service import ReviewService

router = Router(prefix="/reviews")
_service: ReviewService | None = None


def bind(service: ReviewService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_review(key: str) -> dict:
    return ReviewOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_review(body: dict) -> dict:
    data = ReviewIn.parse(body)
    return ReviewOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_reviews(page: int = 1) -> dict:
    return paginate([ReviewOut.from_model(x).dump() for x in _service.list()], page, 20)
