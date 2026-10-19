import { useEffect, useMemo, useState } from "react";
import { SearchQueryStore } from "../store";
import type { SearchQuery } from "../types";

export function useSearch(): { items: SearchQuery[]; loading: boolean } {
  const store = useMemo(() => new SearchQueryStore(), []);
  const [items, setItems] = useState<SearchQuery[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
