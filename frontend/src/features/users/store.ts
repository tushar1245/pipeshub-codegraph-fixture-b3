import { BaseStore } from "../../lib/store";
import { fetchUsers } from "./api";
import type { User } from "./types";

export class UserStore extends BaseStore<User> {
  async load(): Promise<void> {
    this.setItems(await fetchUsers());
  }

  findById(id: string): User | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
