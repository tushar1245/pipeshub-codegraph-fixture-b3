export type ProductStatus = "draft" | "active" | "archived";

export interface Product {
  id: string;
  status: ProductStatus;
  createdAt: string;
  sku: string;
  title: string;
}

export interface ProductInput {
  sku: string;
  title: string;
}
