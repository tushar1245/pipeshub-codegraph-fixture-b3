import { BaseStore } from "../../lib/store";
import { fetchNotifications } from "./api";
import type { Notification } from "./types";

export class NotificationStore extends BaseStore<Notification> {
  async load(): Promise<void> {
    this.setItems(await fetchNotifications());
  }

  findById(id: string): Notification | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
