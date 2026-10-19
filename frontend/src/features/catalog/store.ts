import { BaseStore } from "../../lib/store";
import { fetchCatalog } from "./api";
import type { Product } from "./types";

export class ProductStore extends BaseStore<Product> {
  async load(): Promise<void> {
    this.setItems(await fetchCatalog());
  }

  findById(id: string): Product | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
