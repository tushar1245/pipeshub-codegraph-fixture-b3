import { Injectable } from "../decorators";
import { UpstreamClient } from "../http/upstream";

export interface ProductSummary {
  id: string;
  name: string;
  status: string;
}

@Injectable()
export class ProductsService {
  constructor(private readonly upstream: UpstreamClient) {}

  list(): Promise<ProductSummary[]> {
    return this.upstream.get<ProductSummary[]>("/catalog/products");
  }

  get(id: string): Promise<ProductSummary> {
    return this.upstream.get<ProductSummary>(`/catalog/products/${id}`);
  }

  create(body: Partial<ProductSummary>): Promise<ProductSummary> {
    return this.upstream.post<ProductSummary>("/catalog/products", body);
  }
}
