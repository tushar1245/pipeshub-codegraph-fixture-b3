import { BaseStore } from "../../lib/store";
import { fetchPayments } from "./api";
import type { Payment } from "./types";

export class PaymentStore extends BaseStore<Payment> {
  async load(): Promise<void> {
    this.setItems(await fetchPayments());
  }

  findById(id: string): Payment | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
