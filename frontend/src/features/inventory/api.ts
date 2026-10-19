import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { InventoryItem, InventoryItemInput } from "./types";

const BASE = "/api/inventory";

export function fetchInventory(): Promise<InventoryItem[]> {
  return getJson<InventoryItem[]>(BASE);
}

export function fetchInventoryItem(id: string): Promise<InventoryItem> {
  return getJson<InventoryItem>(`${BASE}/${id}`);
}

export function createInventoryItem(input: InventoryItemInput): Promise<InventoryItem> {
  return postJson<InventoryItem>(BASE, input);
}

export function updateInventoryItem(id: string, input: Partial<InventoryItemInput>): Promise<InventoryItem> {
  return putJson<InventoryItem>(`${BASE}/${id}`, input);
}

export function removeInventoryItem(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
