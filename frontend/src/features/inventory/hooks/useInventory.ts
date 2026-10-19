import { useEffect, useMemo, useState } from "react";
import { InventoryItemStore } from "../store";
import type { InventoryItem } from "../types";

export function useInventory(): { items: InventoryItem[]; loading: boolean } {
  const store = useMemo(() => new InventoryItemStore(), []);
  const [items, setItems] = useState<InventoryItem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
