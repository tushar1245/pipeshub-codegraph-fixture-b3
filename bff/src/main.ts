import { bootstrap } from "./app.module";

const mounted = bootstrap(process.env.UPSTREAM_URL ?? "http://localhost:8000");
for (const controller of mounted) {
  for (const route of controller.routes) {
    console.log(`${route.method} /${controller.prefix}/${route.path} -> ${route.handler}`);
  }
}
