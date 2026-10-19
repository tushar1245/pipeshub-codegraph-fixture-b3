import { BaseStore } from "../../lib/store";
import { fetchWishlist } from "./api";
import type { WishlistItem } from "./types";

export class WishlistItemStore extends BaseStore<WishlistItem> {
  async load(): Promise<void> {
    this.setItems(await fetchWishlist());
  }

  findById(id: string): WishlistItem | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
