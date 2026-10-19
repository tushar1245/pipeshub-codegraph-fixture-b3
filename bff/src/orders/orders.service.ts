import { Injectable } from "../decorators";
import { UpstreamClient } from "../http/upstream";

export interface OrderSummary {
  id: string;
  name: string;
  status: string;
}

@Injectable()
export class OrdersService {
  constructor(private readonly upstream: UpstreamClient) {}

  list(): Promise<OrderSummary[]> {
    return this.upstream.get<OrderSummary[]>("/orders");
  }

  get(id: string): Promise<OrderSummary> {
    return this.upstream.get<OrderSummary>(`/orders/${id}`);
  }

  create(body: Partial<OrderSummary>): Promise<OrderSummary> {
    return this.upstream.post<OrderSummary>("/orders", body);
  }
}
