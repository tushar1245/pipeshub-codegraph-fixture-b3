import * as fmt from "../../../lib/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Order } from "../types";

interface OrderCardProps {
  item: Order;
  onSelect?: (id: string) => void;
}

export function OrderCard({ item, onSelect }: OrderCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{fmt.formatLabel(item.customerId)}</h3>
      <StatusBadge status={item.status} />
      <time>{fmt.formatDate(item.createdAt)}</time>
    </div>
  );
}
