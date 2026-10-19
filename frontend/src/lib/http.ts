import { ApiClient } from "./apiClient";
import { readEnv } from "./env.mjs";

const api = new ApiClient(readEnv("VITE_API_URL", ""));

export function getJson<T>(path: string): Promise<T> {
  return api.get<T>(path);
}

export function postJson<T>(path: string, body: unknown): Promise<T> {
  return api.post<T>(path, body);
}

export function putJson<T>(path: string, body: unknown): Promise<T> {
  return api.put<T>(path, body);
}

export function deleteJson(path: string): Promise<void> {
  return api.delete<void>(path);
}
