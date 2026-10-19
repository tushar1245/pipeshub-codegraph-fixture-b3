export type Listener<T> = (items: T[]) => void;

export abstract class BaseStore<T> {
  protected items: T[] = [];
  private listeners: Listener<T>[] = [];

  abstract load(): Promise<void>;

  getItems(): T[] {
    return this.items;
  }

  subscribe(listener: Listener<T>): () => void {
    this.listeners.push(listener);
    return () => {
      this.listeners = this.listeners.filter((l) => l !== listener);
    };
  }

  protected setItems(items: T[]): void {
    this.items = items;
    this.notify();
  }

  private notify(): void {
    for (const listener of this.listeners) {
      listener(this.items);
    }
  }
}
