import * as fmt from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { InventoryItem } from "../types";

interface InventoryItemCardProps {
  item: InventoryItem;
  onSelect?: (id: string) => void;
}

export function InventoryItemCard({ item, onSelect }: InventoryItemCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{fmt.formatLabel(item.sku)}</h3>
      <StatusBadge status={item.status} />
      <time>{fmt.formatDate(item.createdAt)}</time>
    </div>
  );
}
