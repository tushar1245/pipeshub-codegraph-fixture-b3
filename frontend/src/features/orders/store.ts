import { BaseStore } from "../../lib/store";
import { fetchOrders } from "./api";
import type { Order } from "./types";

export class OrderStore extends BaseStore<Order> {
  async load(): Promise<void> {
    this.setItems(await fetchOrders());
  }

  findById(id: string): Order | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
