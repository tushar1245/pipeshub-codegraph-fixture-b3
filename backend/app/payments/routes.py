from app.shared.http import Router
from app.shared.pagination import paginate
from app.payments.schemas import PaymentIn, PaymentOut
from app.payments.service import PaymentService

router = Router(prefix="/payments")
_service: PaymentService | None = None


def bind(service: PaymentService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_payment(key: str) -> dict:
    return PaymentOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_payment(body: dict) -> dict:
    data = PaymentIn.parse(body)
    return PaymentOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_payments(page: int = 1) -> dict:
    return paginate([PaymentOut.from_model(x).dump() for x in _service.list()], page, 20)
