import { BaseStore } from "../../lib/store";
import { fetchAnalytics } from "./api";
import type { Metric } from "./types";

export class MetricStore extends BaseStore<Metric> {
  async load(): Promise<void> {
    this.setItems(await fetchAnalytics());
  }

  findById(id: string): Metric | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
