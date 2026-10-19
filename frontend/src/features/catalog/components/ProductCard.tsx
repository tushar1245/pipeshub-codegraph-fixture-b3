import { formatDate, formatLabel as label } from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Product } from "../types";

interface ProductCardProps {
  item: Product;
  onSelect?: (id: string) => void;
}

export function ProductCard({ item, onSelect }: ProductCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{label(item.sku)}</h3>
      <StatusBadge status={item.status} />
      <time>{formatDate(item.createdAt)}</time>
    </div>
  );
}
