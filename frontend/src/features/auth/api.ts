import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Session, SessionInput } from "./types";

const BASE = "/api/auth";

export function fetchAuth(): Promise<Session[]> {
  return getJson<Session[]>(BASE);
}

export function fetchSession(id: string): Promise<Session> {
  return getJson<Session>(`${BASE}/${id}`);
}

export function createSession(input: SessionInput): Promise<Session> {
  return postJson<Session>(BASE, input);
}

export function updateSession(id: string, input: Partial<SessionInput>): Promise<Session> {
  return putJson<Session>(`${BASE}/${id}`, input);
}

export function removeSession(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
