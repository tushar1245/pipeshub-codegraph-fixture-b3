import { BaseStore } from "../../lib/store";
import { fetchReviews } from "./api";
import type { Review } from "./types";

export class ReviewStore extends BaseStore<Review> {
  async load(): Promise<void> {
    this.setItems(await fetchReviews());
  }

  findById(id: string): Review | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
