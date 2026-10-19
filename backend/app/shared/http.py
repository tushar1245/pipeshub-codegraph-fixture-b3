from typing import Callable

Handler = Callable[..., dict]


class Registration:
    def __init__(self, router: "Router", method: str, path: str) -> None:
        self.router = router
        self.method = method
        self.path = path

    def __call__(self, fn: Handler) -> Handler:
        self.router.routes.append((self.method, self.router.prefix + self.path, fn))
        return fn


class Router:
    def __init__(self, prefix: str = "") -> None:
        self.prefix = prefix
        self.routes: list[tuple[str, str, Handler]] = []

    def _add(self, method: str, path: str) -> Registration:
        return Registration(self, method, path)

    def get(self, path: str) -> Registration:
        return self._add("GET", path)

    def post(self, path: str) -> Registration:
        return self._add("POST", path)

    def delete(self, path: str) -> Registration:
        return self._add("DELETE", path)


class App:
    def __init__(self) -> None:
        self.routers: list[Router] = []

    def include(self, router: Router) -> None:
        self.routers.append(router)

    def route_table(self) -> list[tuple[str, str]]:
        return [(m, p) for r in self.routers for (m, p, _) in r.routes]
