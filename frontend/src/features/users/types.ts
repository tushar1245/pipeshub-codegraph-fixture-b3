export type UserStatus = "draft" | "active" | "archived";

export interface User {
  id: string;
  status: UserStatus;
  createdAt: string;
  email: string;
  name: string;
}

export interface UserInput {
  email: string;
  name: string;
}
