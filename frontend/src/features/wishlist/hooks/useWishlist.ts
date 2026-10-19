import { useEffect, useMemo, useState } from "react";
import { WishlistItemStore } from "../store";
import type { WishlistItem } from "../types";

export function useWishlist(): { items: WishlistItem[]; loading: boolean } {
  const store = useMemo(() => new WishlistItemStore(), []);
  const [items, setItems] = useState<WishlistItem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
