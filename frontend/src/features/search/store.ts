import { BaseStore } from "../../lib/store";
import { fetchSearch } from "./api";
import type { SearchQuery } from "./types";

export class SearchQueryStore extends BaseStore<SearchQuery> {
  async load(): Promise<void> {
    this.setItems(await fetchSearch());
  }

  findById(id: string): SearchQuery | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
