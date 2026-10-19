from app.shared.db import Database
from app.telemetry.json import dumps


def nightly_rollup(db: Database) -> str:
    rows = db.fetch_many("metrics", 1000)
    return dumps({"rows": len(rows)})
