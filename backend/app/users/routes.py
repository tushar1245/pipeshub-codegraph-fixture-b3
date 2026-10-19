from app.shared.http import Router
from app.shared.pagination import paginate
from app.users.schemas import UserIn, UserOut
from app.users.service import UserService

router = Router(prefix="/users")
_service: UserService | None = None


def bind(service: UserService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_user(key: str) -> dict:
    return UserOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_user(body: dict) -> dict:
    data = UserIn.parse(body)
    return UserOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_users(page: int = 1) -> dict:
    return paginate([UserOut.from_model(x).dump() for x in _service.list()], page, 20)
