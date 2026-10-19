import { BaseStore } from "../../lib/store";
import { fetchShipping } from "./api";
import type { Shipment } from "./types";

export class ShipmentStore extends BaseStore<Shipment> {
  async load(): Promise<void> {
    this.setItems(await fetchShipping());
  }

  findById(id: string): Shipment | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
