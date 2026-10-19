from app.shared.http import Router
from app.shared.pagination import paginate
from app.notifications.schemas import NotificationIn, NotificationOut
from app.notifications.service import NotificationService

router = Router(prefix="/notifications")
_service: NotificationService | None = None


def bind(service: NotificationService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_notification(key: str) -> dict:
    return NotificationOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_notification(body: dict) -> dict:
    data = NotificationIn.parse(body)
    return NotificationOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_notifications(page: int = 1) -> dict:
    return paginate([NotificationOut.from_model(x).dump() for x in _service.list()], page, 20)
