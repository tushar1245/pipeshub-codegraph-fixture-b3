export type ShipmentStatus = "draft" | "active" | "archived";

export interface Shipment {
  id: string;
  status: ShipmentStatus;
  createdAt: string;
  orderId: string;
  carrier: string;
}

export interface ShipmentInput {
  orderId: string;
  carrier: string;
}
