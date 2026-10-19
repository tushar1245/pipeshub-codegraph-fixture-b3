from app.shared.http import Router
from app.shared.pagination import paginate
from app.billing.schemas import InvoiceIn, InvoiceOut
from app.billing.service import InvoiceService

router = Router(prefix="/billing")
_service: InvoiceService | None = None


def bind(service: InvoiceService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_invoice(key: str) -> dict:
    return InvoiceOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_invoice(body: dict) -> dict:
    data = InvoiceIn.parse(body)
    return InvoiceOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_billing(page: int = 1) -> dict:
    return paginate([InvoiceOut.from_model(x).dump() for x in _service.list()], page, 20)
