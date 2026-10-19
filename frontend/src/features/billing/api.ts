import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Invoice, InvoiceInput } from "./types";

const BASE = "/api/billing";

export function fetchBilling(): Promise<Invoice[]> {
  return getJson<Invoice[]>(BASE);
}

export function fetchInvoice(id: string): Promise<Invoice> {
  return getJson<Invoice>(`${BASE}/${id}`);
}

export function createInvoice(input: InvoiceInput): Promise<Invoice> {
  return postJson<Invoice>(BASE, input);
}

export function updateInvoice(id: string, input: Partial<InvoiceInput>): Promise<Invoice> {
  return putJson<Invoice>(`${BASE}/${id}`, input);
}

export function removeInvoice(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
