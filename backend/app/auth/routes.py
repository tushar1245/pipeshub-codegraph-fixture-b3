from app.shared.http import Router
from app.shared.pagination import paginate
from app.auth.schemas import SessionIn, SessionOut
from app.auth.service import SessionService

router = Router(prefix="/auth")
_service: SessionService | None = None


def bind(service: SessionService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_session(key: str) -> dict:
    return SessionOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_session(body: dict) -> dict:
    data = SessionIn.parse(body)
    return SessionOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_auth(page: int = 1) -> dict:
    return paginate([SessionOut.from_model(x).dump() for x in _service.list()], page, 20)
