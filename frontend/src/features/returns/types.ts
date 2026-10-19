export type ReturnRequestStatus = "draft" | "active" | "archived";

export interface ReturnRequest {
  id: string;
  status: ReturnRequestStatus;
  createdAt: string;
  orderId: string;
  reason: string;
}

export interface ReturnRequestInput {
  orderId: string;
  reason: string;
}
