import { BaseStore } from "../../lib/store";
import { fetchAuth } from "./api";
import type { Session } from "./types";

export class SessionStore extends BaseStore<Session> {
  async load(): Promise<void> {
    this.setItems(await fetchAuth());
  }

  findById(id: string): Session | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
