from app.shared.http import Router
from app.shared.pagination import paginate
from app.inventory.schemas import InventoryItemIn, InventoryItemOut
from app.inventory.service import InventoryItemService

router = Router(prefix="/inventory")
_service: InventoryItemService | None = None


def bind(service: InventoryItemService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_inventory_item(key: str) -> dict:
    return InventoryItemOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_inventory_item(body: dict) -> dict:
    data = InventoryItemIn.parse(body)
    return InventoryItemOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_inventory(page: int = 1) -> dict:
    return paginate([InventoryItemOut.from_model(x).dump() for x in _service.list()], page, 20)
