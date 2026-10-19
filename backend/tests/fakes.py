from app.shared.db import Database


class FakeDatabase(Database):
    def __init__(self) -> None:
        super().__init__("sqlite://")
