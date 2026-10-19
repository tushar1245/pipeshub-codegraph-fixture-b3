from dataclasses import dataclass

from .models import Metric


@dataclass
class MetricIn:
    name: str
    value: str

    @staticmethod
    def parse(body: dict) -> "MetricIn":
        return MetricIn(str(body.get("name", "")), str(body.get("value", "")))


@dataclass
class MetricOut:
    id: str
    status: str

    @staticmethod
    def from_model(metric: Metric) -> "MetricOut":
        return MetricOut(id=metric.id, status=metric.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
