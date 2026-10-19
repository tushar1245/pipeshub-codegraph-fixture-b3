export type CouponStatus = "draft" | "active" | "archived";

export interface Coupon {
  id: string;
  status: CouponStatus;
  createdAt: string;
  code: string;
  percent: number;
}

export interface CouponInput {
  code: string;
  percent: number;
}
