import csv
import io


class Base:
    """Reads rows from an upload and hands each to ``handle_row``."""

    delimiter = ","

    def run(self, raw: str) -> int:
        count = 0
        for row in csv.DictReader(io.StringIO(raw), delimiter=self.delimiter):
            self.handle_row(row)
            count += 1
        return count

    def handle_row(self, row: dict) -> None:
        raise NotImplementedError
