from app.shared.http import Router
from app.shared.pagination import paginate
from app.shipping.schemas import ShipmentIn, ShipmentOut
from app.shipping.service import ShipmentService

router = Router(prefix="/shipping")
_service: ShipmentService | None = None


def bind(service: ShipmentService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_shipment(key: str) -> dict:
    return ShipmentOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_shipment(body: dict) -> dict:
    data = ShipmentIn.parse(body)
    return ShipmentOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_shipping(page: int = 1) -> dict:
    return paginate([ShipmentOut.from_model(x).dump() for x in _service.list()], page, 20)
