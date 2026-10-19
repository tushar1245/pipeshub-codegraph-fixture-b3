"""Structured log lines for the analytics exporters."""
import json

from app.shared.clock import now


class StructuredLogger:
    def __init__(self, name: str) -> None:
        self.name = name

    def info(self, message: str, **fields) -> str:
        return format_line("info", self.name, message, fields)

    def debug(self, message: str, **fields) -> str:
        return format_line("debug", self.name, message, fields)


def getLogger(name: str) -> StructuredLogger:
    return StructuredLogger(name)


def format_line(level: str, name: str, message: str, fields: dict) -> str:
    return json.dumps({"level": level, "logger": name, "msg": message, "at": now(), **fields})
