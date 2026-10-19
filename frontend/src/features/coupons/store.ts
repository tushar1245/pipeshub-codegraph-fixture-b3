import { BaseStore } from "../../lib/store";
import { fetchCoupons } from "./api";
import type { Coupon } from "./types";

export class CouponStore extends BaseStore<Coupon> {
  async load(): Promise<void> {
    this.setItems(await fetchCoupons());
  }

  findById(id: string): Coupon | undefined {
    return this.getItems().find((item) => item.id === id);
  }
}
