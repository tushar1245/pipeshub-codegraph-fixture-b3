import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Payment, PaymentInput } from "./types";

const BASE = "/api/payments";

export function fetchPayments(): Promise<Payment[]> {
  return getJson<Payment[]>(BASE);
}

export function fetchPayment(id: string): Promise<Payment> {
  return getJson<Payment>(`${BASE}/${id}`);
}

export function createPayment(input: PaymentInput): Promise<Payment> {
  return postJson<Payment>(BASE, input);
}

export function updatePayment(id: string, input: Partial<PaymentInput>): Promise<Payment> {
  return putJson<Payment>(`${BASE}/${id}`, input);
}

export function removePayment(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
