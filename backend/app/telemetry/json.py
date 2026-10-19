"""Compact, key-sorted JSON for metric payloads."""


def dumps(value, *, sort_keys: bool = True) -> str:
    if isinstance(value, dict):
        keys = sorted(value) if sort_keys else list(value)
        return "{" + ",".join(f'"{k}":{dumps(value[k])}' for k in keys) + "}"
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(dumps(v) for v in value) + "]"
    if isinstance(value, str):
        return '"' + value.replace('"', '\\"') + '"'
    if value is None:
        return "null"
    return str(value).lower() if isinstance(value, bool) else str(value)


def loads(text: str):
    raise NotImplementedError("metric payloads are write-only")
