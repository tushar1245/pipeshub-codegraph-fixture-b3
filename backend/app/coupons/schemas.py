from dataclasses import dataclass

from .models import Coupon


@dataclass
class CouponIn:
    code: str
    percent: str

    @staticmethod
    def parse(body: dict) -> "CouponIn":
        return CouponIn(str(body.get("code", "")), str(body.get("percent", "")))


@dataclass
class CouponOut:
    id: str
    status: str

    @staticmethod
    def from_model(coupon: Coupon) -> "CouponOut":
        return CouponOut(id=coupon.id, status=coupon.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
