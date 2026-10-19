import { formatDate, formatLabel as label } from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { WishlistItem } from "../types";

interface WishlistItemCardProps {
  item: WishlistItem;
  onSelect?: (id: string) => void;
}

export function WishlistItemCard({ item, onSelect }: WishlistItemCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{label(item.userId)}</h3>
      <StatusBadge status={item.status} />
      <time>{formatDate(item.createdAt)}</time>
    </div>
  );
}
