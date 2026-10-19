import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { WishlistItem, WishlistItemInput } from "./types";

const BASE = "/api/wishlist";

export function fetchWishlist(): Promise<WishlistItem[]> {
  return getJson<WishlistItem[]>(BASE);
}

export function fetchWishlistItem(id: string): Promise<WishlistItem> {
  return getJson<WishlistItem>(`${BASE}/${id}`);
}

export function createWishlistItem(input: WishlistItemInput): Promise<WishlistItem> {
  return postJson<WishlistItem>(BASE, input);
}

export function updateWishlistItem(id: string, input: Partial<WishlistItemInput>): Promise<WishlistItem> {
  return putJson<WishlistItem>(`${BASE}/${id}`, input);
}

export function removeWishlistItem(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
