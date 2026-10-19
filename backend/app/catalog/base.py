class Base:
    """A catalog listing's display defaults."""

    currency = "USD"

    def run(self, raw: str) -> int:
        return len(raw.splitlines())
