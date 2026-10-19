export type SessionStatus = "draft" | "active" | "archived";

export interface Session {
  id: string;
  status: SessionStatus;
  createdAt: string;
  userId: string;
  token: string;
}

export interface SessionInput {
  userId: string;
  token: string;
}
