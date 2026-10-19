from dataclasses import dataclass

from .models import ReturnRequest


@dataclass
class ReturnRequestIn:
    order_id: str
    reason: str

    @staticmethod
    def parse(body: dict) -> "ReturnRequestIn":
        return ReturnRequestIn(str(body.get("order_id", "")), str(body.get("reason", "")))


@dataclass
class ReturnRequestOut:
    id: str
    status: str

    @staticmethod
    def from_model(return_request: ReturnRequest) -> "ReturnRequestOut":
        return ReturnRequestOut(id=return_request.id, status=return_request.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
