from app.shared.clock import now


def run(window: float = 3600.0) -> dict:
    end = now()
    return {"start": end - window, "end": end}


def describe() -> str:
    return "rolls up the last hour of metrics"
