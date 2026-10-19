import { formatDate, formatLabel as label } from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Coupon } from "../types";

interface CouponCardProps {
  item: Coupon;
  onSelect?: (id: string) => void;
}

export function CouponCard({ item, onSelect }: CouponCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{label(item.code)}</h3>
      <StatusBadge status={item.status} />
      <time>{formatDate(item.createdAt)}</time>
    </div>
  );
}
