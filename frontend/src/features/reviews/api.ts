import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Review, ReviewInput } from "./types";

const BASE = "/api/reviews";

export function fetchReviews(): Promise<Review[]> {
  return getJson<Review[]>(BASE);
}

export function fetchReview(id: string): Promise<Review> {
  return getJson<Review>(`${BASE}/${id}`);
}

export function createReview(input: ReviewInput): Promise<Review> {
  return postJson<Review>(BASE, input);
}

export function updateReview(id: string, input: Partial<ReviewInput>): Promise<Review> {
  return putJson<Review>(`${BASE}/${id}`, input);
}

export function removeReview(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
