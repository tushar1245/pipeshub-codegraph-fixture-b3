import { BaseStore } from "../../lib/store";
import { fetchBilling } from "./api";
import type { Invoice } from "./types";

export class InvoiceStore extends BaseStore<Invoice> {
  async load(): Promise<void> {
    this.setItems(await fetchBilling());
  }

  findById(id: string): Invoice | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
