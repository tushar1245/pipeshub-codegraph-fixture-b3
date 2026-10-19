export type PaymentStatus = "draft" | "active" | "archived";

export interface Payment {
  id: string;
  status: PaymentStatus;
  createdAt: string;
  orderId: string;
  amount: number;
}

export interface PaymentInput {
  orderId: string;
  amount: number;
}
