from app.shared.http import Router
from app.shared.pagination import paginate
from app.catalog.schemas import ProductIn, ProductOut
from app.catalog.service import ProductService

router = Router(prefix="/catalog")
_service: ProductService | None = None


def bind(service: ProductService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_product(key: str) -> dict:
    return ProductOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_product(body: dict) -> dict:
    data = ProductIn.parse(body)
    return ProductOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_catalog(page: int = 1) -> dict:
    return paginate([ProductOut.from_model(x).dump() for x in _service.list()], page, 20)
