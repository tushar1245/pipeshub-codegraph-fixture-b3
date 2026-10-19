import { BaseStore } from "../../lib/store";
import { fetchReturns } from "./api";
import type { ReturnRequest } from "./types";

export class ReturnRequestStore extends BaseStore<ReturnRequest> {
  async load(): Promise<void> {
    this.setItems(await fetchReturns());
  }

  findById(id: string): ReturnRequest | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
