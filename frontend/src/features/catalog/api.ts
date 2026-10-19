import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Product, ProductInput } from "./types";

const BASE = "/api/catalog";

export function fetchCatalog(): Promise<Product[]> {
  return getJson<Product[]>(BASE);
}

export function fetchProduct(id: string): Promise<Product> {
  return getJson<Product>(`${BASE}/${id}`);
}

export function createProduct(input: ProductInput): Promise<Product> {
  return postJson<Product>(BASE, input);
}

export function updateProduct(id: string, input: Partial<ProductInput>): Promise<Product> {
  return putJson<Product>(`${BASE}/${id}`, input);
}

export function removeProduct(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
