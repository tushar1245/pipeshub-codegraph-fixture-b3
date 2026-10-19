import { formatDate, formatLabel as label } from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Review } from "../types";

interface ReviewCardProps {
  item: Review;
  onSelect?: (id: string) => void;
}

export function ReviewCard({ item, onSelect }: ReviewCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{label(item.productId)}</h3>
      <StatusBadge status={item.status} />
      <time>{formatDate(item.createdAt)}</time>
    </div>
  );
}
