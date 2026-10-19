from app.shared.compat import fast_dumps
from app.telemetry import json as metric_json
from app.telemetry.logging import getLogger as structured_logger

log = structured_logger("analytics.exporter")


def export_snapshot(rows: list[dict]) -> bytes:
    log.info("exporting", rows=len(rows))
    return fast_dumps(rows)


def export_compact(rows: list[dict]) -> str:
    return metric_json.dumps({"rows": rows})
