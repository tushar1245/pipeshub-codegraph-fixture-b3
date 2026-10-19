import { useEffect, useMemo, useState } from "react";
import { MetricStore } from "../store";
import type { Metric } from "../types";

export function useAnalytics(): { items: Metric[]; loading: boolean } {
  const store = useMemo(() => new MetricStore(), []);
  const [items, setItems] = useState<Metric[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
