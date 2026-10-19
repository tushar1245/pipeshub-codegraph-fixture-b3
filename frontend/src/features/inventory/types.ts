export type InventoryItemStatus = "draft" | "active" | "archived";

export interface InventoryItem {
  id: string;
  status: InventoryItemStatus;
  createdAt: string;
  sku: string;
  quantity: number;
}

export interface InventoryItemInput {
  sku: string;
  quantity: number;
}
