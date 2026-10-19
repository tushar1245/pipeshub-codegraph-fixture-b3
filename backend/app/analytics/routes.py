from app.shared.http import Router
from app.shared.pagination import paginate
from app.analytics.schemas import MetricIn, MetricOut
from app.analytics.service import MetricService

router = Router(prefix="/analytics")
_service: MetricService | None = None


def bind(service: MetricService) -> None:
    global _service
    _service = service


@router.get("/{key}")
def get_metric(key: str) -> dict:
    return MetricOut.from_model(_service.get(key)).dump()


@router.post("/")
def create_metric(body: dict) -> dict:
    data = MetricIn.parse(body)
    return MetricOut.from_model(_service.create(vars(data))).dump()


@router.get("/")
def list_analytics(page: int = 1) -> dict:
    return paginate([MetricOut.from_model(x).dump() for x in _service.list()], page, 20)
