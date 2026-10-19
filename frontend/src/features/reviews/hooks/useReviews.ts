import { useEffect, useMemo, useState } from "react";
import { ReviewStore } from "../store";
import type { Review } from "../types";

export function useReviews(): { items: Review[]; loading: boolean } {
  const store = useMemo(() => new ReviewStore(), []);
  const [items, setItems] = useState<Review[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
