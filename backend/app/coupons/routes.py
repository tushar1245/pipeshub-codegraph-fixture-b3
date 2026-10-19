from app.shared.http import Router
from app.shared.pagination import paginate
from app.coupons.schemas import CouponIn, CouponOut
from app.coupons.service import CouponService

router = Router(prefix="/coupons")
_service: CouponService | None = None


def bind(service: CouponService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_coupon(key: str) -> dict:
    return CouponOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_coupon(body: dict) -> dict:
    data = CouponIn.parse(body)
    return CouponOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_coupons(page: int = 1) -> dict:
    return paginate([CouponOut.from_model(x).dump() for x in _service.list()], page, 20)
