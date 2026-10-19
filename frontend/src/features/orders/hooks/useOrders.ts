import { useEffect, useMemo, useState } from "react";
import { OrderStore } from "../store";
import type { Order } from "../types";

export function useOrders(): { items: Order[]; loading: boolean } {
  const store = useMemo(() => new OrderStore(), []);
  const [items, setItems] = useState<Order[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
