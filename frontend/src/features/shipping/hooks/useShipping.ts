import { useEffect, useMemo, useState } from "react";
import { ShipmentStore } from "../store";
import type { Shipment } from "../types";

export function useShipping(): { items: Shipment[]; loading: boolean } {
  const store = useMemo(() => new ShipmentStore(), []);
  const [items, setItems] = useState<Shipment[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
