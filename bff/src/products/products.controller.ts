import { Controller, Get, Post } from "../decorators";
import { clamp } from "../util/clamp";
import { ProductsService, type ProductSummary } from "./products.service";

@Controller("products")
export class ProductsController {
  constructor(private readonly products: ProductsService) {}

  @Get()
  async list(limit = 20): Promise<ProductSummary[]> {
    const all = await this.products.list();
    return all.slice(0, clamp(limit, 1, 100));
  }

  @Get(":id")
  show(id: string): Promise<ProductSummary> {
    return this.products.get(id);
  }

  @Post()
  create(body: Partial<ProductSummary>): Promise<ProductSummary> {
    return this.products.create(body);
  }
}
