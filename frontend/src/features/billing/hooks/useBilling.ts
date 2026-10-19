import { useEffect, useMemo, useState } from "react";
import { InvoiceStore } from "../store";
import type { Invoice } from "../types";

export function useBilling(): { items: Invoice[]; loading: boolean } {
  const store = useMemo(() => new InvoiceStore(), []);
  const [items, setItems] = useState<Invoice[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
