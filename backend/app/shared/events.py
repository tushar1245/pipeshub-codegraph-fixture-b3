from collections import defaultdict
from dataclasses import dataclass, field
from typing import Callable

from app.shared.clock import now


@dataclass
class Event:
    name: str
    payload: dict
    at: float = field(default_factory=now)


class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable[[Event], None]]] = defaultdict(list)

    def subscribe(self, name: str, handler: Callable[[Event], None]) -> None:
        self._handlers[name].append(handler)

    def publish(self, event: Event) -> int:
        handlers = self._handlers.get(event.name, [])
        for handler in handlers:
            handler(event)
        return len(handlers)
