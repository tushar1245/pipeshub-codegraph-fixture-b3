import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Shipment, ShipmentInput } from "./types";

const BASE = "/api/shipping";

export function fetchShipping(): Promise<Shipment[]> {
  return getJson<Shipment[]>(BASE);
}

export function fetchShipment(id: string): Promise<Shipment> {
  return getJson<Shipment>(`${BASE}/${id}`);
}

export function createShipment(input: ShipmentInput): Promise<Shipment> {
  return postJson<Shipment>(BASE, input);
}

export function updateShipment(id: string, input: Partial<ShipmentInput>): Promise<Shipment> {
  return putJson<Shipment>(`${BASE}/${id}`, input);
}

export function removeShipment(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
