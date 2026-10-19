import { Controller, Get, Post } from "../decorators";
import { clamp } from "../util/clamp";
import { OrdersService, type OrderSummary } from "./orders.service";

@Controller("orders")
export class OrdersController {
  constructor(private readonly orders: OrdersService) {}

  @Get()
  async list(limit = 20): Promise<OrderSummary[]> {
    const all = await this.orders.list();
    return all.slice(0, clamp(limit, 1, 100));
  }

  @Get(":id")
  show(id: string): Promise<OrderSummary> {
    return this.orders.get(id);
  }

  @Post()
  create(body: Partial<OrderSummary>): Promise<OrderSummary> {
    return this.orders.create(body);
  }
}
