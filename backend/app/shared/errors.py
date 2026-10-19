class AppError(Exception):
    status = 500

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class ValidationError(AppError):
    status = 422


class NotFoundError(AppError):
    status = 404

    def __init__(self, kind: str, key: str) -> None:
        super().__init__(f"{kind} {key} not found")


class ConflictError(AppError):
    status = 409
