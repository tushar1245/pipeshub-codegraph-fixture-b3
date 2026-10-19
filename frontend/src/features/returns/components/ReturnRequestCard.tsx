import * as fmt from "../../../lib/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { ReturnRequest } from "../types";

interface ReturnRequestCardProps {
  item: ReturnRequest;
  onSelect?: (id: string) => void;
}

export function ReturnRequestCard({ item, onSelect }: ReturnRequestCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{fmt.formatLabel(item.orderId)}</h3>
      <StatusBadge status={item.status} />
      <time>{fmt.formatDate(item.createdAt)}</time>
    </div>
  );
}
