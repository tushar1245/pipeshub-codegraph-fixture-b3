from app.shared.http import Router
from app.shared.pagination import paginate
from app.search.schemas import SearchQueryIn, SearchQueryOut
from app.search.service import SearchQueryService

router = Router(prefix="/search")
_service: SearchQueryService | None = None


def bind(service: SearchQueryService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_search_query(key: str) -> dict:
    return SearchQueryOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_search_query(body: dict) -> dict:
    data = SearchQueryIn.parse(body)
    return SearchQueryOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_search(page: int = 1) -> dict:
    return paginate([SearchQueryOut.from_model(x).dump() for x in _service.list()], page, 20)
