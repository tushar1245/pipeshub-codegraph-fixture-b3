from dataclasses import dataclass, field


@dataclass
class Cart:
    lines: list[tuple[str, int, float]] = field(default_factory=list)

    def add(self, sku: str, quantity: int, price: float) -> None:
        self.lines.append((sku, quantity, price))

    def total(self) -> float:
        return round(sum(q * p for _, q, p in self.lines), 2)
