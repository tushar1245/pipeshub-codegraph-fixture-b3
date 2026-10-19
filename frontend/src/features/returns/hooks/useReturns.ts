import { useEffect, useMemo, useState } from "react";
import { ReturnRequestStore } from "../store";
import type { ReturnRequest } from "../types";

export function useReturns(): { items: ReturnRequest[]; loading: boolean } {
  const store = useMemo(() => new ReturnRequestStore(), []);
  const [items, setItems] = useState<ReturnRequest[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
