import * as fmt from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Invoice } from "../types";

interface InvoiceCardProps {
  item: Invoice;
  onSelect?: (id: string) => void;
}

export function InvoiceCard({ item, onSelect }: InvoiceCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{fmt.formatLabel(item.customerId)}</h3>
      <StatusBadge status={item.status} />
      <time>{fmt.formatDate(item.createdAt)}</time>
    </div>
  );
}
