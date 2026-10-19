from ..shared.events import Event
from .models import Metric


def metric_created(metric: Metric) -> Event:
    return Event(name="analytics.created", payload=metric.to_dict())


def metric_archived(metric: Metric) -> Event:
    return Event(name="analytics.archived", payload={"id": metric.id})
