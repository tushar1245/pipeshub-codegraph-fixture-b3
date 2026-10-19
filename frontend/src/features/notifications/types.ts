export type NotificationStatus = "draft" | "active" | "archived";

export interface Notification {
  id: string;
  status: NotificationStatus;
  createdAt: string;
  userId: string;
  channel: string;
}

export interface NotificationInput {
  userId: string;
  channel: string;
}
