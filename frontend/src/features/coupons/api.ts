import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Coupon, CouponInput } from "./types";

const BASE = "/api/coupons";

export function fetchCoupons(): Promise<Coupon[]> {
  return getJson<Coupon[]>(BASE);
}

export function fetchCoupon(id: string): Promise<Coupon> {
  return getJson<Coupon>(`${BASE}/${id}`);
}

export function createCoupon(input: CouponInput): Promise<Coupon> {
  return postJson<Coupon>(BASE, input);
}

export function updateCoupon(id: string, input: Partial<CouponInput>): Promise<Coupon> {
  return putJson<Coupon>(`${BASE}/${id}`, input);
}

export function removeCoupon(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
