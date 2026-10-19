import { prefixFor, routesFor, type RouteMeta } from "./decorators";
import { UpstreamClient } from "./http/upstream";
import { OrdersController } from "./orders/orders.controller";
import { OrdersService } from "./orders/orders.service";
import { ProductsController } from "./products/products.controller";
import { ProductsService } from "./products/products.service";
import { UsersController } from "./users/users.controller";
import { UsersService } from "./users/users.service";

export interface MountedController {
  prefix: string;
  routes: RouteMeta[];
}

export function bootstrap(upstreamUrl: string): MountedController[] {
  const upstream = new UpstreamClient(upstreamUrl);
  const controllers = [
    new OrdersController(new OrdersService(upstream)),
    new ProductsController(new ProductsService(upstream)),
    new UsersController(new UsersService(upstream)),
  ];
  return controllers.map((controller) => ({
    prefix: prefixFor(controller.constructor),
    routes: routesFor(controller.constructor),
  }));
}
