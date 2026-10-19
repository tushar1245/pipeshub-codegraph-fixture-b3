import { useEffect, useMemo, useState } from "react";
import { UserStore } from "../store";
import type { User } from "../types";

export function useUsers(): { items: User[]; loading: boolean } {
  const store = useMemo(() => new UserStore(), []);
  const [items, setItems] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = store.subscribe(setItems);
    store.load().finally(() => setLoading(false));
    return unsubscribe;
  }, [store]);

  return { items, loading };
}
