from app.analytics import jobs


def run() -> int:
    return 1


def tick() -> dict:
    started = run()
    window = jobs.run()
    return {"started": started, **window}
