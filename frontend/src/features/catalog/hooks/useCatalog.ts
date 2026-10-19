import { useEffect, useMemo, useState } from "react";
import { ProductStore } from "../store";
import type { Product } from "../types";

export function useCatalog(): { items: Product[]; loading: boolean } {
  const store = useMemo(() => new ProductStore(), []);
  const [items, setItems] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
