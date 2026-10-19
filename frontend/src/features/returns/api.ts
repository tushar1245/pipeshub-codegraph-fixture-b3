import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { ReturnRequest, ReturnRequestInput } from "./types";

const BASE = "/api/returns";

export function fetchReturns(): Promise<ReturnRequest[]> {
  return getJson<ReturnRequest[]>(BASE);
}

export function fetchReturnRequest(id: string): Promise<ReturnRequest> {
  return getJson<ReturnRequest>(`${BASE}/${id}`);
}

export function createReturnRequest(input: ReturnRequestInput): Promise<ReturnRequest> {
  return postJson<ReturnRequest>(BASE, input);
}

export function updateReturnRequest(id: string, input: Partial<ReturnRequestInput>): Promise<ReturnRequest> {
  return putJson<ReturnRequest>(`${BASE}/${id}`, input);
}

export function removeReturnRequest(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
