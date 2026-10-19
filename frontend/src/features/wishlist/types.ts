export type WishlistItemStatus = "draft" | "active" | "archived";

export interface WishlistItem {
  id: string;
  status: WishlistItemStatus;
  createdAt: string;
  userId: string;
  productId: string;
}

export interface WishlistItemInput {
  userId: string;
  productId: string;
}
