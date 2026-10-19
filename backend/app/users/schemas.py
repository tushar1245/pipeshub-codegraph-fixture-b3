from dataclasses import dataclass

from .models import User


@dataclass
class UserIn:
    email: str
    name: str

    @staticmethod
    def parse(body: dict) -> "UserIn":
        return UserIn(str(body.get("email", "")), str(body.get("name", "")))


@dataclass
class UserOut:
    id: str
    status: str

    @staticmethod
    def from_model(user: User) -> "UserOut":
        return UserOut(id=user.id, status=user.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
