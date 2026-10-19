from dataclasses import dataclass

from .models import Session


@dataclass
class SessionIn:
    user_id: str
    token: str

    @staticmethod
    def parse(body: dict) -> "SessionIn":
        return SessionIn(str(body.get("user_id", "")), str(body.get("token", "")))


@dataclass
class SessionOut:
    id: str
    status: str

    @staticmethod
    def from_model(session: Session) -> "SessionOut":
        return SessionOut(id=session.id, status=session.status)

    def dump(self) -> dict:
        return {"id": self.id, "status": self.status}
