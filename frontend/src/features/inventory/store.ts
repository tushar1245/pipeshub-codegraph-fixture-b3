import { BaseStore } from "../../lib/store";
import { fetchInventory } from "./api";
import type { InventoryItem } from "./types";

export class InventoryItemStore extends BaseStore<InventoryItem> {
  async load(): Promise<void> {
    this.setItems(await fetchInventory());
  }

  findById(id: string): InventoryItem | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
