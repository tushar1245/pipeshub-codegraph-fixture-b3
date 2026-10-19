import { formatLabel } from "../../../lib/format";
import { describeSpec, parseSpec } from "../spec/productSpec";
import type { Product } from "../types";

export function ProductDetails({ product, rawSpec }: { product: Product; rawSpec: string }) {
  const spec = parseSpec(rawSpec);
  return (
    <section>
      <h2>{formatLabel(product.title)}</h2>
      <p>{describeSpec(spec)}</p>
    </section>
  );
}
