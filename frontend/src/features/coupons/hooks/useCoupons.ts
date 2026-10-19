import { useEffect, useMemo, useState } from "react";
import { CouponStore } from "../store";
import type { Coupon } from "../types";

export function useCoupons(): { items: Coupon[]; loading: boolean } {
  const store = useMemo(() => new CouponStore(), []);
  const [items, setItems] = useState<Coupon[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
