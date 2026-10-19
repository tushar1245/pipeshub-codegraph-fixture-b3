import { describe, expect, it } from "vitest";
import { OrdersController } from "../src/orders/orders.controller";
import type { OrdersService } from "../src/orders/orders.service";

const rows = Array.from({ length: 150 }, (_, i) => ({ id: String(i), name: `order ${i}`, status: "active" }));

describe("OrdersController", () => {
  it("caps the page size at 100", async () => {
    const service = { list: async () => rows } as unknown as OrdersService;
    const controller = new OrdersController(service);
    expect(await controller.list(500)).toHaveLength(100);
  });
});
