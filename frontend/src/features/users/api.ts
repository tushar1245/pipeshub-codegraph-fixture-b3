import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { User, UserInput } from "./types";

const BASE = "/api/users";

export function fetchUsers(): Promise<User[]> {
  return getJson<User[]>(BASE);
}

export function fetchUser(id: string): Promise<User> {
  return getJson<User>(`${BASE}/${id}`);
}

export function createUser(input: UserInput): Promise<User> {
  return postJson<User>(BASE, input);
}

export function updateUser(id: string, input: Partial<UserInput>): Promise<User> {
  return putJson<User>(`${BASE}/${id}`, input);
}

export function removeUser(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
