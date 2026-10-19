import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Notification, NotificationInput } from "./types";

const BASE = "/api/notifications";

export function fetchNotifications(): Promise<Notification[]> {
  return getJson<Notification[]>(BASE);
}

export function fetchNotification(id: string): Promise<Notification> {
  return getJson<Notification>(`${BASE}/${id}`);
}

export function createNotification(input: NotificationInput): Promise<Notification> {
  return postJson<Notification>(BASE, input);
}

export function updateNotification(id: string, input: Partial<NotificationInput>): Promise<Notification> {
  return putJson<Notification>(`${BASE}/${id}`, input);
}

export function removeNotification(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
