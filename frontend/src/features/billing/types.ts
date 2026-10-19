export type InvoiceStatus = "draft" | "active" | "archived";

export interface Invoice {
  id: string;
  status: InvoiceStatus;
  createdAt: string;
  customerId: string;
  amount: number;
}

export interface InvoiceInput {
  customerId: string;
  amount: number;
}
