import * as fmt from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Shipment } from "../types";

interface ShipmentCardProps {
  item: Shipment;
  onSelect?: (id: string) => void;
}

export function ShipmentCard({ item, onSelect }: ShipmentCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{fmt.formatLabel(item.orderId)}</h3>
      <StatusBadge status={item.status} />
      <time>{fmt.formatDate(item.createdAt)}</time>
    </div>
  );
}
