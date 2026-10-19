import { useEffect, useMemo, useState } from "react";
import { NotificationStore } from "../store";
import type { Notification } from "../types";

export function useNotifications(): { items: Notification[]; loading: boolean } {
  const store = useMemo(() => new NotificationStore(), []);
  const [items, setItems] = useState<Notification[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
