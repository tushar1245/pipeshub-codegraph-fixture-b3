from app.shared.http import Router
from app.shared.pagination import paginate
from app.wishlist.schemas import WishlistItemIn, WishlistItemOut
from app.wishlist.service import WishlistItemService

router = Router(prefix="/wishlist")
_service: WishlistItemService | None = None


def bind(service: WishlistItemService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_wishlist_item(key: str) -> dict:
    return WishlistItemOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_wishlist_item(body: dict) -> dict:
    data = WishlistItemIn.parse(body)
    return WishlistItemOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_wishlist(page: int = 1) -> dict:
    return paginate([WishlistItemOut.from_model(x).dump() for x in _service.list()], page, 20)
