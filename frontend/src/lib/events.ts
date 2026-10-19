import { newId } from "./ids.js";

export interface AppEvent<T = unknown> {
  id: string;
  name: string;
  payload: T;
  at: string;
}

export type Handler = (event: AppEvent) => void;

export class EventBus {
  private readonly handlers = new Map<string, Handler[]>();

  on(name: string, handler: Handler): () => void {
    const list = this.handlers.get(name) ?? [];
    this.handlers.set(name, [...list, handler]);
    return () => this.off(name, handler);
  }

  off(name: string, handler: Handler): void {
    this.handlers.set(name, (this.handlers.get(name) ?? []).filter((h) => h !== handler));
  }

  emit<T>(name: string, payload: T): AppEvent<T> {
    const event: AppEvent<T> = { id: newId("evt"), name, payload, at: new Date().toISOString() };
    for (const handler of this.handlers.get(name) ?? []) {
      handler(event as AppEvent);
    }
    return event;
  }
}

export function createBus(): EventBus {
  return new EventBus();
}
