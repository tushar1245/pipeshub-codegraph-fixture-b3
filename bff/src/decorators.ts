export interface RouteMeta {
  method: "GET" | "POST";
  path: string;
  handler: string;
}

const registry = {
  controllers: new Map<unknown, string>(),
  routes: new Map<unknown, RouteMeta[]>(),
  injectables: new Set<unknown>(),
};

export function Controller(prefix: string): ClassDecorator {
  return (target) => {
    registry.controllers.set(target, prefix);
  };
}

function route(method: RouteMeta["method"], path: string): MethodDecorator {
  return (target, key) => {
    const list = registry.routes.get(target.constructor) ?? [];
    list.push({ method, path, handler: String(key) });
    registry.routes.set(target.constructor, list);
  };
}

export function Get(path = ""): MethodDecorator {
  return route("GET", path);
}

export function Post(path = ""): MethodDecorator {
  return route("POST", path);
}

export function Injectable(): ClassDecorator {
  return (target) => {
    registry.injectables.add(target);
  };
}

export function routesFor(controller: unknown): RouteMeta[] {
  return registry.routes.get(controller) ?? [];
}

export function prefixFor(controller: unknown): string {
  return registry.controllers.get(controller) ?? "";
}
