from app.shared.http import Router
from app.shared.pagination import paginate
from app.returns.schemas import ReturnRequestIn, ReturnRequestOut
from app.returns.service import ReturnRequestService

router = Router(prefix="/returns")
_service: ReturnRequestService | None = None


def bind(service: ReturnRequestService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_return_request(key: str) -> dict:
    return ReturnRequestOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_return_request(body: dict) -> dict:
    data = ReturnRequestIn.parse(body)
    return ReturnRequestOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_returns(page: int = 1) -> dict:
    return paginate([ReturnRequestOut.from_model(x).dump() for x in _service.list()], page, 20)
