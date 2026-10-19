import { useEffect, useMemo, useState } from "react";
import { SessionStore } from "../store";
import type { Session } from "../types";

export function useAuth(): { items: Session[]; loading: boolean } {
  const store = useMemo(() => new SessionStore(), []);
  const [items, setItems] = useState<Session[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
