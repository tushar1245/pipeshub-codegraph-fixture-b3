export type ReviewStatus = "draft" | "active" | "archived";

export interface Review {
  id: string;
  status: ReviewStatus;
  createdAt: string;
  productId: string;
  rating: number;
}

export interface ReviewInput {
  productId: string;
  rating: number;
}
