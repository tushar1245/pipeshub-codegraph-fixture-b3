from app.shared.http import Router
from app.shared.pagination import paginate
from app.orders.schemas import OrderIn, OrderOut
from app.orders.service import OrderService

router = Router(prefix="/orders")
_service: OrderService | None = None


def bind(service: OrderService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_order(key: str) -> dict:
    return OrderOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_order(body: dict) -> dict:
    data = OrderIn.parse(body)
    return OrderOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_orders(page: int = 1) -> dict:
    return paginate([OrderOut.from_model(x).dump() for x in _service.list()], page, 20)
