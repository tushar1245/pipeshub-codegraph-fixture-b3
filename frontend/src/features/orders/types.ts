export type OrderStatus = "draft" | "active" | "archived";

export interface Order {
  id: string;
  status: OrderStatus;
  createdAt: string;
  customerId: string;
  total: number;
}

export interface OrderInput {
  customerId: string;
  total: number;
}
