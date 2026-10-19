import { useEffect, useMemo, useState } from "react";
import { PaymentStore } from "../store";
import type { Payment } from "../types";

export function usePayments(): { items: Payment[]; loading: boolean } {
  const store = useMemo(() => new PaymentStore(), []);
  const [items, setItems] = useState<Payment[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
