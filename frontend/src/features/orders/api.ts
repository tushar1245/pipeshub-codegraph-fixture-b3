import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Order, OrderInput } from "./types";

const BASE = "/api/orders";

export function fetchOrders(): Promise<Order[]> {
  return getJson<Order[]>(BASE);
}

export function fetchOrder(id: string): Promise<Order> {
  return getJson<Order>(`${BASE}/${id}`);
}

export function createOrder(input: OrderInput): Promise<Order> {
  return postJson<Order>(BASE, input);
}

export function updateOrder(id: string, input: Partial<OrderInput>): Promise<Order> {
  return putJson<Order>(`${BASE}/${id}`, input);
}

export function removeOrder(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
